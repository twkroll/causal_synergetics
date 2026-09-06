# MANUSCRIPT Prompt — Manuscript Chaos Regular-Article Format Adaptation 0.1

Assigned chat: `90 – MANUSCRIPT – Manuskript & Figuren`
Status: AUTHORISED / AWAIT GO
Dependency: `RP-029 — Manuscript Venue Selection & Format Specification Freeze 0.1`
Primary venue: `Chaos: An Interdisciplinary Journal of Nonlinear Science` (AIP Publishing)
Article type: `Regular Article / Research Article — NOT Fast Track`

## Purpose

Create a new venue-specific Chaos Regular-Article package from the frozen canonical editorial manuscript and accepted venue-neutral package using only claim-neutral presentational transformations authorised by MASTER.

Do not submit.

## Required inputs

Read before execution:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/manuscript/STATUS.md`;
- `research/master/manuscript_venue_selection_format_specification_0_1.md`;
- `research/master/manuscript_venue_selection_format_specification_result_freeze_0_1.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/manuscript/manuscript_editorial_completion_0_1.md`;
- `research/manuscript/venue_neutral_0_2/README.md`;
- `research/manuscript/venue_neutral_0_2/reproducibility_manifest_0_2.md`;
- `research/manuscript/venue_neutral_0_2/supplement_0_1.md`;
- all four frozen SVG figures in `research/manuscript/venue_neutral_0_2/figures/`.

## Required output directory

Create a new directory only:

`research/manuscript/chaos_regular_article_0_1/`

Do not overwrite or modify:

- `research/manuscript/manuscript_editorial_completion_0_1.md`;
- `research/manuscript/venue_neutral_0_1/`;
- `research/manuscript/venue_neutral_0_2/`.

## Required outputs

At minimum create:

1. `manuscript_chaos_0_1.tex` — AIP/Chaos-oriented LaTeX source;
2. `supplement_chaos_0_1.tex` — typeset source carrying the frozen supplement substance only;
3. `alt_text_0_1.md` — neutral alt text for Figures 1–4;
4. `submission_metadata_checklist_0_1.md` — venue metadata/declaration checklist with explicit `AUTHOR INPUT REQUIRED` placeholders where necessary;
5. `CHANGELOG.md` — exact claim-neutral changes from the frozen editorial/venue-neutral sources;
6. `README.md` — package index and non-submission disclaimer.

Do not create or upload a submission to AIP. A compiled PDF may be produced only if the available execution environment can do so without changing scientific content; if compilation would require unsupported packages or substantive repair, record that fact rather than changing content.

## Exact authorised transformations

### Abstract

Shorten the frozen one-paragraph abstract from approximately 274 words to no more than 250 words.

Must preserve, in order:

1. passive/current macro sufficiency versus declared intervention sufficiency;
2. standard controlled-projectability/closure bridge, explicitly not new;
3. frozen neural and power-grid witnesses/countercontrols plus output-preserving preparation benchmark;
4. explicit no-new-quotient / no-universal-law / no-generic-control limitation.

Do not strengthen any scientific claim while shortening.

### Chaos Lead Paragraph

Make the first Introduction paragraph a Chaos Lead Paragraph that gives the big picture/main points for non-specialist readers.

You may reorder/compress already frozen introductory sentences and move displaced background into later Introduction/Related Work text.

You must not:

- add a new contribution;
- use novelty/priority language;
- hide the negative evidence;
- imply projectability or APP-C is new.

### Venue source

Convert the frozen manuscript to AIP-compatible LaTeX structure while preserving the frozen section architecture and scientific wording ceiling.

Use Regular Article structure, not Fast Track compression.

### Figures

Carry forward the four frozen SVG figures without scientific-content changes.

You may reference/embed the existing files from `venue_neutral_0_2/` or copy them byte-identically into the Chaos package. If copied, record matching Git blob SHAs in the CHANGELOG.

Do not regenerate trajectories or change quantitative content.

### Alt text

Create concise neutral alt text for every figure consistent with current AIP accessibility guidance.

Alt text must describe what the schematic communicates; it must not introduce new conclusions, causal claims, novelty, or quantitative values not already displayed/frozen.

### Supplement

Convert the frozen `supplement_0_1.md` substance into `supplement_chaos_0_1.tex` without scientific or interpretive change.

Preserve all Appendices A–F, including:

- neural WEAK result;
- specification-classification FAIL;
- exact Gram-PCA control;
- PARK decision;
- exact APP-B mean/COI closure control;
- APP-C limitations;
- governance limitation that auditability is not scientific validation/novelty proof.

Add only venue-required supplementary-material wrapper/metadata.

### References

Retain the existing cited-work set and mandatory citation placement.

Normalize the existing author-year logic to one consistent AIP-accepted alphabetical author-year form.

Do not add, remove, substitute, or update scientific references. Do not perform new literature search.

### Required declarations / metadata

Add venue-specific sections/placeholders as applicable:

- Conflict of Interest;
- CRediT Author Contributions;
- Data Availability Statement;
- acknowledgments/funding;
- authors, affiliations, corresponding author, ORCID where available.

If facts are not present in Git, write exactly `AUTHOR INPUT REQUIRED` rather than inventing them.

The Data Availability wording may point to the public GitHub repository and frozen reproducibility manifest, but must not claim CI success, external replication, or general reproducibility beyond the frozen record.

### Submission note

The package README/checklist must state that:

- Chaos is the selected primary venue;
- article type is Regular Article / Research Article;
- Fast Track is not authorised;
- venue-specific formatting does not alter claim strength;
- no submission has occurred;
- final submission requires a later MASTER compliance/readiness gate.

## Mandatory preservation

The main manuscript body must continue to show:

- Response Coordinate Pilot = WEAK versus equal-dimensional raw PCA;
- nuisance-invariance = `FAIL — SPECIFICATION CLASSIFICATION GAP`;
- exact symmetry-aware 2D Gram-PCA successful control;
- `STOP / PARK RESPONSE-COORDINATE DIRECTION`;
- exact arithmetic mean/COI closure in APP-B;
- C5 as SAME-level illustration only;
- APP-C as established output-constrained/preview/preventive-control benchmark, not a new method.

Package P remains the sole contribution-bearing framing.

## STOP boundary

STOP and return to MASTER immediately if adaptation appears to require any of:

- removing mandatory negative evidence/countercontrols;
- scientific rewriting rather than presentational compression/reordering;
- a new result, metric, equation, figure, trajectory, benchmark or literature item;
- claim strengthening or novelty/priority language;
- reclassification/repair of WEAK or FAIL;
- changing Figure 3 to a generated trajectory plot;
- selecting a different venue/article type;
- OA/payment decision based on missing author/funder facts;
- actual AIP submission, editor contact, reviewer selection, or account action.

## Completion protocol

After creating the venue-specific package:

1. verify the canonical editorial manuscript and `venue_neutral_0_2/` are unchanged;
2. update `research/manuscript/STATUS.md` with exact created files and commit hashes;
3. set `Next instruction: RETURN TO MASTER`;
4. report that no submission occurred;
5. end exactly:

`STOP — RETURN TO MASTER`
