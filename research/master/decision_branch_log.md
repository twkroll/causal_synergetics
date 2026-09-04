# Decision & Branch Log — causal_synergetics

Last updated: 2026-09-04
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

Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen observations include identical current function, matched simple norms, symmetric reversal of one-step adaptation preference, exact analytic/autograd agreement, local `4 passed`, and no retuning.

### DEC-013 — Historical reachability and nonlinear scaling were blocked pending minimal benchmark
Status: SATISFIED / CLOSED

The minimal benchmark returned before either extension was opened.

### DEC-014 — Neural Minimal Benchmark Result Freeze 0.1
Status: FROZEN

Rollback point: `RP-004 — Neural Minimal Benchmark Result Freeze 0.1`.

The exact linear benchmark may not be retrospectively improved by changing states, tasks, learning rate, optimizer, horizon, or response metric.

### DEC-015 — Neural Historical Reachability 0.1
Status: SATISFIED / CLOSED

The single pre-frozen historical construction was executed without retuning.

Canonical result: `research/app_a/neural_historical_reachability_0_1.md`.
Historical test-addition commit: `ad9cc18a0519ffcfc4e6bc2e919e82f40bf54208`.
Historical implementation commit: `e342ef5c5cefae30df45e23bc667f149e818238c`.
Canonical result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`.
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Frozen conclusions:

1. Both histories start from the same `U_0=0` and fixed main readout `v=e1`.
2. A fixed auxiliary readout `a=e2` with symmetric targets `e1/e2` and exactly one `U`-only gradient step at `eta_hist=1` reaches the previously frozen A/B states exactly.
3. The main function remains exactly `w=0` before and after preparation.
4. Historical analytical/autograd discrepancy is `0.0` in float64.
5. The previously frozen C/D evaluation reproduces unchanged.
6. Combined frozen local tests report `8 passed`.
7. No alternative history was tried.

### DEC-016 — Nonlinear scaling remained blocked pending historical return
Status: SATISFIED / CLOSED

The historical gate returned before nonlinear work was authorised.

### DEC-017 — Neural Historical Reachability Result Freeze 0.1
Status: FROZEN

The historical result is accepted as canonical and may not be retrospectively naturalised by changing the auxiliary readout, targets, learning rate, initialization, number of steps, or optimizer semantics.

Rollback point: `RP-005 — Neural Historical Reachability Result Freeze 0.1`.

Claim ceiling: reachability is established only for the explicit symmetric auxiliary-gradient preparation mechanism. Ordinary single-head SGD reachability, generic SGD reachability, necessity/uniqueness, and realistic training-history claims remain OPEN / unestablished.

### DEC-018 — Neural Nonlinear ReLU Pilot 0.1 authorised
Status: ACTIVE / FROZEN SPECIFICATION

The next scientific activity remains in the existing chat:

`50 – APP-A – Neuronaler Minimalbenchmark`.

Canonical prompt:
`research/master/prompts/app_a_neural_nonlinear_relu_pilot_0_1.md`.

Purpose: test a single pre-specified nonlinear extension using a bias-free two-unit ReLU network, without searching for a favourable nonlinear example.

Frozen before execution:

- model `f_{U,v}(x)=v^T ReLU(Ux)`, `d=h=2`, no bias;
- State A: `U_A=[[2,0],[0,1]]`, `v_A=(1/2,1)`;
- State B: `U_B=[[1,0],[0,2]]`, `v_B=(1,1/2)`;
- global current-function equality by positive homogeneity;
- matched simple norms;
- Task C: `x=(1,-1)`, target `2`;
- Task D: `x=(-1,1)`, target `2`;
- exactly one simultaneous full-batch GD step on `(U,v)` at `eta=0.1`;
- ordered probe set `[(1,-1),(-1,1),(1,1),(-1,-1)]`;
- frozen response vectors and post-step losses;
- absolute tolerance `1e-12`;
- no alternative ReLU scaling/state pair if the pilot fails.

Frozen expected losses:

- Task C: A `0.14045`, B `0.2312`;
- Task D: A `0.2312`, B `0.14045`;
- symmetric directed advantage `0.09075`.

This gate carries `NO NOVELTY PROMOTION`.

### DEC-019 — Learned coordinates and broader scaling remain blocked
Status: ACTIVE

Even if the nonlinear ReLU pilot passes, it does not automatically authorise learned response/plasticity coordinates, multi-step or real-data scaling, realistic nonlinear histories, NTK/LoRA/adapter comparisons, power-grid work, controlled state preparation, or manuscript drafting. MASTER must perform a new `Status?` integration first.

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

### RP-005 — Neural Historical Reachability Result Freeze 0.1
Status: STABLE

Frozen exact auxiliary-gradient history from common initialization to the benchmark pair while preserving the main function.

If the nonlinear ReLU pilot fails, return here. Do not repair it by changing the nonlinear state pair, tasks, learning rate, probes, horizon, or response definition.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | ACTIVE / WAIT | Post-history integration complete | nonlinear APP-A return |
| 10 – CORE | COMPLETE / FROZEN / WAIT | CORE Synergetic Sufficiency Boundary 0.1 | satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | READY / AWAIT GO | Neural Nonlinear ReLU Pilot 0.1 | history PASS/FROZEN |
| 60 – APP-B | UNOPENED | none | MASTER authorisation |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN / WAIT | Prior-Art & Definitions Audit 0.1 | satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen results + MASTER authorisation |
