"""Frozen Neural Response Coordinate Nuisance-Invariance Pilot 0.1."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import torch

ETA = 0.1
RHO = 0.5
INPUT_DIM = 4
HIDDEN_DIM = 5
PCA_DIM = 2
ATOL = 1e-12
GRID = np.array([-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0], dtype=np.float64)
PHI = np.arange(8, dtype=np.float64) * np.pi / 4.0
DTYPE = torch.float64

CAL_INTERVENTIONS = np.array(
    [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]],
    dtype=np.float64,
) / 2.0

HOLD_INTERVENTIONS = np.array(
    [
        [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
        [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, -1], [0, 1, -1, 0],
    ],
    dtype=np.float64,
)
HOLD_INTERVENTIONS[4:] /= np.sqrt(2.0)


@dataclass(frozen=True)
class GaugeState:
    index: int
    i: int
    j: int
    phi_index: int
    z1: float
    z2: float
    phi: float
    U: np.ndarray
    v: np.ndarray


@dataclass(frozen=True)
class PCAModel:
    mean: np.ndarray
    components: np.ndarray
    score_mean: np.ndarray
    score_scale: np.ndarray


@dataclass(frozen=True)
class Standardizer:
    mean: np.ndarray
    scale: np.ndarray


@dataclass(frozen=True)
class MetricResult:
    r2_state: float
    per_intervention_r2: np.ndarray
    nrmse: float


@dataclass(frozen=True)
class PredictionBundle:
    predictions: Mapping[str, Mapping[str, np.ndarray]]
    representations: Mapping[str, np.ndarray]
    response_decoder: np.ndarray
    partitions: Mapping[str, np.ndarray]


def rotation_matrix(phi: float) -> np.ndarray:
    Q = np.eye(HIDDEN_DIM, dtype=np.float64)
    c, s = np.cos(phi), np.sin(phi)
    Q[:2, :2] = np.array([[c, -s], [s, c]], dtype=np.float64)
    return Q


def canonical_base(z1: float, z2: float) -> tuple[np.ndarray, np.ndarray]:
    q = np.array(
        [1.0 + RHO * z1, 1.0 - RHO * z1, 1.0 + RHO * z2, 1.0 - RHO * z2],
        dtype=np.float64,
    )
    U = np.zeros((HIDDEN_DIM, INPUT_DIM), dtype=np.float64)
    U[1:5, :] = np.diag(np.sqrt(q))
    v = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float64)
    return U, v


def build_states() -> list[GaugeState]:
    states = []
    index = 0
    for i, z1 in enumerate(GRID):
        for j, z2 in enumerate(GRID):
            U0, v0 = canonical_base(float(z1), float(z2))
            for p, phi in enumerate(PHI):
                Q = rotation_matrix(float(phi))
                states.append(
                    GaugeState(index, i, j, p, float(z1), float(z2), float(phi), Q @ U0, Q @ v0)
                )
                index += 1
    return states


def partition_indices(states: list[GaugeState]) -> dict[str, np.ndarray]:
    return {
        "train": np.array([s.index for s in states if (s.i + s.j) % 2 == 0 and s.phi_index % 2 == 0], dtype=np.int64),
        "nuis": np.array([s.index for s in states if (s.i + s.j) % 2 == 0 and s.phi_index % 2 == 1], dtype=np.int64),
        "latent": np.array([s.index for s in states if (s.i + s.j) % 2 == 1 and s.phi_index % 2 == 0], dtype=np.int64),
        "joint": np.array([s.index for s in states if (s.i + s.j) % 2 == 1 and s.phi_index % 2 == 1], dtype=np.int64),
    }


def effective_weight(state: GaugeState) -> np.ndarray:
    return state.U.T @ state.v


def plasticity_matrix(state: GaugeState) -> np.ndarray:
    return state.U.T @ state.U + np.dot(state.v, state.v) * np.eye(INPUT_DIM, dtype=np.float64)


def analytical_response(state: GaugeState, c: np.ndarray) -> np.ndarray:
    return ETA * (plasticity_matrix(state) @ np.asarray(c, dtype=np.float64))


def autograd_response(state: GaugeState, c: np.ndarray) -> np.ndarray:
    U = torch.tensor(state.U, dtype=DTYPE, requires_grad=True)
    v = torch.tensor(state.v, dtype=DTYPE, requires_grad=True)
    target = torch.tensor(np.asarray(c, dtype=np.float64), dtype=DTYPE)
    w = U.T @ v
    loss = 0.5 * torch.sum((w - target) ** 2)
    loss.backward()
    with torch.no_grad():
        U_plus = U - ETA * U.grad
        v_plus = v - ETA * v.grad
        return (U_plus.T @ v_plus).cpu().numpy()


def response_cube(states: list[GaugeState], interventions: np.ndarray, *, autograd: bool = False) -> np.ndarray:
    fn = autograd_response if autograd else analytical_response
    return np.array([[fn(s, c) for c in interventions] for s in states], dtype=np.float64)


def calibration_fingerprint(calibration_responses: np.ndarray) -> np.ndarray:
    arr = np.asarray(calibration_responses, dtype=np.float64)
    if arr.shape[1:] != (4, 4):
        raise ValueError("calibration responses must have shape (n_states, 4, 4)")
    return arr.reshape(arr.shape[0], 16)


def fit_pca2(train_matrix: np.ndarray) -> PCAModel:
    X = np.asarray(train_matrix, dtype=np.float64)
    mean = X.mean(axis=0)
    centered = X - mean
    _, _, vt = np.linalg.svd(centered, full_matrices=False)
    components = vt[:PCA_DIM].copy()
    scores = centered @ components.T
    score_mean = scores.mean(axis=0)
    score_scale = scores.std(axis=0, ddof=0)
    score_scale = np.where(score_scale == 0.0, 1.0, score_scale)
    return PCAModel(mean, components, score_mean, score_scale)


def transform_pca2(matrix: np.ndarray, model: PCAModel) -> np.ndarray:
    scores = (np.asarray(matrix, dtype=np.float64) - model.mean) @ model.components.T
    return (scores - model.score_mean) / model.score_scale


def fit_standardizer(train_matrix: np.ndarray) -> Standardizer:
    X = np.asarray(train_matrix, dtype=np.float64)
    mean = X.mean(axis=0)
    scale = X.std(axis=0, ddof=0)
    scale = np.where(scale == 0.0, 1.0, scale)
    return Standardizer(mean, scale)


def transform_standardized(matrix: np.ndarray, standardizer: Standardizer) -> np.ndarray:
    return (np.asarray(matrix, dtype=np.float64) - standardizer.mean) / standardizer.scale


def bilinear_feature(r: np.ndarray, c: np.ndarray) -> np.ndarray:
    rr = np.asarray(r, dtype=np.float64).reshape(-1)
    cc = np.asarray(c, dtype=np.float64).reshape(INPUT_DIM)
    return np.concatenate([cc] + [value * cc for value in rr])


def fit_decoder(state_features: np.ndarray, interventions: np.ndarray, calibration_responses: np.ndarray) -> np.ndarray:
    design, target = [], []
    for si, r in enumerate(np.asarray(state_features, dtype=np.float64)):
        for ci, c in enumerate(np.asarray(interventions, dtype=np.float64)):
            design.append(bilinear_feature(r, c))
            target.append(calibration_responses[si, ci])
    return np.linalg.lstsq(np.asarray(design), np.asarray(target), rcond=None)[0]


def predict_decoder(decoder: np.ndarray, state_features: np.ndarray, interventions: np.ndarray) -> np.ndarray:
    return np.array(
        [[bilinear_feature(r, c) @ decoder for c in interventions] for r in state_features],
        dtype=np.float64,
    )


def b0_current_function_features(states: list[GaugeState]) -> np.ndarray:
    return np.array([effective_weight(s) for s in states], dtype=np.float64)


def b1_summary_features(states: list[GaugeState]) -> np.ndarray:
    rows = []
    for s in states:
        singular_values = np.linalg.svd(s.U, compute_uv=False)
        row_norms = np.linalg.norm(s.U, axis=1)
        nonzero = row_norms[row_norms > 0.0]
        rows.append([
            np.linalg.norm(s.U), np.linalg.norm(s.v), singular_values.max(), singular_values.sum(),
            row_norms.max(), nonzero.min(),
        ])
    return np.asarray(rows, dtype=np.float64)


def raw_parameter_features(states: list[GaugeState]) -> np.ndarray:
    return np.array([np.concatenate([s.U.reshape(-1), s.v]) for s in states], dtype=np.float64)


def gram_features(states: list[GaugeState]) -> np.ndarray:
    rows = []
    for s in states:
        G = s.U.T @ s.U
        vals = [G[a, b] for a in range(INPUT_DIM) for b in range(a, INPUT_DIM)]
        vals.append(np.dot(s.v, s.v))
        rows.append(vals)
    return np.asarray(rows, dtype=np.float64)


def _fit_all(states: list[GaugeState], calibration_responses: np.ndarray):
    parts = partition_indices(states)
    train = parts["train"]
    fp = calibration_fingerprint(calibration_responses)

    resp_model = fit_pca2(fp[train])
    resp = transform_pca2(fp, resp_model)
    resp_decoder = fit_decoder(resp[train], CAL_INTERVENTIONS, calibration_responses[train])

    b0 = b0_current_function_features(states)
    b0_decoder = fit_decoder(b0[train], CAL_INTERVENTIONS, calibration_responses[train])

    b1 = b1_summary_features(states)
    b1_scaler = fit_standardizer(b1[train])
    b1z = transform_standardized(b1, b1_scaler)
    b1_decoder = fit_decoder(b1z[train], CAL_INTERVENTIONS, calibration_responses[train])

    theta = raw_parameter_features(states)
    raw_model = fit_pca2(theta[train])
    raw2 = transform_pca2(theta, raw_model)
    raw_decoder = fit_decoder(raw2[train], CAL_INTERVENTIONS, calibration_responses[train])

    grams = gram_features(states)
    gram_model = fit_pca2(grams[train])
    gram2 = transform_pca2(grams, gram_model)
    gram_decoder = fit_decoder(gram2[train], CAL_INTERVENTIONS, calibration_responses[train])

    fp_scaler = fit_standardizer(fp[train])
    fp16 = transform_standardized(fp, fp_scaler)
    c0_decoder = fit_decoder(fp16[train], CAL_INTERVENTIONS, calibration_responses[train])

    return parts, {
        "response": (resp, resp_decoder), "B0": (b0, b0_decoder), "B1": (b1z, b1_decoder),
        "B2": (raw2, raw_decoder), "B3": (gram2, gram_decoder), "C0": (fp16, c0_decoder),
    }, resp_decoder


def build_predictions(states: list[GaugeState], calibration_responses: np.ndarray) -> PredictionBundle:
    """Fit only on S_train/calibration and generate predictions without held-out truth."""
    parts, fitted, response_decoder = _fit_all(states, calibration_responses)
    predictions = {}
    for partition in ("nuis", "latent", "joint"):
        idx = parts[partition]
        pd = {name: predict_decoder(decoder, features[idx], HOLD_INTERVENTIONS)
              for name, (features, decoder) in fitted.items()}
        pd["C1"] = np.array(
            [[analytical_response(states[int(k)], c) for c in HOLD_INTERVENTIONS] for k in idx],
            dtype=np.float64,
        )
        null_features = np.roll(fitted["response"][0][idx], shift=1, axis=0)
        pd["N0"] = predict_decoder(response_decoder, null_features, HOLD_INTERVENTIONS)
        predictions[partition] = pd
    representations = {name: features for name, (features, _) in fitted.items() if name in ("response", "B2", "B3")}
    return PredictionBundle(predictions, representations, response_decoder, parts)


def generate_heldout_truth(states: list[GaugeState], partition: str) -> np.ndarray:
    """Evaluator-only held-out autograd truth, generated after prediction construction."""
    idx = partition_indices(states)[partition]
    return np.array([[autograd_response(states[int(k)], c) for c in HOLD_INTERVENTIONS] for k in idx], dtype=np.float64)


def evaluate_predictions(predictions: np.ndarray, truth: np.ndarray) -> MetricResult:
    pred = np.asarray(predictions, dtype=np.float64)
    truth = np.asarray(truth, dtype=np.float64)
    sse = float(np.sum((pred - truth) ** 2))
    held_mean = truth.mean(axis=0, keepdims=True)
    sst = float(np.sum((truth - held_mean) ** 2))
    r2 = 1.0 - sse / sst
    per = []
    for ci in range(truth.shape[1]):
        tc = truth[:, ci, :]
        pc = pred[:, ci, :]
        csse = float(np.sum((pc - tc) ** 2))
        cmean = tc.mean(axis=0, keepdims=True)
        csst = float(np.sum((tc - cmean) ** 2))
        per.append(1.0 - csse / csst)
    nrmse = float(np.sqrt(sse / float(np.sum(truth ** 2))))
    return MetricResult(float(r2), np.asarray(per, dtype=np.float64), nrmse)


def nuisance_fraction(states: list[GaugeState], representation: np.ndarray) -> float:
    R = np.asarray(representation, dtype=np.float64)
    latent_means = []
    within_sum = 0.0
    count = 0
    for i in range(len(GRID)):
        for j in range(len(GRID)):
            idx = [s.index for s in states if s.i == i and s.j == j]
            vals = R[idx]
            mu = vals.mean(axis=0)
            latent_means.append(mu)
            within_sum += float(np.sum((vals - mu) ** 2))
            count += len(idx)
    W = within_sum / count
    latent_means = np.asarray(latent_means, dtype=np.float64)
    mu = latent_means.mean(axis=0)
    B = float(np.mean(np.sum((latent_means - mu) ** 2, axis=1)))
    if W == 0.0 and B == 0.0:
        return 1.0
    return float(W / (W + B))


def invariant_errors(states: list[GaugeState]) -> dict[str, float]:
    current = max(float(np.max(np.abs(effective_weight(s)))) for s in states)
    frob = max(abs(float(np.linalg.norm(s.U)) - 2.0) for s in states)
    readout = max(abs(float(np.linalg.norm(s.v)) - 1.0) for s in states)
    orth = max(float(np.max(np.abs(rotation_matrix(float(phi)).T @ rotation_matrix(float(phi)) - np.eye(HIDDEN_DIM)))) for phi in PHI)
    p_orbit = 0.0
    response_orbit = 0.0
    all_interventions = np.vstack([CAL_INTERVENTIONS, HOLD_INTERVENTIONS])
    for i in range(len(GRID)):
        for j in range(len(GRID)):
            orbit = [s for s in states if s.i == i and s.j == j]
            p0 = plasticity_matrix(orbit[0])
            base = [analytical_response(orbit[0], c) for c in all_interventions]
            for s in orbit:
                p_orbit = max(p_orbit, float(np.max(np.abs(plasticity_matrix(s) - p0))))
                for ci, c in enumerate(all_interventions):
                    response_orbit = max(response_orbit, float(np.max(np.abs(analytical_response(s, c) - base[ci]))))
    return {
        "current_function": current, "frobenius_norm": frob, "readout_norm": readout,
        "orthogonality": orth, "P_orbit": p_orbit, "response_orbit": response_orbit,
    }


def audit_all_responses(states: list[GaugeState]) -> float:
    maximum = 0.0
    for s in states:
        for c in np.vstack([CAL_INTERVENTIONS, HOLD_INTERVENTIONS]):
            maximum = max(maximum, float(np.max(np.abs(analytical_response(s, c) - autograd_response(s, c)))))
    return maximum


def evaluate_bundle(states: list[GaugeState], bundle: PredictionBundle) -> dict[str, dict[str, MetricResult]]:
    out = {}
    for partition in ("nuis", "latent", "joint"):
        truth = generate_heldout_truth(states, partition)
        out[partition] = {name: evaluate_predictions(pred, truth) for name, pred in bundle.predictions[partition].items()}
    return out


def classify(metrics: Mapping[str, Mapping[str, MetricResult]], jvals: Mapping[str, float], sanity_ok: bool) -> str:
    if not sanity_ok:
        return "FAIL"
    joint, nuis, latent = metrics["joint"], metrics["nuis"], metrics["latent"]
    R_resp = joint["response"].r2_state
    R_raw = joint["B2"].r2_state
    R_nuis = nuis["response"].r2_state
    R_lat = latent["response"].r2_state
    R_min = float(np.min(joint["response"].per_intervention_r2))
    J_resp, J_raw = float(jvals["response"]), float(jvals["B2"])
    R_null = joint["N0"].r2_state
    if (R_resp >= 0.95 and R_nuis >= 0.95 and R_lat >= 0.95 and R_min >= 0.90
            and R_resp - R_raw >= 0.10 and J_resp <= 1e-8 and J_raw - J_resp >= 0.05
            and R_null <= 0.10):
        return "PASS"
    weak_ok = (
        R_resp >= 0.90 and R_nuis >= 0.90 and R_lat >= 0.90 and R_min >= 0.75
        and J_resp <= 1e-4 and R_null <= 0.25
        and ((R_resp - R_raw < 0.10) or (J_raw - J_resp < 0.05)
             or (R_resp < 0.95) or (R_nuis < 0.95) or (R_lat < 0.95) or (R_min < 0.90))
    )
    if weak_ok:
        return "WEAK"
    if (R_resp < 0.90 or R_nuis < 0.90 or R_lat < 0.90 or R_min < 0.75
            or J_resp > 1e-4 or R_resp <= R_raw):
        return "NULL"
    # Frozen rules are not total for a failed N0 alone; do not invent a post-hoc scientific category.
    return "FAIL"


def classification_gap(metrics: Mapping[str, Mapping[str, MetricResult]], jvals: Mapping[str, float], sanity_ok: bool) -> bool:
    if not sanity_ok:
        return False
    joint, nuis, latent = metrics["joint"], metrics["nuis"], metrics["latent"]
    R_resp = joint["response"].r2_state
    R_raw = joint["B2"].r2_state
    R_nuis = nuis["response"].r2_state
    R_lat = latent["response"].r2_state
    R_min = float(np.min(joint["response"].per_intervention_r2))
    J_resp, J_raw = float(jvals["response"]), float(jvals["B2"])
    R_null = joint["N0"].r2_state
    pass_ok = (R_resp >= .95 and R_nuis >= .95 and R_lat >= .95 and R_min >= .90 and R_resp - R_raw >= .10 and J_resp <= 1e-8 and J_raw - J_resp >= .05 and R_null <= .10)
    weak_ok = (R_resp >= .90 and R_nuis >= .90 and R_lat >= .90 and R_min >= .75 and J_resp <= 1e-4 and R_null <= .25 and ((R_resp - R_raw < .10) or (J_raw - J_resp < .05) or (R_resp < .95) or (R_nuis < .95) or (R_lat < .95) or (R_min < .90)))
    null_ok = (R_resp < .90 or R_nuis < .90 or R_lat < .90 or R_min < .75 or J_resp > 1e-4 or R_resp <= R_raw)
    return not (pass_ok or weak_ok or null_ok)
