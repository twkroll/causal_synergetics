# Decision & Branch Log — causal_synergetics

Last updated: 2026-09-03
Governance: `PROJECT_GOVERNANCE_0_1.md`

## Decisions

### DEC-001 — Project Governance 0.1
Status: FROZEN

The project adopts `research/master/PROJECT_GOVERNANCE_0_1.md` as the canonical governance protocol.

### DEC-002 — Git as single source of truth
Status: STABLE

Repository `twkroll/causal_synergetics` is the canonical persistent project state. Chat context may guide work, but durable status, prompts, decisions, freezes, and results must be reflected in Git when they become canonical.

### DEC-003 — Lazy chat creation
Status: STABLE

Specialist chats are created only when MASTER authorises a concrete task. Uncreated chats are classified as `UNOPENED`, not as missing or failed.

### DEC-004 — MASTER Baseline Freeze 0.1
Status: FROZEN

Rollback point: `RP-001 — MASTER Baseline Freeze 0.1`.

### DEC-005 — First scientific activity
Status: SATISFIED / CLOSED

`Prior-Art & Definitions Audit 0.1` was executed by `80 – LIT – Literatur & Neuheitspositionierung`.
Result: `PASS — CLAIM-RESTRICTED`.
Programme action: `RESTRICT / REINTERPRET`.
Canonical result: `research/literature/prior_art_definitions_audit_0_1.md`.

### DEC-006 — CORE dependency on first literature audit
Status: SATISFIED / CLOSED

CORE remained unopened until the first definitions/prior-art audit was frozen.

### DEC-007 — Prior-Art & Definitions Audit Freeze 0.1
Status: FROZEN

Rollback point: `RP-002 — Prior-Art & Definitions Audit Freeze 0.1`.
Audit deliverable commit: `e21f3086657b9eb89f5b9ffa5ffdbdc4ba8b5b0d`.

### DEC-008 — Generic controlled-state novelty claims demoted
Status: FROZEN

The programme must not claim generic novelty for intervention/action-conditioned future responses as state descriptors, equivalence by identical controlled/interventional behavior, low-dimensional intervention-sufficient representations, or dynamic closure / controlled lumpability as a generic requirement.

`Causal order parameter`, `interventional slaving`, local causal atlases, and controlled state preparation remain restricted project terms / OPEN directions, not established novelty claims.

### DEC-009 — Surviving CORE boundary
Status: SATISFIED / CLOSED

CORE was authorised to test only the theorem-level relationship between a pre-existing synergetic order-parameter/slaving reduction and a frozen intervention-relative response sufficiency / controlled-closure criterion.

Canonical prompt: `research/master/prompts/core_synergetic_sufficiency_boundary_0_1.md`.

### DEC-010 — Applications blocked pending CORE
Status: SATISFIED / CLOSED

No application branch opened before CORE returned and MASTER re-integrated the result.

### DEC-011 — CORE Synergetic Sufficiency Boundary Freeze 0.1
Status: FROZEN

Canonical result: `research/core/synergetic_sufficiency_boundary_0_1.md`.
Canonical result commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`.
Decision: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.

Frozen central conclusions:

1. For the frozen full `q(·)` response, exact fibre response homogeneity is equivalent to controlled projectability / exact controlled closure; this is `SUBSUMED` prior-art structure.
2. Classical unforced slaving alone does not imply controlled response sufficiency.
3. The minimal scalar slow/fast counterexample `q̇=ur`, `ṙ=-λr+u` has exact passive slaving but controlled response failure.
4. Exact model-specific finite-horizon bounds and a general comparison/ISS-style bridge bound connect fast relaxation, slaving defect, intervention leakage, and finite-horizon response error.
5. The bridge result is useful as a quantitative compatibility diagnostic but is not promoted as publication-level novel control theory.

Rollback point: `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`.

The CORE result may not be retrospectively strengthened by widening the literature claim boundary or changing its frozen response definition.

### DEC-012 — Neural Minimal Benchmark 0.1 authorised
Status: ACTIVE / FROZEN SPECIFICATION

The next scientific activity is assigned to:

`50 – APP-A – Neuronaler Minimalbenchmark`.

Canonical prompt:
`research/master/prompts/app_a_neural_minimal_benchmark_0_1.md`.

Purpose: create the smallest exact analytical + numerical neural benchmark showing that two parameter states with the same current function and matched simple norms can respond differently to the same frozen one-step learning intervention.

This benchmark is a feasibility scaffold only and carries `NO NOVELTY PROMOTION`.

The following are frozen before execution:

- factorised linear network `f_{U,v}(x)=v^T Ux`, `d=h=2`;
- exact state pair A/B;
- symmetric tasks `c_C=e1`, `c_D=e2`;
- one simultaneous full-batch GD step;
- `eta=0.1`;
- one-step horizon;
- primary response `w^+` and secondary response post-step task loss;
- analytical expected values and numerical tolerances;
- PASS/FAIL criteria.

No parameter, task, optimizer, model, horizon, or response search is allowed after execution begins.

### DEC-013 — Historical reachability and nonlinear scaling remain blocked
Status: ACTIVE

Even if Neural Minimal Benchmark 0.1 passes, it does not authorise:

- historical training construction of the state pair;
- nonlinear networks;
- learned response/plasticity coordinates;
- NTK/LoRA/adapter comparisons;
- multi-step or real-dataset experiments;
- power-grid work;
- manuscript drafting.

Each requires a new MASTER gate after the frozen minimal benchmark returns.

## Rollback points

### RP-001 — MASTER Baseline Freeze 0.1
Status: STABLE

Governance-only pre-scientific baseline.

### RP-002 — Prior-Art & Definitions Audit Freeze 0.1
Status: STABLE

Contains the frozen claim restriction and surviving synergetic boundary.

### RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1
Status: STABLE

Contains the theorem-level boundary, minimal slow/fast counterexample, quantitative bridge diagnostic, and explicit `NO NOVELTY PROMOTION` ceiling.

If the neural benchmark fails, the project returns here without retuning the benchmark or altering the prior CORE/LIT freezes.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | ACTIVE / WAIT | Post-CORE integration complete | APP-A return |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | RETURN TO MASTER satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | READY / CHAT UNOPENED | Neural Minimal Benchmark 0.1 | CORE result satisfied |
| 60 – APP-B | UNOPENED | none | MASTER authorisation |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | RETURN TO MASTER satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen scientific results + MASTER authorisation |
