import math

import torch

from causal_synergetics.benchmarks.neural_relu import (
    DTYPE,
    ETA,
    HIDDEN_DIM,
    INPUT_DIM,
    analytic_step,
    autograd_step,
    frozen_states,
    frozen_tasks,
    probe_response,
)

ATOL = 1e-12


def assert_close(actual: torch.Tensor, expected: torch.Tensor) -> None:
    assert torch.allclose(actual, expected, atol=ATOL, rtol=0.0)


def test_frozen_specification_current_probe_equivalence_and_norm_symmetry() -> None:
    states = frozen_states()
    tasks = frozen_tasks()
    expected_probe = torch.tensor([1.0, 1.0, 2.0, 0.0], dtype=DTYPE)

    assert INPUT_DIM == 2
    assert HIDDEN_DIM == 2
    assert ETA == 0.1
    assert_close(tasks["C"][0], torch.tensor([1.0, -1.0], dtype=DTYPE))
    assert_close(tasks["D"][0], torch.tensor([-1.0, 1.0], dtype=DTYPE))
    assert tasks["C"][1].item() == 2.0
    assert tasks["D"][1].item() == 2.0

    for U, v in states.values():
        assert_close(probe_response(U, v), expected_probe)
        assert abs(torch.linalg.matrix_norm(U).item() - math.sqrt(5.0)) <= ATOL
        assert abs(torch.linalg.vector_norm(v).item() - math.sqrt(5.0 / 4.0)) <= ATOL


def test_activation_margins_remain_strict_before_and_after_step() -> None:
    active_index = {"C": 0, "D": 1}
    for U, v in frozen_states().values():
        for task_name, (x, y) in frozen_tasks().items():
            result = analytic_step(U, v, x, y)
            active = active_index[task_name]
            inactive = 1 - active
            assert result.preactivation_before[active].item() > 0.0
            assert result.preactivation_before[inactive].item() < 0.0
            assert result.preactivation_after[active].item() > 0.0
            assert result.preactivation_after[inactive].item() < 0.0


def test_analytic_autograd_and_frozen_probe_predictions() -> None:
    expected = {
        ("A", "C"): (torch.tensor([1.47, 1.0, 2.4, 0.0], dtype=DTYPE), 0.14045),
        ("B", "C"): (torch.tensor([1.32, 1.0, 2.1, 0.0], dtype=DTYPE), 0.2312),
        ("A", "D"): (torch.tensor([1.0, 1.32, 2.1, 0.0], dtype=DTYPE), 0.2312),
        ("B", "D"): (torch.tensor([1.0, 1.47, 2.4, 0.0], dtype=DTYPE), 0.14045),
    }

    for state_name, (U, v) in frozen_states().items():
        for task_name, (x, y) in frozen_tasks().items():
            analytic = analytic_step(U, v, x, y)
            automatic = autograd_step(U, v, x, y)
            expected_probe, expected_loss = expected[(state_name, task_name)]

            assert_close(automatic.U_plus, analytic.U_plus)
            assert_close(automatic.v_plus, analytic.v_plus)
            assert_close(automatic.probe_plus, analytic.probe_plus)
            assert_close(analytic.probe_plus, expected_probe)
            assert abs(automatic.loss_plus.item() - analytic.loss_plus.item()) <= ATOL
            assert abs(analytic.loss_plus.item() - expected_loss) <= ATOL


def test_directed_crossing_and_symmetric_advantage() -> None:
    states = frozen_states()
    tasks = frozen_tasks()
    losses = {}
    for state_name, (U, v) in states.items():
        for task_name, (x, y) in tasks.items():
            losses[(state_name, task_name)] = analytic_step(U, v, x, y).loss_plus.item()

    assert losses[("A", "C")] < losses[("B", "C")]
    assert losses[("B", "D")] < losses[("A", "D")]
    advantage_c = losses[("B", "C")] - losses[("A", "C")]
    advantage_d = losses[("A", "D")] - losses[("B", "D")]
    assert abs(advantage_c - advantage_d) <= ATOL
    assert abs(advantage_c - 0.09075) <= ATOL
