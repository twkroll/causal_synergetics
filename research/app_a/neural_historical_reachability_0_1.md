# Neural Historical Reachability 0.1

Status: EXECUTED
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-03
Dependencies:
- `research/core/synergetic_sufficiency_boundary_0_1.md`
- `research/app_a/neural_minimal_benchmark_0_1.md` (`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`)
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The frozen `Neural Historical Reachability 0.1` gate passes all six pre-specified criteria without retuning.

Starting from the same hidden matrix `U_0=0` with fixed main readout `v=e1`, the two frozen one-step auxiliary-gradient histories differ only in the symmetric historical target (`e1` versus `e2`). With the fixed auxiliary readout `a=e2` and historical learning rate `eta_hist=1`, they reach exactly the two parameter states A/B already frozen in `Neural Minimal Benchmark 0.1`:

- History A reaches `U_A=[[0,0],[1,0]]`.
- History B reaches `U_B=[[0,0],[0,1]]`.

The main effective function remains exactly `w=U^T v=(0,0)` before and after preparation for both histories. The historical analytic update and PyTorch autograd update agree componentwise with maximum observed absolute difference `0.0` in float64. Re-running the already-frozen C/D evaluation from the prepared endpoints reproduces all four prior effective weights and post-step losses.

This result establishes only feasibility under the explicitly frozen auxiliary-gradient preparation mechanism. It does not establish natural reachability under ordinary single-head SGD, generic SGD reachability, nonlinear generalisation, novelty, or causal synergetics.

---

## 2. Frozen preparation protocol

### Network and common initialization

Use exactly

`f_{U,v}(x)=v^T U x`, with `d=h=2`.

The fixed main readout during preparation is

`v=e1=(1,0)^T`.

Both histories start from the same hidden matrix

`U_0=[[0,0],[0,0]]`.

Therefore the initial main effective function is

`w_0=U_0^T v=(0,0)^T`.

### Auxiliary preparation mechanism

The temporary auxiliary readout is fixed as

`a=e2=(0,1)^T`.

For historical target `c`, the frozen preparation loss is

`H_c(U)=1/2 ||U^T a-c||_2^2`.

The two histories are:

- History A: `c_A=e1=(1,0)^T`.
- History B: `c_B=e2=(0,1)^T`.

Preparation consists of exactly one full-batch gradient-descent step on `U` only, with

`eta_hist=1`.

The main readout `v` and auxiliary readout `a` are fixed and are not updated. No momentum, weight decay, stochasticity, optimizer state, noise, additional step, alternative initialization, alternative readout, or alternative target is used.

After the single preparation step, the auxiliary head is discarded. No reset or modification of `U` or `v` is allowed before the frozen C/D evaluation.

---

## 3. Full analytical derivation of the historical update

Define

`z(U)=U^T a`.

Then

`H_c(U)=1/2 (z-c)^T(z-c)`.

For an infinitesimal perturbation `dU`,

`dz=(dU)^T a`,

so

`dH=(z-c)^T (dU)^T a`.

Using the Frobenius inner product,

`dH = tr((a(z-c)^T)^T dU)`.

Therefore

`grad_U H_c = a(U^T a-c)^T`.

At the common initialization `U_0=0`,

`U_0^T a=0`,

hence

`grad_U H_c(U_0) = -a c^T`.

One gradient-descent step with the frozen historical learning rate `eta_hist=1` gives

`U^+ = U_0 - grad_U H_c(U_0)`

`= a c^T`.

For History A, `a=e2` and `c_A=e1`, therefore

`U_A^+ = e2 e1^T = [[0,0],[1,0]]`.

For History B, `a=e2` and `c_B=e2`, therefore

`U_B^+ = e2 e2^T = [[0,0],[0,1]]`.

These are exactly the previously frozen benchmark states A and B.

The historical loss also falls exactly from

`H_c(U_0)=1/2`

to

`H_c(U^+)=0`

for both histories, because `(U^+)^T a = c` when `||a||_2=1`.

---

## 4. Proof of main-function preservation

The main function is determined only by `(U,v)`:

`w=U^T v`.

Initially,

`w_0=U_0^T v=0`.

After the frozen historical update,

`U^+=a c^T`.

Therefore

`w^+=(U^+)^T v=(a c^T)^T v`

`=c a^T v`.

The frozen readouts satisfy

`a^T v=e2^T e1=0`.

Hence

`w^+=0`

for either historical target `c_A` or `c_B`.

Equivalently, the historical update changes only the second row of `U`, while the main readout `v=e1` selects only the first row; that first row remains zero.

For completeness, along the linear interpolation between the discrete endpoints,

`U(alpha)=alpha a c^T`, `0<=alpha<=1`,

one also has

`U(alpha)^T v = alpha c(a^T v)=0`.

Thus the endpoint transition itself lies entirely inside the same main-function fibre, although the actual optimizer protocol remains the single frozen discrete step.

---

## 5. Exact endpoint comparison with frozen states A/B

| History | Common start `U_0` | Target | Analytical endpoint | Previously frozen state | Difference |
|---|---|---|---|---|---:|
| A | `[[0,0],[0,0]]` | `e1` | `[[0,0],[1,0]]` | `U_A=[[0,0],[1,0]]` | `0.0` |
| B | `[[0,0],[0,0]]` | `e2` | `[[0,0],[0,1]]` | `U_B=[[0,0],[0,1]]` | `0.0` |

The main readout remains `v=e1` for both endpoints, exactly matching the previously frozen benchmark pair.

---

## 6. Numerical and autograd verification

The historical step was implemented in Python/PyTorch using `torch.float64` in two independent forms:

1. `analytic_history_step`: applies the exact gradient `a(U^T a-c)^T`.
2. `autograd_history_step`: computes the same historical loss in PyTorch, calls `backward()`, and applies one optimizer-equivalent update to `U` only.

Frozen execution environment:

- Python `3.13.5`
- PyTorch `2.10.0+cpu`
- pytest `9.0.2`
- platform: Linux

Observed historical results:

| History | `U^+` | `w_before` | `w_after` | `H_before` | `H_after` | max analytic/autograd difference |
|---|---|---|---|---:|---:|---:|
| A | `[[0,0],[1,0]]` | `(0,0)` | `(0,0)` | `0.5` | `0.0` | `0.0` |
| B | `[[0,0],[0,1]]` | `(0,0)` | `(0,0)` | `0.5` | `0.0` | `0.0` |

The maximum observed absolute analytical/autograd discrepancy over the tested historical `U^+`, `w_before`, `w_after`, and historical losses is `0.0`.

The local frozen test command was

`PYTHONPATH=src pytest -q tests/test_neural_linear_benchmark.py tests/test_neural_linear_history.py`

Observed result:

`8 passed in 1.08s`

---

## 7. Reproduction of the previously frozen C/D evaluation

After preparation, the auxiliary head is discarded and the original frozen benchmark evaluation is applied without modification:

- Task C: `c_C=e1`.
- Task D: `c_D=e2`.
- One simultaneous full-batch GD step in `(U,v)`.
- `eta_eval=0.1`.
- Primary response: `w^+`.
- Secondary response: post-step task loss.

Observed values:

| Prepared history/state | Task | `w^+` | Post-step loss |
|---|---|---|---:|
| A | C | `(0.2,0)` | `0.32000000000000006` |
| B | C | `(0.1,0)` | `0.405` |
| A | D | `(0,0.1)` | `0.405` |
| B | D | `(0,0.2)` | `0.32000000000000006` |

These reproduce the prior frozen analytical values within the required absolute tolerance `1e-12`. The binary floating-point representation of `0.32` is far inside that tolerance.

The previously frozen opposite adaptation preference is therefore retained:

- on C, History/State A reaches the lower post-step loss;
- on D, History/State B reaches the lower post-step loss.

No evaluation parameter or response metric was changed.

---

## 8. Frozen success criteria

| # | Criterion | Frozen observation | Result |
|---|---|---|---|
| 1 | Common initialization | Both histories use exactly `U_0=0` and `v=e1` | **PASS** |
| 2 | Exact endpoint reachability | One step reaches the previously frozen `U_A` and `U_B`; maximum endpoint error `0.0 < 1e-12` | **PASS** |
| 3 | Main-function preservation | `w=(0,0)` before and after both histories; observed error `0.0 < 1e-12` | **PASS** |
| 4 | Symmetric protocol | All preparation settings are identical except targets `e1` versus `e2` | **PASS** |
| 5 | Benchmark reproduction | All four frozen C/D `w^+` values and losses reproduced within `1e-12` | **PASS** |
| 6 | No retuning | No alternative initialization, readout, targets, `eta_hist`, step count, optimizer, or evaluation setting was tried | **PASS** |

All six pre-specified criteria pass.

Classification:

**PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

---

## 9. Interpretation ceiling

The strongest allowed statement is exactly:

> The exact function-equivalent state pair used in the frozen linear benchmark can be generated from a common hidden initialization by two symmetric one-step auxiliary gradient histories while the main readout and current main function remain unchanged; the resulting states retain the previously frozen opposite one-step adaptation preferences.

This gate does **not** establish:

- natural reachability under ordinary single-head training;
- generic reachability under SGD;
- nonlinear or real-data generalisation;
- novelty of the mechanism;
- that auxiliary pretraining is required or unique;
- that the result establishes causal synergetics.

No broader claim is authorised by this result.

---

## 10. Open issues

The following remain explicitly outside this gate and require new MASTER authorisation:

1. Ordinary single-head training reachability from a matched initialization/history.
2. Genericity or robustness of reachability under SGD perturbations, stochasticity, or different hyperparameters.
3. Nonlinear networks, multi-step training, real datasets, transformers, LoRA, adapters, or learned representations.
4. Whether auxiliary preparation is necessary, unique, natural, or representative of realistic training histories.
5. Any learned causal/plasticity coordinate or universal interpretation of the previously defined response matrix.
6. Any novelty claim or manuscript-level promotion.

No exploration of these issues was performed in this gate.

---

## 11. Code, tests, commit and CI status

Implementation:

`src/causal_synergetics/benchmarks/neural_linear.py`

Historical tests:

`tests/test_neural_linear_history.py`

Previously frozen benchmark regression tests:

`tests/test_neural_linear_benchmark.py`

Historical test-addition commit:

`ad9cc18a0519ffcfc4e6bc2e919e82f40bf54208`

Implementation commit completing the frozen historical functionality:

`e342ef5c5cefae30df45e23bc667f149e818238c`

GitHub reports no commit status checks and no workflow runs for the implementation commit. Repository CI is therefore **not configured / not applicable for this execution commit**. The frozen local execution result is `8 passed`.

---

STOP — RETURN TO MASTER
