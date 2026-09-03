import torch

from causal_synergetics.benchmarks.neural_linear import (
    DTYPE,
    ETA_HIST,
    analytic_history_step,
    analytic_step,
    autograd_history_step,
    effective_weight,
    frozen_history_setup,
    frozen_states,
    frozen_tasks,
)

ATOL = 1e-12


def assert_close(actual: torch.Tensor, expected: torch.Tensor) -> None:
    assert torch.allclose(actual, expected, atol=ATOL, rtol=0.0)


def prepared_states():
    U0, v, a, targets = frozen_history_setup()
    return {
        name: analytic_history_step(U0, v, a, target)
        for name, target in targets.items()
    }, U0, v, a, targets


def test_common_initialization_symmetric_protocol_and_exact_endpoints() -> None:
    histories, U0, v, a, targets = prepared_states()
    frozen = frozen_states()

    assert ETA_HIST == 1.0
    assert_close(U0, torch.zeros((2, 2), dtype=DTYPE))
    assert_close(v, torch.tensor([1.0, 0.0], dtype=DTYPE))
    assert_close(a, torch.tensor([0.0, 1.0], dtype=DTYPE))
    assert_close(targets["A"], torch.tensor([1.0, 0.0], dtype=DTYPE))
    assert_close(targets["B"], torch.tensor([0.0, 1.0], dtype=DTYPE))

    assert_close(histories["A"].U_plus, frozen["A"][0])
    assert_close(histories["B"].U_plus, frozen["B"][0])
    assert_close(frozen["A"][1], v)
    assert_close(frozen["B"][1], v)


def test_main_function_preserved_before_and_after_both_histories() -> None:
    histories, U0, v, _, _ = prepared_states()
    zero = torch.zeros(2, dtype=DTYPE)

    assert_close(effective_weight(U0, v), zero)
    for history in histories.values():
        assert_close(history.w_before, zero)
        assert_close(history.w_after, zero)


def test_historical_autograd_matches_analytic_update() -> None:
    U0, v, a, targets = frozen_history_setup()
    for c in targets.values():
        analytic = analytic_history_step(U0, v, a, c)
        automatic = autograd_history_step(U0, v, a, c)

        assert_close(automatic.U_plus, analytic.U_plus)
        assert_close(automatic.w_before, analytic.w_before)
        assert_close(automatic.w_after, analytic.w_after)
        assert abs(automatic.history_loss_before.item() - analytic.history_loss_before.item()) <= ATOL
        assert abs(automatic.history_loss_after.item() - analytic.history_loss_after.item()) <= ATOL


def test_frozen_benchmark_reproduced_after_history() -> None:
    histories, _, v, _, _ = prepared_states()
    tasks = frozen_tasks()
    expected = {
        ("A", "C"): (torch.tensor([0.2, 0.0], dtype=DTYPE), 0.32),
        ("B", "C"): (torch.tensor([0.1, 0.0], dtype=DTYPE), 0.405),
        ("A", "D"): (torch.tensor([0.0, 0.1], dtype=DTYPE), 0.405),
        ("B", "D"): (torch.tensor([0.0, 0.2], dtype=DTYPE), 0.32),
    }

    for history_name, history in histories.items():
        for task_name, c in tasks.items():
            result = analytic_step(history.U_plus, v, c)
            expected_w, expected_loss = expected[(history_name, task_name)]
            assert_close(result.w_plus, expected_w)
            assert abs(result.loss_plus.item() - expected_loss) <= ATOL
