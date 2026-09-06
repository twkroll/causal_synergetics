# STATUS — 90 – MANUSCRIPT – Manuskript & Figuren

Current Gate: `Manuscript Venue-Neutral Artifact Metadata Correction 0.1`
Status: READY / AWAIT GO
Latest claim/architecture freeze: `research/master/manuscript_claim_freeze_architecture_0_1.md`
Canonical editorial manuscript: `research/manuscript/manuscript_editorial_completion_0_1.md`
Frozen prior package: `research/manuscript/venue_neutral_0_1/`
Latest compliance memo: `research/master/manuscript_venue_neutral_artifact_integration_compliance_0_1.md`
Execution prompt: `research/master/prompts/manuscript_venue_neutral_artifact_metadata_correction_0_1.md`
Dependency: `RP-027 — Manuscript Venue-Neutral Artifact Integration & Compliance Freeze 0.1`
MASTER decision: `REVISE — ARTIFACT COMPLIANCE FIXES REQUIRED`
Next instruction: On exact user command `GO`, execute only `Manuscript Venue-Neutral Artifact Metadata Correction 0.1`.
STOP boundary: Do not alter `venue_neutral_0_1`, scientific content, figures, supplement text, frozen values/claims, bibliography positioning, WEAK/FAIL classifications, Gram/PARK/mean-COI limitations; do not rerun science, select a venue, apply templates/page limits, or submit.

## Frozen manuscript role

Restricted theory/diagnostic synthesis. Package P remains the sole contribution-bearing framing.

- C1: CLOSE / RETAIN-RESTRICTED;
- C2: RELATED / REINTERPRET;
- C3: CLOSE / RETAIN-RESTRICTED;
- C4: CLOSE / REINTERPRET;
- C5: SAME / DEMOTE — illustration only;
- Package P: DISTINCT-ENOUGH-FOR-RESTRICTED-CLAIM / RETAIN-RESTRICTED.

No novelty or priority promotion is authorised.

## MASTER compliance result

The frozen `venue_neutral_0_1` package passed scientific, numerical, figure, supplement and claim compliance.

The only required correction is claim-neutral CORE reproducibility commit-role metadata.

MASTER verified:

- canonical CORE result-creation/result commit: `0ebd50e5c8c072cf59ae86502a25b97e78c4722f`;
- subsequent CORE STATUS/result-freeze bookkeeping commit: `1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`.

The `0_1` manifest must not be edited because it is frozen under `RP-026`.

## Required output

Create a new package:

`research/manuscript/venue_neutral_0_2/`

with:

- byte-identical copies of Figures 1–4 from `venue_neutral_0_1`;
- byte-identical copy of `supplement_0_1.md`;
- corrected `reproducibility_manifest_0_2.md` distinguishing the two CORE commit roles;
- new `README.md`;
- new `CHANGELOG.md`.

All non-CORE scientific pointers, values and classifications must remain unchanged.

## Completion verification

Before return:

- verify identical figure/supplement blob SHAs between `0_1` and `0_2`;
- verify editorial manuscript blob remains `5116cb99a011416943bef908079ba7489eb597a3`;
- verify the corrected manifest contains both CORE SHAs with distinct roles;
- verify no scientific rerun or venue/submission action occurred.

Then update this STATUS to:

`COMPLETE / VENUE-NEUTRAL ARTIFACT METADATA CORRECTED / RETURN TO MASTER`

and return to MASTER.

STOP — AWAIT GO
