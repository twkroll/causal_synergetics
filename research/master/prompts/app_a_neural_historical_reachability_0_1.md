# Prompt — Neural Historical Reachability 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-03
Dependencies satisfied by:
- `research/core/synergetic_sufficiency_boundary_0_1.md`
- `research/app_a/neural_minimal_benchmark_0_1.md` (`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`)

## Purpose

Test one pre-specified, symmetry-controlled gradient-history construction that reaches the exact frozen state pair A/B from a common initial hidden state while preserving the current main function throughout the preparation phase.

This is a reachability feasibility gate only. It does not establish that ordinary single-head SGD naturally produces these states, that the construction is generic, or that the phenomenon is novel.

## Frozen model and evaluation state

Use exactly the factorised linear network from Neural Minimal Benchmark 0.1:

`f_{U,v}(x)=v^T U x`, with `d=h=2`.

The main readout is frozen during preparation as

`v=e1=(1,0)^T`.

The common initial hidden matrix is

`U_0 = [[0,0],[0,0]]`.

Thus the main effective function is initially

`w_0=U_0^T v=(0,0)^T`.

## Frozen historical preparation mechanism

Introduce one temporary auxiliary readout used only during the historical preparation phase:

`a=e2=(0,1)^T`.

For a historical target `c`, define the auxiliary preparation loss

`H_c(U)=1/2 ||U^T a-c||_2^2`.

Freeze the two symmetric histories:

- History A: `c_A=e1`.
- History B: `c_B=e2`.

Preparation intervention:

- exactly one simultaneous full-batch gradient-descent step on `U` only;
- historical learning rate `eta_hist=1`;
- `v` and `a` are fixed and not updated;
- no weight decay, momentum, stochasticity, optimizer state, noise, or additional steps.

Starting from `U_0=0`, the analytically predicted update is

`grad_U H_c = a(U^T a-c)^T`,

so at `U_0=0`,

`U^+ = a c^T`.

Therefore the frozen expected endpoints are exactly:

History A:

`U_A = [[0,0],[1,0]]`.

History B:

`U_B = [[0,0],[0,1]]`.

These are exactly the frozen states used in Neural Minimal Benchmark 0.1 with common main readout `v=e1`.

## Main-function preservation criterion

During preparation the main function is defined only by `(U,v)` with `v=e1`.

Because the auxiliary update changes only the second row of `U`, the first row remains zero. Therefore the frozen analytical prediction is

`w(t=0)=w(t=1)=U^T v=(0,0)`

for both histories.

The auxiliary head is discarded after the single preparation step. No reset or modification of `U` or main readout `v` is allowed before evaluation.

## Frozen post-history evaluation

After preparation, execute the already-frozen Neural Minimal Benchmark 0.1 evaluation without modification:

- Task C: `c_C=e1`;
- Task D: `c_D=e2`;
- one simultaneous full-batch GD step in `(U,v)`;
- `eta_eval=0.1`;
- primary response `w^+`;
- secondary response post-step task loss.

Expected responses remain:

Task C:
- History/State A: `w^+=(0.2,0)`, loss `0.32`;
- History/State B: `w^+=(0.1,0)`, loss `0.405`.

Task D:
- History/State A: `w^+=(0,0.1)`, loss `0.405`;
- History/State B: `w^+=(0,0.2)`, loss `0.32`.

## Required implementation

Extend the existing benchmark code minimally. Add a deterministic historical-preparation function and tests. Do not refactor unrelated code.

Suggested paths:

- implementation: `src/causal_synergetics/benchmarks/neural_linear.py`
- tests: `tests/test_neural_linear_history.py`

Use `torch.float64` for numerical verification.

## Frozen success criteria

All must pass:

1. **Common initialization:** both histories start from exactly the same `U_0=0` and main `v=e1`.
2. **Exact endpoint reachability:** one frozen historical step reaches the exact previously frozen `U_A` and `U_B` within absolute tolerance `1e-12`.
3. **Main-function preservation:** `w=U^T v=(0,0)` both before and after preparation for both histories within `1e-12`.
4. **Symmetric protocol:** histories differ only by the symmetric auxiliary targets `e1` versus `e2`; all other preparation settings are identical.
5. **Benchmark reproduction:** the already-frozen C/D evaluation reproduces all four prior `w^+` values and losses within `1e-12`.
6. **No retuning:** no alternative initialization, auxiliary readout, target pair, historical learning rate, number of steps, optimizer, or evaluation setting is tried after execution begins.

## Required deliverable

Create:

`research/app_a/neural_historical_reachability_0_1.md`

It must contain:

1. Executive verdict.
2. Frozen preparation protocol.
3. Full analytical derivation of the historical update.
4. Proof that the main function stays fixed during the preparation endpoint transition.
5. Exact endpoint comparison with frozen states A/B.
6. Numerical/autograd verification.
7. Reproduction of the previously frozen C/D evaluation.
8. PASS / FAIL result against all six frozen criteria.
9. Explicit interpretation ceiling.
10. Open issues.
11. Code/test paths, commit hash, and CI status.

## PASS condition

PASS means only that the exact frozen benchmark pair is reachable from a common hidden initialization by the single pre-specified auxiliary gradient-history construction while the main function remains fixed.

## FAIL condition

FAIL if any frozen endpoint, preservation, symmetry, reproduction, or numerical criterion fails. Do not repair the gate by changing the protocol.

## Interpretation ceiling

If PASS, the strongest allowed statement is:

> The exact function-equivalent state pair used in the frozen linear benchmark can be generated from a common hidden initialization by two symmetric one-step auxiliary gradient histories while the main readout and current main function remain unchanged; the resulting states retain the previously frozen opposite one-step adaptation preferences.

Do not claim:

- natural reachability under ordinary single-head training;
- generic reachability under SGD;
- nonlinear or real-data generalisation;
- novelty of the mechanism;
- that auxiliary pretraining is required or unique;
- that the result establishes causal synergetics.

## Forbidden actions

Do not:

- change the frozen historical protocol after inspection;
- search over initializations, heads, tasks, learning rates, horizons, or optimizers;
- open nonlinear, learned-coordinate, LoRA, power-grid, state-preparation, or manuscript work;
- introduce a second historical candidate if this one fails;
- promote any novelty claim.

## Final handoff

After committing the deliverable:

1. update `research/app_a/STATUS.md` with the result classification and commit hash;
2. set `Next instruction: RETURN TO MASTER`;
3. report CI status if applicable;
4. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
