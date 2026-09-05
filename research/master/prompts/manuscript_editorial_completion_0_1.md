# Prompt — Manuscript Editorial Completion 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `90 – MANUSCRIPT – Manuskript & Figuren`
Status: READY / AWAIT GO
Date: 2026-09-05
Dependency: `RP-023 — Manuscript Initial Draft Compliance Freeze 0.1`

## Name

`Manuscript Editorial Completion 0.1`

## Purpose

Perform exactly one claim-preserving editorial completion pass on the frozen `Manuscript Initial Draft 0.1` after MASTER found no scientific/claim blocker.

This is not a scientific revision. Do not add theory, evidence, experiments, claims, literature families, applications, controllers, metrics, baselines or interpretations.

## Frozen basis

Read and obey:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/manuscript/STATUS.md`;
- `research/master/manuscript_claim_freeze_architecture_0_1.md`;
- `research/master/manuscript_initial_draft_integration_compliance_0_1.md`;
- `research/literature/claim_level_theorem_level_prior_art_revalidation_0_1.md`;
- `research/manuscript/manuscript_initial_draft_0_1.md`;
- canonical frozen result files only as needed for consistency checks.

## Allowed work

Only:

1. complete and normalize bibliographic metadata for works already cited in the frozen manuscript;
2. perform narrowly targeted bibliographic metadata verification for those already cited works only;
3. fix the explicitly identified records:
   - Ntogramatzidis et al. (2017) geometric-control/output-nulling citation;
   - Tabuada & Pappas, `Quotients of Fully Nonlinear Control Systems`, including missing year;
   - `Preventive Control for Dynamic Security of Power Systems` (1995), including author metadata if available;
4. normalize citation/reference formatting consistently;
5. fix typographic, grammar, notation, cross-reference and formatting errors that do not alter scientific meaning;
6. preserve all frozen main-text negative evidence, countercontrols, numerical values and claim limitations;
7. keep figure/table specifications inside the frozen inventory; no new scientific rendering/data generation.

## Forbidden work

Do not:

- conduct broad or exploratory literature search;
- add new references because they appear scientifically useful;
- replace the frozen claim-positioning literature with a stronger/newer family;
- change Package P or C1–C5 roles;
- rewrite text to strengthen novelty, priority, genericity, robustness or optimality;
- remove or weaken WEAK/FAIL/Gram/PARK/mean-COI evidence;
- rerun any scientific code or simulation;
- generate new metrics or empirical figures;
- change APP-C from benchmark instantiation to method claim;
- change C5 from illustration to contribution;
- add submission venue claims, cover letter, response-to-reviewers, or submission action.

## Required deliverable

Create a new canonical editorial version:

`research/manuscript/manuscript_editorial_completion_0_1.md`

Do not overwrite the frozen initial draft.

Also create a short change log inside or alongside the editorial version listing only editorial/bibliographic changes from the initial draft.

Update `research/manuscript/STATUS.md` to:

`COMPLETE / EDITORIAL VERSION FROZEN / RETURN TO MASTER`

and return to MASTER.

## Scientific STOP boundary

If completing a citation requires selecting between scientifically different predecessor claims, if any factual inconsistency is discovered, or if any wording change would strengthen or alter a scientific claim, stop immediately with:

`STOP — RETURN TO MASTER: SCIENTIFIC CHANGE REQUIRED`

## Claim ceiling

No novelty or priority promotion. Package P remains the sole contribution-bearing framing; C1–C4 remain restricted; C5 remains SAME-level illustration only.

## Final state

After completing only the authorised editorial work:

`STOP — RETURN TO MASTER`
