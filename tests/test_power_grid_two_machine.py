import numpy as np

from causal_synergetics.benchmarks.power_grid_two_machine import (
    AMPLITUDES,
    D,
    DT_FINE,
    DT_PRIMARY,
    INITIAL_STATES,
    K,
    M,
    T,
    b0_rhs,
    b1_rhs,
    benchmark_report,
    controlled_invariance_defect,
    full_rhs,
    generate_all_trajectories,
    qr_coordinates,
)


def test_frozen_specification_and_qr_transform() -> None:
    assert M == D == K == 1.0
    assert T == 5.0
    assert DT_PRIMARY == 0.001
    assert DT_FINE == 0.0005
    assert AMPLITUDES == {"u0": 0.0, "u_plus": 0.2, "u_minus": -0.2}
    assert set(INITIAL_STATES) == {"I_minus", "I_zero", "I_plus"}
    q, r = qr_coordinates(np.array([0.2, -0.3, 0.7, 0.4], dtype=np.float64))
    assert np.array_equal(q, np.array([0.2, -0.3]))
    assert np.allclose(r, np.array([0.5, 0.7]), atol=1e-15, rtol=0.0)


def test_rhs_and_controlled_invariance_defect() -> None:
    zero = np.zeros(4, dtype=np.float64)
    assert np.array_equal(full_rhs(zero, 0.2), np.array([0.0, 0.0, 0.0, 0.2]))
    assert np.array_equal(b0_rhs(np.zeros(2), 0.2), np.zeros(2))
    assert np.array_equal(b1_rhs(np.zeros(2), 0.2), np.array([0.0, 0.1]))
    for u in AMPLITUDES.values():
        assert np.array_equal(controlled_invariance_defect(u), np.array([0.0, u]))


def test_exact_trajectory_counts_and_shapes() -> None:
    trajectories = generate_all_trajectories()
    assert len(trajectories) == 9
    for bundle in trajectories.values():
        assert bundle.full.shape == (5001, 4)
        assert bundle.b0.shape == (5001, 2)
        assert bundle.b1.shape == (5001, 2)
        assert bundle.full_fine_on_primary.shape == (5001, 4)
        assert bundle.b0_fine_on_primary.shape == (5001, 2)
        assert bundle.b1_fine_on_primary.shape == (5001, 2)


def test_all_frozen_numerical_sanity_checks_except_repository_regression() -> None:
    report = benchmark_report()
    assert all(report["sanity"].values())
    assert report["convergence_error"] <= 1e-8
    assert report["mean_closure_error"] <= 1e-10
    assert report["symmetry_error"] <= 1e-10


def test_frozen_mechanical_classification_is_pass_before_repository_regression() -> None:
    report = benchmark_report()
    assert report["H_delta"] < np.pi / 2.0
    assert report["E_pass"] <= 1e-10
    assert report["E_B0_min"] >= 1e-4
    assert report["E_B1_min"] >= 1e-4
    assert report["verdict_without_regression"] == "PASS"
