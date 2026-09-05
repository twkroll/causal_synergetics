# Project Status — causal_synergetics

Version: 1.8
Date: 2026-09-05
Overall status: CONTROLLED STATE PREPARATION SPECIFICATION FROZEN / APP-C READY / RESPONSE-COORDINATE DIRECTION PARKED
Governance status: FROZEN v0.1
Latest rollback point: `RP-017 — Controlled State Preparation Specification Freeze 0.1`

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
- Neural response-coordinate direction: STOP / PARKED.
- `Power-Grid Minimal Benchmark 0.1`: PASS — RESULT FROZEN / NO NOVELTY PROMOTION.
- `Cross-Domain Intervention-Sufficiency Integration Gate 0.1`: GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.
- `Controlled State Preparation Feasibility & Specification Gate 0.1`: **SPECIFICATION FROZEN / PREPARATION EXECUTION READY / NO NOVELTY PROMOTION**.

All prior claim ceilings remain controlling.

## Frozen preparation specification

Canonical memo:
`research/master/controlled_state_preparation_feasibility_specification_0_1.md`.

Execution prompt:
`research/master/prompts/app_c_controlled_state_preparation_0_1.md`.

Exactly one preparation benchmark is frozen before execution:

- normalized two-machine nonlinear swing system with `M=D=K=1`;
- fixed common initial state `x=(0,0,0,0)`;
- current representative-machine macro `q=(delta1,omega1)` preserved throughout preparation;
- hidden coherency state `(e_delta,e_omega)`;
- future local evaluation steps `a=±0.2` on machine 2;
- analytically selected forced-relative-equilibrium target `e_delta*=asin(a/2)`, `e_omega*=0`;
- quintic smoothstep hidden path over `tau_prep=2`;
- exact open-loop inverse-dynamics feedforward preparation;
- preparation amplitude cap `0.35` and energy budget `0.25`;
- P0 no-preparation baseline;
- PT matched targeted preparation;
- PM sign-mismatched, exactly cost-symmetric preparation as the strong directional comparator;
- evaluation horizon `T_eval=5` with no feedback during evaluation;
- standard coherent aggregate B1, initialized at the preserved macro, as the target future response;
- deterministic NumPy float64 RK4 with `dt=0.001` and `dt=0.0005` audit;
- frozen preservation, target, cost, safety, response-benefit, symmetry, regression and convergence metrics;
- exhaustive PASS/WEAK/NULL/FAIL hierarchy.

The target and preparation path are fixed analytically from the model and future disturbance before any new preparation outcome is inspected. No trajectory optimization, learned controller or policy search is authorised.

## Scientific distinction

The benchmark tests more than hidden-state reachability:

1. one fixed physical initial state is used;
2. the present representative macro must remain unchanged throughout preparation;
3. hidden coherency state is changed under a bounded dynamical action with explicit cost;
4. the preparation ends before the future disturbance;
5. later representative response is evaluated against a frozen physical aggregate trajectory;
6. no preparation and an equal-cost sign-reversed preparation are mandatory comparators.

The method is still related to established anticipatory feedforward, equilibrium pre-positioning and preconditioning. No novelty or optimal-control claim is licensed.

## Branch state

- `00 – MASTER`: COMPLETE / WAIT FOR APP-C.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: PARKED / FROZEN / WAIT.
- `60 – APP-B`: COMPLETE / PASS — RESULT FROZEN / WAIT.
- `70 – APP-C`: READY / AWAIT GO — Controlled State Preparation 0.1.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

`RP-017` freezes the preparation domain/system, current macro, hidden state, initial state, future interventions, target hidden equilibrium, preparation path, control formula, duration, budgets, P0/PT/PM conditions, B1 target, horizon, numerical method/resolutions, metrics, classifier, anti-retuning rule and claim ceiling before execution.

All rollback points through `RP-016` remain stable. No APP-A or APP-B result is reinterpreted or modified.

## Branching check

OK.

Exactly one scientific execution is authorised: APP-C `Controlled State Preparation 0.1`.

## Rollback

Latest stable savepoint:

`RP-017 — Controlled State Preparation Specification Freeze 0.1`.

Any APP-C PASS/WEAK/NULL/FAIL return must be frozen and integrated by MASTER rather than repaired in-place.

## Current claim ceiling

No preparation result exists yet.

The project may state the exact frozen LIT/CORE/neural/power-grid findings, the cross-domain GO decision, and that one narrow same-current-macro preparation benchmark has been prospectively specified.

It may not claim:

- generic controlled state preparation;
- novelty or optimality of the preparation method;
- robustness to unknown/stochastic future disturbances;
- generic power-grid preparation benefit;
- a new state-equivalence or causal-state formalism;
- a generally useful learned causal/plasticity coordinate;
- field-level establishment or novelty of causal synergetics.

## Manuscript

UNOPENED.

No manuscript claim freeze is authorised.

## CI

Repository CI remains not configured. Current MASTER changes are specification/governance commits only; no APP-C scientific execution has occurred.

## Next global step

Open/return to:

`70 – APP-C – Controlled State Preparation`

and enter exactly:

`GO`

After APP-C reaches `STOP — RETURN TO MASTER`, return to MASTER and enter:

`Status?`
