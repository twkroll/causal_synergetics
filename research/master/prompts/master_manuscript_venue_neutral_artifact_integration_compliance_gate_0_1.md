# Prompt — Manuscript Venue-Neutral Artifact Integration & Compliance Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-05
Dependency: `RP-026 — Manuscript Venue-Neutral Artifact Completion Freeze 0.1`

## Name

`Manuscript Venue-Neutral Artifact Integration & Compliance Gate 0.1`

## Purpose

Formally audit the frozen venue-neutral artifact package against the canonical manuscript, branch STATUS files, result files and frozen claim/figure constraints before any venue-selection step.

This is an artifact/reproducibility compliance gate only. It must not create or correct artifacts inside the gate, select a venue, submit, rerun scientific code, add literature, change claims or alter scientific content.

## Frozen basis

Read and obey:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/master/STATUS.md`;
- `research/master/manuscript_submission_readiness_artifact_packaging_0_1.md`;
- `research/master/manuscript_venue_neutral_artifact_result_freeze_0_1.md`;
- `research/manuscript/STATUS.md`;
- `research/manuscript/manuscript_editorial_completion_0_1.md`;
- `research/manuscript/venue_neutral_0_1/README.md`;
- `research/manuscript/venue_neutral_0_1/CHANGELOG.md`;
- `research/manuscript/venue_neutral_0_1/supplement_0_1.md`;
- `research/manuscript/venue_neutral_0_1/reproducibility_manifest_0_1.md`;
- all four SVG figure files;
- canonical CORE/APP-A/APP-B/APP-C STATUS/result files as needed for pointer and numerical fidelity.

## Mandatory checks

1. Confirm the canonical editorial manuscript blob remains unchanged.
2. Audit every commit/result/source/test pointer in the reproducibility manifest against canonical Git records.
3. Audit all scientific numbers in supplement/figures against frozen result files at reported precision.
4. Verify WEAK, FAIL, exact Gram-PCA, PARK and exact APP-B mean/COI control remain visible and unreclassified.
5. Verify Figure 3 remains schematic/non-trajectory and no regenerated curve/trajectory data appear.
6. Verify Figures 1, 2 and 4 use only frozen conceptual roles and approved scalar data.
7. Verify supplement A–F contains only frozen derivations/results and does not add a theorem, metric, interpretation or scientific ranking.
8. Verify package README/CHANGELOG do not imply submission approval or novelty promotion.
9. Separate artifact metadata defects from scientific/claim defects.
10. Preserve all earlier rollback points and claim ceilings.

## Known discrepancy to audit explicitly

The frozen returned manifest records CORE commit `1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`, while canonical `research/core/STATUS.md` records `0ebd50e5c8c072cf59ae86502a25b97e78c4722f` as the canonical CORE result commit.

Do not repair this inside the gate. Determine whether this and any other discovered defects require a single claim-neutral artifact correction pass.

## Required decision

Choose exactly one:

- `GO — VENUE SELECTION / FORMAT SPECIFICATION READY`
- `REVISE — ARTIFACT COMPLIANCE FIXES REQUIRED`
- `STOP — SCIENTIFIC OR CLAIM INCONSISTENCY`

If `REVISE`, enumerate only concrete artifact/pointer/presentation defects and authorise exactly one tightly scoped MANUSCRIPT correction task. No scientific change may be included.

If `GO`, freeze the package as compliant and make venue selection/format specification the only next step; do not choose the venue inside this gate.

If `STOP`, identify the scientific/claim inconsistency and return to the last stable freeze.

## Mandatory deliverable

Create:

`research/master/manuscript_venue_neutral_artifact_integration_compliance_0_1.md`

Then update MASTER/project status/Decision Log and choose exactly one next user command.

## Forbidden actions

No artifact correction, manuscript rewrite, new science, rerun, new metric, new figure data, new literature, claim promotion, venue selection, template formatting, cover letter or submission action inside this gate.
