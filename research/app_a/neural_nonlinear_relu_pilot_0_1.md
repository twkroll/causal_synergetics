# Neural Nonlinear ReLU Pilot 0.1

Status: EXECUTED
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-04
Dependencies:
- `research/app_a/neural_minimal_benchmark_0_1.md` (`PASS — RESULT FROZEN`)
- `research/app_a/neural_historical_reachability_0_1.md` (`PASS — RESULT FROZEN`)
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The frozen two-unit ReLU pilot passes all eight pre-specified success criteria without retuning.

The two parameter states are globally function-equivalent and have matched simple norms, yet one simultaneous full-batch gradient step on the frozen symmetric tasks produces different post-step functions and losses. The preferred state reverses across the task pair exactly as pre-specified.

Observed frozen post-step losses:

- Task C: state A `0.14045`, state B `0.2312`.
- Task D: state A `0.2312`, state B `0.14045`.
- Directed symmetric advantage: `0.09075` in both directions.

The independently coded analytical update and PyTorch autograd update agree componentwise with maximum observed absolute difference `0.0` in float64. The combined APP-A regression run, including the unchanged linear and history tests, reports `12 passed`.

This is a nonlinear feasibility pilot only. It carries no novelty promotion.

---

## 2. Frozen specification

### Model

`f_{U,v}(x)=v^T ReLU(Ux)`, bias-free, with `d=h=2`.

### State A

`U_A=[[2,0],[0,1]]`

`v_A=(1/2,1)^T`

### State B

`U_B=[[1,0],[0,2]]`

`v_B=(1,1/2)^T`

### Tasks

Task C:

`x_C=(1,-1)^T`, `y_C=2`.

Task D:

`x_D=(-1,1)^T`, `y_D=2`.

Loss:

`L=1/2(f(x)-y)^2`.

### Intervention

Exactly one simultaneous full-batch gradient-descent step on all entries of `(U,v)` with

`eta=0.1`.

No momentum, weight decay, stochasticity, optimizer state, clipping, noise, or extra step was used.

### Horizon and response

Horizon: exactly one optimizer step.

Ordered frozen probe set:

1. `(1,-1)`
2. `(-1,1)`
3. `(1,1)`
4. `(-1,-1)`

Primary response:

`Gamma_primary=[f^+(x_C),f^+(x_D),f^+(x_S),f^+(x_N)]`.

Secondary response: post-step task loss.

Absolute tolerance for all frozen expected values and analytic/autograd comparisons:

`1e-12`.

No alternative state, task, scaling, learning rate, probe, horizon, optimizer, or response definition was tried.

---

## 3. Analytical global function-equivalence proof

For every `lambda>0`, ReLU is positively homogeneous:

`ReLU(lambda z)=lambda ReLU(z)`.

Therefore for state A,

`f_A(x)=(1/2)ReLU(2x_1)+ReLU(x_2)`

`=ReLU(x_1)+ReLU(x_2)`.

For state B,

`f_B(x)=ReLU(x_1)+(1/2)ReLU(2x_2)`

`=ReLU(x_1)+ReLU(x_2)`.

Hence

`f_A(x)=f_B(x)=ReLU(x_1)+ReLU(x_2)`

for every `x in R^2`, not merely on the frozen probes.

The simple norms also match exactly:

`||U_A||_F=||U_B||_F=sqrt(5)`

and

`||v_A||_2=||v_B||_2=sqrt(5/4)`.

The common pre-update frozen probe vector is exactly

`[1,1,2,0]`.

---

## 4. Analytical one-step derivation

For one frozen sample `(x,y)`, define

`z=Ux`, `h=ReLU(z)`, `r=f_{U,v}(x)-y`.

Because every frozen task has one strictly active and one strictly inactive unit, no ReLU derivative at zero is involved. With indicator vector

`m_i=1[z_i>0]`,

the exact gradients are

`grad_v L = r h`,

`grad_U L = r (v \odot m) x^T`.

Thus the simultaneous step is

`v^+=v-eta r h`,

`U^+=U-eta r (v \odot m)x^T`.

At every frozen initial `(state,task)` combination, the task output is `1`, the target is `2`, and therefore `r=-1`.

For the active hidden unit with scaling `a`, active incoming vector `u=a e_j`, output coefficient `v=1/a`, and frozen task input satisfying `||x||^2=2`,

`u^+=u+(eta/a)x`,

`v^+=1/a+eta a`.

Its post-step preactivation on the task sample is

`u^{+T}x=a+2eta/a`.

Therefore the task output is

`f^+(x)=(1/a+eta a)(a+2eta/a)`

`=1+eta(a^2+2/a^2)+2eta^2`.

With `eta=0.1`:

- high scaling `a=2`: `f^+(x)=1.47`, loss `0.5(1.47-2)^2=0.14045`;
- low scaling `a=1`: `f^+(x)=1.32`, loss `0.5(1.32-2)^2=0.2312`.

This is the pre-specified nonlinear response crossing.

---

## 5. Activation-margin verification

The intended active/inactive preactivations remain strictly separated before and after the frozen step:

| State | Task | Before | After |
|---|---|---|---|
| A | C | `(2,-1)` | `(2.1,-1)` |
| B | C | `(1,-2)` | `(1.2,-2)` |
| A | D | `(-2,1)` | `(-2,1.2)` |
| B | D | `(-1,2)` | `(-1,2.1)` |

Thus no frozen update crosses a ReLU boundary on the task sample, and no derivative-at-zero convention affects the result.

---

## 6. Numerical/autograd results

Execution environment for the frozen local run:

- Python `3.13.5`
- PyTorch `2.10.0+cpu`
- pytest `9.0.2`
- Linux

The implementation contains two independent paths:

1. an explicit analytical update using the fixed-activation gradient formula;
2. a PyTorch autograd update with one optimizer-equivalent simultaneous parameter step.

Maximum observed absolute analytical/autograd difference over all tested updated `U`, updated `v`, and probe-response components:

`0.0`.

---

## 7. Frozen probe-response table

| State | Task | Frozen post-step probe vector | Post-step task loss |
|---|---|---|---:|
| A | C | `[1.47, 1.0, 2.4, 0.0]` | `0.14045` |
| B | C | `[1.32, 1.0, 2.1, 0.0]` | `0.2312` |
| A | D | `[1.0, 1.32, 2.1, 0.0]` | `0.2312` |
| B | D | `[1.0, 1.47, 2.4, 0.0]` | `0.14045` |

Directed advantages:

`0.2312-0.14045=0.09075`

for both task directions.

---

## 8. Frozen success criteria

| # | Criterion | Frozen observation | Result |
|---|---|---|---|
| 1 | Global current-function equivalence | Proved analytically by positive homogeneity; common probe vector `[1,1,2,0]` | **PASS** |
| 2 | Simple norm symmetry | Both `U` norms `sqrt(5)` and both `v` norms `sqrt(5/4)` within `1e-12` | **PASS** |
| 3 | Activation-margin check | Intended active preactivation remains positive and inactive remains negative before/after every frozen step | **PASS** |
| 4 | Analytic/autograd agreement | Maximum observed tested component difference `0.0 < 1e-12` | **PASS** |
| 5 | Directed nonlinear crossing | C: `0.14045 < 0.2312` for A; D: `0.14045 < 0.2312` for B | **PASS** |
| 6 | Symmetry | Both directed advantages equal `0.09075` within `1e-12` | **PASS** |
| 7 | No retuning | Only the pre-frozen configuration was executed | **PASS** |
| 8 | Regression safety | Unchanged prior linear/history tests plus new ReLU tests: `12 passed` | **PASS** |

All eight frozen criteria pass.

---

## 9. Classification

**PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

No repair, replacement pair, alternative scaling, alternative task, tolerance widening, optimizer change, or horizon change was used.

---

## 10. Interpretation ceiling

The strongest allowed statement is exactly:

> In this frozen two-unit ReLU pilot, two globally function-equivalent and simple-norm-matched parameterisations exhibit different one-step learning responses under symmetric tasks, with the preferred state reversing across the task pair.

This does **not** establish:

- novelty;
- generic nonlinear behaviour;
- realistic training-history reachability;
- learned causal/plasticity coordinates;
- LoRA or transformer behaviour;
- real-data or multi-step scaling;
- causal synergetics.

These restrictions are part of the result freeze.

---

## 11. Code, tests, commits, and CI

Implementation:

`src/causal_synergetics/benchmarks/neural_relu.py`

Implementation commit:

`b5ba5da30d869d160eab0a7801bcfa324860b19a`

Tests:

`tests/test_neural_relu_pilot.py`

Test commit containing both implementation and ReLU tests:

`3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`

Frozen local command:

`PYTHONPATH=src pytest -q tests/test_neural_linear_benchmark.py tests/test_neural_linear_history.py tests/test_neural_relu_pilot.py`

Observed result:

`12 passed in 1.01s`.

GitHub reports no commit status checks and no workflow runs for test commit `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`. Repository CI is therefore not configured / not applicable for this execution commit.

The canonical result-freeze commit is recorded in `research/app_a/STATUS.md` after this result file is committed.

---

## 12. Open issues and STOP

Generic nonlinear scaling, realistic nonlinear training-history reachability, multi-step or real-data experiments, learned response/plasticity coordinates, LoRA/adapters, power-grid work, controlled state preparation, and manuscript work remain outside this gate and require new MASTER authorisation.

STOP — RETURN TO MASTER
