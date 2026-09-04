# Project Status — causal_synergetics

Version: 1.2
Date: 2026-09-04
Overall status: NUISANCE-INVARIANCE RESULT FROZEN / SPECIFICATION FAIL INTEGRATION READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-012 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1`

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
- `Neural Response Coordinate WEAK Integration Gate 0.1`: REVISE — CLAIM-RESTRICTED.
- `Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`: SPECIFICATION FROZEN.
- `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`: **FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION**.

## Frozen nuisance-invariance result

Canonical result:
`research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`.

Implementation commit:
`988db41bad5d46615b00defe2da8964c15a5203f`.

Test commit:
`2d7ac6171323607bfeeec12f3657b56b162e0406`.

Canonical result-freeze commit:
`8f2be1871605b39d9e851d1b47ed9c30ec7bf21f`.

### Scientific/numerical observations

All mandatory sanity conditions pass, including:

- exact 648-state construction and partitions `164/164/160/160`;
- current-function equality within `8.433854195116819e-17`;
- hidden-gauge orthogonality within `2.220446049250313e-16`;
- within-orbit `P` invariance within `8.881784197001252e-16`;
- analytical/autograd agreement over all `7776` state/intervention pairs within `1.6653345369377348e-16`;
- leakage separation;
- full-fingerprint ceiling and B3 strong-control requirements;
- combined regression suite `36 passed`.

Frozen predictive/invariance metrics:

- candidate response coordinate:
  - `R2_state(S_nuis)=1.0`;
  - `R2_state(S_latent)=1.0`;
  - `R2_state(S_joint)=1.0`;
  - minimum joint per-intervention `R2=1.0`;
  - `J_nuis=5.596227006606825e-32`;
- naive B2 raw-parameter PCA:
  - joint `R2_state=2.220446049250313e-16`;
  - `J_nuis=1.0`;
- gauge-aware B3 Gram-PCA:
  - joint `R2_state=1.0`;
  - `J_nuis=2.692209973425601e-32`;
- frozen N0 null:
  - nuisance `R2_state=0.7071428571428566`;
  - latent `R2_state=0.6999999999999995`;
  - joint `R2_state=0.6999999999999995`.

## Why the formal result is FAIL

The scientific classifier frozen before execution is not exhaustive for the realised metric combination:

- PASS fails because `R_null<=0.10` is false;
- WEAK fails because `R_null<=0.25` is false;
- none of the explicitly enumerated NULL conditions is true;
- all mandatory sanity conditions pass, so this is not a numerical/leakage/oracle FAIL.

APP-A therefore correctly froze the gate as:

**`FAIL — SPECIFICATION CLASSIFICATION GAP`**.

No post-hoc NULL clause, orbit-deduplicated null, changed cyclic shift, new threshold or relabelling was introduced.

The structural explanation that the one-state cyclic shift frequently maps to another gauge-equivalent copy of the same response-latent state is a plausible diagnosis of the high N0 score, but it is not permission to repair the frozen result.

## Result freeze

The execution is frozen as:

`RP-012 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1`.

The prior WEAK coordinate result and all earlier freezes remain unchanged.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt:
`research/master/prompts/master_neural_response_coordinate_nuisance_fail_integration_gate_0_1.md`.

Purpose: integrate the frozen specification/classification FAIL and choose exactly one of `GO`, `REVISE`, or `STOP` without repairing the failed pilot.

## Branch state

- `00 – MASTER`: READY — nuisance FAIL integration gate.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: COMPLETE / FROZEN / WAIT.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.

## Blocked future work

Until the FAIL integration gate completes, do not open:

- a repaired or replacement null/classifier execution;
- another nuisance, coordinate or state family;
- nonlinear/multi-step/real-data response-coordinate scaling;
- realistic neural history/reachability;
- NTK/LoRA/adapter work;
- power-grid / ODE discovery;
- controlled state preparation;
- new literature positioning;
- manuscript drafting.

## Freeze check

OK.

`RP-012` preserves the failed gate exactly, including the high N0 score and non-total classifier. No prior result is relabelled or repaired.

## Branching check

OK.

Exactly one next activity is authorised and remains in MASTER: integration of the specification FAIL. No scientific execution is open.

## Rollback

Latest stable savepoint:

`RP-012 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1`.

Any prospective methodological validation must branch explicitly from this freeze; it may not overwrite the failed nuisance pilot.

## Current claim ceiling

The project may state the exact frozen gauge-invariance/prediction observations and the exact specification-classification failure.

It may not claim:

- that the nuisance-invariance gate passed;
- a scientific NULL or WEAK classification for the failed gate;
- unique information unavailable from symmetry-aware raw-state quotients;
- a generally useful low-dimensional causal/plasticity coordinate;
- generic nonlinear scaling;
- realistic SGD-history relevance;
- LoRA/transformer or real-data usefulness;
- controlled state preparation;
- field-level causal-synergetics novelty.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. The nuisance-pilot test commit has no GitHub status checks; the frozen local combined test result is `36 passed`.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1`
