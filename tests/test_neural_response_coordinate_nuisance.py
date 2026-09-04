import inspect
import numpy as np

from causal_synergetics.benchmarks.neural_response_coordinate_nuisance import (
    ATOL,
    CAL_INTERVENTIONS,
    HOLD_INTERVENTIONS,
    PHI,
    PCA_DIM,
    audit_all_responses,
    build_predictions,
    build_states,
    calibration_fingerprint,
    classify,
    classification_gap,
    evaluate_bundle,
    fit_decoder,
    fit_pca2,
    generate_heldout_truth,
    gram_features,
    invariant_errors,
    nuisance_fraction,
    partition_indices,
    predict_decoder,
    raw_parameter_features,
    response_cube,
)


def test_state_count_order_and_partition_counts():
    states = build_states()
    parts = partition_indices(states)
    assert len(states) == 648
    assert [len(parts[k]) for k in ("train", "nuis", "latent", "joint")] == [164, 164, 160, 160]
    assert (states[0].i, states[0].j, states[0].phi_index) == (0, 0, 0)
    assert (states[-1].i, states[-1].j, states[-1].phi_index) == (8, 8, 7)


def test_frozen_interventions_and_angles():
    assert len(PHI) == 8
    assert np.allclose(PHI, np.arange(8) * np.pi / 4, atol=0, rtol=0)
    assert CAL_INTERVENTIONS.shape == (4, 4)
    assert HOLD_INTERVENTIONS.shape == (8, 4)


def test_exact_gauge_invariants():
    errors = invariant_errors(build_states())
    for key in ("current_function", "frobenius_norm", "readout_norm", "orthogonality", "P_orbit", "response_orbit"):
        assert errors[key] <= ATOL


def test_all_7776_analytical_autograd_responses_agree():
    assert audit_all_responses(build_states()) <= ATOL


def test_response_raw_and_gram_pca_are_exactly_2d():
    states = build_states()
    train = partition_indices(states)["train"]
    cal = response_cube(states, CAL_INTERVENTIONS)
    fp = calibration_fingerprint(cal)
    assert PCA_DIM == 2
    assert fit_pca2(fp[train]).components.shape == (2, 16)
    assert fit_pca2(raw_parameter_features(states)[train]).components.shape == (2, 25)
    assert fit_pca2(gram_features(states)[train]).components.shape == (2, 11)


def test_fit_predict_apis_accept_no_heldout_truth():
    forbidden = {"heldout_truth", "heldout_responses", "truth", "hold_truth", "y_hold"}
    assert set(inspect.signature(fit_decoder).parameters).isdisjoint(forbidden)
    assert set(inspect.signature(predict_decoder).parameters).isdisjoint(forbidden)
    assert set(inspect.signature(build_predictions).parameters) == {"states", "calibration_responses"}


def test_prediction_bundle_precedes_truth_generation():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    for partition in ("nuis", "latent", "joint"):
        assert bundle.predictions[partition]["response"].shape[1:] == (8, 4)
        truth = generate_heldout_truth(states, partition)
        assert truth.shape == bundle.predictions[partition]["response"].shape


def test_candidate_b3_and_c0_are_exact_predictors():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    metrics = evaluate_bundle(states, bundle)
    for partition in ("nuis", "latent", "joint"):
        assert metrics[partition]["response"].r2_state >= 0.999999999999
        assert metrics[partition]["B3"].r2_state >= 0.999999999999
        assert metrics[partition]["C0"].r2_state >= 0.999999999999
        assert metrics[partition]["C1"].r2_state >= 0.999999999999


def test_nuisance_fractions_match_frozen_semantics():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    j_resp = nuisance_fraction(states, bundle.representations["response"])
    j_b2 = nuisance_fraction(states, bundle.representations["B2"])
    j_b3 = nuisance_fraction(states, bundle.representations["B3"])
    assert j_resp <= 1e-8
    assert j_b2 - j_resp >= 0.05
    assert j_b3 <= 1e-8


def test_naive_b2_fails_joint_gauge_generalisation():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    metrics = evaluate_bundle(states, bundle)
    assert metrics["joint"]["response"].r2_state >= 0.95
    assert metrics["joint"]["response"].r2_state - metrics["joint"]["B2"].r2_state >= 0.10


def test_frozen_cyclic_null_is_one_position_and_high_due_duplicate_gauge_orbits():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    metrics = evaluate_bundle(states, bundle)
    idx = bundle.partitions["joint"]
    expected = predict_decoder(
        bundle.response_decoder,
        np.roll(bundle.representations["response"][idx], 1, axis=0),
        HOLD_INTERVENTIONS,
    )
    assert np.allclose(expected, bundle.predictions["joint"]["N0"], atol=ATOL, rtol=0)
    assert metrics["joint"]["N0"].r2_state > 0.25


def test_mechanical_rule_exposes_frozen_classification_gap_without_retuning():
    states = build_states()
    cal = response_cube(states, CAL_INTERVENTIONS)
    bundle = build_predictions(states, cal)
    metrics = evaluate_bundle(states, bundle)
    jvals = {key: nuisance_fraction(states, bundle.representations[key]) for key in ("response", "B2", "B3")}
    errors = invariant_errors(states)
    sanity = (
        len(states) == 648
        and all(errors[key] <= ATOL for key in ("current_function", "frobenius_norm", "readout_norm", "orthogonality", "P_orbit", "response_orbit"))
        and audit_all_responses(states) <= ATOL
        and metrics["joint"]["C0"].r2_state >= 0.99
        and metrics["joint"]["B3"].r2_state >= 0.95
        and jvals["B3"] <= 1e-8
    )
    assert sanity
    assert classification_gap(metrics, jvals, sanity)
    assert classify(metrics, jvals, sanity) == "FAIL"
