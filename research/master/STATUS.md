# STATUS — 00 – MASTER – Projektplan & Status

Current Gate: `Post-Venue-Selection / Manuscript Chaos Regular-Article Format Adaptation 0.1`
Status: COMPLETE / WAIT FOR MANUSCRIPT
Latest canonical venue memo: `research/master/manuscript_venue_selection_format_specification_0_1.md`
Latest canonical venue freeze: `research/master/manuscript_venue_selection_format_specification_result_freeze_0_1.md`
Decision: `GO — PRIMARY VENUE & FORMAT SPECIFICATION FROZEN / NO NOVELTY PROMOTION`
Primary venue: `Chaos: An Interdisciplinary Journal of Nonlinear Science` (AIP Publishing)
Article type: `Regular Article / Research Article — NOT Fast Track`
Latest rollback point: `RP-029 — Manuscript Venue Selection & Format Specification Freeze 0.1`
Authorised manuscript prompt: `research/master/prompts/manuscript_chaos_regular_article_format_adaptation_0_1.md`
Next instruction: User opens/returns to `90 – MANUSCRIPT – Manuskript & Figuren` and enters exactly `GO`.
STOP boundary: MASTER must not perform the venue adaptation itself, submit, alter frozen science/claims/results, remove mandatory negative evidence/countercontrols, choose OA/payment terms, switch venue/article type, or promote novelty before MANUSCRIPT returns.

## Freeze state

- Governance: FROZEN v0.1
- Prior-Art & Definitions Audit: FROZEN / PASS — CLAIM-RESTRICTED
- CORE: FROZEN / PASS — CLAIM-RESTRICTED
- APP-A neural minimal/history/ReLU: FROZEN / PASS
- Neural response-coordinate pilot: FROZEN / WEAK
- Neural nuisance-invariance pilot: FROZEN / FAIL — SPECIFICATION CLASSIFICATION GAP
- Neural response-coordinate direction: FROZEN / STOP — PARKED
- APP-B Power-Grid Minimal Benchmark: FROZEN / PASS
- APP-C Controlled State Preparation: FROZEN / PASS
- Claim-Level & Theorem-Level Prior-Art Revalidation: FROZEN / MANUSCRIPT-READY — CLAIM-RESTRICTED
- Manuscript Claim & Architecture: FROZEN / MANUSCRIPT READY
- Manuscript Initial Draft 0.1: FROZEN / COMPLETE
- Manuscript Initial Draft Integration & Compliance 0.1: FROZEN / GO — EDITORIAL COMPLETION ONLY
- Manuscript Editorial Completion 0.1: FROZEN / COMPLETE
- Manuscript Submission Readiness & Artifact Packaging Gate 0.1: FROZEN / GO — VENUE-NEUTRAL ARTIFACT COMPLETION ONLY
- Manuscript Venue-Neutral Artifact Completion 0.1: FROZEN / COMPLETE under `RP-026`
- Manuscript Venue-Neutral Artifact Integration & Compliance Gate 0.1: FROZEN / REVISE under `RP-027`
- Manuscript Venue-Neutral Artifact Metadata Correction 0.1: COMPLETE / ACCEPTED / FROZEN under `RP-028`
- Manuscript Venue Selection & Format Specification Gate 0.1: COMPLETE / GO / FROZEN
- Latest rollback point: `RP-029 — Manuscript Venue Selection & Format Specification Freeze 0.1`

## Frozen venue decision

Primary venue:

**Chaos: An Interdisciplinary Journal of Nonlinear Science (AIP Publishing)**

Article type:

**Regular Article / Research Article — NOT Fast Track**

Fallback only, not authorised for adaptation:

`Physical Review E — Regular Article`.

The venue was selected for scope and frozen-claim compatibility, not perceived acceptance ease. `Journal of Physics: Complexity` was audited but not selected.

## Frozen Chaos format snapshot

Current official publisher guidance accessed 2026-09-06 was frozen in `research/master/manuscript_venue_selection_format_specification_0_1.md`.

Key adaptation requirements:

- initial submission uses a compiled manuscript PDF; supplementary material is a separate PDF;
- AIP LaTeX source selected for the adaptation pass;
- abstract must be one paragraph and `<=250` words; current frozen abstract therefore requires claim-neutral shortening only;
- first Introduction paragraph must serve as the Chaos Lead Paragraph;
- Fast Track has a `5750`-word-equivalent cap and is expressly not selected;
- existing SVG figures are acceptable; scientific content remains frozen and neutral alt text must be added;
- supplement A–F remains scientifically unchanged;
- COI, CRediT, Data Availability, funding/acknowledgment and author metadata must be supplied or explicitly marked `AUTHOR INPUT REQUIRED` when absent;
- references remain the same cited-work set and mandatory placement, with style normalization only;
- no OA/payment decision is authorised; AIP Author Select remains optional downstream.

## Authorised next task

Exactly one MANUSCRIPT task is authorised:

`Manuscript Chaos Regular-Article Format Adaptation 0.1`

It must create only:

`research/manuscript/chaos_regular_article_0_1/`

The canonical editorial manuscript and both venue-neutral packages remain immutable.

Permitted changes are presentational only: AIP/Chaos LaTeX conversion, abstract shortening without strengthening, Lead Paragraph reordering/compression from existing material, administrative placeholders/declarations, author-year reference style normalization, figure placement/alt text, supplement typesetting, and a compliance checklist/change log.

## Branch state

- 00 – MASTER: COMPLETE / WAIT FOR MANUSCRIPT
- 10 – CORE: COMPLETE / FROZEN / WAIT
- 20/30/40 – THEORY-*`: UNOPENED
- 50 – APP-A: PARKED / FROZEN / WAIT
- 60 – APP-B: COMPLETE / PASS — RESULT FROZEN / WAIT
- 70 – APP-C: COMPLETE / PASS — RESULT FROZEN / WAIT
- 80 – LIT: COMPLETE / FROZEN / WAIT
- 90 – MANUSCRIPT: READY / AWAIT GO — Manuscript Chaos Regular-Article Format Adaptation 0.1

## Active blocker

Venue-specific presentational adaptation only. No scientific, claim, numerical, bibliography-content, figure-substance, supplement-substance or reproducibility blocker remains.

Submission remains unauthorised. After MANUSCRIPT returns, MASTER must run a separate venue-adapted compliance/submission-readiness gate.

## Claim ceiling

No novelty or priority promotion. Package P remains the sole contribution-bearing framing; C1–C4 remain restricted and C5 remains illustrative/SAME-level prior art. WEAK/FAIL/Gram/PARK/mean-COI evidence remains mandatory.

## CI

Repository CI remains not configured. No scientific code/test was executed in the venue-selection gate.

## Return protocol

Open/return to `90 – MANUSCRIPT – Manuskript & Figuren` and enter exactly:

`GO`

After MANUSCRIPT reaches `STOP — RETURN TO MASTER`, return here and enter:

`Status?`

STOP — WAIT
