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
`Prior-Art & Definitions Audit 0.1` completed `PASS — CLAIM-RESTRICTED`; programme action `RESTRICT / REINTERPRET`.

### DEC-006 — CORE dependency on first literature audit
Status: SATISFIED / CLOSED
CORE stayed unopened until the literature audit was frozen.

### DEC-007 — Prior-Art & Definitions Audit Freeze 0.1
Status: FROZEN
Rollback point: `RP-002 — Prior-Art & Definitions Audit Freeze 0.1`; canonical commit `e21f3086657b9eb89f5b9ffa5ffdbdc4ba8b5b0d`.

### DEC-008 — Generic controlled-state novelty claims demoted
Status: FROZEN
No generic novelty claim is allowed for intervention-conditioned responses, controlled equivalence, low-dimensional sufficient representations, or controlled closure/lumpability. `Causal order parameter`, `interventional slaving`, local causal atlases and controlled state preparation remain restricted/open terms.

### DEC-009 — Surviving CORE boundary
Status: SATISFIED / CLOSED
CORE tested the relation between pre-existing synergetic slaving/order-parameter structure and frozen intervention-relative sufficiency/closure.

### DEC-010 — Applications blocked pending CORE
Status: SATISFIED / CLOSED
No application opened before CORE returned.

### DEC-011 — CORE Synergetic Sufficiency Boundary Freeze 0.1
Status: FROZEN
Canonical result `research/core/synergetic_sufficiency_boundary_0_1.md`; commit `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`; decision `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`; rollback `RP-003`.

### DEC-012 — Neural Minimal Benchmark 0.1
Status: SATISFIED / CLOSED
Canonical result `research/app_a/neural_minimal_benchmark_0_1.md`; implementation/test `649a187125c4ad410e0b16b77accbfacfb577371`; result freeze `f5f02c871093129ef012780dbfcbcf55ef4de6f3`; decision PASS.

### DEC-013 — Historical reachability and nonlinear scaling blocked pending minimal benchmark
Status: SATISFIED / CLOSED
The minimal benchmark returned before either extension opened.

### DEC-014 — Neural Minimal Benchmark Result Freeze 0.1
Status: FROZEN
Rollback `RP-004`; no retrospective change of states, tasks, optimizer, learning rate, horizon or response.

### DEC-015 — Neural Historical Reachability 0.1
Status: SATISFIED / CLOSED
Canonical result `research/app_a/neural_historical_reachability_0_1.md`; implementation `e342ef5c5cefae30df45e23bc667f149e818238c`; result freeze `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`; decision PASS.

### DEC-016 — Nonlinear scaling blocked pending historical return
Status: SATISFIED / CLOSED
Historical reachability returned before nonlinear work opened.

### DEC-017 — Neural Historical Reachability Result Freeze 0.1
Status: FROZEN
Rollback `RP-005`; claim ceiling is explicit auxiliary-gradient reachability only.

### DEC-018 — Neural Nonlinear ReLU Pilot 0.1
Status: SATISFIED / CLOSED
Canonical result `research/app_a/neural_nonlinear_relu_pilot_0_1.md`; implementation `b5ba5da30d869d160eab0a7801bcfa324860b19a`; test `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`; result freeze `ff9f575839848e80705cd73062d431b20ca4eb10`; decision PASS.

### DEC-019 — Learned coordinates and broader scaling blocked pending ReLU return
Status: SATISFIED / CLOSED
The ReLU pilot returned before learned-coordinate work.

### DEC-020 — Neural Nonlinear ReLU Pilot Result Freeze 0.1
Status: FROZEN
Rollback `RP-006`; interpretation remains restricted to the exact frozen two-unit ReLU symmetry pair.

### DEC-021 — Neural Vertical Slice Go/Revise/Stop Gate 0.1
Status: FROZEN / COMPLETE
Canonical memo `research/master/neural_vertical_slice_go_revise_stop_0_1.md`; decision `GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`; rollback `RP-007`.

### DEC-022 — Neural Response Coordinate Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
Specification completed before held-out inspection.

### DEC-023 — Neural Response Coordinate Specification Freeze 0.1
Status: FROZEN
Decision `SPECIFICATION FROZEN / APP-A READY`; rollback `RP-008`.

### DEC-024 — Neural Response Coordinate Pilot 0.1 authorised
Status: SATISFIED / CLOSED
Execution prompt `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.

### DEC-025 — Neural Response Coordinate Pilot 0.1 result
Status: FROZEN / COMPLETE
Canonical result `research/app_a/neural_response_coordinate_pilot_0_1.md`; decision `WEAK — RESULT FROZEN`; candidate `R2=1.0`, equal-dimensional raw PCA `R2=0.999883026432542`; no retuning.

### DEC-026 — Neural Response Coordinate Result Freeze 0.1
Status: FROZEN
Rollback `RP-009`; no repair by changing family, coordinate, dimension, baselines, split, metrics, thresholds, interventions, learning rate, horizon or nulls.

### DEC-027 — Neural Response Coordinate WEAK Integration Gate 0.1
Status: SATISFIED / CLOSED
Canonical memo `research/master/neural_response_coordinate_weak_integration_0_1.md`; decision `REVISE — CLAIM-RESTRICTED`; rollback `RP-010`.

### DEC-028 — Nuisance-invariance discriminator selected as sole revision prerequisite
Status: FROZEN
Any nuisance had to derive from explicit model gauge/symmetry or independently justified redundancy, not anticipated baseline failure.

### DEC-029 — Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
MASTER-only specification completed without held-out execution.

### DEC-030 — Orthogonal hidden-basis gauge selected as neutral nuisance
Status: FROZEN
`(U,v)->(QU,Qv)` with frozen subgroup `Q(phi)=R(phi)⊕I3` preserves current function and exact response operator.

### DEC-031 — Neural Response Coordinate Nuisance-Invariance Specification Freeze 0.1
Status: FROZEN
Canonical memo `research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`; rollback `RP-011`.

### DEC-032 — Neural Response Coordinate Nuisance-Invariance Pilot 0.1 authorised
Status: SATISFIED / CLOSED
APP-A executed only the frozen specification.

### DEC-033 — Neural Response Coordinate Nuisance-Invariance Pilot 0.1 result
Status: FROZEN / COMPLETE
Canonical result `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`; decision `FAIL — SPECIFICATION CLASSIFICATION GAP`; candidate and symmetry-aware Gram-PCA both exact; high N0 left unrepaired; combined tests `36 passed`.

### DEC-034 — Neural Response Coordinate Nuisance-Invariance Result Freeze 0.1
Status: FROZEN
Rollback `RP-012`; failed gate may not be repaired or relabelled.

### DEC-035 — Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1
Status: SATISFIED / CLOSED
Canonical memo `research/master/neural_response_coordinate_nuisance_fail_integration_0_1.md`; decision `STOP / PARK RESPONSE-COORDINATE DIRECTION`.

### DEC-036 — Response-coordinate direction parked
Status: FROZEN
Further neural response-coordinate/null/nuisance construction is parked because symmetry-aware Gram-PCA matches the candidate and further repair has low incremental value.

### DEC-037 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1
Status: FROZEN
Rollback `RP-013`; APP-A response-coordinate work is PARKED / FROZEN / WAIT.

### DEC-038 — Post-coordinate programme reselection
Status: STABLE / SELECTED
MASTER selected cross-domain transfer before further neural depth.

### DEC-039 — Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1 authorised
Status: SATISFIED / CLOSED
Canonical prompt `research/master/prompts/master_power_grid_minimal_benchmark_feasibility_specification_gate_0_1.md`; completed before any effect inspection.

### DEC-040 — Power-Grid Minimal Benchmark Specification Freeze 0.1
Status: FROZEN
Canonical specification `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`; decision `SPECIFICATION FROZEN / APP-B READY`; rollback `RP-014`.

### DEC-041 — Power-Grid Minimal Benchmark 0.1 authorised
Status: SATISFIED / CLOSED
Execution prompt `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`; APP-B executed only the freeze.

### DEC-042 — Power-Grid Minimal Benchmark 0.1 result
Status: FROZEN / COMPLETE
Canonical result `research/app_b/power_grid_minimal_benchmark_0_1.md`; implementation `a98c9447aa50b6bb8974b2522543d72784be24ce`; test `5774dac821fc3d4878feee32a4fe13b7553abe33`; result creation `c0c24c2a3266eb69daaa12340e8b7dc68248956f`; decision PASS. Frozen metrics include `E_pass=0`, `E_B0_min=0.3549858420076152`, `E_B1_min=0.06534774384333092`, `H_delta=0.13069548768668177`, mean/COI closure error `3.885780586188048e-14`, tests `5 passed`.

### DEC-043 — Power-Grid Minimal Benchmark Result Freeze 0.1
Status: FROZEN
Rollback `RP-015`; PASS is restricted to the exact representative-machine macro; exact mean/COI closure blocks claims that all low-dimensional grid aggregates fail.

### DEC-044 — Cross-Domain Intervention-Sufficiency Integration Gate 0.1 authorised
Status: SATISFIED / CLOSED
Canonical prompt `research/master/prompts/master_cross_domain_intervention_sufficiency_integration_gate_0_1.md`; integration executed from frozen state through `RP-015`.

### DEC-045 — Cross-Domain Intervention-Sufficiency Integration decision
Status: FROZEN / COMPLETE
Canonical memo: `research/master/cross_domain_intervention_sufficiency_integration_0_1.md`.
Decision: **GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**.
The CORE boundary plus neural minimal/history/ReLU evidence and the physically distinct power-grid PASS form a coherent feasibility chain. The neural response-coordinate WEAK/FAIL evidence remains visible and parked. Programme coherence is not novelty or generic universality.

### DEC-046 — Cross-Domain Intervention-Sufficiency Integration Freeze 0.1
Status: FROZEN
Rollback point: `RP-016 — Cross-Domain Intervention-Sufficiency Integration Freeze 0.1`.
No prior result is promoted, repaired or weakened. No specialist execution branch is opened by this freeze.

### DEC-047 — Controlled State Preparation Feasibility & Specification Gate 0.1 authorised
Status: ACTIVE / MASTER-SPECIFICATION ONLY
Canonical prompt: `research/master/prompts/master_controlled_state_preparation_feasibility_specification_gate_0_1.md`.
Purpose: determine whether exactly one narrow preparation benchmark can be frozen in which a declared current observable/macro/function is preserved, hidden/internal state is deliberately changed under a fixed admissible preparation budget, and a separately frozen later intervention response changes in a targeted measurable way.
The gate must select exactly one domain/candidate or return REVISE/STOP. It may not execute preparation, reopen response-coordinate work, retune APP-B, start new literature/theory/manuscript work, or open multiple preparation branches.

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
- `RP-016 — Cross-Domain Intervention-Sufficiency Integration Freeze 0.1` — STABLE.

No prior freeze may be weakened. WEAK/NULL/FAIL/PASS outcomes remain canonical and may not be retuned or relabelled.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | READY | Controlled State Preparation Feasibility & Specification Gate 0.1 | `RP-016` stable |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | PARKED / FROZEN / WAIT | response-coordinate direction parked | new independent MASTER question required |
| 60 – APP-B | COMPLETE / PASS — RESULT FROZEN / WAIT | Power-Grid Minimal Benchmark 0.1 | returned to MASTER |
| 70 – APP-C | UNOPENED | none | successful preparation specification freeze required |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen results + MASTER authorisation |
