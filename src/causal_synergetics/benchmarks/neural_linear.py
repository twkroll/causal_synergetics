"""Frozen factorised-linear neural benchmarks for APP-A."""

from __future__ import annotations

from dataclasses import dataclass

import torch

DTYPE = torch.float64
ETA = 0.1
ETA_HIST = 1.0
INPUT_DIM = 2
HIDDEN_DIM = 2


@dataclass(frozen=True)
class StepResult:
    U_plus: torch.Tensor
    v_plus: torch.Tensor
    w_plus: torch.Tensor
    loss_plus: torch.Tensor


@dataclass(frozen=True)
class HistoryResult:
    U_plus: torch.Tensor
    w_before: torch.Tensor
    w_after: torch.Tensor
    history_loss_before: torch.Tensor
    history_loss_after: torch.Tensor


def frozen_states() -> dict[str, tuple[torch.Tensor, torch.Tensor]]:
    """Return the two frozen initial parameter states as float64 tensors."""
    v = torch.tensor([1.0, 0.0], dtype=DTYPE)
    return {
        "A": (
            torch.tensor([[0.0, 0.0], [1.0, 0.0]], dtype=DTYPE),
            v.clone(),
        ),
        "B": (
            torch.tensor([[0.0, 0.0], [0.0, 1.0]], dtype=DTYPE),
            v.clone(),
        ),
    }


def frozen_tasks() -> dict[str, torch.Tensor]:
    """Return the two frozen regression targets."""
    return {
        "C": torch.tensor([1.0, 0.0], dtype=DTYPE),
        "D": torch.tensor([0.0, 1.0], dtype=DTYPE),
    }


def frozen_history_setup() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, dict[str, torch.Tensor]]:
    """Return the common historical initialization, fixed readouts, and targets."""
    U0 = torch.zeros((HIDDEN_DIM, INPUT_DIM), dtype=DTYPE)
    v = torch.tensor([1.0, 0.0], dtype=DTYPE)
    a = torch.tensor([0.0, 1.0], dtype=DTYPE)
    targets = {
        "A": torch.tensor([1.0, 0.0], dtype=DTYPE),
        "B": torch.tensor([0.0, 1.0], dtype=DTYPE),
    }
    return U0, v, a, targets


def effective_weight(U: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    return U.T @ v


def task_loss(w: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
    return 0.5 * torch.sum((w - c) ** 2)


def history_loss(U: torch.Tensor, a: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
    return 0.5 * torch.sum((U.T @ a - c) ** 2)


def plasticity_matrix(U: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    identity = torch.eye(U.shape[1], dtype=U.dtype, device=U.device)
    return U.T @ U + torch.dot(v, v) * identity


def analytic_history_step(
    U: torch.Tensor,
    v: torch.Tensor,
    a: torch.Tensor,
    c: torch.Tensor,
    eta_hist: float = ETA_HIST,
) -> HistoryResult:
    """One frozen U-only historical preparation step using exact gradients."""
    w_before = effective_weight(U, v)
    residual = U.T @ a - c
    grad_U = torch.outer(a, residual)
    U_plus = U - eta_hist * grad_U
    w_after = effective_weight(U_plus, v)
    return HistoryResult(
        U_plus=U_plus,
        w_before=w_before,
        w_after=w_after,
        history_loss_before=history_loss(U, a, c),
        history_loss_after=history_loss(U_plus, a, c),
    )


def autograd_history_step(
    U: torch.Tensor,
    v: torch.Tensor,
    a: torch.Tensor,
    c: torch.Tensor,
    eta_hist: float = ETA_HIST,
) -> HistoryResult:
    """One optimizer-equivalent U-only historical step using PyTorch autograd."""
    U_var = U.detach().clone().requires_grad_(True)
    w_before = effective_weight(U_var, v)
    loss_before = history_loss(U_var, a, c)
    loss_before.backward()

    with torch.no_grad():
        U_plus = U_var - eta_hist * U_var.grad
        w_after = effective_weight(U_plus, v)
        loss_after = history_loss(U_plus, a, c)

    return HistoryResult(
        U_plus=U_plus,
        w_before=w_before.detach(),
        w_after=w_after,
        history_loss_before=loss_before.detach(),
        history_loss_after=loss_after,
    )


def analytic_step(
    U: torch.Tensor,
    v: torch.Tensor,
    c: torch.Tensor,
    eta: float = ETA,
) -> StepResult:
    """One simultaneous GD step using the exact analytical gradients."""
    w = effective_weight(U, v)
    g = w - c
    U_plus = U - eta * torch.outer(v, g)
    v_plus = v - eta * (U @ g)

    P = plasticity_matrix(U, v)
    correction = eta**2 * g * torch.dot(v, U @ g)
    w_plus = w - eta * (P @ g) + correction

    return StepResult(
        U_plus=U_plus,
        v_plus=v_plus,
        w_plus=w_plus,
        loss_plus=task_loss(w_plus, c),
    )


def autograd_step(
    U: torch.Tensor,
    v: torch.Tensor,
    c: torch.Tensor,
    eta: float = ETA,
) -> StepResult:
    """One optimizer-equivalent simultaneous GD step using PyTorch autograd."""
    U_var = U.detach().clone().requires_grad_(True)
    v_var = v.detach().clone().requires_grad_(True)

    w = effective_weight(U_var, v_var)
    loss = task_loss(w, c)
    loss.backward()

    with torch.no_grad():
        U_plus = U_var - eta * U_var.grad
        v_plus = v_var - eta * v_var.grad
        w_plus = effective_weight(U_plus, v_plus)
        loss_plus = task_loss(w_plus, c)

    return StepResult(
        U_plus=U_plus,
        v_plus=v_plus,
        w_plus=w_plus,
        loss_plus=loss_plus,
    )
