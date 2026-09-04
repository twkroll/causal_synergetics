"""Frozen Neural Response Coordinate Pilot 0.1 for APP-A."""

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
DTYPE = torch.float64

CAL_INTERVENTIONS = np.array(
    [
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, -1.0, -1.0],
        [1.0, -1.0, 1.0, -1.0],
        [1.0, -1.0, -1.0, 1.0],
    ],
    dtype=np.float64,
) / 2.0

HOLD_INTERVENTIONS = np.array(
    [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, -1.0],
        [0.0, 1.0, -1.0, 0.0],
    ],
    dtype=np.float64,
)
HOLD_INTERVENTIONS[4:] /= np.sqrt(2.0)


@dataclass(frozen=True)
class FrozenState:
    index: int
    i: int
    j: int
    z1: float
    z2: float
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
    predictions: Mapping[str, np.ndarray]
    response_train_features: np.ndarray
    response_test_features: np.ndarray
    raw2_train_features: np.ndarray
    raw2_test_features: np.ndarray
    response_decoder: np.ndarray


def build_states() -> list[FrozenState]:
    states: list[FrozenState] = []
    index = 0
    v = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float64)
    for i, z1 in enumerate(GRID):
        for j, z2 in enumerate(GRID):
            q = np.array(
                [1.0 + RHO * z1, 1.0 - RHO * z1, 1.0 + RHO * z2, 1.0 - RHO * z2],
                dtype=np.float64,
            )
            U = np.zeros((HIDDEN_DIM, INPUT_DIM), dtype=np.float64)
            U[1:5, :] = np.diag(np.sqrt(q))
            states.append(FrozenState(index, i, j, float(z1), float(z2), U, v.copy()))
            index += 1
    return states


def state_split(states: list[FrozenState]) -> tuple[np.ndarray, np.ndarray]:
    train = np.array([s.index for s in states if (s.i + s.j) % 2 == 0], dtype=np.int64)
    test = np.array([s.index for s in states if (s.i + s.j) % 2 == 1], dtype=np.int64)
    return train, test


def effective_weight(state: FrozenState) -> np.ndarray:
    return state.U.T @ state.v


def plasticity_matrix(state: FrozenState) -> np.ndarray:
    return state.U.T @ state.U + np.dot(state.v, state.v) * np.eye(INPUT_DIM, dtype=np.float64)


def analytical_response(state: FrozenState, c: np.ndarray) -> np.ndarray:
    return ETA * (plasticity_matrix(state) @ np.asarray(c, dtype=np.float64))


def autograd_response(state: FrozenState, c: np.ndarray) -> np.ndarray:
    U = torch.tensor(state.U, dtype=DTYPE, requires_grad=True)
    v = torch.tensor(state.v, dtype=DTYPE, requires_grad=True)
    target = torch.tensor(np.asarray(c, dtype=np.float64), dtype=DTYPE)
    w = U.T @ v
    loss = 0.5 * torch.sum((w - target) ** 2)
    loss.backward()
    with torch.no_grad():
        U_plus = U - ETA * U.grad
        v_plus = v - ETA * v.grad
        w_plus = U_plus.T @ v_plus
    return w_plus.cpu().numpy()


def response_cube(states: list[FrozenState], interventions: np.ndarray, *, autograd: bool = False) -> np.ndarray:
    fn = autograd_response if autograd else analytical_response
    return np.array([[fn(state, c) for c in interventions] for state in states], dtype=np.float64)


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
    r_arr = np.asarray(r, dtype=np.float64).reshape(-1)
    c_arr = np.asarray(c, dtype=np.float64).reshape(INPUT_DIM)
    return np.concatenate([c_arr] + [value * c_arr for value in r_arr])


def fit_decoder(state_features: np.ndarray, interventions: np.ndarray, calibration_responses: np.ndarray) -> np.ndarray:
    """Fit OLS on calibration responses only; no held-out truth is accepted."""
    R = np.asarray(state_features, dtype=np.float64)
    C = np.asarray(interventions, dtype=np.float64)
    Y = np.asarray(calibration_responses, dtype=np.float64)
    design = []
    target = []
    for si, r in enumerate(R):
        for ci, c in enumerate(C):
            design.append(bilinear_feature(r, c))
            target.append(Y[si, ci])
    coef, _, _, _ = np.linalg.lstsq(np.asarray(design), np.asarray(target), rcond=None)
    return coef


def predict_decoder(decoder: np.ndarray, state_features: np.ndarray, interventions: np.ndarray) -> np.ndarray:
    """Predict from fitted state features and intervention descriptors only."""
    R = np.asarray(state_features, dtype=np.float64)
    C = np.asarray(interventions, dtype=np.float64)
    return np.array([[bilinear_feature(r, c) @ decoder for c in C] for r in R], dtype=np.float64)


def b0_current_function_features(states: list[FrozenState]) -> np.ndarray:
    return np.array([effective_weight(s) for s in states], dtype=np.float64)


def b1_summary_features(states: list[FrozenState]) -> np.ndarray:
    rows = []
    for state in states:
        U = state.U
        singular_values = np.linalg.svd(U, compute_uv=False)
        row_norms = np.linalg.norm(U, axis=1)
        nonzero = row_norms[row_norms > 0.0]
        rows.append(
            [
                np.linalg.norm(U),
                np.linalg.norm(state.v),
                singular_values.max(),
                singular_values.sum(),
                row_norms.max(),
                nonzero.min(),
            ]
        )
    return np.asarray(rows, dtype=np.float64)


def raw_parameter_features(states: list[FrozenState]) -> np.ndarray:
    return np.array([np.concatenate([s.U.reshape(-1), s.v]) for s in states], dtype=np.float64)


def oracle_predictions(states: list[FrozenState], test_indices: np.ndarray, interventions: np.ndarray) -> np.ndarray:
    return np.array(
        [[analytical_response(states[int(idx)], c) for c in interventions] for idx in test_indices],
        dtype=np.float64,
    )


def build_predictions(states: list[FrozenState], calibration_responses: np.ndarray) -> PredictionBundle:
    """Fit all frozen models and generate held-out predictions without held-out truth."""
    train_idx, test_idx = state_split(states)
    fingerprint = calibration_fingerprint(calibration_responses)

    resp_pca = fit_pca2(fingerprint[train_idx])
    resp_all = transform_pca2(fingerprint, resp_pca)
    resp_decoder = fit_decoder(resp_all[train_idx], CAL_INTERVENTIONS, calibration_responses[train_idx])
    pred_resp = predict_decoder(resp_decoder, resp_all[test_idx], HOLD_INTERVENTIONS)

    b0 = b0_current_function_features(states)
    b0_decoder = fit_decoder(b0[train_idx], CAL_INTERVENTIONS, calibration_responses[train_idx])
    pred_b0 = predict_decoder(b0_decoder, b0[test_idx], HOLD_INTERVENTIONS)

    b1 = b1_summary_features(states)
    b1_scaler = fit_standardizer(b1[train_idx])
    b1_all = transform_standardized(b1, b1_scaler)
    b1_decoder = fit_decoder(b1_all[train_idx], CAL_INTERVENTIONS, calibration_responses[train_idx])
    pred_b1 = predict_decoder(b1_decoder, b1_all[test_idx], HOLD_INTERVENTIONS)

    theta = raw_parameter_features(states)
    raw_pca = fit_pca2(theta[train_idx])
    raw2_all = transform_pca2(theta, raw_pca)
    raw2_decoder = fit_decoder(raw2_all[train_idx], CAL_INTERVENTIONS, calibration_responses[train_idx])
    pred_b2 = predict_decoder(raw2_decoder, raw2_all[test_idx], HOLD_INTERVENTIONS)

    fp_scaler = fit_standardizer(fingerprint[train_idx])
    fp_all = transform_standardized(fingerprint, fp_scaler)
    c0_decoder = fit_decoder(fp_all[train_idx], CAL_INTERVENTIONS, calibration_responses[train_idx])
    pred_c0 = predict_decoder(c0_decoder, fp_all[test_idx], HOLD_INTERVENTIONS)

    pred_c1 = oracle_predictions(states, test_idx, HOLD_INTERVENTIONS)

    null_features = np.roll(resp_all[test_idx], shift=1, axis=0)
    pred_n0 = predict_decoder(resp_decoder, null_features, HOLD_INTERVENTIONS)

    predictions = {
        "response": pred_resp,
        "B0": pred_b0,
        "B1": pred_b1,
        "B2": pred_b2,
        "C0": pred_c0,
        "C1": pred_c1,
        "N0": pred_n0,
    }
    return PredictionBundle(
        predictions=predictions,
        response_train_features=resp_all[train_idx],
        response_test_features=resp_all[test_idx],
        raw2_train_features=raw2_all[train_idx],
        raw2_test_features=raw2_all[test_idx],
        response_decoder=resp_decoder,
    )


def generate_heldout_truth(states: list[FrozenState]) -> np.ndarray:
    """Evaluator-only generation of held-out autograd truth for test states."""
    _, test_idx = state_split(states)
    return np.array(
        [[autograd_response(states[int(idx)], c) for c in HOLD_INTERVENTIONS] for idx in test_idx],
        dtype=np.float64,
    )


def evaluate_predictions(predictions: np.ndarray, heldout_truth: np.ndarray) -> MetricResult:
    pred = np.asarray(predictions, dtype=np.float64)
    truth = np.asarray(heldout_truth, dtype=np.float64)
    sse = float(np.sum((pred - truth) ** 2))
    held_means = truth.mean(axis=0, keepdims=True)
    sst = float(np.sum((truth - held_means) ** 2))
    r2 = 1.0 - sse / sst
    per = []
    for ci in range(truth.shape[1]):
        c_truth = truth[:, ci, :]
        c_pred = pred[:, ci, :]
        c_sse = float(np.sum((c_pred - c_truth) ** 2))
        c_mean = c_truth.mean(axis=0, keepdims=True)
        c_sst = float(np.sum((c_truth - c_mean) ** 2))
        per.append(1.0 - c_sse / c_sst)
    denominator = float(np.sum(truth**2))
    nrmse = float(np.sqrt(sse / denominator))
    return MetricResult(float(r2), np.asarray(per, dtype=np.float64), nrmse)


def audit_all_responses(states: list[FrozenState]) -> float:
    all_interventions = np.vstack([CAL_INTERVENTIONS, HOLD_INTERVENTIONS])
    maximum = 0.0
    for state in states:
        for c in all_interventions:
            err = np.max(np.abs(analytical_response(state, c) - autograd_response(state, c)))
            maximum = max(maximum, float(err))
    return maximum


def invariant_errors(states: list[FrozenState]) -> dict[str, float]:
    current_function_error = max(float(np.max(np.abs(effective_weight(s)))) for s in states)
    frobenius_error = max(abs(float(np.linalg.norm(s.U)) - 2.0) for s in states)
    readout_error = max(abs(float(np.linalg.norm(s.v)) - 1.0) for s in states)
    q_bounds_error = 0.0
    for s in states:
        q = np.diag(s.U[1:, :]) ** 2
        q_bounds_error = max(q_bounds_error, max(0.5 - float(q.min()), float(q.max()) - 1.5, 0.0))
    return {
        "current_function": current_function_error,
        "frobenius_norm": frobenius_error,
        "readout_norm": readout_error,
        "q_bounds": q_bounds_error,
    }


def classify(metrics: Mapping[str, MetricResult], sanity_ok: bool) -> str:
    if not sanity_ok:
        return "FAIL"
    r_resp = metrics["response"].r2_state
    r_func = metrics["B0"].r2_state
    r_norm = metrics["B1"].r2_state
    r_raw2 = metrics["B2"].r2_state
    r_null = metrics["N0"].r2_state
    r_min = float(np.min(metrics["response"].per_intervention_r2))

    pass_ok = (
        r_resp >= 0.95
        and r_min >= 0.90
        and r_resp - r_func >= 0.25
        and r_resp - r_norm >= 0.20
        and r_resp - r_raw2 >= 0.05
        and r_null <= 0.10
    )
    if pass_ok:
        return "PASS"

    weak_ok = (
        r_resp >= 0.90
        and r_min >= 0.75
        and r_resp - r_func >= 0.10
        and r_resp - r_norm >= 0.10
        and r_resp - r_raw2 > -0.05
        and r_null <= 0.25
    )
    return "WEAK" if weak_ok else "NULL"
