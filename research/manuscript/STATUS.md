# STATUS — 90 – MANUSCRIPT – Manuskript & Figuren

Current Gate: `Manuscript Chaos Submission Artifact Correction 0.1`
Status: READY / AWAIT GO
Latest claim/architecture freeze: `research/master/manuscript_claim_freeze_architecture_0_1.md`
Canonical editorial manuscript: `research/manuscript/manuscript_editorial_completion_0_1.md`
Canonical corrected venue-neutral package: `research/manuscript/venue_neutral_0_2/`
Frozen Chaos adaptation: `research/manuscript/chaos_regular_article_0_1/`
Required corrected package: `research/manuscript/chaos_regular_article_0_2/`
Primary venue: `Chaos: An Interdisciplinary Journal of Nonlinear Science` (AIP Publishing)
Article type: `Regular Article / Research Article — NOT Fast Track`
Latest MASTER freeze: `RP-031 — Manuscript Chaos Adapted Compliance & Submission Readiness Freeze 0.1`
Execution prompt: `research/master/prompts/manuscript_chaos_submission_artifact_correction_0_1.md`
Next instruction: On exact user command `GO`, read governance, this STATUS, the readiness memo/freeze, venue memo, claim freeze, frozen `chaos_regular_article_0_1/`, `venue_neutral_0_2/` supplement/reproducibility manifest, and execution prompt; then execute only `Manuscript Chaos Submission Artifact Correction 0.1`.
STOP boundary: Do not modify frozen `chaos_regular_article_0_1/`; do not populate author/admin facts, change scientific claims/results/equations/figure substance/supplement substance/cited-work set, rerun science, regenerate trajectories, switch venue/article type, choose OA/payment terms, contact the journal, populate a submission system, or submit.

## MASTER readiness decision

Decision:

`REVISE — ARTIFACT AND/OR AUTHOR INPUT PREREQUISITES REQUIRED`.

No scientific or claim inconsistency was found in the Chaos adaptation.

The exact deterministic blocker is submission packaging of the supplementary material: current AIP guidance requires a separate supplementary PDF at initial submission, while the frozen `supplement_chaos_0_1.tex` was not independently compiled and depends on a repository-relative Markdown source.

## Exact authorised correction

Create only:

`research/manuscript/chaos_regular_article_0_2/`

Required:

- carry forward main scientific manuscript/sections without scientific or claim change;
- carry forward the cited-work set and alt text without substantive change;
- make the supplementary source self-contained for build purposes while preserving the exact frozen Appendix A–F substance;
- independently compile/verify the supplementary PDF artifact;
- recompile/verify the main manuscript PDF;
- record build commands/toolchain, page counts and PDF SHA-256 values in `submission_build_manifest_0_2.md`;
- if binary PDFs cannot be Git-persisted through the available connector, state that accurately and preserve the self-contained sources/build manifest in Git;
- preserve all `AUTHOR INPUT REQUIRED` placeholders.

## Frozen manuscript role

Restricted theory/diagnostic synthesis. Package P remains the sole contribution-bearing framing.

- C1: CLOSE / RETAIN-RESTRICTED;
- C2: RELATED / REINTERPRET;
- C3: CLOSE / RETAIN-RESTRICTED;
- C4: CLOSE / REINTERPRET;
- C5: SAME / DEMOTE — illustration only;
- Package P: DISTINCT-ENOUGH-FOR-RESTRICTED-CLAIM / RETAIN-RESTRICTED.

No novelty or priority promotion is authorised.

## Mandatory evidence

Must remain visible and unchanged:

- response-coordinate WEAK versus equal-dimensional raw PCA;
- nuisance `FAIL — SPECIFICATION CLASSIFICATION GAP`;
- exact symmetry-aware 2D Gram-PCA control;
- STOP / PARK response-coordinate direction;
- exact APP-B arithmetic mean/COI closure;
- C5 illustration-only status;
- APP-C established-control framing.

## Author/admin boundary

Do not collect or populate author names/order, affiliations, corresponding-author data, ORCID, COI, CRediT, acknowledgments, funding/grants, funder OA obligations, final Data Availability approval, repository DOI/archive choice, reviewer suggestions/exclusions, or OA/Author Select/payment choices.

These remain downstream of the deterministic artifact correction.

## Submission state

No submission is authorised.

## Completion target

On completion, update this STATUS to:

`COMPLETE / CHAOS SUBMISSION ARTIFACT CORRECTION COMPLETE / RETURN TO MASTER`

and end:

`STOP — RETURN TO MASTER`

STOP — AWAIT GO
