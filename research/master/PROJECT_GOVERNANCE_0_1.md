# Project Governance 0.1 — causal_synergetics

Status: FROZEN
Adopted by: 00 – MASTER – Projektplan & Status
Date: 2026-09-03

## 1. Purpose

`causal_synergetics` is governed as a controlled multi-chat research programme rather than as one unconstrained conversation. The goal is to parallelise scientific work while protecting reproducibility, pre-result commitments, negative results, rollback points, and the distinction between domain-specific and general claims.

## 2. Authority

MASTER is the only authority that may:

- open or close research chats/branches;
- authorise gates, freezes, executions, and cross-branch integration;
- change global success criteria;
- authorise retuning after result inspection;
- promote domain-specific findings into general claims;
- authorise manuscript claim freezes or submission steps.

Specialist chats may not silently expand their own scope.

## 3. Chat architecture

Chats are created lazily, only when MASTER authorises them.

Canonical names:

- `00 – MASTER – Projektplan & Status`
- `10 – CORE – Haupttheorie / mathematischer Kern`
- `20/30/40 – THEORY-*` when explicitly authorised
- `50/60/70 – APP-*` when explicitly authorised
- `80 – LIT – Literatur & Neuheitspositionierung`
- `90 – MANUSCRIPT – Manuskript & Figuren`

A chat that does not yet exist is `UNOPENED`, not missing or blocked.

## 4. Core workflow

Preferred sequence:

`GATE → FREEZE → EXECUTION → RESULT FREEZE`

Definitions:

- **GATE**: determines whether a candidate, branch, or activity is scientifically admissible.
- **FREEZE**: fixes assumptions, parameters, models, objectives, admissible geometries, horizons, methods, metrics, or claims before the next result inspection.
- **EXECUTION**: performs only the already authorised frozen analysis.
- **RESULT FREEZE**: preserves the observed result, including WEAK, NULL, or FAIL outcomes.

After a result freeze, improving the result through retuning is forbidden unless MASTER opens a new, explicitly separated branch before further inspection.

## 5. Commands

### GO

`GO` executes only the currently authorised `Next instruction` of that chat.

Before execution the chat must check:

1. current branch status;
2. explicit next instruction;
3. MASTER authorisation;
4. STOP boundary.

If no active authorised next instruction exists, return:

`GO ist derzeit blockiert. Dieser Branch muss zu MASTER zurück. Bitte dort Status? ausführen.`

`GO` never implicitly authorises new theory, parameter search, objective changes, model changes, application branches, literature branches, or freeze bypasses.

### Status?

`Status?` is primarily a MASTER command. MASTER reconstructs global project status, checks blockers, dependencies, freezes, branching discipline, rollback points, branch-independent versus branch-dependent results, and selects exactly one global next step.

The final MASTER status must state:

- overall status;
- active blocker;
- active branch;
- waiting branches;
- freeze check;
- rollback point;
- manuscript status;
- exactly one next global step;
- exact user command.

### PDF

`PDF` is a MASTER command that creates or updates a versioned canonical project report. The report must preserve current freeze status, negative results, assumptions, decision history, rollback points, branch-independent and branch-dependent results, claims, blockers, and roadmap.

## 6. Repository as single source of truth

Git is the canonical persistent state of the project.

Minimum MASTER files:

- `research/master/STATUS.md`
- `research/master/project_status.md`
- `research/master/decision_branch_log.md`
- `research/master/PROJECT_GOVERNANCE_0_1.md`
- `research/master/prompts/`

Specialist branch status files are created only when the corresponding chat/branch is authorised.

Each authorised branch should eventually maintain:

- `Current Gate`
- `Status`
- `Latest canonical file`
- `Dependencies`
- `Next instruction`
- `STOP boundary`

Versioned prompts and results are not overwritten after execution.

## 7. Decision & Branch Log

MASTER records decisions sequentially as `DEC-001`, `DEC-002`, ... . Earlier decisions are preserved and may later be marked STABLE, FROZEN, ACTIVE, OPEN, CLOSED, DEMOTED, or RESTRICTED; they are not erased.

## 8. Rollback points

Every major freeze establishes a rollback point. Failed later branches return the project to the latest stable rollback point rather than rewriting earlier results.

## 9. Branch-independent vs branch-dependent results

MASTER must distinguish:

- **branch-independent** results: general mathematical structure, shared methodology, shared governance;
- **branch-dependent** results: domain semantics, parameters, application-specific effects, optimisers, or effect magnitudes.

No application result becomes a theorem without an explicit justification and MASTER promotion.

## 10. Protected branches

MASTER may mark future work as `PROTECTED`. A protected branch is scientifically reserved but may neither be discarded because of current results nor opened without a new MASTER gate.

## 11. Anti-cherry-picking discipline

Where scientifically applicable, freeze before effect inspection:

- model;
- physical or learning parameters;
- observable/channel;
- objective;
- admissible intervention/input geometry;
- normalisation;
- horizon ladder;
- numerical resolution;
- success and robustness criteria;
- numerical methods.

After effect inspection, the following are forbidden without a newly authorised branch:

- parameter retuning;
- new horizon selection;
- new objective or representation chosen for stronger effect;
- new admissible geometry;
- omission of weak horizons;
- repeated candidate search until a strong result appears.

Weak and negative outcomes remain valid scientific results.

## 12. CORE

CORE may develop definitions, propositions, lemmas, theorems, proofs, invariances, bounds, asymptotics, and operator structure. It must distinguish `THEOREM/PROVED`, `PROPOSITION`, `LEMMA`, `ASSUMPTION`, `CONJECTURE`, `INTERPRETATION`, and `OPEN QUESTION`.

A `CORE Mathematical Freeze` may only be changed through new MASTER authorisation.

## 13. APPLICATION chats

Each application chat covers one domain and must explicitly define the physical or computational semantics of state, interventions, observables, admissible inputs, parameters, objectives, and interpretation. Candidate selection may not be guided only by effect magnitude.

Frozen executions may end as `STRONG`, `WEAK`, `NULL`, or `FAIL`; all are admissible.

## 14. LITERATURE

The literature chat researches prior art, novelty positioning, mandatory citations, and claim limits. It does not automatically generate new theory.

Useful classifications include:

- `SAME / CLOSE / RELATED / DISTANT`
- `CONFIRM / RESTRICT / REINTERPRET / PROMOTE / DEMOTE / OPEN`

Absence of a SAME hit is never a novelty proof.

## 15. MANUSCRIPT

The manuscript chat writes only from MASTER-approved or frozen results unless new science is explicitly authorised. It may not create new simulations, horizons, parameter searches, or novelty claims on its own.

## 16. Prompt handoff

MASTER writes substantive authorised tasks to versioned files under:

`research/master/prompts/`

A specialist chat reads its `STATUS.md` and the referenced versioned prompt before `GO`.

After completion, the specialist records its result, updates status, reports the commit and CI state when relevant, then ends with an explicit STOP.

## 17. STOP discipline

Controlled work ends with one of:

- `STOP — RETURN TO MASTER`
- `STOP — WAIT`
- `STOP — AWAIT GO`
- `STOP — RESULT FROZEN`
- `STOP — BLOCKED`

After STOP, no new research begins autonomously.

## 18. Highest governance rule

When it is uncertain whether a new scientific step, branch, retuning, objective, simulation, or manuscript change is authorised, do not continue automatically.

Return:

`STOP — RETURN TO MASTER`

The optimisation target is not maximal research speed. It is a reproducible, auditable research process protected against post-hoc scientific decision-making.
