# Decision & Branch Log — causal_synergetics

Last updated: 2026-09-04
Governance: `PROJECT_GOVERNANCE_0_1.md`

## Decisions

### DEC-001 — Project Governance 0.1
Status: FROZEN

The project adopts `research/master/PROJECT_GOVERNANCE_0_1.md` as canonical governance.

### DEC-002 — Git as single source of truth
Status: STABLE

Repository `twkroll/causal_synergetics` is the canonical persistent project state.

### DEC-003 — Lazy chat creation
Status: STABLE

Specialist chats are created only when MASTER authorises a concrete task. Uncreated chats are `UNOPENED`, not failed.

### DEC-004 — MASTER Baseline Freeze 0.1
Status: FROZEN

Rollback point: `RP-001 — MASTER Baseline Freeze 0.1`.

### DEC-005 — First scientific activity
Status: SATISFIED / CLOSED

`Prior-Art & Definitions Audit 0.1` completed with `PASS — CLAIM-RESTRICTED`; programme action `RESTRICT / REINTERPRET`.

### DEC-006 — CORE dependency on first literature audit
Status: SATISFIED / CLOSED

CORE remained unopened until the literature audit was frozen.

### DEC-007 — Prior-Art & Definitions Audit Freeze 0.1
Status: FROZEN

Rollback point: `RP-002 — Prior-Art & Definitions Audit Freeze 0.1`.
Canonical commit: `e21f3086657b9eb89f5b9ffa5ffdbdc4ba8b5b0d`.

### DEC-008 — Generic controlled-state novelty claims demoted
Status: FROZEN

No generic novelty claim is allowed for intervention-conditioned future responses, controlled/interventional behavioral equivalence, intervention-sufficient low-dimensional state representations, or controlled closure/lumpability. `Causal order parameter`, `interventional slaving`, local causal atlases, and controlled state preparation remain restricted project terms / OPEN directions.

### DEC-009 — Surviving CORE boundary
Status: SATISFIED / CLOSED

CORE tested only the theorem-level relationship between pre-existing synergetic slaving/order-parameter structure and frozen intervention-relative sufficiency/closure.

### DEC-010 — Applications blocked pending CORE
Status: SATISFIED / CLOSED

No application branch opened before CORE returned and MASTER integrated the result.

### DEC-011 — CORE Synergetic Sufficiency Boundary Freeze 0.1
Status: FROZEN

Canonical result: `research/core/synergetic_sufficiency_boundary_0_1.md`.
Canonical result commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`.
Decision: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.

Frozen conclusions include exact full-trajectory fibre sufficiency iff controlled projectability/closure (`SUBSUMED`), failure of classical unforced slaving to imply controlled sufficiency, the witness `q̇=ur`, `ṙ=-λr+u`, and exact/general finite-horizon bridge bounds without novelty promotion.

Rollback point: `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`.

### DEC-012 — Neural Minimal Benchmark 0.1
Status: SATISFIED / CLOSED

Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen observations include identical current function, matched simple norms, symmetric reversal of one-step adaptation preference, exact analytic/autograd agreement, local `4 passed`, and no retuning.

### DEC-013 — Historical reachability and nonlinear scaling blocked pending minimal benchmark
Status: SATISFIED / CLOSED

The minimal benchmark returned before either extension opened.

### DEC-014 — Neural Minimal Benchmark Result Freeze 0.1
Status: FROZEN

Rollback point: `RP-004 — Neural Minimal Benchmark Result Freeze 0.1`.

The exact linear benchmark may not be retrospectively improved by changing states, tasks, learning rate, optimizer, horizon, or response metric.

### DEC-015 — Neural Historical Reachability 0.1
Status: SATISFIED / CLOSED

Canonical result: `research/app_a/neural_historical_reachability_0_1.md`.
Historical implementation commit: `e342ef5c5cefae30df45e23bc667f149e818238c`.
Canonical result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen conclusions: one pre-specified auxiliary-gradient history from common initialization reaches the exact A/B states while the main function remains fixed; prior C/D responses reproduce; combined local tests report `8 passed`; no alternative history was tried.

### DEC-016 — Nonlinear scaling blocked pending historical return
Status: SATISFIED / CLOSED

The historical gate returned before nonlinear work was authorised.

### DEC-017 — Neural Historical Reachability Result Freeze 0.1
Status: FROZEN

Rollback point: `RP-005 — Neural Historical Reachability Result Freeze 0.1`.

Claim ceiling: reachability is established only for the explicit symmetric auxiliary-gradient preparation mechanism. Ordinary single-head SGD reachability and generic/realistic training-history claims remain unestablished.

### DEC-018 — Neural Nonlinear ReLU Pilot 0.1
Status: SATISFIED / CLOSED

Canonical result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`.
Implementation commit: `b5ba5da30d869d160eab0a7801bcfa324860b19a`.
Test commit: `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`.
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen observations:

1. The two bias-free two-unit ReLU states are globally function-equivalent by positive homogeneity.
2. Simple norms match.
3. Task C gives state A lower one-step loss (`0.14045` vs `0.2312`).
4. Task D gives state B lower one-step loss (`0.14045` vs `0.2312`).
5. Directed advantage magnitude is `0.09075` symmetrically.
6. Activation margins remain strict.
7. Analytical/autograd discrepancy is `0.0` in float64.
8. Combined unchanged regression suite reports `12 passed`.
9. No alternative scaling, state pair, task, optimizer, tolerance, probe set, or horizon was tried.

### DEC-019 — Learned coordinates and broader scaling blocked pending ReLU return
Status: SATISFIED / CLOSED

The ReLU pilot returned before learned-coordinate, multi-step, real-data, LoRA, power-grid, state-preparation, or manuscript work was opened.

### DEC-020 — Neural Nonlinear ReLU Pilot Result Freeze 0.1
Status: FROZEN

The ReLU pilot is accepted as canonical and may not be retrospectively improved by changing its scaling symmetry, states, tasks, probe set, learning rate, optimizer, horizon, tolerance, or response definition.

Rollback point: `RP-006 — Neural Nonlinear ReLU Pilot Result Freeze 0.1`.

Allowed interpretation remains restricted to one exact frozen two-unit ReLU symmetry pair with opposite symmetric one-step adaptation preferences. No generic nonlinear, realistic-history, learned-coordinate, or novelty claim is promoted.

### DEC-021 — Neural Vertical Slice Go/Revise/Stop Gate 0.1
Status: FROZEN / COMPLETE

Canonical integration memo:
`research/master/neural_vertical_slice_go_revise_stop_0_1.md`.

Decision: **GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.

The five-stage vertical slice is accepted as a coherent feasibility chain because all pre-specified stages completed without post-hoc repair. The decision does not promote novelty. The strongest remaining limitations are prior-art subsumption, artificial historical reachability, tiny scale, one-step horizon, and symmetry-engineered nonlinear evidence.

The next unresolved capability is held-out intervention prediction from a compact response/plasticity representation, not another showcase crossing.

Rollback point: `RP-007 — Neural Vertical Slice Decision Freeze 0.1`.

### DEC-022 — Neural Response Coordinate Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED

The specification gate was executed in MASTER before any held-out coordinate benchmark result was inspected.

Canonical gate memo:
`research/master/neural_response_coordinate_specification_gate_0_1.md`.

### DEC-023 — Neural Response Coordinate Specification Freeze 0.1
Status: FROZEN

Decision: **SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION**.

The frozen benchmark contains:

- one deterministic factorised-linear `d=4,h=5` family with 81 exactly function-equivalent states;
- a fixed two-dimensional latent response geometry with constant total layer/readout norms;
- deterministic 41/40 train/test state split;
- four fixed Hadamard calibration interventions and eight fixed held-out interventions;
- exact one-step full-batch GD response with `eta=0.1`;
- exactly 2D response-PCA coordinate from 16D calibration fingerprints;
- fixed bilinear OLS decoder;
- B0 current-function, B1 simple norm summaries, and B2 equal-dimensional raw-parameter PCA baselines;
- full-fingerprint and analytical-operator ceilings plus deterministic cyclic state-association null;
- fixed aggregate/per-intervention `R2_state`, NRMSE, leakage rules, and disjoint PASS/WEAK/NULL/FAIL thresholds;
- no dimension sweep, second coordinate, second state family, or threshold repair after held-out inspection.

Rollback point: `RP-008 — Neural Response Coordinate Specification Freeze 0.1`.

No scientific result is implied by this specification freeze.

### DEC-024 — Neural Response Coordinate Pilot 0.1 authorised
Status: SATISFIED / CLOSED

The frozen response-coordinate pilot was executed by `50 – APP-A – Neuronaler Minimalbenchmark` without repair or retuning.

Canonical execution prompt:
`research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.

### DEC-025 — Neural Response Coordinate Pilot 0.1 result
Status: FROZEN / COMPLETE

Canonical result:
`research/app_a/neural_response_coordinate_pilot_0_1.md`.
Implementation commit: `86715dfb9de78220964e137759c66785373f6de8`.
Test commit: `48d850c22ca156af892db11cbbdb95b20693bb08`.
Canonical result-freeze commit: `18618368991d818b3bfe883975b3ab2573bed0c6`.
Decision: **WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**.

Frozen observations:

- candidate 2D response coordinate: aggregate held-out `R2_state=1.0`;
- minimum per-held-out intervention `R2_state(c)=1.0`;
- B0 current-function baseline approximately `0.0`;
- B1 simple-summary baseline `0.070803629370716`;
- B2 equal-dimensional raw-parameter PCA baseline `0.999883026432542`;
- response-coordinate margin over B2 `0.000116973567458323`, below the frozen PASS requirement `>=0.05`;
- full-fingerprint ceiling `R2_state=1.0`;
- cyclic association null `R2_state=-0.200000000000001`;
- analytical/autograd maximum discrepancy `2.7755575615628914e-17` over all 972 audited state/intervention pairs;
- leakage controls and all sanity checks passed;
- new coordinate tests `12 passed`; combined APP-A regression suite `24 passed`;
- no retuning or alternate coordinate/family was tried.

The result establishes excellent held-out prediction in this synthetic family but not material predictive value beyond an equally compact raw-parameter PCA representation.

### DEC-026 — Neural Response Coordinate Result Freeze 0.1
Status: FROZEN

The WEAK result is accepted as canonical and may not be repaired by changing the family, coordinate, dimensionality, baselines, split, metrics, thresholds, interventions, learning rate, horizon, or null controls.

Rollback point: `RP-009 — Neural Response Coordinate Result Freeze 0.1`.

Claim ceiling: no generally useful causal/plasticity coordinate, no special response-aware value beyond raw-state geometry in general, and no novelty promotion.

### DEC-027 — Neural Response Coordinate WEAK Integration Gate 0.1
Status: SATISFIED / CLOSED

Canonical prompt:
`research/master/prompts/master_neural_response_coordinate_weak_integration_gate_0_1.md`.

Canonical integration memo:
`research/master/neural_response_coordinate_weak_integration_0_1.md`.

Decision: **REVISE — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.

The direction is not stopped because the response-aware coordinate achieved essentially exact held-out prediction with all validity controls passing. Direct GO to broader neural scaling is rejected because the equal-dimensional raw-state PCA comparator also achieved essentially exact prediction. The single unresolved prerequisite is a neutral nuisance-/reparameterisation-invariance discriminator.

Rollback point: `RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`.

### DEC-028 — Nuisance-invariance discriminator selected as sole revision prerequisite
Status: FROZEN

Before any broader response-coordinate claim, MASTER must determine whether a scientifically neutral benchmark can separate response-relevant geometry from response-irrelevant parameterisation nuisance.

The next construction must derive from explicit model reparameterisation/gauge/symmetry structure or another independently justified redundancy. It may not be chosen because it is expected to make raw PCA fail.

If no such construction can be specified cleanly, the coordinate direction must be parked rather than repaired by effect-guided family search.

### DEC-029 — Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1 authorised
Status: ACTIVE / MASTER-SPECIFICATION ONLY

The single next gate is:

`Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`.

Canonical prompt:
`research/master/prompts/master_neural_response_coordinate_nuisance_invariance_specification_gate_0_1.md`.

This gate is specification-only. It must define exactly one independently justified nuisance-control benchmark and pre-freeze state family, invariants, nuisance variables/levels, intervention split, coordinate, raw-state baselines, predictors, metrics, invariance measures, nulls, numerical tolerances, and PASS/WEAK/NULL/FAIL criteria before any execution.

No APP-A execution or broader neural/domain work is authorised until this gate completes.

## Rollback points

- `RP-001 — MASTER Baseline Freeze 0.1` — STABLE.
- `RP-002 — Prior-Art & Definitions Audit Freeze 0.1` — STABLE.
- `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1` — STABLE.
- `RP-004 — Neural Minimal Benchmark Result Freeze 0.1` — STABLE.
- `RP-005 — Neural Historical Reachability Result Freeze 0.1` — STABLE.
- `RP-006 — Neural Nonlinear ReLU Pilot Result Freeze 0.1` — STABLE.
- `RP-007 — Neural Vertical Slice Decision Freeze 0.1` — STABLE.
- `RP-008 — Neural Response Coordinate Specification Freeze 0.1` — STABLE.
- `RP-009 — Neural Response Coordinate Result Freeze 0.1` — STABLE.
- `RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1` — STABLE.

No prior freeze may be weakened. If the nuisance-invariance specification cannot be made scientifically neutral and falsifiable, return to `RP-010` and park the response-coordinate direction.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | READY | Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1 | WEAK integration REVISE frozen |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | COMPLETE / FROZEN / WAIT | Neural Response Coordinate Pilot 0.1 | no active execution |
| 60 – APP-B | UNOPENED | none | MASTER authorisation |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen results + MASTER authorisation |
