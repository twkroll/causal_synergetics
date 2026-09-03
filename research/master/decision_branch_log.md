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

The initial governance state, project question, branch architecture, and first-step decision are frozen before scientific execution.

Rollback point: `RP-001 — MASTER Baseline Freeze 0.1`.

### DEC-005 — First scientific activity
Status: SATISFIED / CLOSED

`Prior-Art & Definitions Audit 0.1` was executed by `80 – LIT – Literatur & Neuheitspositionierung`.

Canonical result:
`research/literature/prior_art_definitions_audit_0_1.md`

Result: `PASS — CLAIM-RESTRICTED`.
Programme action: `RESTRICT / REINTERPRET`.

### DEC-006 — CORE dependency on first literature audit
Status: SATISFIED / CLOSED

CORE remained unopened until the first definitions/prior-art audit was frozen. That dependency is now satisfied.

### DEC-007 — Prior-Art & Definitions Audit Freeze 0.1
Status: FROZEN

The LIT audit is accepted as the canonical first scientific result and may not be retrospectively rewritten to widen novelty claims.

Rollback point: `RP-002 — Prior-Art & Definitions Audit Freeze 0.1`.

Audit deliverable commit: `e21f3086657b9eb89f5b9ffa5ffdbdc4ba8b5b0d`.

### DEC-008 — Generic controlled-state novelty claims demoted
Status: FROZEN

The programme must not claim generic novelty for:

- intervention/action-conditioned future responses as state descriptors;
- equivalence by identical controlled/interventional behavior;
- low-dimensional intervention-sufficient representations;
- dynamic closure / controlled lumpability as a generic requirement.

These have substantial SAME/CLOSE prior art in PSRs, input-output computational mechanics, bisimulation/homomorphism/lumpability, causal abstraction, control-oriented reduction, and related frameworks.

`Causal order parameter`, `interventional slaving`, local causal atlases, and controlled state preparation remain restricted project terms / OPEN directions, not established novelty claims.

### DEC-009 — Surviving CORE boundary
Status: ACTIVE / FROZEN SCOPE

The only currently authorised mathematical novelty boundary is a theorem-level test of the relationship between a **pre-existing classical synergetic order-parameter/slaving reduction** and a **frozen intervention-relative response sufficiency / controlled-closure criterion**.

CORE must ask whether synergetic slaving assumptions:

1. imply response homogeneity along order-parameter fibres under a frozen intervention family;
2. fail under a minimal controlled counterexample when nominally slaved modes are transiently/directly excited;
3. support a quantitative response-error bound under explicit assumptions;
4. imply controlled closure separately from response sufficiency.

If these results are fully subsumed by established singular perturbation, lumpability/bisimulation, or causal-abstraction theory, CORE must classify them `SUBSUMED` / `FAIL` rather than widening terminology.

Authorised prompt:
`research/master/prompts/core_synergetic_sufficiency_boundary_0_1.md`

### DEC-010 — Applications remain unopened
Status: ACTIVE

No neural, power-grid, ODE-discovery, atlas, or controlled-state-preparation branch may open before CORE returns from `CORE Synergetic Sufficiency Boundary 0.1` and MASTER performs a new `Status?` integration.

## Rollback points

### RP-001 — MASTER Baseline Freeze 0.1
Status: STABLE

Contains governance 0.1, Git single-source-of-truth, lazy chat creation, and the pre-scientific baseline.

### RP-002 — Prior-Art & Definitions Audit Freeze 0.1
Status: STABLE

Contains the first scientific prior-art boundary:

- constructs 1–4 generic novelty claims demoted;
- programme-level action `RESTRICT / REINTERPRET`;
- surviving candidate boundary restricted to synergetic order-parameter/slaving structure versus intervention-relative response sufficiency/closure;
- local atlas and controlled state preparation retained only as restricted OPEN future directions.

If CORE fails, the project returns here without reopening or weakening the audit.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | ACTIVE / WAIT | Post-LIT integration complete | CORE return |
| 10 – CORE | READY / CHAT UNOPENED | CORE Synergetic Sufficiency Boundary 0.1 | LIT audit satisfied |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | UNOPENED | none | CORE result + MASTER authorisation |
| 60 – APP-B | UNOPENED | none | CORE result + MASTER authorisation |
| 70 – APP-C | UNOPENED | none | CORE result + MASTER authorisation |
| 80 – LIT | COMPLETE / FROZEN | Prior-Art & Definitions Audit 0.1 | RETURN TO MASTER satisfied |
| 90 – MANUSCRIPT | UNOPENED | none | frozen scientific results + MASTER authorisation |
