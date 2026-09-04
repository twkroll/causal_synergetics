# Project Status — causal_synergetics

Version: 1.1
Date: 2026-09-04
Overall status: NUISANCE-INVARIANCE SPECIFICATION FROZEN / APP-A PILOT READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-011 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1`

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
- `Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`: **SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION**.

## Frozen prior WEAK result

The prior 2D response-aware coordinate achieved aggregate and per-held-out-intervention `R2_state=1.0`, but equal-dimensional raw-parameter PCA achieved `R2_state=0.999883026432542`, leaving only `0.000116973567458323` advantage against a frozen `0.05` PASS margin. All validity checks passed. The result remains WEAK and is not repaired.

## Newly frozen nuisance-invariance specification

Canonical memo:
`research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`.

Execution prompt:
`research/master/prompts/app_a_neural_response_coordinate_nuisance_invariance_pilot_0_1.md`.

The nuisance construction is independently justified by exact hidden-basis gauge symmetry of the factorised linear model:

`(U,v) -> (QU,Qv)` for orthogonal `Q`.

This preserves exactly:

- current function `w=U^T v`;
- `U^T U`;
- `||v||`;
- one-step response operator `P=U^T U+||v||^2 I`;
- frozen response `Gamma=eta P c`.

It changes raw parameter coordinates nontrivially.

The frozen nuisance family uses exactly one canonical subgroup:

`Q(phi)=R(phi)⊕I3`,

with eight equally spaced angles `phi_j=j*pi/4`, `j=0,...,7`.

No alternative nuisance family or amplitude search is authorised.

## Frozen state and evaluation design

- same 9x9 response-latent grid and `rho=0.5` as the prior coordinate control;
- 81 response-relevant base states;
- eight gauge orientations each;
- total 648 states;
- deterministic four-way split:
  - `S_train=E_z x E_phi`: 164;
  - `S_nuis=E_z x O_phi`: 164;
  - `S_latent=O_z x E_phi`: 160;
  - `S_joint=O_z x O_phi`: 160;
- same four Hadamard calibration interventions;
- same eight held-out interventions;
- one full-batch GD step at `eta=0.1`;
- response `Gamma=Delta w=w^+`;
- candidate: train-only 2D PCA of 16D calibration response fingerprint;
- fixed bilinear OLS decoder.

Primary prediction evaluation is `S_joint`; nuisance-only and latent-only partitions are mandatory diagnostics.

## Frozen baselines and controls

- B0 current function;
- B1 six simple norm/state summaries;
- B2 naive equal-dimensional 2D raw-parameter PCA;
- B3 symmetry-aware equal-dimensional 2D Gram PCA from `[vech(U^T U),||v||^2]`;
- C0 full calibration fingerprint ceiling;
- C1 exact analytical operator oracle;
- N0 deterministic cyclic state-association null.

B3 is deliberately mandatory so a future advantage over naive raw PCA cannot be misreported as uniquely response-specific information. A PASS can establish only automatic gauge-invariance value relative to naive parameter coordinates in this control.

## Frozen invariance metric

For any 2D representation `r(z,phi)`, define within-orbit variance `W`, between-latent variance `B`, and

`J_nuis=W/(W+B)`.

`J_nuis=0` means perfect gauge invariance with nonzero response-latent variation.

No post-hoc alignment/rotation is permitted before this metric.

## Frozen primary PASS discriminator

All sanity controls must pass. Full PASS additionally requires:

- candidate joint `R2_state>=0.95`;
- candidate nuisance-only `R2_state>=0.95`;
- candidate latent-only `R2_state>=0.95`;
- minimum joint per-intervention `R2>=0.90`;
- candidate minus B2 joint `R2>=0.10`;
- `J_nuis(candidate)<=1e-8`;
- `J_nuis(B2)-J_nuis(candidate)>=0.05`;
- N0 joint `R2<=0.10`.

B3 must independently satisfy its frozen strong-control sanity thresholds (`R2_state(S_joint)>=0.95`, `J_nuis<=1e-8`).

WEAK/NULL/FAIL thresholds are frozen in the canonical specification memo. No threshold repair is allowed.

## Active branch

`50 – APP-A – Neuronaler Minimalbenchmark`

Current gate: `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`.
Status: READY / AWAIT GO.

APP-A must execute only the versioned frozen prompt and return the result without repair.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.
- nonlinear/multi-step/real-data coordinate scaling: BLOCKED.
- realistic neural history/reachability: BLOCKED.
- NTK/LoRA/adapter work: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- controlled state preparation: BLOCKED.

## Freeze check

OK.

`RP-011` freezes the base family, exact gauge subgroup, angle grid, state partitions, intervention sets, response semantics, coordinate dimension/construction, B0/B1/B2/B3, decoder, invariance metric, ceilings/nulls, metrics, thresholds, tolerances, software stack and anti-retuning rule before execution.

No alternative gauge group, rotation plane, angle amplitude, second coordinate or alternate family is authorised after WEAK/NULL/FAIL.

## Branching check

OK.

Exactly one scientific execution is authorised: the nuisance-invariance pilot in existing APP-A.

## Rollback

Latest stable savepoint:

`RP-011 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1`.

Any WEAK, NULL or FAIL outcome is retained and returned to MASTER rather than repaired.

## Current claim ceiling

No nuisance-invariance result exists yet.

The project may not claim a useful gauge-invariant response coordinate, response-aware superiority, generic nonlinear scaling, realistic SGD-history relevance, LoRA/transformer or real-data usefulness, controlled state preparation, or field-level causal-synergetics novelty.

Even a future PASS is restricted to the frozen synthetic gauge-control statement and does not establish superiority over explicitly symmetry-aware raw-state quotients.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. Current MASTER changes are specification/governance only and have no GitHub status checks.

## Next global step

Return to the existing chat:

`50 – APP-A – Neuronaler Minimalbenchmark`

Enter exactly:

`GO`

After APP-A reaches `STOP — RETURN TO MASTER`, return here and enter:

`Status?`
