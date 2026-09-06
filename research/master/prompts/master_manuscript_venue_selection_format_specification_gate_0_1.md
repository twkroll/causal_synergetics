# MASTER Prompt — Manuscript Venue Selection & Format Specification Gate 0.1

Assigned chat: `00 – MASTER – Projektplan & Status`
Status: AUTHORISED / AWAIT NAMED GATE
Dependency: `RP-028 — Manuscript Venue-Neutral Artifact Metadata Correction Freeze 0.1`

## Purpose

Select and freeze exactly one primary manuscript venue and its current official submission-format requirements using the frozen scientific/manuscript/package state only.

This gate is venue-selection/format-specification only. It may use current official venue/publisher sources and current submission guidance because venue requirements are time-sensitive. It must not alter scientific content, claims, results, figures, supplement substance, or literature positioning, and it must not submit.

## Required inputs

Read at minimum:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/master/STATUS.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/manuscript/manuscript_editorial_completion_0_1.md`;
- `research/manuscript/venue_neutral_0_2/README.md`;
- `research/manuscript/venue_neutral_0_2/reproducibility_manifest_0_2.md`;
- `research/master/manuscript_venue_neutral_artifact_metadata_correction_result_freeze_0_1.md`;
- final claim-level literature revalidation.

## Gate task

1. Define a short candidate set of plausible current venues compatible with a restricted theory/diagnostic synthesis spanning complex systems/synergetics, control/projectability, minimal neural illustrations, power-grid witness, and output-preserving preparation.
2. Use current official venue/publisher documentation to verify scope, article type, length/page/word limits where applicable, figure/supplement constraints, anonymisation/review model, reference style requirements, data/code availability expectations, fees/open-access constraints if materially relevant, and submission-system requirements.
3. Evaluate fit against the frozen manuscript without changing science or inflating novelty.
4. Select exactly one primary venue if defensible. A secondary fallback may be named only as contingency, but the gate must freeze one primary venue or return STOP/REVISE.
5. Produce a venue-format specification containing only transformations necessary to adapt the frozen venue-neutral manuscript/package to the selected venue.
6. Explicitly identify which adaptation steps are purely presentational and which would require MASTER return because they risk changing scientific emphasis or claim strength.

## Prohibited

Do not:

- rewrite the manuscript inside this gate;
- change claims, results, metrics, equations, figures' scientific content or supplement substance;
- remove mandatory WEAK/FAIL/Gram/PARK/mean-COI evidence to satisfy length limits;
- add new experiments, analyses, literature families, benchmarks or trajectories;
- claim novelty/priority beyond the frozen claim ceiling;
- submit, create accounts, enter submission-system metadata, contact editors, or pay fees;
- choose a venue because it appears easier to accept absent scope/claim compatibility.

## Required decision

Return exactly one:

- `GO — PRIMARY VENUE & FORMAT SPECIFICATION FROZEN`;
- `REVISE — VENUE/FIT PREREQUISITE REQUIRED`;
- `STOP — NO DEFENSIBLE VENUE FIT UNDER FROZEN MANUSCRIPT`.

If GO, freeze the selected venue, official requirements consulted with access dates, allowed venue-specific formatting transformations, prohibited scientific changes, and the exact next manuscript adaptation task.

No submission is authorised by GO.
