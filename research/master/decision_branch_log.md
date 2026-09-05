# Decision & Branch Log — causal_synergetics

Last updated: 2026-09-05
Governance: `PROJECT_GOVERNANCE_0_1.md`

## Decisions

### DEC-001 — Project Governance 0.1
Status: FROZEN
`research/master/PROJECT_GOVERNANCE_0_1.md` is canonical governance.

### DEC-002 — Git as single source of truth
Status: STABLE
Repository `twkroll/causal_synergetics` is the canonical persistent project state.

### DEC-003 — Lazy chat creation
Status: STABLE
Specialist chats are created only when MASTER authorises a concrete task; uncreated chats are `UNOPENED`.

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
No generic novelty claim is allowed for intervention-conditioned future responses, controlled/interventional behavioral equivalence, intervention-sufficient low-dimensional representations, or controlled closure/lumpability. `Causal order parameter`, `interventional slaving`, local causal atlases, and controlled state preparation remain restricted/open project terms.

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
Rollback point: `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`.
Frozen conclusions include controlled-projectability/full-trajectory sufficiency (`SUBSUMED`), failure of classical unforced slaving to imply controlled sufficiency, the minimal witness `q̇=ur`, `ṙ=-λr+u`, and finite-horizon bridge bounds without novelty promotion.

### DEC-012 — Neural Minimal Benchmark 0.1
Status: SATISFIED / CLOSED
Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### DEC-013 — Historical reachability and nonlinear scaling blocked pending minimal benchmark
Status: SATISFIED / CLOSED
The minimal benchmark returned before either extension opened.

### DEC-014 — Neural Minimal Benchmark Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-004 — Neural Minimal Benchmark Result Freeze 0.1`.
No retrospective change of states, tasks, learning rate, optimizer, horizon, or response metric is allowed.

### DEC-015 — Neural Historical Reachability 0.1
Status: SATISFIED / CLOSED
Canonical result: `research/app_a/neural_historical_reachability_0_1.md`.
Implementation commit: `e342ef5c5cefae30df45e23bc667f149e818238c`.
Result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### DEC-016 — Nonlinear scaling blocked pending historical return
Status: SATISFIED / CLOSED
The historical gate returned before nonlinear work was authorised.

### DEC-017 — Neural Historical Reachability Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-005 — Neural Historical Reachability Result Freeze 0.1`.
Claim ceiling remains explicit auxiliary-gradient reachability only; ordinary/generic SGD reachability is unestablished.

### DEC-018 — Neural Nonlinear ReLU Pilot 0.1
Status: SATISFIED / CLOSED
Canonical result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`.
Implementation commit: `b5ba5da30d869d160eab0a7801bcfa324860b19a`.
Test commit: `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`.
Result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### DEC-019 — Learned coordinates and broader scaling blocked pending ReLU return
Status: SATISFIED / CLOSED
The ReLU pilot returned before learned-coordinate or broader scaling work opened.

### DEC-020 — Neural Nonlinear ReLU Pilot Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-006 — Neural Nonlinear ReLU Pilot Result Freeze 0.1`.
Allowed interpretation remains restricted to one exact frozen two-unit ReLU symmetry pair.

### DEC-021 — Neural Vertical Slice Go/Revise/Stop Gate 0.1
Status: FROZEN / COMPLETE
Canonical memo: `research/master/neural_vertical_slice_go_revise_stop_0_1.md`.
Decision: `GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.
Rollback point: `RP-007 — Neural Vertical Slice Decision Freeze 0.1`.

### DEC-022 — Neural Response Coordinate Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
The specification gate completed before held-out result inspection.

### DEC-023 — Neural Response Coordinate Specification Freeze 0.1
Status: FROZEN
Decision: `SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION`.
Rollback point: `RP-008 — Neural Response Coordinate Specification Freeze 0.1`.

### DEC-024 — Neural Response Coordinate Pilot 0.1 authorised
Status: SATISFIED / CLOSED
Canonical execution prompt: `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.

### DEC-025 — Neural Response Coordinate Pilot 0.1 result
Status: FROZEN / COMPLETE
Canonical result: `research/app_a/neural_response_coordinate_pilot_0_1.md`.
Implementation commit: `86715dfb9de78220964e137759c66785373f6de8`.
Test commit: `48d850c22ca156af892db11cbbdb95b20693bb08`.
Result-freeze commit: `18618368991d818b3bfe883975b3ab2573bed0c6`.
Decision: `WEAK — RESULT FROZEN / NO NOVELTY PROMOTION`.
Frozen facts include candidate `R2_state=1.0`, equal-dimensional raw PCA `R2_state=0.999883026432542`, and candidate-minus-B2 `0.000116973567458323 < 0.05`; no retuning.

### DEC-026 — Neural Response Coordinate Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-009 — Neural Response Coordinate Result Freeze 0.1`.
No repair by changing family, coordinate, dimension, baselines, split, metrics, thresholds, interventions, learning rate, horizon or nulls.

### DEC-027 — Neural Response Coordinate WEAK Integration Gate 0.1
Status: SATISFIED / CLOSED
Canonical memo: `research/master/neural_response_coordinate_weak_integration_0_1.md`.
Decision: `REVISE — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.
Rollback point: `RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`.

### DEC-028 — Nuisance-invariance discriminator selected as sole revision prerequisite
Status: FROZEN
Any next nuisance construction had to derive from explicit model reparameterisation/gauge/symmetry or another independently justified redundancy, not anticipated baseline failure.

### DEC-029 — Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
The MASTER-only specification gate completed without benchmark execution or held-out result inspection.

### DEC-030 — Orthogonal hidden-basis gauge selected as neutral nuisance
Status: FROZEN
The nuisance is `(U,v)->(QU,Qv)` for orthogonal hidden-space `Q`, preserving `w`, `U^TU`, `||v||`, the one-step response operator and response semantics. The single frozen subgroup is `Q(phi)=R(phi)⊕I3` at eight equally spaced angles.

### DEC-031 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1
Status: FROZEN
Canonical memo: `research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`.
Decision: `SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION`.
Rollback point: `RP-011 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1`.

### DEC-032 — Neural Response Coordinate Nuisance-Invariance Pilot 0.1 authorised
Status: SATISFIED / CLOSED
APP-A executed only the frozen specification and returned without repair.

### DEC-033 — Neural Response Coordinate Nuisance-Invariance Pilot 0.1 result
Status: FROZEN / COMPLETE
Canonical result: `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`.
Implementation commit: `988db41bad5d46615b00defe2da8964c15a5203f`.
Test commit: `2d7ac6171323607bfeeec12f3657b56b162e0406`.
Result-freeze commit: `8f2be1871605b39d9e851d1b47ed9c30ec7bf21f`.
Decision: `FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION`.
Frozen observations include exact candidate prediction/invariance, raw-PCA failure under gauge, exact gauge-aware Gram-PCA control, high N0, and `36 passed`; the classifier was non-total and was not repaired.

### DEC-034 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-012 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1`.
The failed gate may not be repaired or relabelled.

### DEC-035 — Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1
Status: SATISFIED / CLOSED
Canonical memo: `research/master/neural_response_coordinate_nuisance_fail_integration_0_1.md`.
Decision: `STOP / PARK RESPONSE-COORDINATE DIRECTION — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.

### DEC-036 — Response-coordinate direction parked
Status: FROZEN
MASTER parks further neural response-coordinate/null/nuisance benchmark construction under the current synthetic programme framing because the symmetry-aware Gram-PCA control matches the response coordinate and further repair has low incremental value.

### DEC-037 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1
Status: FROZEN
Rollback point: `RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1`.
`50 – APP-A` is `PARKED / FROZEN / WAIT` for response-coordinate work.

### DEC-038 — Post-coordinate programme reselection
Status: STABLE / SELECTED
After full MASTER reconstruction from `RP-013`, the programme selected cross-domain transfer before further neural depth.

### DEC-039 — Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
Canonical prompt: `research/master/prompts/master_power_grid_minimal_benchmark_feasibility_specification_gate_0_1.md`.
The gate completed before any power-grid trajectory/effect inspection.

### DEC-040 — Power-Grid Minimal Benchmark Specification Freeze 0.1
Status: FROZEN
Canonical specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`.
Decision: `SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION`.
Rollback point: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`.
Frozen design: one normalized two-machine nonlinear swing topology with `M=D=K=1`, representative-machine macro, hidden coherency errors, coherent initial states, `u=0,±0.2`, `T=5`, fixed RK4 resolutions, B0/B1/C1 controls and exhaustive classifier. No candidate search or retuning authorised.

### DEC-041 — Power-Grid Minimal Benchmark 0.1 authorised
Status: SATISFIED / CLOSED
Canonical execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`.
APP-B executed only the frozen benchmark and returned to MASTER.

### DEC-042 — Power-Grid Minimal Benchmark 0.1 result
Status: FROZEN / COMPLETE
Canonical result: `research/app_b/power_grid_minimal_benchmark_0_1.md`.
Implementation commit: `a98c9447aa50b6bb8974b2522543d72784be24ce`.
Test commit: `5774dac821fc3d4878feee32a4fe13b7553abe33`.
Result creation commit: `c0c24c2a3266eb69daaa12340e8b7dc68248956f`.
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**.
Frozen metrics: `E_pass=0`, `E_B0_min=0.3549858420076152`, `E_B1_min=0.06534774384333092`, `H_delta=0.13069548768668177`, mean/COI closure error `3.885780586188048e-14`, convergence error `8.1601392309949e-15`, odd-sign symmetry error `3.83026943495679e-14`, APP-B tests `5 passed`. No retuning or second candidate.

### DEC-043 — Power-Grid Minimal Benchmark Result Freeze 0.1
Status: FROZEN
Rollback point: `RP-015 — Power-Grid Minimal Benchmark Result Freeze 0.1`.
The PASS is restricted to the exact frozen representative-machine macro. The exact mean/COI closure remains a mandatory limitation and blocks claims that all low-dimensional grid aggregates fail.

### DEC-044 — Cross-Domain Intervention-Sufficiency Integration Gate 0.1 authorised
Status: ACTIVE / MASTER-INTEGRATION ONLY
Canonical prompt: `research/master/prompts/master_cross_domain_intervention_sufficiency_integration_gate_0_1.md`.
Purpose: integrate all frozen evidence through `RP-015` and choose exactly one of `GO`, `REVISE`, or `STOP` for the next programme stage. No state-preparation, new theory/literature, manuscript, APP-A reopening or second power-grid candidate is authorised during this gate.

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
- `RP-011 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1` — STABLE.
- `RP-012 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1` — STABLE.
- `RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1` — STABLE.
- `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1` — STABLE.
- `RP-015 — Power-Grid Minimal Benchmark Result Freeze 0.1` — STABLE.

No prior freeze may be weakened. Weak/NULL/FAIL/PASS results remain canonical and may not be retuned or relabelled.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | READY | Cross-Domain Intervention-Sufficiency Integration Gate 0.1 | `RP-015` stable |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | PARKED / FROZEN / WAIT | response-coordinate direction parked | new independent MASTER question required |
| 60 – APP-B | COMPLETE / PASS — RESULT FROZEN / WAIT | Power-Grid Minimal Benchmark 0.1 | returned to MASTER |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen results + MASTER authorisation |
