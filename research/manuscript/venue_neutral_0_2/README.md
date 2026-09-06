# Venue-Neutral Manuscript Artifact Package 0.2

Status: corrected venue-neutral production package derived only from frozen manuscript and scientific results.

`research/manuscript/venue_neutral_0_1/` remains frozen under `RP-026 — Manuscript Venue-Neutral Artifact Completion Freeze 0.1` and is not overwritten. This `0_2` package changes reproducibility metadata only: it distinguishes the canonical CORE result-creation/result commit from the subsequent CORE STATUS/result-freeze bookkeeping commit. Scientific content is unchanged.

This directory does **not** select a venue, adapt the manuscript to a publisher template or page limit, authorize submission, or change scientific content.

## Canonical manuscript source

The canonical editorial manuscript remains unchanged outside this directory:

`research/manuscript/manuscript_editorial_completion_0_1.md`

No package-facing manuscript copy is created because the canonical source can be referenced directly without wording changes.

## Package contents

### Figures

1. `figures/figure_1_diagnostic_schematic.svg` — byte-identical carry-forward of the frozen diagnostic schematic from `venue_neutral_0_1`.
2. `figures/figure_2_cross_domain_witness_schematic.svg` — byte-identical carry-forward preserving neural WEAK/FAIL/Gram/PARK limitations and the exact power-grid mean/COI countercontrol.
3. `figures/figure_3_power_grid_schematic.svg` — byte-identical schematic/non-trajectory carry-forward; no trajectories were regenerated.
4. `figures/figure_4_preparation_protocol.svg` — byte-identical carry-forward of the frozen preparation-protocol schematic.

### Supplement

`supplement_0_1.md` is copied byte-identically from `venue_neutral_0_1` and preserves complete Appendices A–F without scientific or textual changes.

### Reproducibility manifest

`reproducibility_manifest_0_2.md` carries forward the frozen manifest and corrects the CORE commit-role metadata verified by MASTER:

- canonical CORE result-creation/result commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`;
- subsequent CORE STATUS/result-freeze bookkeeping commit: `1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`.

All non-CORE scientific pointers, frozen local-test statements, scientific classifications, numerical values, CI limitations, and claim boundaries are unchanged.

### Change log

`CHANGELOG.md` records only the metadata correction and byte-identical carry-forward.

## Mandatory evidence preserved

This package preserves without reclassification or weakening:

- response-coordinate **WEAK** versus equal-dimensional raw PCA;
- nuisance-invariance **FAIL — SPECIFICATION CLASSIFICATION GAP**;
- exact symmetry-aware 2D Gram-PCA control;
- **STOP / PARK RESPONSE-COORDINATE DIRECTION**;
- exact APP-B arithmetic mean/COI closure control;
- frozen APP-B/APP-C numerical values and limitations.

## Current claim ceiling

The manuscript remains a restricted theory/diagnostic synthesis.

- C1: `CLOSE / RETAIN-RESTRICTED`;
- C2: `RELATED / REINTERPRET`;
- C3: `CLOSE / RETAIN-RESTRICTED`;
- C4: `CLOSE / REINTERPRET`;
- C5: `SAME / DEMOTE` — illustration only;
- Package P: `DISTINCT-ENOUGH-FOR-RESTRICTED-CLAIM / RETAIN-RESTRICTED`.

Package P remains the sole contribution-bearing framing. No novelty or priority promotion is authorized.

## Downstream dependency

This package is venue-neutral and is **not submission approval**. Venue selection, page/word limits, publisher template choice, figure-placement constraints, bibliography style, anonymization, author/affiliation metadata, declarations, cover letter, submission-system fields, and actual submission require a later explicit MASTER decision.

No scientific simulation, benchmark, test, analysis, trajectory generation, literature task, venue choice, or submission action occurred during this metadata correction.
