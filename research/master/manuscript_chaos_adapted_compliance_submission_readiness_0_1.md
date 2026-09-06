# Manuscript Chaos Adapted Compliance & Submission Readiness Gate 0.1

Status: COMPLETE / FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-06
Dependency: `RP-030 — Manuscript Chaos Regular-Article Format Adaptation Freeze 0.1`
Decision: **REVISE — ARTIFACT AND/OR AUTHOR INPUT PREREQUISITES REQUIRED**

No novelty or priority promotion is authorised.

## 1. Executive decision

The frozen Chaos Regular-Article adaptation is scientifically, numerically, claim-wise, reference-wise, figure-wise, and main-manuscript-format compliant with the frozen programme state. No scientific or claim inconsistency was identified.

The package is not yet ready for final non-submitting submission preparation because one deterministic artifact prerequisite remains: AIP Publishing's current official author instructions require supplementary material to be uploaded at initial submission as a separate PDF (`SI.pdf`). The frozen Chaos package currently contains only an uncompiled supplementary LaTeX wrapper that depends on the repository-relative frozen Markdown supplement through the `markdown` package. That wrapper is a valid provenance bridge but is not itself the required submission artifact and has not been independently compilation-verified.

Therefore the exact gate decision is:

**REVISE — ARTIFACT AND/OR AUTHOR INPUT PREREQUISITES REQUIRED**.

The next step is **deterministic artifact correction in `90 – MANUSCRIPT – Manuskript & Figuren` only**. Author/admin metadata collection is intentionally deferred until that deterministic correction returns, because the correction is independent of author identity and can be completed without asking the user to supply personal or administrative facts.

No submission is authorised.

## 2. Current official AIP/Chaos rules reverified

Official AIP Publishing author guidance was rechecked on 2026-09-06.

Sources:

- AIP Publishing Author Instructions: `https://publishing.aip.org/resources/researchers/author-instructions/`
- AIP Publishing Research Data Policy: `https://publishing.aip.org/resources/researchers/open-science/research-data-policy/`
- AIP Publishing Conflict of Interest policy: `https://publishing.aip.org/resources/researchers/policies-and-ethics/conflict-of-interests/`
- AIP Publishing Open Access options: `https://publishing.aip.org/resources/researchers/open-science/open-access/`

Relevant current requirements:

1. Initial submission requires a single compiled manuscript PDF.
2. If supplementary material is present, initial submission requires a separate supplementary-material PDF.
3. General abstract guidance is one paragraph and no more than 250 words; the frozen Chaos abstract satisfies this.
4. Chaos requires the first paragraph to function as a non-specialist Lead Paragraph; the adapted first paragraph satisfies the frozen transformation.
5. Conflict-of-interest disclosure is required for every article, including a statement when no conflicts exist.
6. A CRediT author-contribution statement is required for all submissions.
7. A Data Availability statement is required for all manuscripts.
8. AIP Author Select is optional for subscription journals unless an external funder/institutional obligation changes the author's choice; no OA/payment decision is made here.
9. Reviewer suggestions/exclusions are submission-system dependent and are not assumed mandatory in advance.

## 3. Compliance matrix

| Dimension | Audit finding | Classification |
|---|---|---|
| Primary venue/article type | Chaos / Regular Article retained; no Fast Track switch | PASS |
| Canonical source immutability | Editorial manuscript and `venue_neutral_0_2` remain unchanged | PASS |
| Title | Frozen safe title retained; no novelty/priority language | PASS |
| Abstract | One paragraph; independently below 250 words; no references/display equations; four frozen abstract roles preserved | PASS |
| Lead Paragraph | First Introduction paragraph contains big-picture question, established criterion boundary, restricted package contribution, and mandatory limitations without escalation | PASS |
| Claim hierarchy | Package P only contribution-bearing; C1–C4 restricted; C5 SAME-level illustration | PASS |
| CORE framing | Proposition explicitly labelled standard/subsumed; finite-horizon bounds explicitly standard fast-slow/ISS-style ingredients | PASS |
| Neural evidence | WEAK, specification-classification FAIL, exact Gram-PCA control, PARK all visible and unreclassified | PASS |
| Power-grid evidence | Representative mismatch and exact mean/COI closure shown together | PASS |
| APP-C framing | Known-disturbance bounded open-loop benchmark inside established output-constrained/preview/preventive-control literature | PASS |
| Numerical fidelity | Checked values in neural, APP-B and APP-C sections agree with frozen canonical results | PASS |
| Reference roles | Mandatory Haken, projectability/abstraction, neural SAME-level, coherency, output-nulling/preview/preventive-control groups remain positioned correctly | PASS |
| Cited-work set | `references_chaos_0_1.bib` preserves the cited-work set of the frozen editorial manuscript; normalization is presentational | PASS |
| Figure substance | Figures 1–4 remain the byte-frozen venue-neutral SVGs; no trajectory regeneration | PASS |
| Alt text | Neutral accessibility descriptions preserve scientific scope and limitations | PASS |
| Main source compilation | Presentation-only main REVTeX compilation previously succeeded; not treated as scientific validation | PASS |
| Supplement substance | Frozen Appendices A–F remain the controlling source | PASS |
| Supplement submission artifact | Current wrapper is uncompiled and repository-relative; AIP initial submission requires separate SM PDF | **REVISE — DETERMINISTIC ARTIFACT FIX** |
| Author/admin metadata | Correctly left unknown rather than invented | BOUNDED AUTHOR INPUT — AFTER ARTIFACT FIX |

No scientific/claim STOP condition is present.

## 4. Deterministic artifact prerequisite

The current file

`research/manuscript/chaos_regular_article_0_1/supplement_chaos_0_1.tex`

contains

`\markdownInput{../venue_neutral_0_2/supplement_0_1.md}`

and was not independently compiled during the venue adaptation.

AIP's current official rule is explicit: supplementary material must be uploaded at initial submission as a separate PDF (`SI.pdf`). A repository-relative wrapper is therefore insufficient as the final submission artifact unless a deterministic build verifies that the exact frozen supplement can be rendered into the required separate PDF.

This is a presentational/reproducibility issue only. No supplement text, scientific result, table, equation, metric, classification, claim, or interpretation may change.

## 5. Exact next task

Authorise exactly one MANUSCRIPT task:

`Manuscript Chaos Submission Artifact Correction 0.1`

Assigned branch:

`90 – MANUSCRIPT – Manuskript & Figuren`.

It must create a new versioned package:

`research/manuscript/chaos_regular_article_0_2/`

The frozen `chaos_regular_article_0_1/` package remains immutable under `RP-030`.

Required correction scope:

1. Carry the main scientific manuscript, section files, BibTeX cited-work set, alt text, and all frozen figure content forward without scientific or claim change.
2. Materialize a self-contained supplementary source from the exact frozen `venue_neutral_0_2/supplement_0_1.md` content. The frozen supplement substance must be preserved exactly; only deterministic markup/typesetting transformations are permitted.
3. Remove the repository-relative dependency as a submission-build requirement. A local copy of the frozen supplement source may be carried byte-identically into the new package, or an equivalent self-contained TeX materialization may be produced, provided substantive text and tables do not change.
4. Independently compile/verify the supplementary material into the AIP-required separate PDF artifact in the execution environment. Record the exact build command/toolchain, page count, and SHA-256 of the produced PDF in a Git-tracked build manifest. Do not treat compilation as scientific validation.
5. Recompile/verify the main manuscript PDF from the carried-forward source and record its build command/toolchain, page count, and SHA-256 in the same build manifest. No scientific repair may be triggered by compilation warnings.
6. If binary PDFs cannot be committed through the available Git interface, do not fabricate Git persistence. Record reproducible build metadata and preserve the self-contained source in Git; the later final submission-preparation task may regenerate the binary PDFs from the frozen source.
7. Create `README.md`, `CHANGELOG.md`, and `submission_build_manifest_0_2.md` documenting only this deterministic artifact correction.
8. Preserve all `AUTHOR INPUT REQUIRED` placeholders; do not collect or populate author/admin facts in this task.

STOP and return to MASTER if faithful self-contained supplement rendering would require scientific/textual editing rather than deterministic typesetting.

## 6. Author/admin input classification

These inputs remain genuine author facts and must not be inferred.

### Hard pre-submission author/admin blockers

The following must be supplied or explicitly confirmed before actual submission:

- author names and order;
- affiliations;
- corresponding author name and email;
- Conflict of Interest statement, including an explicit no-conflict statement if applicable;
- CRediT Author Contributions agreed by all listed authors;
- funding source/grant information or explicit confirmation that no reportable funding applies;
- funder/institutional open-access obligations, because they may constrain the publication route;
- final Data Availability statement choice and author approval.

### Optional / conditional / downstream inputs

- ORCID identifiers: encouraged/useful but not established by the audited AIP guidance as a universal hard pre-submission requirement;
- acknowledgments: may be omitted if there is nothing to acknowledge, but the author must confirm whether any are needed;
- repository DOI/archive: optional for the current public-repository route; a DOI may improve archival citation but is not required by the audited general AIP rule;
- reviewer suggestions/exclusions: only if requested by the submission system; any suggestions must respect conflict-of-interest rules;
- OA / Author Select choice: optional for the selected subscription-journal route unless funder/institutional obligations require OA; no payment choice is authorised now.

### Can be omitted under the frozen scientific record

- human/animal ethics approval statement: the frozen manuscript contains no human or animal experiments, so no ethics statement is required on the current record unless the author identifies contrary facts.

## 7. Why author input is not collected first

Both the separate supplementary PDF and hard author metadata are ultimately required for submission. The artifact correction is independent of author identity and can be completed deterministically now. Collecting personal/admin facts first would not resolve the known technical artifact defect and would create unnecessary coupling between author data and a still-incomplete package.

Therefore the ordering is frozen as:

`DETERMINISTIC ARTIFACT CORRECTION → MASTER INTEGRATION → BOUNDED AUTHOR INPUT COLLECTION → FINAL NON-SUBMITTING SUBMISSION PACKAGE → EXPLICIT SUBMISSION AUTHORISATION (if later granted)`.

## 8. Submission state

No submission, journal contact, submission-system entry, reviewer selection, OA/payment choice, license action, or editor communication is authorised by this gate.

## 9. Rollback recommendation

Create and register:

`RP-031 — Manuscript Chaos Adapted Compliance & Submission Readiness Freeze 0.1`.

This rollback freezes:

- PASS of scientific/claim/reference/figure/main-format compliance;
- the single deterministic supplement/PDF artifact prerequisite;
- the bounded hard/optional author-input classification;
- the ordering: artifact correction before author-input collection;
- continued prohibition on submission and novelty promotion.

All earlier freezes remain stable.

## 10. Exact next action

In `90 – MANUSCRIPT – Manuskript & Figuren`, the user enters exactly:

`GO`

MANUSCRIPT executes only `Manuscript Chaos Submission Artifact Correction 0.1` and then returns to MASTER.

No author metadata collection or submission is authorised inside that task.
