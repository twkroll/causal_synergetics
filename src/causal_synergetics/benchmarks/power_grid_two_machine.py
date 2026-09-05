"""Frozen two-machine power-grid minimal benchmark for APP-B."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

DTYPE = np.float64
M = D = K = 1.0
T = 5.0
DT_PRIMARY = 0.001
DT_FINE = 0.0005
AMPLITUDES = {"u0": 0.0, "u_plus": 0.2, "u_minus": -0.2}
INITIAL_STATES = {
    "I_minus": np.array([0.0, -0.1, 0.0, -0.1], dtype=DTYPE),
    "I_zero": np.array([0.0, 0.0, 0.0, 0.0], dtype=DTYPE),
    "I_plus": np.array([0.0, 0.1, 0.0, 0.1], dtype=DTYPE),
}
CONVERGENCE_TOL = 1e-8
PASSIVE_COHERENCY_TOL = 1e-12
PASSIVE_B0_TOL = 1e-10
MEAN_CLOSURE_TOL = 1e-10
SYMMETRY_TOL = 1e-10
MATERIALITY = 1e-4
NUMERICAL_SCALE = 1e-10


@dataclass(frozen=True)
class ErrorMetrics:
    d_inf: float
    e_delta: float
    e_omega: float
    rms: float


@dataclass(frozen=True)
class TrajectoryBundle:
    full: np.ndarray
    b0: np.ndarray
    b1: np.ndarray
    full_fine_on_primary: np.ndarray
    b0_fine_on_primary: np.ndarray
    b1_fine_on_primary: np.ndarray


def full_rhs(state: np.ndarray, u: float) -> np.ndarray:
    delta1, omega1, delta2, omega2 = np.asarray(state, dtype=DTYPE)
    return np.array(
        [
            omega1,
            -omega1 + np.sin(delta2 - delta1),
            omega2,
            -omega2 + np.sin(delta1 - delta2) + u,
        ],
        dtype=DTYPE,
    )


def qr_coordinates(state: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    delta1, omega1, delta2, omega2 = np.asarray(state, dtype=DTYPE)
    q = np.array([delta1, omega1], dtype=DTYPE)
    r = np.array([delta2 - delta1, omega2 - omega1], dtype=DTYPE)
    return q, r


def b0_rhs(state: np.ndarray, u: float) -> np.ndarray:
    del u
    delta, omega = np.asarray(state, dtype=DTYPE)
    return np.array([omega, -omega], dtype=DTYPE)


def b1_rhs(state: np.ndarray, u: float) -> np.ndarray:
    delta, omega = np.asarray(state, dtype=DTYPE)
    return np.array([omega, -omega + u / 2.0], dtype=DTYPE)


def controlled_invariance_defect(u: float) -> np.ndarray:
    return np.array([0.0, u], dtype=DTYPE)


def rk4(
    rhs: Callable[[np.ndarray, float], np.ndarray],
    initial_state: np.ndarray,
    u: float,
    dt: float,
    horizon: float = T,
) -> np.ndarray:
    steps = int(round(horizon / dt))
    if not np.isclose(steps * dt, horizon, atol=0.0, rtol=0.0):
        raise ValueError("horizon must be an exact integer multiple of dt")
    state = np.asarray(initial_state, dtype=DTYPE).copy()
    trajectory = np.empty((steps + 1, state.size), dtype=DTYPE)
    trajectory[0] = state
    for index in range(steps):
        k1 = rhs(state, u)
        k2 = rhs(state + (dt / 2.0) * k1, u)
        k3 = rhs(state + (dt / 2.0) * k2, u)
        k4 = rhs(state + dt * k3, u)
        state = state + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        trajectory[index + 1] = state
    return trajectory


def error_metrics(actual: np.ndarray, predicted: np.ndarray) -> ErrorMetrics:
    difference = np.asarray(actual, dtype=DTYPE) - np.asarray(predicted, dtype=DTYPE)
    componentwise = np.max(np.abs(difference), axis=0)
    return ErrorMetrics(
        d_inf=float(np.max(componentwise)),
        e_delta=float(componentwise[0]),
        e_omega=float(componentwise[1]),
        rms=float(np.sqrt(np.mean(difference**2))),
    )


def simulate_bundle(initial_state: np.ndarray, u: float) -> TrajectoryBundle:
    q0 = np.asarray(initial_state, dtype=DTYPE)[:2]
    full = rk4(full_rhs, initial_state, u, DT_PRIMARY)
    b0 = rk4(b0_rhs, q0, u, DT_PRIMARY)
    b1 = rk4(b1_rhs, q0, u, DT_PRIMARY)
    full_fine = rk4(full_rhs, initial_state, u, DT_FINE)[::2]
    b0_fine = rk4(b0_rhs, q0, u, DT_FINE)[::2]
    b1_fine = rk4(b1_rhs, q0, u, DT_FINE)[::2]
    return TrajectoryBundle(full, b0, b1, full_fine, b0_fine, b1_fine)


def generate_all_trajectories() -> dict[tuple[str, str], TrajectoryBundle]:
    return {
        (initial_name, intervention_name): simulate_bundle(initial_state, u)
        for initial_name, initial_state in INITIAL_STATES.items()
        for intervention_name, u in AMPLITUDES.items()
    }


def _max_state_convergence(bundle: TrajectoryBundle) -> float:
    return float(
        max(
            np.max(np.abs(bundle.full - bundle.full_fine_on_primary)),
            np.max(np.abs(bundle.b0 - bundle.b0_fine_on_primary)),
            np.max(np.abs(bundle.b1 - bundle.b1_fine_on_primary)),
        )
    )


def _mean_coordinate(full: np.ndarray) -> np.ndarray:
    return np.column_stack(
        ((full[:, 0] + full[:, 2]) / 2.0, (full[:, 1] + full[:, 3]) / 2.0)
    ).astype(DTYPE, copy=False)


def benchmark_report() -> dict[str, object]:
    trajectories = generate_all_trajectories()
    pair_metrics: dict[tuple[str, str], dict[str, object]] = {}

    convergence_error = 0.0
    passive_coherency_error = 0.0
    mean_closure_error = 0.0
    finite_ok = True
    h_delta = 0.0
    h_omega = 0.0

    for key, bundle in trajectories.items():
        initial_name, intervention_name = key
        u = AMPLITUDES[intervention_name]
        full = bundle.full
        q_full = full[:, :2]
        e_delta = full[:, 2] - full[:, 0]
        e_omega = full[:, 3] - full[:, 1]
        pair_h_delta = float(np.max(np.abs(e_delta)))
        pair_h_omega = float(np.max(np.abs(e_omega)))
        convergence = _max_state_convergence(bundle)
        mean_closure = float(np.max(np.abs(_mean_coordinate(full) - bundle.b1)))
        b0_error = error_metrics(q_full, bundle.b0)
        b1_error = error_metrics(q_full, bundle.b1)

        finite_ok = finite_ok and all(
            np.all(np.isfinite(array))
            for array in (
                bundle.full,
                bundle.b0,
                bundle.b1,
                bundle.full_fine_on_primary,
                bundle.b0_fine_on_primary,
                bundle.b1_fine_on_primary,
            )
        )
        convergence_error = max(convergence_error, convergence)
        mean_closure_error = max(mean_closure_error, mean_closure)
        if u == 0.0:
            passive_coherency_error = max(passive_coherency_error, pair_h_delta, pair_h_omega)
        else:
            h_delta = max(h_delta, pair_h_delta)
            h_omega = max(h_omega, pair_h_omega)

        pair_metrics[key] = {
            "B0": b0_error,
            "B1": b1_error,
            "max_abs_e_delta": pair_h_delta,
            "max_abs_e_omega": pair_h_omega,
            "mean_closure_error": mean_closure,
            "convergence_error": convergence,
            "initial_name": initial_name,
            "intervention_name": intervention_name,
        }

    symmetry_error = 0.0
    for initial_name in INITIAL_STATES:
        for field in ("full", "b0", "b1"):
            passive = getattr(trajectories[(initial_name, "u0")], field)
            positive = getattr(trajectories[(initial_name, "u_plus")], field)
            negative = getattr(trajectories[(initial_name, "u_minus")], field)
            odd_defect = (positive - passive) + (negative - passive)
            symmetry_error = max(symmetry_error, float(np.max(np.abs(odd_defect))))

    passive_b0_error = max(pair_metrics[(name, "u0")]["B0"].d_inf for name in INITIAL_STATES)
    controlled_keys = [
        (name, sign)
        for name in INITIAL_STATES
        for sign in ("u_plus", "u_minus")
    ]
    e_b0_min = min(pair_metrics[key]["B0"].d_inf for key in controlled_keys)
    e_b1_min = min(pair_metrics[key]["B1"].d_inf for key in controlled_keys)

    constants_ok = (
        M == D == K == 1.0
        and T == 5.0
        and DT_PRIMARY == 0.001
        and DT_FINE == 0.0005
        and AMPLITUDES == {"u0": 0.0, "u_plus": 0.2, "u_minus": -0.2}
        and np.array_equal(INITIAL_STATES["I_minus"], np.array([0.0, -0.1, 0.0, -0.1], dtype=DTYPE))
        and np.array_equal(INITIAL_STATES["I_zero"], np.zeros(4, dtype=DTYPE))
        and np.array_equal(INITIAL_STATES["I_plus"], np.array([0.0, 0.1, 0.0, 0.1], dtype=DTYPE))
    )
    trajectory_count_ok = len(trajectories) == 9
    defect_ok = all(
        np.array_equal(controlled_invariance_defect(u), np.array([0.0, u], dtype=DTYPE))
        for u in AMPLITUDES.values()
    )

    sanity = {
        "frozen_constants_states_interventions": bool(constants_ok),
        "exact_trajectory_count": bool(trajectory_count_ok),
        "finite_states": bool(finite_ok),
        "convergence": convergence_error <= CONVERGENCE_TOL,
        "passive_coherency": passive_coherency_error <= PASSIVE_COHERENCY_TOL,
        "passive_full_vs_B0": passive_b0_error <= PASSIVE_B0_TOL,
        "mean_COI_vs_B1": mean_closure_error <= MEAN_CLOSURE_TOL,
        "odd_sign_symmetry": symmetry_error <= SYMMETRY_TOL,
        "controlled_invariance_defect": bool(defect_ok),
    }
    sanity_ok_without_regression = all(sanity.values())

    if not sanity_ok_without_regression:
        verdict = "FAIL"
    elif (
        h_delta < np.pi / 2.0
        and passive_b0_error <= PASSIVE_B0_TOL
        and e_b0_min >= MATERIALITY
        and e_b1_min >= MATERIALITY
    ):
        verdict = "PASS"
    elif h_delta < np.pi / 2.0 and min(e_b0_min, e_b1_min) > NUMERICAL_SCALE:
        verdict = "WEAK"
    else:
        verdict = "NULL"

    return {
        "verdict_without_regression": verdict,
        "sanity": sanity,
        "pair_metrics": pair_metrics,
        "E_pass": float(passive_b0_error),
        "E_B0_min": float(e_b0_min),
        "E_B1_min": float(e_b1_min),
        "H_delta": float(h_delta),
        "H_omega": float(h_omega),
        "mean_closure_error": float(mean_closure_error),
        "convergence_error": float(convergence_error),
        "symmetry_error": float(symmetry_error),
        "trajectories": trajectories,
    }
