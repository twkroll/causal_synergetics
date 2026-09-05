# Project Status — causal_synergetics

Version: 1.6
Date: 2026-09-05
Overall status: POWER-GRID PASS FROZEN / CROSS-DOMAIN INTEGRATION READY / RESPONSE-COORDINATE DIRECTION PARKED
Governance status: FROZEN v0.1
Latest rollback point: `RP-015 — Power-Grid Minimal Benchmark Result Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an established theory.

## Frozen scientific chain

- `Prior-Art & Definitions Audit 0.1`: PASS — CLAIM-RESTRICTED / RESTRICT / REINTERPRET.
- `CORE Synergetic Sufficiency Boundary 0.1`: PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.
- `Neural Minimal Benchmark 0.1`: PASS — RESULT FROZEN.
- `Neural Historical Reachability 0.1`: PASS — RESULT FROZEN.
- `Neural Nonlinear ReLU Pilot 0.1`: PASS — RESULT FROZEN.
- `Neural Response Coordinate Pilot 0.1`: WEAK — RESULT FROZEN.
- `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`: FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP.
- `Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1`: STOP / PARK RESPONSE-COORDINATE DIRECTION.
- `Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1`: SPECIFICATION FROZEN.
- `Power-Grid Minimal Benchmark 0.1`: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**.

All prior claim ceilings remain controlling.

## Frozen power-grid result

Canonical result:
`research/app_b/power_grid_minimal_benchmark_0_1.md`.

Frozen metrics:

- `E_pass=0`;
- `E_B0_min=0.3549858420076152`;
- `E_B1_min=0.06534774384333092`;
- `H_delta=0.13069548768668177 < pi/2`;
- max controlled `|e_omega|=0.08954202393695339`;
- mean/COI closure error `3.885780586188048e-14`;
- primary/half-step convergence error `8.1601392309949e-15`;
- odd-sign symmetry error `3.83026943495679e-14`;
- APP-B local tests `5 passed`.

Interpretation ceiling:

> In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

No alternative topology, model, parameter, macro, intervention amplitude/location, horizon, baseline, threshold, or numerical method was tried after `GO`.

## Cross-domain scientific state

The programme now has two distinct application domains exhibiting the narrower intervention-sufficiency boundary:

- neural parameter states can share the same current function yet differ in one-step learning response under frozen interventions;
- in a physical controlled ODE, a pre-declared representative-machine macro can be exact for passive coherent dynamics yet fail under a localized intervention that excites hidden coherency modes.

This supports programme coherence around the CORE diagnostic, not generic universality or novelty.

The power-grid strong control is equally important: the arithmetic mean/COI coordinate is exactly closed under the same disturbance. Therefore the result is about insufficiency of a particular pre-declared passive macro, not failure of low-dimensional aggregation in general.

## Frozen neural conclusion

The neural response-coordinate/null/nuisance direction remains parked under `RP-013`. The earlier exact neural minimal/history/ReLU results remain independently frozen; WEAK/FAIL results are not repaired.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Cross-Domain Intervention-Sufficiency Integration Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt:
`research/master/prompts/master_cross_domain_intervention_sufficiency_integration_gate_0_1.md`.

Purpose: integrate all frozen evidence through `RP-015` and choose exactly one programme action `GO`, `REVISE`, or `STOP` before a new capability stage is opened.

## Branch state

- `00 – MASTER`: READY — cross-domain integration gate.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: PARKED / FROZEN / WAIT.
- `60 – APP-B`: COMPLETE / PASS — RESULT FROZEN / WAIT.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `70 – APP-C`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

`RP-015` freezes the complete APP-B result. `RP-014` remains the specification freeze and all earlier rollback points remain stable. No result is being retuned or promoted.

## Branching check

OK.

No new specialist execution is open. Exactly one MASTER integration gate is authorised.

## Rollback

Latest stable savepoint:

`RP-015 — Power-Grid Minimal Benchmark Result Freeze 0.1`.

## Current claim ceiling

The project may state the exact frozen LIT/CORE/neural/power-grid findings and that the CORE-style intervention-sufficiency boundary now has two-domain application support under tightly restricted benchmarks.

It may not claim:

- generic cross-domain universality;
- a new state-equivalence or causal-state formalism;
- generic power-grid insufficiency;
- failure of all low-dimensional grid aggregates;
- a generally useful learned causal/plasticity coordinate;
- controlled state preparation as an established capability;
- field-level causal-synergetics novelty.

## Manuscript

UNOPENED.

No manuscript claim freeze is yet authorised.

## CI

Repository CI remains not configured. APP-B reports `5 passed` locally and no GitHub status contexts/workflow runs for the queried execution head.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Cross-Domain Intervention-Sufficiency Integration Gate 0.1`
