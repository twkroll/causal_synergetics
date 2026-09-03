import torch

from causal_synergetics.benchmarks.neural_linear import (
    DTYPE,
    ETA,
    HIDDEN_DIM,
    INPUT_DIM,
    analytic_step,
    autograd_step,
    effective_weight,
    frozen_states,
    frozen_tasks,
    plasticity_matrix,
)

ATOL = 1e-12


def assert_close(actual: torch.Tensor, expected: torch.Tensor) -> None:
    assert torch.allclose(actual, expected, atol=ATOL, rtol=0.0)


def test_frozen_specification_and_initial_symmetry() -> None:
    states = frozen_states()
    tasks = frozen_tasks()

    assert INPUT_DIM == 2
    assert HIDDEN_DIM == 2
    assert ETA == 0.1
    assert states["A"][0].dtype == DTYPE
    assert states["B"][0].dtype == DTYPE
    assert_close(tasks["C"], torch.tensor([1.0, 0.0], dtype=DTYPE))
    assert_close(tasks["D"], torch.tensor([0.0, 1.0], dtype=DTYPE))

    U_A, v_A = states["A"]
    U_B, v_B = states["B"]
    zero = torch.zeros(2, dtype=DTYPE)

    assert_close(effective_weight(U_A, v_A), zero)
    assert_close(effective_weight(U_B, v_B), zero)
    assert abs(torch.linalg.matrix_norm(U_A).item() - 1.0) <= ATOL
    assert abs(torch.linalg.matrix_norm(U_B).item() - 1.0) <= ATOL
    assert abs(torch.linalg.vector_norm(v_A).item() - 1.0) <= ATOL
    assert abs(torch.linalg.vector_norm(v_B).item() - 1.0) <= ATOL

    assert_close(plasticity_matrix(U_A, v_A), torch.diag(torch.tensor([2.0, 1.0], dtype=DTYPE)))
    assert_close(plasticity_matrix(U_B, v_B), torch.diag(torch.tensor([1.0, 2.0], dtype=DTYPE)))


def test_analytic_formula_matches_explicit_parameter_update_and_predictions() -> None:
    states = frozen_states()
    tasks = frozen_tasks()
    expected = {
        ("A", "C"): (torch.tensor([0.2, 0.0], dtype=DTYPE), 0.32),
        ("B", "C"): (torch.tensor([0.1, 0.0], dtype=DTYPE), 0.405),
        ("A", "D"): (torch.tensor([0.0, 0.1], dtype=DTYPE), 0.405),
        ("B", "D"): (torch.tensor([0.0, 0.2], dtype=DTYPE), 0.32),
    }

    for state_name, (U, v) in states.items():
        for task_name, c in tasks.items():
            result = analytic_step(U, v, c)
            w_from_updated_parameters = effective_weight(result.U_plus, result.v_plus)
            expected_w, expected_loss = expected[(state_name, task_name)]

            assert_close(result.w_plus, w_from_updated_parameters)
            assert_close(result.w_plus, expected_w)
            assert abs(result.loss_plus.item() - expected_loss) <= ATOL


def test_autograd_agrees_with_analytic_update_componentwise() -> None:
    for U, v in frozen_states().values():
        for c in frozen_tasks().values():
            analytic = analytic_step(U, v, c)
            automatic = autograd_step(U, v, c)

            assert_close(automatic.U_plus, analytic.U_plus)
            assert_close(automatic.v_plus, analytic.v_plus)
            assert_close(automatic.w_plus, analytic.w_plus)
            assert abs(automatic.loss_plus.item() - analytic.loss_plus.item()) <= ATOL


def test_directed_crossing_and_symmetric_loss_advantage() -> None:
    states = frozen_states()
    tasks = frozen_tasks()

    loss_A_C = analytic_step(*states["A"], tasks["C"]).loss_plus.item()
    loss_B_C = analytic_step(*states["B"], tasks["C"]).loss_plus.item()
    loss_A_D = analytic_step(*states["A"], tasks["D"]).loss_plus.item()
    loss_B_D = analytic_step(*states["B"], tasks["D"]).loss_plus.item()

    assert loss_A_C < loss_B_C
    assert loss_B_D < loss_A_D

    advantage_C = loss_B_C - loss_A_C
    advantage_D = loss_A_D - loss_B_D
    assert abs(advantage_C - advantage_D) <= ATOL
    assert abs(advantage_C - 0.085) <= ATOL
