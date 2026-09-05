# Prompt — Manuscript Submission Readiness & Artifact Packaging Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-05
Dependency: `RP-024 — Manuscript Editorial Completion Freeze 0.1`

## Name

`Manuscript Submission Readiness & Artifact Packaging Gate 0.1`

## Purpose

Audit whether the frozen editorial manuscript can proceed toward a submission package without any new science or claim change, and determine exactly one minimum next action.

This is a MASTER governance/artifact-readiness gate only. It must not submit the manuscript, select stronger claims, run simulations, add literature families, or rewrite scientific content.

## Frozen basis

Use only canonical state through `RP-024`, especially:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/master/manuscript_initial_draft_integration_compliance_0_1.md`;
- `research/master/manuscript_editorial_completion_result_freeze_0_1.md`;
- `research/manuscript/manuscript_editorial_completion_0_1.md`;
- `research/manuscript/STATUS.md`;
- repository artifact inventory and frozen scientific source/result files as needed only for reproducibility pointers.

## Required evaluation dimensions

Evaluate at least:

1. **Editorial integrity:** verify that the editorial version changed only authorised bibliographic/formatting material and preserved the scientific claim ceiling.
2. **Submission-source completeness:** identify whether a venue-neutral manuscript source package exists beyond Markdown and what conversion/formatting is still required.
3. **Figure readiness:** audit the frozen Figure 1–4 inventory; determine which are conceptual and may be rendered without new science, whether any frozen trajectory artifacts already exist, and whether any figure request would require forbidden reruns.
4. **Table readiness:** verify that all tables use only frozen values and can be rendered directly from canonical manuscript content.
5. **Supplement readiness:** distinguish a supplement outline from a complete supplement; identify which appendices can be compiled directly from frozen canonical results without new scientific work.
6. **Reproducibility pointers:** inventory frozen code/test/result paths and determine what repository references can be included without reruns or new evidence.
7. **Bibliography readiness:** confirm that the explicitly identified metadata TODOs are closed and identify only ordinary formatting issues if any remain.
8. **Venue dependency:** determine whether venue selection is now a necessary prerequisite before final typesetting/page-limit decisions, or whether a venue-neutral artifact package should be created first.
9. **Submission blockers:** separate scientific/claim blockers from artifact, formatting, venue and administrative blockers.
10. **Governance:** preserve all freezes, negative evidence and claim demotions; no submission action may occur inside this gate.

## Required decision

Choose exactly one:

- `GO — VENUE-NEUTRAL ARTIFACT COMPLETION ONLY`
- `GO — VENUE SELECTION / FORMAT SPECIFICATION REQUIRED`
- `REVISE — PRESENTATIONAL / ARTIFACT COMPLIANCE FIXES REQUIRED`
- `STOP — SCIENTIFIC OR CLAIM READINESS LOST`

If the first option is selected, authorise exactly one tightly scoped MANUSCRIPT task to create only venue-neutral, claim-preserving artifacts from frozen content (for example rendered conceptual figures, complete supplement text, bibliography-normalised source, and a submission-neutral manuscript package) with no new scientific execution.

If venue selection is required first, specify exactly what venue-dependent decision cannot be safely deferred and stop without formatting work.

If REVISE, enumerate only concrete presentational/artifact defects and authorise one correction pass.

If STOP, identify the scientific/claim inconsistency that invalidates readiness.

## Mandatory deliverable

Create:

`research/master/manuscript_submission_readiness_artifact_packaging_0_1.md`

It must include:

- executive decision;
- artifact-readiness matrix;
- figure/table/supplement inventory;
- bibliography and reproducibility status;
- venue-dependency assessment;
- exact remaining blockers;
- exactly one next action or STOP;
- rollback/branch recommendation;
- exact next user command.

## Forbidden actions

Do not:

- submit to any venue;
- choose or imply a venue unless required by the gate decision;
- rewrite scientific claims;
- run or rerun simulations;
- create new empirical data or metrics;
- broaden literature positioning;
- repair WEAK/FAIL outcomes;
- introduce new figures requiring scientific result generation;
- promote novelty, priority, robustness, optimality or genericity;
- open parallel artifact/submission routes.

## Final handoff

After committing the readiness memo, update MASTER status, project status and Decision & Branch Log. End with exactly one next user action consistent with the decision.
