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
Status: ACTIVE

The first authorised scientific activity is `Prior-Art & Definitions Audit 0.1`, assigned to the future chat:

`80 – LIT – Literatur & Neuheitspositionierung`

This is a structural definitions/novelty audit, not effect-guided literature selection.

The audit must compare the proposed core constructs against at least:

- classical synergetics;
- computational mechanics / causal states;
- predictive state representations;
- bisimulation and controlled lumpability;
- causal abstraction / causal feature learning;
- control/system identification where directly relevant.

The audit may restrict or demote claims. It may not invent replacement theory.

### DEC-006 — CORE remains unopened
Status: ACTIVE

`10 – CORE – Haupttheorie / mathematischer Kern` remains `UNOPENED` until the first literature/definitions audit is frozen or MASTER explicitly overrides this dependency.

Rationale: the mathematical core should be written against a documented prior-art boundary rather than against an assumed novelty boundary.

## Rollback points

### RP-001 — MASTER Baseline Freeze 0.1
Status: STABLE

Contains:

- Governance 0.1;
- Git single-source-of-truth decision;
- lazy chat architecture;
- first scientific branch selection;
- dependency that CORE remains unopened pending audit.

If the first literature branch fails or is inconclusive, the project returns here without rewriting the initial governance state.

## Branch registry

| Chat / branch | Status | Current gate | Dependency |
|---|---|---|---|
| 00 – MASTER | ACTIVE / FROZEN BASELINE | MASTER Initialization Gate 0.1 | none |
| 10 – CORE | UNOPENED | none | Prior-Art & Definitions Audit 0.1 result |
| 20 – THEORY-A | UNOPENED | none | MASTER authorisation |
| 30 – THEORY-B | UNOPENED | none | MASTER authorisation |
| 40 – THEORY-C | UNOPENED | none | MASTER authorisation |
| 50 – APP-A | UNOPENED | none | MASTER authorisation |
| 60 – APP-B | UNOPENED | none | MASTER authorisation |
| 70 – APP-C | UNOPENED | none | MASTER authorisation |
| 80 – LIT | READY / CHAT UNOPENED | Prior-Art & Definitions Audit 0.1 | user creates chat, then GO |
| 90 – MANUSCRIPT | UNOPENED | none | frozen scientific results |
