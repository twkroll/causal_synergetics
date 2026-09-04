# Project Status — causal_synergetics

Version: 0.8
Date: 2026-09-04
Overall status: RESPONSE COORDINATE SPECIFICATION FROZEN / APP-A PILOT READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-008 — Neural Response Coordinate Specification Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an established theory.

## Frozen scientific chain

- `Prior-Art & Definitions Audit 0.1`: PASS — CLAIM-RESTRICTED / RESTRICT / REINTERPRET.
- `CORE Synergetic Sufficiency Boundary 0.1`: PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.
- `Neural Minimal Benchmark 0.1`: PASS — RESULT FROZEN.
- `Neural Historical Reachability 0.1`: PASS — RESULT FROZEN.
- `Neural Nonlinear ReLU Pilot 0.1`: PASS — RESULT FROZEN.
- `Neural Vertical Slice Go/Revise/Stop Gate 0.1`: GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.

All prior claim ceilings remain controlling.

## Newly frozen specification

Gate: `Neural Response Coordinate Specification Gate 0.1`.
Decision: **SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION**.
Canonical memo: `research/master/neural_response_coordinate_specification_gate_0_1.md`.
Execution prompt: `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.

The next pilot is frozen before held-out inspection with:

- factorised-linear model `d=4,h=5`;
- 81 exactly function-equivalent states on a fixed 9x9 latent grid;
- constant current function and constant total `U`/`v` norms;
- deterministic 41/40 train/test state split;
- four fixed Hadamard calibration interventions;
- eight fixed held-out interventions;
- exactly one full-batch GD step at `eta=0.1`;
- 16D calibration fingerprint compressed by train-only PCA to exactly 2 dimensions;
- fixed bilinear OLS decoder;
- B0 current-function baseline;
- B1 fixed simple norm/state-summary baseline;
- B2 equal-dimensional raw-parameter PCA baseline;
- full calibration-fingerprint and exact operator ceilings;
- deterministic cyclic state-association null;
- fixed aggregate/per-intervention `R2_state`, NRMSE, leakage tests, numerical tolerances, and disjoint PASS/WEAK/NULL/FAIL thresholds.

The critical PASS condition includes a material `>=0.05` aggregate `R2_state` advantage over the equal-dimensional raw-parameter PCA baseline. A near-tie is at most WEAK; a clear raw-state loss is NULL.

No held-out benchmark result has been executed or inspected in MASTER.

## Active branch

`50 – APP-A – Neuronaler Minimalbenchmark`

Current gate: `Neural Response Coordinate Pilot 0.1`.
Status: READY / AWAIT GO.

APP-A must execute only the frozen versioned prompt and return the result without repair.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.
- multi-step/real-data scaling: BLOCKED.
- realistic nonlinear history/reachability: BLOCKED.
- broader nonlinear scaling: BLOCKED.
- NTK/LoRA/adapter work: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- controlled state preparation: BLOCKED.

## Freeze check

OK.

`RP-008` freezes state family, splits, interventions, coordinate dimension/construction, decoder, baselines, controls, metrics, thresholds, numerical tolerances, software stack, and anti-retuning rule before APP-A execution.

No second coordinate or alternate family is authorised after a WEAK/NULL/FAIL result.

## Branching check

OK.

Exactly one scientific execution is authorised: `Neural Response Coordinate Pilot 0.1` in the existing APP-A chat.

## Rollback

Latest stable savepoint:

`RP-008 — Neural Response Coordinate Specification Freeze 0.1`.

A weak, null, or failed result is retained and returned to MASTER; the specification is not repaired post hoc.

## Current claim ceiling

The project may state only the previously frozen LIT/CORE/linear/history/ReLU findings and the fact that this predictive benchmark has been pre-specified.

It may not yet claim:

- a useful low-dimensional response/plasticity coordinate;
- held-out intervention prediction;
- generic nonlinear scaling;
- realistic SGD history;
- LoRA/transformer or real-data relevance;
- controlled state preparation;
- field-level causal-synergetics novelty.

Even a future PASS would initially support only the frozen synthetic-family benchmark claim.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. The current MASTER changes are specification/governance commits with no GitHub status checks.

## Next global step

Return to the existing chat:

`50 – APP-A – Neuronaler Minimalbenchmark`

Enter exactly:

`GO`

After APP-A reaches `STOP — RETURN TO MASTER`, return here and enter:

`Status?`
