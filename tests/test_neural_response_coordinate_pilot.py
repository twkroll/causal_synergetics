import inspect
import math

import numpy as np

from causal_synergetics.benchmarks.neural_response_coordinate import (
    ATOL,
    CAL_INTERVENTIONS,
    GRID,
    HOLD_INTERVENTIONS,
    PCA_DIM,
    MetricResult,
    audit_all_responses,
    b0_current_function_features,
    b1_summary_features,
    build_predictions,
    build_states,
    calibration_fingerprint,
    classify,
    evaluate_predictions,
    fit_decoder,
    fit_pca2,
    generate_heldout_truth,
    invariant_errors,
    oracle_predictions,
    predict_decoder,
    raw_parameter_features,
    response_cube,
    state_split,
)


def test_81_state_construction_and_deterministic_lexicographic_ordering() -> None:
    states = build_states()
    assert len(states) == 81
    assert (states[0].i, states[0].j, states[0].z1, states[0].z2) == (0, 0, -1.0, -1.0)
    assert (states[-1].i, states[-1].j, states[-1].z1, states[-1].z2) == (8, 8, 1.0, 1.0)
    assert [(s.z1, s.z2) for s in states] == [(float(z1), float(z2)) for z1 in GRID for z2 in GRID]


def test_current_function_and_frozen_norm_invariants() -> None:
    errors = invariant_errors(build_states())
    assert errors["current_function"] <= ATOL
    assert errors["frobenius_norm"] <= ATOL
    assert errors["readout_norm"] <= ATOL
    assert errors["q_bounds"] <= ATOL


def test_state_split_is_exact_checkerboard_41_40() -> None:
    states = build_states()
    train, test = state_split(states)
    assert len(train) == 41
    assert len(test) == 40
    assert set(train).isdisjoint(set(test))
    assert sorted(np.concatenate([train, test]).tolist()) == list(range(81))
    assert all((states[int(idx)].i + states[int(idx)].j) % 2 == 0 for idx in train)
    assert all((states[int(idx)].i + states[int(idx)].j) % 2 == 1 for idx in test)


def test_exact_calibration_and_heldout_interventions() -> None:
    expected_cal = np.array(
        [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]],
        dtype=np.float64,
    ) / 2.0
    expected_hold = np.array(
        [
            [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
            [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, -1], [0, 1, -1, 0],
        ], dtype=np.float64,
    )
    expected_hold[4:] /= math.sqrt(2.0)
    assert np.array_equal(CAL_INTERVENTIONS, expected_cal)
    assert np.allclose(HOLD_INTERVENTIONS, expected_hold, atol=0.0, rtol=0.0)


def test_all_972_analytical_autograd_responses_agree() -> None:
    assert audit_all_responses(build_states()) <= ATOL


def test_exact_oracle_agreement_on_heldout_truth() -> None:
    states = build_states()
    _, test = state_split(states)
    truth = generate_heldout_truth(states)
    oracle = oracle_predictions(states, test, HOLD_INTERVENTIONS)
    assert np.max(np.abs(oracle - truth)) <= ATOL


def test_response_and_raw_parameter_pca_are_exactly_two_dimensional() -> None:
    states = build_states()
    train, _ = state_split(states)
    cal = response_cube(states, CAL_INTERVENTIONS)
    fp = calibration_fingerprint(cal)
    response_pca = fit_pca2(fp[train])
    raw_pca = fit_pca2(raw_parameter_features(states)[train])
    assert PCA_DIM == 2
    assert response_pca.components.shape == (2, 16)
    assert raw_pca.components.shape == (2, 25)


def test_fit_and_predict_apis_accept_no_heldout_truth_argument() -> None:
    fit_names = set(inspect.signature(fit_decoder).parameters)
    predict_names = set(inspect.signature(predict_decoder).parameters)
    forbidden = {"heldout_truth", "heldout_responses", "truth", "hold_truth", "y_hold"}
    assert fit_names.isdisjoint(forbidden)
    assert predict_names.isdisjoint(forbidden)
    assert set(inspect.signature(build_predictions).parameters) == {"states", "calibration_responses"}


def test_deterministic_cyclic_null_is_exact_one_position_roll() -> None:
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    expected_null_features = np.roll(bundle.response_test_features, shift=1, axis=0)
    expected_null_predictions = predict_decoder(bundle.response_decoder, expected_null_features, HOLD_INTERVENTIONS)
    assert np.allclose(bundle.predictions["N0"], expected_null_predictions, atol=ATOL, rtol=0.0)


def test_frozen_pipeline_metrics_and_mechanical_weak_classification() -> None:
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    truth = generate_heldout_truth(states)
    metrics = {name: evaluate_predictions(pred, truth) for name, pred in bundle.predictions.items()}
    sanity = (
        invariant_errors(states)["current_function"] <= ATOL
        and invariant_errors(states)["frobenius_norm"] <= ATOL
        and invariant_errors(states)["readout_norm"] <= ATOL
        and audit_all_responses(states) <= ATOL
        and np.max(np.abs(bundle.predictions["C1"] - truth)) <= ATOL
        and metrics["C0"].r2_state >= 0.99
    )
    assert metrics["response"].r2_state >= 0.999999999999
    assert metrics["B2"].r2_state > 0.9998
    assert metrics["response"].r2_state - metrics["B2"].r2_state < 0.05
    assert metrics["N0"].r2_state <= 0.10
    assert classify(metrics, sanity) == "WEAK"


def test_metric_and_classification_threshold_logic_is_frozen() -> None:
    per_pass = np.full(8, 0.95)
    pass_metrics = {
        "response": MetricResult(0.96, per_pass, 0.01),
        "B0": MetricResult(0.60, per_pass, 0.1),
        "B1": MetricResult(0.70, per_pass, 0.1),
        "B2": MetricResult(0.90, per_pass, 0.1),
        "N0": MetricResult(0.10, per_pass, 0.2),
    }
    assert classify(pass_metrics, True) == "PASS"
    weak_metrics = dict(pass_metrics)
    weak_metrics["response"] = MetricResult(0.94, np.full(8, 0.80), 0.02)
    weak_metrics["B2"] = MetricResult(0.93, per_pass, 0.1)
    assert classify(weak_metrics, True) == "WEAK"
    null_metrics = dict(weak_metrics)
    null_metrics["B2"] = MetricResult(1.0, per_pass, 0.1)
    assert classify(null_metrics, True) == "NULL"
    assert classify(pass_metrics, False) == "FAIL"


def test_feature_shapes_and_full_fingerprint_ceiling() -> None:
    states = build_states()
    train, test = state_split(states)
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    truth = generate_heldout_truth(states)
    assert calibration_fingerprint(cal).shape == (81, 16)
    assert b0_current_function_features(states).shape == (81, 4)
    assert b1_summary_features(states).shape == (81, 6)
    assert raw_parameter_features(states).shape == (81, 25)
    assert bundle.response_train_features.shape == (41, 2)
    assert bundle.response_test_features.shape == (40, 2)
    assert bundle.raw2_train_features.shape == (41, 2)
    assert bundle.raw2_test_features.shape == (40, 2)
    assert len(train) == 41 and len(test) == 40
    assert evaluate_predictions(bundle.predictions["C0"], truth).r2_state >= 0.99
