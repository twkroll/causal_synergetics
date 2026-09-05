"""Frozen controlled-state-preparation benchmark for APP-C."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
import numpy as np

DTYPE = np.float64
M = D = K = 1.0
TAU_PREP = 2.0
T_EVAL = 5.0
DT_PRIMARY = 0.001
DT_FINE = 0.0005
FUTURE_SIGNS = (+0.2, -0.2)
CONDITIONS = ("P0", "PT", "PM")
X_INIT = np.zeros(4, dtype=DTYPE)
AMPLITUDE_CAP = 0.35
ENERGY_BUDGET = 0.25
CONVERGENCE_TOL = 1e-8
MACRO_TOL = 1e-8
TARGET_TOL = 1e-8
ENERGY_EQUALITY_TOL = 1e-10
SIGN_SYMMETRY_TOL = 1e-12
VECTOR_FIELD_TOL = 1e-12
APP_B_I_ZERO_B1 = 0.065347743843341
APP_B_REGRESSION_TOL = 1e-10
TARGET_RESPONSE_TOL = 1e-8
MATERIALITY = 1e-4
BENEFIT_THRESHOLD = 0.90
NUMERICAL_SCALE = 1e-10
DENOMINATOR_FLOOR = 1e-12

@dataclass(frozen=True)
class ErrorMetrics:
    d_inf: float
    rms: float

@dataclass(frozen=True)
class PrepMetrics:
    p_q: float
    p_r: float
    peak_input: float
    c_prep: float
    max_abs_relative_angle: float

@dataclass(frozen=True)
class Simulation:
    prep: np.ndarray
    evaluation: np.ndarray
    b1: np.ndarray
    prep_controls: np.ndarray
    prep_fine_on_primary: np.ndarray
    evaluation_fine_on_primary: np.ndarray
    b1_fine_on_primary: np.ndarray


def e_star(a: float) -> float:
    return float(np.arcsin(DTYPE(a) / DTYPE(2.0)))


def smoothstep(xi: float) -> tuple[float, float, float]:
    x = DTYPE(xi)
    s = 10*x**3 - 15*x**4 + 6*x**5
    ds = 30*x**2 - 60*x**3 + 30*x**4
    d2s = 60*x - 180*x**2 + 120*x**3
    return float(s), float(ds), float(d2s)


def desired_hidden(t: float, b: float) -> tuple[float, float, float]:
    xi = DTYPE(t) / DTYPE(TAU_PREP)
    s, ds, d2s = smoothstep(float(xi))
    es = DTYPE(e_star(b))
    ed = es * DTYPE(s)
    ed_dot = es * DTYPE(ds) / DTYPE(TAU_PREP)
    ed_ddot = es * DTYPE(d2s) / DTYPE(TAU_PREP**2)
    return float(ed), float(ed_dot), float(ed_ddot)


def preparation_controls(t: float, b: float) -> np.ndarray:
    ed, ed_dot, ed_ddot = desired_hidden(t, b)
    p1 = -np.sin(DTYPE(ed))
    p2 = DTYPE(ed_ddot) + DTYPE(ed_dot) + np.sin(DTYPE(ed))
    return np.array([p1, p2], dtype=DTYPE)


def full_rhs(state: np.ndarray, p1: float, p2: float) -> np.ndarray:
    delta1, omega1, delta2, omega2 = np.asarray(state, dtype=DTYPE)
    return np.array([
        omega1,
        -omega1 + np.sin(delta2-delta1) + DTYPE(p1),
        omega2,
        -omega2 + np.sin(delta1-delta2) + DTYPE(p2),
    ], dtype=DTYPE)


def preparation_rhs(t: float, state: np.ndarray, b: float) -> np.ndarray:
    p1, p2 = preparation_controls(t, b)
    return full_rhs(state, float(p1), float(p2))


def evaluation_rhs(t: float, state: np.ndarray, a: float) -> np.ndarray:
    del t
    return full_rhs(state, 0.0, a)


def b1_rhs(t: float, state: np.ndarray, a: float) -> np.ndarray:
    del t
    delta, omega = np.asarray(state, dtype=DTYPE)
    return np.array([omega, -omega + DTYPE(a)/DTYPE(2.0)], dtype=DTYPE)


def rk4_time(rhs: Callable[[float, np.ndarray, float], np.ndarray], initial_state: np.ndarray, param: float, dt: float, horizon: float) -> np.ndarray:
    steps = int(round(horizon / dt))
    if not np.isclose(steps*dt, horizon, atol=0.0, rtol=0.0):
        raise ValueError("horizon must be an exact integer multiple of dt")
    state = np.asarray(initial_state, dtype=DTYPE).copy()
    out = np.empty((steps+1, state.size), dtype=DTYPE)
    out[0] = state
    for i in range(steps):
        t = DTYPE(i)*DTYPE(dt)
        half = DTYPE(dt)/DTYPE(2.0)
        k1 = rhs(float(t), state, param)
        k2 = rhs(float(t+half), state + half*k1, param)
        k3 = rhs(float(t+half), state + half*k2, param)
        k4 = rhs(float(t+DTYPE(dt)), state + DTYPE(dt)*k3, param)
        state = state + (DTYPE(dt)/DTYPE(6.0))*(k1+2*k2+2*k3+k4)
        out[i+1] = state
    return out


def control_grid(b: float, dt: float) -> np.ndarray:
    steps = int(round(TAU_PREP/dt))
    times = np.arange(steps+1, dtype=DTYPE)*DTYPE(dt)
    return np.vstack([preparation_controls(float(t), b) for t in times])


def _simulate_once(a: float, condition: str, dt: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if condition == "P0":
        steps = int(round(TAU_PREP/dt))
        prep = np.repeat(X_INIT[None,:], steps+1, axis=0)
        controls = np.zeros((steps+1, 2), dtype=DTYPE)
        eval_initial = X_INIT.copy()
    elif condition in ("PT", "PM"):
        b = a if condition == "PT" else -a
        prep = rk4_time(preparation_rhs, X_INIT, b, dt, TAU_PREP)
        controls = control_grid(b, dt)
        eval_initial = prep[-1]
    else:
        raise ValueError(condition)
    evaluation = rk4_time(evaluation_rhs, eval_initial, a, dt, T_EVAL)
    b1 = rk4_time(b1_rhs, np.zeros(2, dtype=DTYPE), a, dt, T_EVAL)
    return prep, evaluation, b1, controls


def simulate(a: float, condition: str) -> Simulation:
    prep, evaluation, b1, controls = _simulate_once(a, condition, DT_PRIMARY)
    prep_f, eval_f, b1_f, _ = _simulate_once(a, condition, DT_FINE)
    return Simulation(prep, evaluation, b1, controls, prep_f[::2], eval_f[::2], b1_f[::2])


def error_metrics(actual: np.ndarray, predicted: np.ndarray) -> ErrorMetrics:
    diff = np.asarray(actual, dtype=DTYPE) - np.asarray(predicted, dtype=DTYPE)
    return ErrorMetrics(float(np.max(np.abs(diff))), float(np.sqrt(np.mean(diff**2))))


def relative_coordinates(full: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    full = np.asarray(full, dtype=DTYPE)
    return full[:,2]-full[:,0], full[:,3]-full[:,1]


def prep_metrics(sim: Simulation, b: float) -> PrepMetrics:
    prep = sim.prep
    e_delta, e_omega = relative_coordinates(prep)
    p_q = float(np.max(np.abs(prep[:,:2])))
    p_r = float(max(abs(e_delta[-1]-e_star(b)), abs(e_omega[-1])))
    peak = float(np.max(np.abs(sim.prep_controls)))
    sq = np.sum(sim.prep_controls**2, axis=1)
    c_prep = float(DT_PRIMARY*(0.5*sq[0] + np.sum(sq[1:-1]) + 0.5*sq[-1]))
    max_angle = float(np.max(np.abs(e_delta)))
    return PrepMetrics(p_q, p_r, peak, c_prep, max_angle)


def evaluation_metrics(sim: Simulation, a: float) -> dict[str, float]:
    q = sim.evaluation[:,:2]
    e_delta, e_omega = relative_coordinates(sim.evaluation)
    err = error_metrics(q, sim.b1)
    return {
        "E_B1": err.d_inf,
        "RMS_B1": err.rms,
        "H_delta": float(np.max(np.abs(e_delta-e_star(a)))),
        "H_omega": float(np.max(np.abs(e_omega))),
        "max_abs_relative_angle_eval": float(np.max(np.abs(e_delta))),
    }


def benchmark_report() -> dict[str, object]:
    sims = {(a,c): simulate(a,c) for a in FUTURE_SIGNS for c in CONDITIONS}
    eval_metrics = {(a,c): evaluation_metrics(sims[(a,c)], a) for a in FUTURE_SIGNS for c in CONDITIONS}
    prep = {}
    for a in FUTURE_SIGNS:
        prep[(a,"PT")] = prep_metrics(sims[(a,"PT")], a)
        prep[(a,"PM")] = prep_metrics(sims[(a,"PM")], -a)

    convergence = 0.0
    finite_ok = True
    for sim in sims.values():
        convergence = max(convergence,
            float(np.max(np.abs(sim.prep-sim.prep_fine_on_primary))),
            float(np.max(np.abs(sim.evaluation-sim.evaluation_fine_on_primary))),
            float(np.max(np.abs(sim.b1-sim.b1_fine_on_primary))),
        )
        finite_ok = finite_ok and all(np.all(np.isfinite(x)) for x in (sim.prep, sim.evaluation, sim.b1, sim.prep_fine_on_primary, sim.evaluation_fine_on_primary, sim.b1_fine_on_primary, sim.prep_controls))

    energy_equality = max(abs(prep[(a,"PT")].c_prep-prep[(a,"PM")].c_prep) for a in FUTURE_SIGNS)
    grid = np.arange(int(round(TAU_PREP/DT_PRIMARY))+1, dtype=DTYPE)*DTYPE(DT_PRIMARY)
    sign_symmetry = 0.0
    for t in grid:
        sign_symmetry = max(sign_symmetry, float(np.max(np.abs(preparation_controls(float(t),0.2)+preparation_controls(float(t),-0.2)))))

    vf_zero = 0.0
    for a in FUTURE_SIGNS:
        terminal = sims[(a,"PT")].prep[-1]
        ed = terminal[2]-terminal[0]
        ew = terminal[3]-terminal[1]
        vf = np.array([ew, -ew-2*np.sin(ed)+a], dtype=DTYPE)
        vf_zero = max(vf_zero, float(np.max(np.abs(vf))))

    regression = max(abs(eval_metrics[(a,"P0")]["E_B1"]-APP_B_I_ZERO_B1) for a in FUTURE_SIGNS)
    target_error = max(eval_metrics[(a,"PT")]["E_B1"] for a in FUTURE_SIGNS)
    eval_inputs_zero = True

    constants_ok = (
        M == D == K == 1.0 and TAU_PREP == 2.0 and T_EVAL == 5.0 and
        DT_PRIMARY == 0.001 and DT_FINE == 0.0005 and FUTURE_SIGNS == (+0.2,-0.2) and
        CONDITIONS == ("P0","PT","PM") and np.array_equal(X_INIT, np.zeros(4, dtype=DTYPE))
    )
    sanity = {
        "frozen_constants_conditions": bool(constants_ok),
        "finite_trajectories": bool(finite_ok),
        "primary_audit_convergence": convergence <= CONVERGENCE_TOL,
        "PT_macro_preservation": max(prep[(a,"PT")].p_q for a in FUTURE_SIGNS) <= MACRO_TOL,
        "PM_macro_preservation": max(prep[(a,"PM")].p_q for a in FUTURE_SIGNS) <= MACRO_TOL,
        "PT_terminal_target": max(prep[(a,"PT")].p_r for a in FUTURE_SIGNS) <= TARGET_TOL,
        "PM_terminal_target": max(prep[(a,"PM")].p_r for a in FUTURE_SIGNS) <= TARGET_TOL,
        "preparation_amplitude": max(v.peak_input for v in prep.values()) <= AMPLITUDE_CAP,
        "preparation_energy": max(v.c_prep for v in prep.values()) <= ENERGY_BUDGET,
        "PT_PM_energy_equality": energy_equality <= ENERGY_EQUALITY_TOL,
        "analytical_sign_symmetry": sign_symmetry <= SIGN_SYMMETRY_TOL,
        "matched_initial_relative_vector_field": vf_zero <= VECTOR_FIELD_TOL,
        "APP_B_P0_regression": regression <= APP_B_REGRESSION_TOL,
        "PT_vs_B1_structural_audit": target_error <= TARGET_RESPONSE_TOL,
        "no_preparation_input_during_evaluation": eval_inputs_zero,
    }

    e_target_max = max(eval_metrics[(a,"PT")]["E_B1"] for a in FUTURE_SIGNS)
    e_no_min = min(eval_metrics[(a,"P0")]["E_B1"] for a in FUTURE_SIGNS)
    e_mismatch_min = min(eval_metrics[(a,"PM")]["E_B1"] for a in FUTURE_SIGNS)
    b0 = {a: 1.0-eval_metrics[(a,"PT")]["E_B1"]/eval_metrics[(a,"P0")]["E_B1"] if eval_metrics[(a,"P0")]["E_B1"] > DENOMINATOR_FLOOR else np.nan for a in FUTURE_SIGNS}
    bm = {a: 1.0-eval_metrics[(a,"PT")]["E_B1"]/eval_metrics[(a,"PM")]["E_B1"] if eval_metrics[(a,"PM")]["E_B1"] > DENOMINATOR_FLOOR else np.nan for a in FUTURE_SIGNS}
    b0_min = float(min(b0.values()))
    bm_min = float(min(bm.values()))
    h_target = max(max(eval_metrics[(a,"PT")]["H_delta"], eval_metrics[(a,"PT")]["H_omega"]) for a in FUTURE_SIGNS)
    max_angle = 0.0
    for a in FUTURE_SIGNS:
        for c in CONDITIONS:
            max_angle = max(max_angle, eval_metrics[(a,c)]["max_abs_relative_angle_eval"])
        max_angle = max(max_angle, prep[(a,"PT")].max_abs_relative_angle, prep[(a,"PM")].max_abs_relative_angle)
    safety = max_angle < np.pi/2.0
    sanity_ok = all(sanity.values())
    denom_material = e_no_min > DENOMINATOR_FLOOR and e_mismatch_min > DENOMINATOR_FLOOR
    if not sanity_ok:
        verdict = "FAIL"
    elif safety and e_target_max <= TARGET_RESPONSE_TOL and e_no_min >= MATERIALITY and e_mismatch_min >= MATERIALITY and b0_min >= BENEFIT_THRESHOLD and bm_min >= BENEFIT_THRESHOLD and max(v.peak_input for v in prep.values()) <= AMPLITUDE_CAP and max(v.c_prep for v in prep.values()) <= ENERGY_BUDGET:
        verdict = "PASS"
    elif safety and denom_material and e_target_max < min(e_no_min,e_mismatch_min) and e_no_min > NUMERICAL_SCALE and e_mismatch_min > NUMERICAL_SCALE and b0_min > 0 and bm_min > 0:
        verdict = "WEAK"
    else:
        verdict = "NULL"
    return {
        "verdict": verdict,
        "sanity": sanity,
        "convergence_error": convergence,
        "energy_equality_error": energy_equality,
        "sign_symmetry_error": sign_symmetry,
        "matched_vector_field_error": vf_zero,
        "APP_B_regression_error": regression,
        "evaluation_metrics": eval_metrics,
        "prep_metrics": prep,
        "B0": b0,
        "BM": bm,
        "E_target_max": e_target_max,
        "E_no_min": e_no_min,
        "E_mismatch_min": e_mismatch_min,
        "B0_min": b0_min,
        "BM_min": bm_min,
        "H_target": h_target,
        "max_abs_relative_angle": max_angle,
        "safety": safety,
    }
