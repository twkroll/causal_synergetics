# Project Status — causal_synergetics

Version: 1.0
Date: 2026-09-04
Overall status: RESPONSE COORDINATE WEAK INTEGRATED / NUISANCE-INVARIANCE SPECIFICATION READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`

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
- `Neural Response Coordinate Pilot 0.1`: WEAK — RESULT FROZEN.
- `Neural Response Coordinate WEAK Integration Gate 0.1`: **REVISE — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.

## Frozen WEAK result

Canonical result:
`research/app_a/neural_response_coordinate_pilot_0_1.md`.

Key facts:

- candidate 2D response-aware coordinate aggregate held-out `R2_state=1.0`;
- minimum held-out intervention `R2_state(c)=1.0`;
- B0 current-function baseline approximately `0.0`;
- B1 simple-summary baseline `0.070803629370716`;
- B2 equal-dimensional raw-parameter PCA baseline `0.999883026432542`;
- response-coordinate margin over B2 `0.000116973567458323`, below frozen PASS requirement `0.05`;
- cyclic association null `R2_state=-0.2`;
- all numerical, oracle, leakage, ceiling and regression checks passed;
- no retuning or alternate coordinate/family was tried.

The direct result is compact held-out predictability without material advantage over equally compact raw-state geometry.

## WEAK integration decision

Canonical memo:
`research/master/neural_response_coordinate_weak_integration_0_1.md`.

Decision: **REVISE — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.

Why REVISE:

- STOP is premature because held-out prediction is essentially exact and all validity controls pass;
- direct GO to broader nonlinear/multi-step/real-data work is premature because the principal discriminator against raw-state geometry failed;
- a second arbitrary coordinate or alternate family would risk post-hoc effect-guided repair;
- the single unresolved question is whether response-aware compression has invariance/predictive value under independently justified parameterisation nuisance.

The plausible explanation that the original 81-state family has intrinsically low-dimensional raw-parameter geometry remains an inference, not a frozen theorem.

The integration freeze establishes:

`RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt:
`research/master/prompts/master_neural_response_coordinate_nuisance_invariance_specification_gate_0_1.md`.

Purpose: define and freeze exactly one scientifically neutral control benchmark testing predictive sufficiency and invariance under independently justified response-irrelevant parameterisation nuisance.

This is specification-only. No new benchmark execution is authorised yet.

A valid nuisance family must be motivated by explicit model reparameterisation/gauge/symmetry structure rather than selected because it makes raw PCA fail. If such a family cannot be cleanly specified, the correct outcome is to park the response-coordinate direction.

## Branch state

- `00 – MASTER`: READY — nuisance-invariance specification gate.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: COMPLETE / FROZEN / WAIT.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.

## Blocked future work

Until the nuisance-invariance specification gate completes, do not open:

- a new response-coordinate execution;
- alternative coordinate/family search;
- nonlinear/multi-step/real-data response-coordinate scaling;
- realistic neural history/reachability;
- NTK/LoRA/adapter work;
- power-grid / ODE discovery;
- controlled state preparation;
- new literature positioning;
- manuscript drafting.

## Freeze check

OK.

`RP-009` preserves the WEAK empirical result. `RP-010` preserves the REVISE integration decision. No prior coordinate, family, baseline, metric, split, threshold, intervention or horizon may be changed retroactively.

## Branching check

OK.

Exactly one next activity is authorised and it remains in MASTER: nuisance-invariance specification. No scientific execution is open.

## Rollback

Latest stable savepoint:

`RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`.

If the next specification cannot define a neutral non-cherry-picked control, return here and park the coordinate direction.

## Current claim ceiling

The project may state the exact frozen LIT/CORE/linear/history/ReLU findings plus the WEAK coordinate result and REVISE decision.

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

Repository CI remains not configured. The WEAK coordinate test commit had no GitHub status checks; frozen local combined tests reported `24 passed`. Current MASTER changes are governance/documentation only.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`
