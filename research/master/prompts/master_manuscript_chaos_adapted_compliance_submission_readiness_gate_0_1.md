# MASTER Prompt — Manuscript Chaos Adapted Compliance & Submission Readiness Gate 0.1

Assigned chat: `00 – MASTER – Projektplan & Status`
Status: AUTHORISED / AWAIT NAMED GATE
Dependency: `RP-030 — Manuscript Chaos Regular-Article Format Adaptation Freeze 0.1`

## Purpose

Audit the frozen Chaos Regular-Article adaptation for final venue compliance and submission-readiness prerequisites without submitting, inventing author metadata, or changing science/claims.

This is a MASTER compliance/readiness gate only.

## Required inputs

Read at minimum:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/master/STATUS.md`;
- `research/master/manuscript_venue_selection_format_specification_0_1.md`;
- `research/master/manuscript_chaos_regular_article_format_adaptation_result_freeze_0_1.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/manuscript/chaos_regular_article_0_1/manuscript_chaos_0_1.tex`;
- all section files referenced by the main source;
- `research/manuscript/chaos_regular_article_0_1/supplement_chaos_0_1.tex`;
- `research/manuscript/chaos_regular_article_0_1/references_chaos_0_1.bib`;
- `research/manuscript/chaos_regular_article_0_1/alt_text_0_1.md`;
- `research/manuscript/chaos_regular_article_0_1/submission_metadata_checklist_0_1.md`;
- `research/manuscript/chaos_regular_article_0_1/CHANGELOG.md`;
- frozen venue-neutral package and reproducibility manifest as needed.

## Gate task

1. Verify that the Chaos-adapted main manuscript preserves the frozen claim hierarchy, title/abstract constraints, mandatory negative evidence, successful countercontrols, citation roles, and section architecture.
2. Verify numerical statements and equation/figure roles against the frozen scientific sources where needed.
3. Verify that the abstract is one paragraph and `<=250` words and that the first Introduction paragraph satisfies the frozen Lead-Paragraph transformation without claim escalation.
4. Audit reference normalization for cited-work-set preservation; no new literature search is authorised unless needed solely to verify a current venue-format rule.
5. Audit figure references, alt text, file-path portability, and the unchanged scientific content of Figures 1–4.
6. Audit the supplementary-material package. Determine whether the uncompiled `markdown`-wrapper/repository-relative dependency is acceptable for a reproducible submission package or requires a deterministic, claim-neutral artifact correction.
7. Classify every `AUTHOR INPUT REQUIRED` item into:
   - hard pre-submission blocker;
   - optional/downstream choice;
   - can be left blank/omitted under the frozen venue rules.
8. Determine whether a later submission-preparation task can proceed before all author inputs are supplied, or whether explicit author input must be obtained first.
9. Distinguish all remaining issues into exactly three classes:
   - scientific/claim issue;
   - deterministic artifact/presentational fix;
   - genuine author/administrative input.
10. Freeze exactly one next action. No submission occurs inside this gate.

## Prohibited

Do not:

- populate or infer author names, affiliations, emails, ORCIDs, COI, CRediT, funding, acknowledgments, reviewer suggestions/exclusions, or OA/payment choices;
- change scientific claims, results, equations, metrics, classifications, figure substance, supplement substance, or cited-work set;
- remove WEAK/FAIL/Gram/PARK/mean-COI evidence;
- rerun scientific code, benchmarks, simulations, tests, or trajectories;
- change venue or article type;
- contact AIP/Chaos, create/use a submission account, fill submission-system fields, choose OA/payment terms, or submit;
- treat successful LaTeX compilation as scientific validation.

## Required decision

Return exactly one:

- `GO — SUBMISSION PREPARATION READY, AUTHOR INPUT BOUNDED`;
- `REVISE — ARTIFACT AND/OR AUTHOR INPUT PREREQUISITES REQUIRED`;
- `STOP — VENUE-ADAPTED PACKAGE SCIENTIFIC/CLAIM NONCOMPLIANT`.

If GO, freeze the exact remaining author-input list and authorise only a non-submitting final submission-preparation package task.

If REVISE, specify exactly whether the next step is:

- deterministic artifact correction in `90 – MANUSCRIPT`, or
- explicit user/author metadata collection in MASTER,

but not both unless both are independently unavoidable; choose the ordering that minimises unnecessary work.

No actual submission is authorised by any decision in this gate.
