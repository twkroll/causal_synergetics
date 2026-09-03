# Neural Minimal Benchmark 0.1

Status: EXECUTED
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-03
Dependency: `research/core/synergetic_sufficiency_boundary_0_1.md` (`PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`)
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The frozen neural minimal benchmark passes all six pre-specified success criteria without retuning.

The two frozen parameter states have exactly the same current effective function `w=U^T v=0` and matched simple norms, but one simultaneous full-batch gradient-descent step with the frozen learning rate `eta=0.1` produces different effective post-step weights. The symmetric task pair reverses which state adapts more strongly:

- Task `C`: state A reaches loss `0.32`, state B reaches loss `0.405`.
- Task `D`: state B reaches loss `0.32`, state A reaches loss `0.405`.

The loss advantage has the same magnitude, `0.085`, in both directions. The exact analytical update and PyTorch autograd implementation agree componentwise with maximum observed absolute difference `0.0` in float64 for every tested `U^+`, `v^+`, and `w^+` component.

This is a feasibility benchmark only. It carries no novelty promotion and does not establish a universal causal/plasticity coordinate, nonlinear generalisation, historical reachability, or causal synergetics.

---

## 2. Frozen specification reproduced exactly

### Model

Use the two-layer factorised linear scalar-output network

`f_{U,v}(x) = v^T U x`,

with input dimension `d=2`, hidden width `h=2`, `U in R^{2x2}`, `v in R^2`, and effective current function parameter

`w = U^T v`.

### Frozen states

State A:

`v_A = (1,0)^T`,

`U_A = [[0,0],[1,0]]`.

State B:

`v_B = (1,0)^T`,

`U_B = [[0,0],[0,1]]`.

Therefore

`w_A = w_B = (0,0)^T`,

and the matched norms are

`||U_A||_F = ||U_B||_F = 1`,

`||v_A||_2 = ||v_B||_2 = 1`.

No alternative state pair was searched.

### Frozen tasks and loss

Task `C`:

`c_C = e_1 = (1,0)^T`.

Task `D`:

`c_D = e_2 = (0,1)^T`.

Loss:

`L_c(w) = 1/2 ||w-c||_2^2`.

Intervention: exactly one simultaneous full-batch gradient-descent step in `(U,v)`.

Learning rate:

`eta = 0.1`.

No optimizer state, momentum, weight decay, stochastic minibatching, or noise is used.

### Frozen horizon and response

Horizon:

`T = 1` optimizer step.

Primary response:

`Gamma_primary(s,c) = w^+`.

Secondary response:

`Gamma_secondary(s,c) = L_c(w^+)`.

No parameter, task, model, optimizer, horizon, or response search was performed.

---

## 3. Full analytical derivation

Let

`w = U^T v`,

and for the frozen quadratic task loss define

`g = grad_w L_c(w) = w-c`.

For perturbations `dU` and `dv`,

`dw = (dU)^T v + U^T dv`.

Hence

`dL = g^T dw`

`= g^T (dU)^T v + g^T U^T dv`

`= tr((v g^T)^T dU) + (U g)^T dv`.

Therefore

`grad_U L = v g^T`,

`grad_v L = U g`.

One simultaneous gradient-descent step gives exactly

`U^+ = U - eta v g^T`,

`v^+ = v - eta U g`.

The effective post-step function parameter is

`w^+ = (U^+)^T v^+`

`= (U^T - eta g v^T)(v - eta U g)`

`= U^T v - eta U^T U g - eta g v^T v + eta^2 g (v^T U g)`.

Thus

`w^+ = w - eta (U^T U + ||v||^2 I) g + eta^2 g (v^T U g)`.

Define

`P(U,v) = U^T U + ||v||^2 I`.

For state A,

`U_A^T U_A = diag(1,0)`,

so

`P_A = diag(2,1)`.

For state B,

`U_B^T U_B = diag(0,1)`,

so

`P_B = diag(1,2)`.

Because `w=U^T v=0` for both frozen states, `v^T U=w^T=0`; therefore

`v^T U g = 0`

for both tasks, and the `eta^2` correction vanishes. Since `g=-c` at `w=0`,

`w^+ = eta P c`.

With `eta=0.1`, this yields the frozen predictions:

### Task C

For state A,

`w_A^+ = 0.1 diag(2,1) e_1 = (0.2,0)^T`.

For state B,

`w_B^+ = 0.1 diag(1,2) e_1 = (0.1,0)^T`.

The explicit parameter updates are

`U_A^+ = [[0.1,0],[1,0]]`,

`v_A^+ = (1,0.1)^T`,

and

`U_B^+ = [[0.1,0],[0,1]]`,

`v_B^+ = (1,0)^T`.

The post-step losses are

`L_C(w_A^+) = 1/2 (0.8)^2 = 0.32`,

`L_C(w_B^+) = 1/2 (0.9)^2 = 0.405`.

### Task D

For state A,

`w_A^+ = 0.1 diag(2,1) e_2 = (0,0.1)^T`.

For state B,

`w_B^+ = 0.1 diag(1,2) e_2 = (0,0.2)^T`.

The explicit parameter updates are

`U_A^+ = [[0,0.1],[1,0]]`,

`v_A^+ = (1,0)^T`,

and

`U_B^+ = [[0,0.1],[0,1]]`,

`v_B^+ = (1,0.1)^T`.

The post-step losses are

`L_D(w_A^+) = 1/2 (0.9)^2 = 0.405`,

`L_D(w_B^+) = 1/2 (0.8)^2 = 0.32`.

Therefore the directed loss advantages are

`L_C(w_B^+) - L_C(w_A^+) = 0.085`,

`L_D(w_A^+) - L_D(w_B^+) = 0.085`.

---

## 4. Numerical implementation summary

The benchmark is implemented in Python/PyTorch using `torch.float64` only.

Execution environment used for the frozen run:

- Python `3.13.5`
- PyTorch `2.10.0+cpu`
- pytest `9.0.2`
- platform: Linux

The implementation contains two independent update paths:

1. `analytic_step`: applies the exact analytical gradients and the derived closed-form expression for `w^+`.
2. `autograd_step`: constructs the same loss in PyTorch, obtains gradients with `backward()`, and applies one simultaneous optimizer-equivalent update.

The test suite also recomputes `w^+ = (U^+)^T v^+` from the analytically updated parameters, independently checking the expanded formula.

Observed frozen numerical values:

| State | Task | `w^+` | Post-step loss | max analytic/autograd component difference |
|---|---|---|---:|---:|
| A | C | `(0.2, 0)` | `0.32000000000000006` | `0.0` |
| B | C | `(0.1, 0)` | `0.405` | `0.0` |
| A | D | `(0, 0.1)` | `0.405` | `0.0` |
| B | D | `(0, 0.2)` | `0.32000000000000006` | `0.0` |

The small decimal representation of `0.32` is ordinary binary floating-point representation and is far inside the frozen `1e-12` tolerance.

Test execution:

`PYTHONPATH=src pytest -q tests/test_neural_linear_benchmark.py`

Observed result:

`4 passed in 1.01s`

---

## 5. Frozen success criteria

| # | Criterion | Frozen observation | Result |
|---|---|---|---|
| 1 | Current-function equality | `w_A=w_B=(0,0)`; numerical absolute error `0.0` | **PASS** |
| 2 | Norm symmetry | `||U_A||_F=||U_B||_F=1`, `||v_A||_2=||v_B||_2=1`; numerical error `0.0` | **PASS** |
| 3 | Analytic/autograd agreement | Every tested component of `U^+`, `v^+`, `w^+` agrees; maximum observed absolute difference `0.0 < 1e-12` | **PASS** |
| 4 | Directed crossing | `0.32 < 0.405` on C for A vs B; `0.32 < 0.405` on D for B vs A | **PASS** |
| 5 | Symmetry check | Both loss advantages equal `0.085`; difference `0.0 < 1e-12` | **PASS** |
| 6 | No retuning | Only the pre-frozen states, tasks, dimensions, `eta=0.1`, one-step horizon, optimizer semantics, and response metrics were executed; no alternative configuration was tried | **PASS** |

All six frozen criteria pass.

---

## 6. Classification

**PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

No repair, parameter search, replacement state pair, alternative task, alternative optimizer, or alternative horizon was used.

---

## 7. Interpretation ceiling

The exact allowed interpretation is:

> In this frozen factorised linear neural benchmark, two parameter states with the same current function and matched simple norms can respond differently to the same one-step learning intervention; a symmetric task pair reverses which state adapts more strongly.

This gate does **not** establish that:

- the phenomenon is novel;
- current function is generally an order parameter;
- `P(U,v)` is a universal causal/plasticity coordinate;
- the result establishes causal synergetics;
- the result generalises to nonlinear networks, multi-step training, LoRA, transformers, or real datasets;
- historical training can reach the two states under a matched protocol.

These restrictions are part of the result freeze.

---

## 8. Open issues

The following remain open and are explicitly outside this gate:

1. **Historical reachability:** whether the two frozen parameter states can arise from a matched training/history protocol was not tested.
2. **Nonlinear extension:** no nonlinear network, real dataset, transformer, adapter, LoRA, or multi-step setting was tested.
3. **Representation question:** no learned response/plasticity representation was introduced or evaluated.
4. **Generality of `P(U,v)`:** the matrix is only the exact one-step factorised-linear response object appearing in this frozen derivation; no universal interpretation is licensed.
5. **Novelty:** no further literature audit was performed; the frozen literature and CORE claim ceilings remain controlling.

Opening any of these issues requires a new MASTER-authorised gate.

---

## 9. Code and test paths

Implementation:

`src/causal_synergetics/benchmarks/neural_linear.py`

Tests:

`tests/test_neural_linear_benchmark.py`

Execution command:

`PYTHONPATH=src pytest -q tests/test_neural_linear_benchmark.py`

---

## 10. Commit and CI status

Implementation/test execution commit:

`649a187125c4ad410e0b16b77accbfacfb577371`

GitHub commit-status query returned no status checks, and the workflow-run query returned no workflow runs for that commit. Therefore repository CI is **not configured / not applicable for this execution commit**; the frozen local test result is `4 passed`.

The canonical result-freeze commit is recorded in `research/app_a/STATUS.md` after the result/status metadata commit is created.

---

STOP — RETURN TO MASTER
