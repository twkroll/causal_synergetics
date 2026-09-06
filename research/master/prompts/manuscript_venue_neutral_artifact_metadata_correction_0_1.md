# Prompt — Manuscript Venue-Neutral Artifact Metadata Correction 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `90 – MANUSCRIPT – Manuskript & Figuren`
Status: READY / AWAIT GO
Date: 2026-09-06
Dependency: `RP-027 — Manuscript Venue-Neutral Artifact Integration & Compliance Freeze 0.1`

## Name

`Manuscript Venue-Neutral Artifact Metadata Correction 0.1`

## Purpose

Perform exactly one claim-neutral artifact/reproducibility metadata correction after MASTER completed `Manuscript Venue-Neutral Artifact Integration & Compliance Gate 0.1` with:

`REVISE — ARTIFACT COMPLIANCE FIXES REQUIRED`.

This task is not a scientific revision, not a manuscript revision, not a venue-selection task, and not a submission task.

## Frozen basis

Read and obey:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/manuscript/STATUS.md`;
- `research/master/manuscript_venue_neutral_artifact_integration_compliance_0_1.md`;
- `research/master/manuscript_venue_neutral_artifact_result_freeze_0_1.md`;
- `research/manuscript/venue_neutral_0_1/README.md`;
- `research/manuscript/venue_neutral_0_1/CHANGELOG.md`;
- `research/manuscript/venue_neutral_0_1/reproducibility_manifest_0_1.md`;
- `research/core/STATUS.md`;
- canonical frozen result/status files only as needed to verify exact metadata copying.

## Exact defect to correct

The frozen `reproducibility_manifest_0_1.md` lists CORE SHA

`1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`

under a `Canonical result-freeze commit` label.

MASTER verified:

- canonical CORE result-creation/result commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`;
- subsequent CORE STATUS/result-freeze bookkeeping commit: `1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`.

The correction must distinguish these two roles explicitly. It must not change the CORE science, theorem status, claims, equations or bounds.

## Required deliverable

Create a new package:

`research/manuscript/venue_neutral_0_2/`

Do not alter or overwrite `research/manuscript/venue_neutral_0_1/`.

The new package must contain:

1. `figures/figure_1_diagnostic_schematic.svg`
2. `figures/figure_2_cross_domain_witness_schematic.svg`
3. `figures/figure_3_power_grid_schematic.svg`
4. `figures/figure_4_preparation_protocol.svg`
5. `supplement_0_1.md`
6. `reproducibility_manifest_0_2.md`
7. `README.md`
8. `CHANGELOG.md`

## Byte-identity rule

The four SVG files and `supplement_0_1.md` must be copied **byte-identically** from `venue_neutral_0_1`.

Record in the new `CHANGELOG.md` that their Git blob SHAs are identical to the frozen `0_1` artifacts. Do not editorially reformat those files.

## Reproducibility-manifest rule

Create `reproducibility_manifest_0_2.md` by carrying forward `reproducibility_manifest_0_1.md` and making only claim-neutral metadata corrections required by the MASTER compliance memo.

For CORE, state explicitly:

- `Canonical result-creation/result commit: 0ebd50e5c8c072cf59ae86502a25b97e78c4722f`;
- `Subsequent STATUS/result-freeze bookkeeping commit: 1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`.

All non-CORE commit pointers, source/test/result paths, frozen local-test statements, numbers, scientific classifications, CI statements and claim limitations must remain unchanged unless direct copying reveals a purely typographic/path error. If any discrepancy would require scientific interpretation or choosing between scientifically different records, stop immediately and return to MASTER.

## README rule

The new `README.md` must:

- identify `venue_neutral_0_2` as the corrected venue-neutral artifact package;
- state that `venue_neutral_0_1` remains frozen under `RP-026` and is not overwritten;
- state that `0_2` changes reproducibility metadata only;
- preserve the no-venue/no-submission/no-new-science boundaries.

## CHANGELOG rule

The new `CHANGELOG.md` must list only:

- the CORE commit-role clarification;
- byte-identical carry-forward of Figures 1–4 and the supplement;
- unchanged editorial manuscript and scientific content;
- no new science, rerun, metric, literature, claim, venue choice or submission.

## Forbidden work

Do not:

- modify `venue_neutral_0_1`;
- modify the canonical editorial manuscript;
- alter any figure or supplement scientific/textual content;
- rerun code, tests, simulations or analyses;
- regenerate trajectories;
- add metrics, results, baselines or literature;
- repair or relabel WEAK/FAIL outcomes;
- weaken Gram/PARK/mean-COI limitations;
- change Package P or C1–C5 roles;
- select a venue;
- apply templates, page limits, anonymisation rules or publisher formatting;
- submit anything;
- promote novelty, priority, robustness, optimality or genericity.

## Completion verification

Before returning:

1. verify the four figure blob SHAs and supplement blob SHA in `0_2` are identical to `0_1`;
2. verify the canonical editorial manuscript blob remains `5116cb99a011416943bef908079ba7489eb597a3`;
3. verify the corrected manifest contains both CORE commits with their exact distinct roles;
4. verify all other manifest scientific pointers and frozen values remain unchanged;
5. record the package creation/content commit(s) in `research/manuscript/STATUS.md`.

Update `research/manuscript/STATUS.md` to:

`COMPLETE / VENUE-NEUTRAL ARTIFACT METADATA CORRECTED / RETURN TO MASTER`

Then stop.

## Scientific STOP boundary

If any change beyond deterministic artifact/reproducibility metadata correction is required, return:

`STOP — RETURN TO MASTER: SCIENTIFIC CHANGE REQUIRED`

## Claim ceiling

No novelty or priority promotion. Package P remains the sole contribution-bearing framing; C1–C4 remain restricted; C5 remains SAME-level illustration only.

## Final state

`STOP — RETURN TO MASTER`
