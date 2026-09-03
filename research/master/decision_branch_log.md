# Decision & Branch Log — causal_synergetics

Last updated: 2026-09-03
Governance: `PROJECT_GOVERNANCE_0_1.md`

## Decisions

### DEC-001 — Project Governance 0.1
Status: FROZEN

The project adopts `research/master/PROJECT_GOVERNANCE_0_1.md` as the canonical governance protocol.

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

Frozen conclusions include: exact full-trajectory fibre sufficiency iff controlled projectability/closure (`SUBSUMED`), classical unforced slaving alone does not imply controlled sufficiency, the minimal witness `q̇=ur`, `ṙ=-λr+u`, and exact/general finite-horizon bridge bounds without novelty promotion.

Rollback point: `RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1`.

### DEC-012 — Neural Minimal Benchmark 0.1
Status: SATISFIED / CLOSED

The pre-frozen factorised-linear benchmark was executed without retuning.

Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen observations:

- identical current function `w_A=w_B=(0,0)`;
- matched simple norms;
- Task C gives A the lower one-step loss (`0.32` vs `0.405`);
- Task D gives B the lower one-step loss (`0.32` vs `0.405`);
- symmetric advantage magnitude `0.085`;
- analytic/autograd maximum observed component difference `0.0` in float64;
- frozen local tests: `4 passed`;
- no alternative configuration was tried.

### DEC-013 — Historical reachability and nonlinear scaling were blocked pending minimal benchmark
Status: SATISFIED / CLOSED

The minimal benchmark has now returned. This decision does not automatically open nonlinear scaling or learned coordinates.

### DEC-014 — Neural Minimal Benchmark Result Freeze 0.1
Status: FROZEN

The APP-A benchmark result is accepted as canonical and may not be retrospectively improved by changing states, tasks, learning rate, optimizer, horizon, or response metric.

Rollback point: `RP-004 — Neural Minimal Benchmark Result Freeze 0.1`.

The allowed interpretation remains limited to the exact frozen factorised-linear benchmark; no novelty or nonlinear/general neural claim is promoted.

### DEC-015 — Neural Historical Reachability 0.1 authorised
Status: ACTIVE / FROZEN SPECIFICATION

The next scientific activity remains in:

`50 – APP-A – Neuronaler Minimalbenchmark`.

Canonical prompt:
`research/master/prompts/app_a_neural_historical_reachability_0_1.md`.

One and only one historical construction is frozen before execution:

- common hidden initialization `U_0=0`;
- frozen main readout `v=e1`;
- temporary auxiliary readout `a=e2`;
- symmetric history targets `c_A=e1`, `c_B=e2`;
- exactly one gradient step on `U` only;
- `eta_hist=1`;
- no momentum, noise, weight decay, stochasticity, optimizer state, or extra steps;
- expected exact endpoints are the previously frozen `U_A` and `U_B`;
- the main function must remain `w=0` before and after preparation;
- the previously frozen C/D benchmark must then reproduce without modification.

No second historical candidate is allowed if this construction fails.

### DEC-016 — Nonlinear scaling remains blocked
Status: ACTIVE

Even if Neural Historical Reachability 0.1 passes, it does not automatically authorise nonlinear networks, learned response/plasticity coordinates, NTK/LoRA/adapter comparisons, power-grid work, controlled state preparation, or manuscript drafting. MASTER must perform a new `Status?` integration first.

## Rollback points

### RP-001 — MASTER Baseline Freeze 0.1
Status: STABLE

Governance-only pre-scientific baseline.

### RP-002 — Prior-Art & Definitions Audit Freeze 0.1
Status: STABLE

Frozen claim restriction and surviving synergetic boundary.

### RP-003 — CORE Synergetic Sufficiency Boundary Freeze 0.1
Status: STABLE

Frozen theorem-level boundary and quantitative diagnostic.

### RP-004 — Neural Minimal Benchmark Result Freeze 0.1
Status: STABLE

Frozen exact linear neural benchmark with symmetric one-step adaptation reversal and no retuning.

If the historical-reachability gate fails, return here. Do not repair it by changing the historical protocol.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | ACTIVE / WAIT | Post-APP-A integration complete | historical APP-A return |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | READY / AWAIT GO | Neural Historical Reachability 0.1 | minimal benchmark PASS/FROZEN |
| 60 – APP-B | UNOPENED | none | MASTER authorisation |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen results + MASTER authorisation |
