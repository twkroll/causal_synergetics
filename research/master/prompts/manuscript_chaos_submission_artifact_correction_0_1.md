# MANUSCRIPT Prompt — Manuscript Chaos Submission Artifact Correction 0.1

Assigned chat: `90 – MANUSCRIPT – Manuskript & Figuren`
Status: AUTHORISED / AWAIT GO
Dependency: `RP-031 — Manuscript Chaos Adapted Compliance & Submission Readiness Freeze 0.1`

## Purpose

Perform only the deterministic submission-artifact correction identified by MASTER for the frozen Chaos Regular-Article adaptation.

This task is presentational/reproducibility packaging only. It must not collect author metadata, change scientific content/claims, or submit.

## Required inputs

Read before execution:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/manuscript/STATUS.md`;
- `research/master/manuscript_chaos_adapted_compliance_submission_readiness_0_1.md`;
- `research/master/manuscript_venue_selection_format_specification_0_1.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/manuscript/chaos_regular_article_0_1/`;
- `research/manuscript/venue_neutral_0_2/supplement_0_1.md`;
- `research/manuscript/venue_neutral_0_2/reproducibility_manifest_0_2.md`.

## Required output

Create a new versioned package only:

`research/manuscript/chaos_regular_article_0_2/`

Do not overwrite or modify `chaos_regular_article_0_1/`.

At minimum the new package must contain:

1. carried-forward main manuscript/section sources with no scientific or claim change;
2. carried-forward `references_chaos_0_1.bib` cited-work set without additions/removals;
3. carried-forward alt text without substantive change;
4. a self-contained supplementary source whose scientific/textual content is exactly the frozen `venue_neutral_0_2/supplement_0_1.md`;
5. a compilation-verified path to the AIP-required separate supplementary PDF artifact;
6. a reverified main-manuscript PDF build;
7. `submission_build_manifest_0_2.md` recording build commands/toolchain, page counts, SHA-256 values of locally produced PDFs, source pointers and any non-scientific warnings;
8. `README.md`;
9. `CHANGELOG.md`.

## Exact artifact correction

AIP initial submission requires:

- one compiled manuscript PDF;
- a separate supplementary-material PDF when supplementary material is present.

The current frozen `supplement_chaos_0_1.tex` was not independently compiled and depends on `../venue_neutral_0_2/supplement_0_1.md` through the `markdown` package.

Correct only this portability/build gap.

Permitted approaches include:

- copy the frozen Markdown supplement byte-identically into `chaos_regular_article_0_2/` and make the wrapper reference the local copy; or
- mechanically materialize the exact frozen supplement into self-contained TeX.

Whichever approach is used, substantive supplement text, equations, tables, numbers, classifications, interpretations and Appendix A–F content must not change.

Compile/verify the supplementary artifact locally. Record the actual generated PDF filename, page count and SHA-256 in `submission_build_manifest_0_2.md`.

Recompile/verify the main manuscript from the carried-forward source and record its generated PDF filename, page count and SHA-256 as well.

If the available Git connector cannot persist binary PDFs, do not misrepresent them as committed. Keep the canonical self-contained sources and build manifest in Git and state explicitly that binary PDFs were generated/verified locally but are not Git-persisted through the text-only connector.

## Frozen scientific/claim requirements

Must remain unchanged:

- Package P sole contribution-bearing framing;
- C1 CLOSE / RETAIN-RESTRICTED;
- C2 RELATED / REINTERPRET;
- C3 CLOSE / RETAIN-RESTRICTED;
- C4 CLOSE / REINTERPRET;
- C5 SAME / DEMOTE illustration only;
- response-coordinate WEAK versus equal-dimensional raw PCA;
- nuisance `FAIL — SPECIFICATION CLASSIFICATION GAP`;
- exact symmetry-aware 2D Gram-PCA control;
- STOP / PARK response-coordinate direction;
- exact APP-B arithmetic mean/COI closure;
- APP-C established output-constrained/preview/preventive-control framing;
- all frozen numerical values and cited-work set.

No novelty/priority promotion.

## Author/admin boundary

Do not populate or infer:

- author names/order;
- affiliations;
- corresponding-author data;
- ORCID;
- COI;
- CRediT;
- acknowledgments;
- funding/grants;
- funder OA obligations;
- final Data Availability approval;
- repository DOI/archive choice;
- reviewer suggestions/exclusions;
- OA/Author Select/payment choices.

Carry the existing `AUTHOR INPUT REQUIRED` placeholders forward where needed.

## Prohibited

Do not:

- rerun scientific code/tests/simulations/benchmarks/trajectories;
- add or update literature;
- alter scientific equations, metrics, results, classifications, figures or supplement substance;
- remove mandatory negative evidence/countercontrols;
- switch venue/article type;
- contact AIP/Chaos;
- enter a submission system;
- choose OA/payment terms;
- submit.

If compilation would require substantive scientific/textual repair, stop and return:

`STOP — RETURN TO MASTER: SCIENTIFIC/TEXTUAL CHANGE REQUIRED`

## Completion

On successful completion:

1. update `research/manuscript/STATUS.md` to `COMPLETE / CHAOS SUBMISSION ARTIFACT CORRECTION COMPLETE / RETURN TO MASTER`;
2. record all creation/build commits and locally generated PDF hashes/page counts;
3. state explicitly that no scientific execution or submission occurred;
4. end with:

`STOP — RETURN TO MASTER`
