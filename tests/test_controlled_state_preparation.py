import numpy as np
from causal_synergetics.benchmarks.controlled_state_preparation import (
    M,D,K,TAU_PREP,T_EVAL,DT_PRIMARY,DT_FINE,FUTURE_SIGNS,CONDITIONS,X_INIT,
    AMPLITUDE_CAP,ENERGY_BUDGET,APP_B_I_ZERO_B1,e_star,preparation_controls,
    evaluation_rhs,benchmark_report,
)

def test_frozen_constants_and_conditions():
    assert M == D == K == 1.0
    assert TAU_PREP == 2.0 and T_EVAL == 5.0
    assert DT_PRIMARY == 0.001 and DT_FINE == 0.0005
    assert FUTURE_SIGNS == (+0.2,-0.2)
    assert CONDITIONS == ("P0","PT","PM")
    assert np.array_equal(X_INIT, np.zeros(4,dtype=np.float64))

def test_analytic_preparation_symmetry_and_evaluation_input_separation():
    for t in np.linspace(0.0, TAU_PREP, 101):
        assert np.max(np.abs(preparation_controls(float(t),0.2)+preparation_controls(float(t),-0.2))) <= 1e-12
    zero = np.zeros(4,dtype=np.float64)
    assert np.array_equal(evaluation_rhs(0.0, zero, 0.2), np.array([0.0,0.0,0.0,0.2]))

def test_all_mandatory_numerical_checks():
    r = benchmark_report()
    assert all(r["sanity"].values())
    assert r["convergence_error"] <= 1e-8
    assert r["APP_B_regression_error"] <= 1e-10
    assert all(abs(r["evaluation_metrics"][(a,"P0")]["E_B1"]-APP_B_I_ZERO_B1) <= 1e-10 for a in FUTURE_SIGNS)
    assert max(v.peak_input for v in r["prep_metrics"].values()) <= AMPLITUDE_CAP
    assert max(v.c_prep for v in r["prep_metrics"].values()) <= ENERGY_BUDGET

def test_targeted_preparation_reaches_forced_relative_equilibrium():
    r = benchmark_report()
    for a in FUTURE_SIGNS:
        assert r["prep_metrics"][(a,"PT")].p_q <= 1e-8
        assert r["prep_metrics"][(a,"PT")].p_r <= 1e-8
        assert r["evaluation_metrics"][(a,"PT")]["E_B1"] <= 1e-8
        assert abs(e_star(a)-np.arcsin(a/2.0)) == 0.0

def test_frozen_classifier_is_pass():
    r = benchmark_report()
    assert r["safety"]
    assert r["E_target_max"] <= 1e-8
    assert r["E_no_min"] >= 1e-4
    assert r["E_mismatch_min"] >= 1e-4
    assert r["B0_min"] >= 0.90
    assert r["BM_min"] >= 0.90
    assert r["verdict"] == "PASS"
