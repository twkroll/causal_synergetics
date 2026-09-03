# Project Status — causal_synergetics

Version: 0.4
Date: 2026-09-03
Overall status: NEURAL MINIMAL BENCHMARK FROZEN / HISTORICAL REACHABILITY READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-004 — Neural Minimal Benchmark Result Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an already established theory.

## Frozen scientific results

### 80 – LIT

Gate: `Prior-Art & Definitions Audit 0.1`.
Decision: `PASS — CLAIM-RESTRICTED`.
Programme action: `RESTRICT / REINTERPRET`.

Generic novelty claims for intervention-conditioned state descriptors, controlled behavioral equivalence, intervention-sufficient representations, and controlled closure/lumpability remain demoted as prior-art territory.

### 10 – CORE

Gate: `CORE Synergetic Sufficiency Boundary 0.1`.
Decision: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.
Canonical result: `research/core/synergetic_sufficiency_boundary_0_1.md`.

Frozen conclusions include the exact controlled-projectability boundary for the full retained trajectory, failure of classical unforced slaving to imply controlled sufficiency, a minimal slow/fast counterexample, and exact/general finite-horizon response bounds without novelty promotion.

### 50 – APP-A — Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.

Frozen observations:

- `w_A=w_B=(0,0)` with matched simple norms;
- `P_A=diag(2,1)`, `P_B=diag(1,2)`;
- Task C: A reaches loss `0.32`, B `0.405`;
- Task D: B reaches loss `0.32`, A `0.405`;
- symmetric advantage magnitude `0.085`;
- analytic/autograd maximum observed component difference `0.0` in float64;
- local frozen test run `4 passed`;
- no retuning or alternate configuration.

Allowed interpretation only: in this exact frozen factorised-linear benchmark, function-equivalent states with matched simple norms can have different symmetric one-step learning responses.

## Active branch

`50 – APP-A – Neuronaler Minimalbenchmark`

Current gate: `Neural Historical Reachability 0.1`.
Status: READY / AWAIT GO.
Canonical prompt: `research/master/prompts/app_a_neural_historical_reachability_0_1.md`.

The gate freezes one historical construction before execution:

- common hidden initialization `U_0=0`;
- fixed main readout `v=e1`;
- temporary auxiliary readout `a=e2`;
- symmetric historical targets `e1` and `e2`;
- exactly one `U`-only full-batch gradient step at `eta_hist=1`;
- no momentum, stochasticity, noise, weight decay, optimizer state, or extra steps;
- expected endpoints exactly equal the previously frozen A/B matrices;
- main function `w=U^T v` must remain zero before and after preparation;
- afterward the already-frozen C/D evaluation must reproduce without modification.

This tests only exact reachability under one explicit auxiliary-gradient preparation history. It is not a natural-SGD or generic neural reachability claim.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- nonlinear neural scaling: BLOCKED pending historical gate return + new MASTER authorisation.
- learned response/plasticity coordinates: BLOCKED.
- NTK/LoRA/adapter comparisons: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- controlled state preparation: BLOCKED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

The Neural Minimal Benchmark result is frozen as `RP-004`. The historical gate's common initialization, auxiliary head, targets, optimizer semantics, learning rate, number of steps, endpoint expectations, evaluation protocol, tolerances, and PASS/FAIL criteria are all frozen before execution.

No second historical construction is authorised if this one fails.

## Branching check

OK.

No new chat is required. The existing APP-A chat receives a new versioned MASTER-authorised task. Parallel nonlinear or learned-coordinate work remains premature.

## Rollback

Latest stable savepoint:

`RP-004 — Neural Minimal Benchmark Result Freeze 0.1`.

If Neural Historical Reachability 0.1 fails, the project returns here. The failed historical gate remains recorded and may not be repaired by changing its frozen construction.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

The frozen minimal benchmark execution commit had no GitHub status checks or workflow runs. Repository CI remains not configured / not applicable; the frozen local test result is `4 passed`.

## Next global step

Return to the existing chat:

`50 – APP-A – Neuronaler Minimalbenchmark`

Enter exactly:

`GO`

The chat must read its updated `research/app_a/STATUS.md` and execute only `research/master/prompts/app_a_neural_historical_reachability_0_1.md`.

After APP-A reaches `STOP — RETURN TO MASTER`, return to `00 – MASTER` and enter:

`Status?`
