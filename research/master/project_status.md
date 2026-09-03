# Project Status — causal_synergetics

Version: 0.3
Date: 2026-09-03
Overall status: CORE BOUNDARY FROZEN / NEURAL MINIMAL BENCHMARK READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an already established theory.

## Frozen scientific results

### 80 – LIT

Gate: `Prior-Art & Definitions Audit 0.1`.
Status: COMPLETE / FROZEN.
Decision: `PASS — CLAIM-RESTRICTED`.
Programme action: `RESTRICT / REINTERPRET`.

Generic novelty claims for intervention-conditioned state descriptors, controlled behavioral equivalence, intervention-sufficient low-dimensional representations, and controlled closure/lumpability remain demoted as prior-art territory.

### 10 – CORE

Gate: `CORE Synergetic Sufficiency Boundary 0.1`.
Status: COMPLETE / FROZEN.
Decision: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.
Canonical result: `research/core/synergetic_sufficiency_boundary_0_1.md`.
Canonical commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`.

Frozen conclusions:

1. For the full frozen retained trajectory `q(·)`, exact fibre response homogeneity is equivalent to controlled projectability / exact controlled closure; this is prior-art structure and is marked `SUBSUMED`.
2. Classical unforced synergetic slaving alone does not imply intervention-relative response sufficiency.
3. The scalar slow/fast system `q̇=ur`, `ṙ=-λr+u` is a proved minimal witness: passive slaving is exact, yet interventions expose hidden fast-state dependence.
4. Exact finite-horizon response bounds are available for the witness, and a general comparison/ISS-style proposition maps fast relaxation, slaving defect, intervention leakage, and tangential sensitivity to finite-horizon response error.
5. The bridge is a quantitative compatibility diagnostic, not an established new generic theory or publication-level novelty claim.

## Claim ceiling

The project may currently claim only the explicit restricted boundary and quantitative compatibility result frozen in CORE.

It may not claim novelty for controlled state equivalence, intervention-sufficient representation, lumpability/closure, the phrase `causal order parameter`, or forced-fast-mode phenomena in general.

A publication-level novelty claim for the bridge proposition remains unresolved and would require a separate theorem-to-theorem prior-art audit.

## Active branch

`50 – APP-A – Neuronaler Minimalbenchmark`

Status: READY / CHAT UNOPENED.
Current gate: `Neural Minimal Benchmark 0.1`.
Prompt: `research/master/prompts/app_a_neural_minimal_benchmark_0_1.md`.

This is a pre-frozen feasibility benchmark, not a novelty test.

Frozen specification:

- factorised linear network `f_{U,v}(x)=v^T Ux`, `d=h=2`;
- exact states A/B with identical current effective function `w=0` and matched simple norms;
- two symmetric linear-regression tasks `c_C=e1`, `c_D=e2`;
- one simultaneous full-batch GD step;
- learning rate `eta=0.1`;
- one-step horizon;
- primary response `w^+`, secondary post-step task loss;
- exact analytical predictions and float64 numerical tolerances fixed before execution;
- no retuning if the benchmark fails.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- historical reachability: BLOCKED pending APP-A return + new MASTER gate.
- nonlinear neural scaling / learned coordinates: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

The next benchmark's model, exact states, intervention family, learning rate, horizon, responses, expected values, numerical tolerances, and PASS/FAIL criteria were frozen before execution.

No alternative benchmark or parameter scan is authorised.

## Branching check

OK.

Exactly one application branch is now authorised. Parallel nonlinear, historical, power-grid, or manuscript work would be premature.

## Rollback

Latest stable savepoint:

`RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`.

If APP-A returns `FAIL`, the project returns here. The failed frozen benchmark is retained; it is not repaired by changing the state pair, tasks, learning rate, model, or endpoint.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## Active blocker

Operational only: the authorised `50 – APP-A – Neuronaler Minimalbenchmark` chat has not yet executed its frozen task.

## Next global step

Create the chat:

`50 – APP-A – Neuronaler Minimalbenchmark`

Paste the authorised start text from:

`research/master/prompts/app_a_neural_minimal_benchmark_0_1.md`

Then enter:

`GO`

After APP-A reaches `STOP — RETURN TO MASTER`, return to `00 – MASTER` and enter:

`Status?`
