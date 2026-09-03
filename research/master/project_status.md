# Project Status — causal_synergetics

Version: 0.2
Date: 2026-09-03
Overall status: FIRST SCIENTIFIC AUDIT FROZEN / CORE READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-002 — Prior-Art & Definitions Audit Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an already established theory.

## Current scientific state

The first scientific result is complete and frozen:

`research/literature/prior_art_definitions_audit_0_1.md`

Decision: `PASS — CLAIM-RESTRICTED`.
Programme action: `RESTRICT / REINTERPRET`.

The audit substantially demotes the generic novelty claims around controlled/intervention-conditioned state description. The programme may not present intervention-relative response kernels, controlled behavioral equivalence, low-dimensional intervention-sufficient representations, or controlled closure/lumpability as generic new ideas.

The surviving candidate boundary is much narrower: test whether a **pre-existing synergetic order-parameter/slaving reduction** has a theorem-level relation to **intervention-relative response sufficiency and controlled closure** that is not merely a restatement of predictive-state, bisimulation/lumpability, causal-abstraction, or standard singular-perturbation theory.

This surviving boundary is a hypothesis target, not an established novelty result.

## Branch-independent results

- Governance 0.1.
- Git single-source-of-truth rule.
- Lazy branch/chat creation.
- MASTER Baseline Freeze 0.1.
- Prior-art claim restriction: generic constructs 1–4 are established-prior-art territory and cannot carry field-level novelty.
- CORE must explicitly classify central results against named prior-art frameworks and accept `SUBSUMED` / `FAIL` outcomes.

## Branch-dependent results

### 80 – LIT

Status: COMPLETE / FROZEN.
Gate: `Prior-Art & Definitions Audit 0.1`.
Result: `PASS — CLAIM-RESTRICTED`.
Canonical file: `research/literature/prior_art_definitions_audit_0_1.md`.
Deliverable commit: `e21f3086657b9eb89f5b9ffa5ffdbdc4ba8b5b0d`.

## Active branch

`10 – CORE – Haupttheorie / mathematischer Kern`

Status: READY / CHAT UNOPENED.
Current gate: `CORE Synergetic Sufficiency Boundary 0.1`.
Prompt: `research/master/prompts/core_synergetic_sufficiency_boundary_0_1.md`.

CORE is authorised to test only the frozen mathematical boundary:

1. whether classical slaving assumptions imply response homogeneity along order-parameter fibres for frozen `(U,T,Gamma)`;
2. a minimal counterexample where passive/unforced reduction is correct but interventions reveal fibre heterogeneity through nominally slaved modes;
3. if feasible, a quantitative response-error bound tied to fast-mode/slaving error and intervention coupling;
4. controlled closure analysed separately from response sufficiency.

## Waiting branches

- `20/30/40 – THEORY-*`: UNOPENED.
- `50/60/70 – APP-*`: UNOPENED and blocked pending CORE return + new MASTER authorisation.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

The prior-art result is frozen as `RP-002`. CORE may not weaken or reinterpret that audit to create novelty. No effect-bearing application model, parameter set, objective, intervention geometry, horizon, or success criterion has yet been selected or tuned.

## Branching check

OK.

Exactly one new scientific branch is authorised: CORE. Applications remain unopened. No parallel application work is justified yet because the theorem-level synergetic boundary may still fail or be fully subsumed.

## Rollback

Latest stable savepoint:

`RP-002 — Prior-Art & Definitions Audit Freeze 0.1`.

If CORE returns `FAIL` or `SUBSUMED`, MASTER returns to RP-002 and reassesses the programme without reopening the literature audit or retroactively widening claims.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## Active blocker

Operational only: the authorised CORE chat has not yet been created/executed.

## Next global step

Create the chat:

`10 – CORE – Haupttheorie / mathematischer Kern`

Paste the authorised start text from:

`research/master/prompts/core_synergetic_sufficiency_boundary_0_1.md`

Then enter:

`GO`

After CORE reaches its prescribed `STOP — RETURN TO MASTER`, return to `00 – MASTER` and enter:

`Status?`
