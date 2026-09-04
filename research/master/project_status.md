# Project Status — causal_synergetics

Version: 0.7
Date: 2026-09-04
Overall status: VERTICAL SLICE GO FROZEN / RESPONSE COORDINATE SPECIFICATION READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-007 — Neural Vertical Slice Decision Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an already established theory.

## Frozen scientific results

### 80 – LIT

`Prior-Art & Definitions Audit 0.1`: `PASS — CLAIM-RESTRICTED`; programme action `RESTRICT / REINTERPRET`.

Generic novelty claims for intervention-conditioned state descriptors, controlled behavioral equivalence, intervention-sufficient low-dimensional representations, and controlled closure/lumpability remain demoted as prior-art territory.

### 10 – CORE

`CORE Synergetic Sufficiency Boundary 0.1`: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.

Frozen conclusions include the controlled-projectability boundary, failure of classical unforced slaving to imply controlled sufficiency, a minimal slow/fast counterexample, and finite-horizon bridge bounds without novelty promotion. Publication-level novelty of the bridge remains unresolved.

### 50 – APP-A — Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Two exact factorised-linear states with identical current function and matched simple norms exhibit opposite symmetric one-step adaptation preferences. No retuning occurred.

### 50 – APP-A — Neural Historical Reachability 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

One frozen symmetric auxiliary-gradient preparation from common initialization reaches the exact linear A/B pair while preserving the main function. This is not ordinary or generic SGD reachability.

### 50 – APP-A — Neural Nonlinear ReLU Pilot 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`.
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.

One pre-specified two-unit ReLU symmetry pair is globally function-equivalent, simple-norm matched, and exhibits opposite symmetric one-step learning preferences. The combined frozen regression suite reported `12 passed`; no alternative nonlinear candidate was tried.

## Vertical-slice integration

Gate: `Neural Vertical Slice Go/Revise/Stop Gate 0.1`.
Canonical memo: `research/master/neural_vertical_slice_go_revise_stop_0_1.md`.
Decision: **GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.

Why GO:

- all five sequential stages were frozen before execution and completed without post-hoc repair;
- the exact linear witness is valid;
- one explicit history establishes feasibility of reaching the linear pair while preserving current function;
- one frozen nonlinear ReLU symmetry pair preserves the qualitative crossing;
- there is now a clear next falsification target with high information value.

Why this is not a novelty promotion:

- generic controlled-state and sufficiency ideas remain prior art;
- the CORE bridge is not established as publication-level novel;
- the historical mechanism is artificial;
- the nonlinear evidence is tiny, one-step and symmetry-engineered;
- no learned coordinate or held-out prediction result exists yet.

The integration freeze establishes:

`RP-007 — Neural Vertical Slice Decision Freeze 0.1`.

## Current claim ceiling

The project may state only the exact frozen LIT/CORE/linear/history/ReLU results with their limitations.

It may not claim:

- a new generic intervention-state theory;
- publication-level novelty of the CORE bridge;
- generic nonlinear scaling;
- ordinary or realistic SGD-history reachability;
- a learned low-dimensional causal/plasticity coordinate;
- held-out intervention prediction;
- LoRA/transformer or real-data relevance;
- controlled state preparation as an established capability;
- causal synergetics as an established field.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Neural Response Coordinate Specification Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt: `research/master/prompts/master_neural_response_coordinate_specification_gate_0_1.md`.

Purpose: define and freeze exactly one falsifiable neural benchmark testing whether a compact response/plasticity representation predicts held-out learning interventions materially better than pre-declared non-response-aware baselines.

This is a specification gate only. No benchmark execution is yet authorised.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- learned response/plasticity coordinate execution: BLOCKED pending specification freeze.
- multi-step/real-data scaling: BLOCKED.
- realistic nonlinear history/reachability: BLOCKED.
- NTK/LoRA/adapter comparisons: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- controlled state preparation: BLOCKED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

All prior results remain frozen. The vertical-slice GO decision is itself frozen as `RP-007`. No response-coordinate model, dimension, intervention split, baseline, metric, or success threshold has yet been executed or inspected.

## Branching check

OK.

Exactly one next gate is authorised, and it remains in MASTER. No new specialist branch or parallel application work is open.

## Rollback

Latest stable savepoint:

`RP-007 — Neural Vertical Slice Decision Freeze 0.1`.

If the specification gate cannot define a sufficiently falsifiable held-out predictive benchmark, return here rather than opening an under-specified learned-coordinate execution.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. The current MASTER changes are documentation/governance commits and have no GitHub status checks.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Neural Response Coordinate Specification Gate 0.1`
