# Project Status — causal_synergetics

Version: 0.9
Date: 2026-09-04
Overall status: RESPONSE COORDINATE WEAK RESULT FROZEN / MASTER INTEGRATION READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-009 — Neural Response Coordinate Result Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an established theory.

## Frozen scientific chain

- `Prior-Art & Definitions Audit 0.1`: PASS — CLAIM-RESTRICTED / RESTRICT / REINTERPRET.
- `CORE Synergetic Sufficiency Boundary 0.1`: PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.
- `Neural Minimal Benchmark 0.1`: PASS — RESULT FROZEN.
- `Neural Historical Reachability 0.1`: PASS — RESULT FROZEN.
- `Neural Nonlinear ReLU Pilot 0.1`: PASS — RESULT FROZEN.
- `Neural Vertical Slice Go/Revise/Stop Gate 0.1`: GO — CLAIM-RESTRICTED.
- `Neural Response Coordinate Specification Gate 0.1`: SPECIFICATION FROZEN.
- `Neural Response Coordinate Pilot 0.1`: **WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**.

## New frozen result

Canonical result:
`research/app_a/neural_response_coordinate_pilot_0_1.md`.

Canonical result-freeze commit:
`18618368991d818b3bfe883975b3ab2573bed0c6`.

Observed frozen result:

- 2D response-aware coordinate aggregate held-out `R2_state = 1.0`;
- minimum held-out intervention `R2_state(c)=1.0`;
- B0 current-function baseline approximately `0.0`;
- B1 simple-summary baseline `0.070803629370716`;
- B2 equal-dimensional raw-parameter PCA baseline `0.999883026432542`;
- response-coordinate advantage over B2 only `0.000116973567458323`, below the pre-frozen PASS margin `0.05`;
- cyclic association null `R2_state=-0.2`;
- all analytical/autograd, oracle, leakage, ceiling and regression sanity conditions passed;
- combined APP-A test run `24 passed`;
- no retuning or alternate coordinate/family was tried.

Mechanical classification: **WEAK**.

## Scientific interpretation

The candidate response coordinate demonstrates essentially exact held-out intervention prediction inside the frozen synthetic family. However, it does not demonstrate material predictive value beyond an equally compact raw-parameter PCA representation.

The plausible diagnosis is that the frozen state family itself has a sufficiently low-dimensional raw-parameter geometry for 2D raw PCA to recover almost all predictive structure. That diagnosis is an inference from the frozen result, not a separately proved theorem.

The result therefore weakens the specific programme claim that response-aware coordinates provide special compression beyond ordinary compact state representations, while preserving the narrower fact that held-out responses can be summarized compactly in this synthetic family.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Neural Response Coordinate WEAK Integration Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt:
`research/master/prompts/master_neural_response_coordinate_weak_integration_gate_0_1.md`.

Purpose: integrate the WEAK result without repair and choose exactly one of `GO`, `REVISE`, or `STOP` for the response-coordinate direction.

## Branch state

- `00 – MASTER`: READY — WEAK integration gate.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: COMPLETE / FROZEN / WAIT.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.

## Blocked future work

Until the WEAK integration gate completes, do not open:

- a second response coordinate or alternate state family;
- nonlinear/multi-step/real-data response-coordinate scaling;
- realistic neural history/reachability;
- NTK/LoRA/adapter work;
- power-grid / ODE discovery;
- controlled state preparation;
- new literature positioning;
- manuscript drafting.

## Freeze check

OK.

`RP-009` preserves the WEAK result exactly. No coordinate, family, baseline, metric, split, threshold, intervention or horizon may be changed retroactively.

## Branching check

OK.

Exactly one next activity is authorised and it remains in MASTER: integration of the WEAK result. No new scientific execution is open.

## Rollback

Latest stable savepoint:

`RP-009 — Neural Response Coordinate Result Freeze 0.1`.

Any future revision must branch prospectively from this frozen result rather than repairing it.

## Current claim ceiling

The project may state the exact frozen LIT/CORE/linear/history/ReLU findings and the WEAK response-coordinate result.

It may not claim:

- a generally useful low-dimensional causal/plasticity coordinate;
- special response-aware value beyond equally compact raw-state geometry in general;
- generic nonlinear scaling;
- realistic SGD history;
- LoRA/transformer or real-data relevance;
- controlled state preparation;
- field-level causal-synergetics novelty.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. For response-coordinate test commit `48d850c22ca156af892db11cbbdb95b20693bb08`, GitHub reports no commit status checks. The frozen local combined test result is `24 passed`.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Neural Response Coordinate WEAK Integration Gate 0.1`
