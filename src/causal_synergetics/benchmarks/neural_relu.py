"""Frozen two-unit ReLU nonlinear pilot for APP-A."""

from __future__ import annotations

from dataclasses import dataclass

import torch

DTYPE = torch.float64
ETA = 0.1
INPUT_DIM = 2
HIDDEN_DIM = 2


@dataclass(frozen=True)
class ReLUStepResult:
    U_plus: torch.Tensor
    v_plus: torch.Tensor
    probe_plus: torch.Tensor
    loss_plus: torch.Tensor
    preactivation_before: torch.Tensor
    preactivation_after: torch.Tensor


def frozen_states() -> dict[str, tuple[torch.Tensor, torch.Tensor]]:
    return {
        "A": (
            torch.tensor([[2.0, 0.0], [0.0, 1.0]], dtype=DTYPE),
            torch.tensor([0.5, 1.0], dtype=DTYPE),
        ),
        "B": (
            torch.tensor([[1.0, 0.0], [0.0, 2.0]], dtype=DTYPE),
            torch.tensor([1.0, 0.5], dtype=DTYPE),
        ),
    }


def frozen_tasks() -> dict[str, tuple[torch.Tensor, torch.Tensor]]:
    return {
        "C": (
            torch.tensor([1.0, -1.0], dtype=DTYPE),
            torch.tensor(2.0, dtype=DTYPE),
        ),
        "D": (
            torch.tensor([-1.0, 1.0], dtype=DTYPE),
            torch.tensor(2.0, dtype=DTYPE),
        ),
    }


def frozen_probes() -> torch.Tensor:
    return torch.tensor(
        [[1.0, -1.0], [-1.0, 1.0], [1.0, 1.0], [-1.0, -1.0]],
        dtype=DTYPE,
    )


def network_output(U: torch.Tensor, v: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    return torch.dot(v, torch.relu(U @ x))


def probe_response(U: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    return torch.stack([network_output(U, v, x) for x in frozen_probes()])


def sample_loss(U: torch.Tensor, v: torch.Tensor, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    residual = network_output(U, v, x) - y
    return 0.5 * residual**2


def analytic_step(
    U: torch.Tensor,
    v: torch.Tensor,
    x: torch.Tensor,
    y: torch.Tensor,
    eta: float = ETA,
) -> ReLUStepResult:
    """One simultaneous GD step from the exact fixed-activation gradients."""
    z = U @ x
    active = (z > 0).to(dtype=U.dtype)
    hidden = torch.relu(z)
    residual = torch.dot(v, hidden) - y

    grad_v = residual * hidden
    grad_U = residual * torch.outer(v * active, x)

    U_plus = U - eta * grad_U
    v_plus = v - eta * grad_v
    z_plus = U_plus @ x

    return ReLUStepResult(
        U_plus=U_plus,
        v_plus=v_plus,
        probe_plus=probe_response(U_plus, v_plus),
        loss_plus=sample_loss(U_plus, v_plus, x, y),
        preactivation_before=z,
        preactivation_after=z_plus,
    )


def autograd_step(
    U: torch.Tensor,
    v: torch.Tensor,
    x: torch.Tensor,
    y: torch.Tensor,
    eta: float = ETA,
) -> ReLUStepResult:
    """One optimizer-equivalent simultaneous GD step using PyTorch autograd."""
    U_var = U.detach().clone().requires_grad_(True)
    v_var = v.detach().clone().requires_grad_(True)
    loss = sample_loss(U_var, v_var, x, y)
    loss.backward()

    with torch.no_grad():
        U_plus = U_var - eta * U_var.grad
        v_plus = v_var - eta * v_var.grad
        z_before = U @ x
        z_after = U_plus @ x
        probes = probe_response(U_plus, v_plus)
        loss_plus = sample_loss(U_plus, v_plus, x, y)

    return ReLUStepResult(
        U_plus=U_plus,
        v_plus=v_plus,
        probe_plus=probes,
        loss_plus=loss_plus,
        preactivation_before=z_before,
        preactivation_after=z_after,
    )
