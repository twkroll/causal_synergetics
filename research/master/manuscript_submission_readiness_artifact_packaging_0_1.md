# Manuscript Submission Readiness & Artifact Packaging Gate 0.1

Status: COMPLETE / FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Dependency: `RP-024 — Manuscript Editorial Completion Freeze 0.1`
Decision: **GO — VENUE-NEUTRAL ARTIFACT COMPLETION ONLY / NO NOVELTY PROMOTION**

## 1. Executive decision

The frozen editorial manuscript is scientifically, claim-wise, and bibliographically ready to proceed to exactly one venue-neutral artifact-completion pass.

Venue selection is **not yet a necessary prerequisite** for the remaining work that can be performed safely without changing science: conceptual figure rendering from the frozen figure inventory, completion of the supplement from already frozen canonical derivations/results, assembly of tables from already frozen values, and creation of a reproducibility/artifact manifest that points to existing source, tests, result files and commits.

The manuscript is **not submission-authorised** by this gate. Venue choice, page-limit adaptation, publisher template conversion, cover letter, metadata forms, declarations, and actual submission remain downstream and require a later MASTER decision.

No scientific result, claim, literature family, metric, comparator, negative result, countercontrol, or numerical value is changed by this gate.

## 2. Artifact-readiness matrix

| Dimension | Current state | Readiness | Gate conclusion |
|---|---|---|---|
| Scientific/claim content | Editorial manuscript passed MASTER compliance under `RP-023`; claim hierarchy unchanged under `RP-024`. | READY | no scientific revision |
| Bibliography | Identified Ntogramatzidis/Padula, Tabuada/Pappas, and Li/Bose metadata TODOs closed; ordinary author-year normalization completed. | READY | no further literature work required for venue-neutral package |
| Main manuscript source | Canonical content exists as frozen Markdown editorial version. | READY AS CONTENT / NOT YET PACKAGED | preserve as source-of-truth; create venue-neutral package without scientific rewriting |
| Figures | Figure 1, 2, 4 are conceptual specifications; Figure 3 allows stored frozen trajectories if available, otherwise schematic/table-only. No stored trajectory artifacts are present in repository inventory. | READY FOR SCHEMATIC RENDERING ONLY | render only claim-neutral conceptual/vector figures; no reruns |
| Tables | Claim matrix, evidence/countercontrol table, and frozen grid/preparation metric table are already specified from canonical frozen values. | READY | render/copy directly; no recomputation |
| Supplement | Appendices A–F currently exist as a detailed outline, not a complete standalone supplement. | INCOMPLETE BUT VENUE-NEUTRAL | complete only by compiling canonical frozen proofs, constructions, audits and tables |
| Reproducibility pointers | Benchmark source modules, tests, result files and historical commits are present in Git. Repository CI is not configured. | READY FOR MANIFEST | create pointers only; do not rerun and do not claim CI success |
| Venue formatting | No venue/template/page limit selected. | DEFER | not needed before venue-neutral artifact completion |
| Submission administration | Authors, affiliations, declarations, cover letter, venue forms not frozen. | DOWNSTREAM | no submission action in this or next artifact pass |

## 3. Figure inventory

### Figure 1 — Diagnostic schematic

Frozen role: conceptual only.

Allowed venue-neutral rendering:

`full-state fibre -> pre-declared synergetic macro/slaving map -> frozen intervention family and retained response -> standard controlled-projectability test -> sufficient macro or hidden-mode leakage`.

No quantitative data and no new derivation are required.

### Figure 2 — Cross-domain witness schematic

Frozen role: conceptual two-panel comparison.

Allowed rendering:

- neural side: same current function, same frozen learning intervention, different one-step response; show WEAK/FAIL/Gram/PARK limitation beside it;
- power-grid side: passively exact representative macro, localized hidden-machine step, representative mismatch; exact mean/COI closure shown as successful control.

This must remain a feasibility-witness schematic and must not visually imply universality or equal evidential strength of all branches.

### Figure 3 — Power-grid frozen result

Frozen rule: use already stored frozen trajectory artifacts **only if they exist**; otherwise use schematic plus frozen scalar/Table-3 information and do not regenerate trajectories.

Repository inventory through `RP-024` contains no stored trajectory/plot artifact in the manuscript tree or frozen scientific artifact set. Therefore the venue-neutral artifact pass is authorised to create **only the schematic/non-trajectory version** of Figure 3 from the equations, coordinate definitions and already frozen scalar values. It may not rerun APP-B to obtain curves.

### Figure 4 — Preparation protocol

Frozen role: conceptual protocol.

Allowed rendering:

preparation phase holding `q=(delta1,omega1)` fixed -> move hidden `(e_delta,e_omega)` along the frozen analytic quintic path -> preparation off -> known localized step `a` -> compare P0/PT/PM against B1.

Only the already frozen analytic formula and frozen scalar outcomes may appear. No regenerated trajectory is allowed.

## 4. Table readiness

The manuscript tables are venue-neutral and can be materialised directly from the frozen editorial manuscript:

1. Claim/prior-art/manuscript-role matrix.
2. Frozen evidence and countercontrols table, including WEAK, FAIL, Gram control, PARK and mean/COI closure.
3. Frozen power-grid and preparation metric table.

No table may add a derived ranking, new summary metric, omitted weak result, or new aggregation of results not already present in canonical text.

## 5. Supplement readiness

The current Appendices A–F are an outline rather than a complete submission supplement.

Exactly the following venue-neutral completion is admissible:

- Appendix A: reproduce the frozen CORE assumptions, standard projectability proof, scalar witness, exact bounds and general comparison-bound derivation from the canonical CORE result;
- Appendix B: reproduce the frozen neural linear, historical-reachability and ReLU constructions with their exact values and no stronger interpretation;
- Appendix C: reproduce the response-coordinate WEAK audit, nuisance-classification FAIL, exact Gram control and PARK decision;
- Appendix D: reproduce the APP-B equations, frozen specification, full nine-case metric table, convergence/symmetry audits and exact mean/COI control;
- Appendix E: reproduce the APP-C inverse-dynamics derivation, budgets, P0/PT/PM tables, convergence audit and explicit absence of preparation inputs during evaluation;
- Appendix F: compile the prospective-freeze/governance table from existing frozen gates and outcomes without implying that governance substitutes for scientific validation.

No supplement section may introduce a new theorem, new experiment, new result, new metric, new literature claim, or repaired classifier.

## 6. Reproducibility pointers

The venue-neutral package may include a reproducibility manifest with pointers to existing repository files only.

Scientific source modules currently include:

- `src/causal_synergetics/benchmarks/neural_linear.py`
- `src/causal_synergetics/benchmarks/neural_relu.py`
- `src/causal_synergetics/benchmarks/neural_response_coordinate.py`
- `src/causal_synergetics/benchmarks/neural_response_coordinate_nuisance.py`
- `src/causal_synergetics/benchmarks/power_grid_two_machine.py`
- `src/causal_synergetics/benchmarks/controlled_state_preparation.py`

Existing tests include:

- `tests/test_neural_linear_benchmark.py`
- `tests/test_neural_linear_history.py`
- `tests/test_neural_relu_pilot.py`
- `tests/test_neural_response_coordinate_pilot.py`
- `tests/test_neural_response_coordinate_nuisance.py`
- `tests/test_power_grid_two_machine.py`
- `tests/test_controlled_state_preparation.py`

Canonical result files and their recorded implementation/test commits must be cited by path/commit exactly as frozen. The manifest must state that repository CI is not configured and may report only previously frozen local test outcomes; no rerun is authorised.

## 7. Bibliography status

The specific metadata blockers identified in the prior compliance gate are closed in `research/manuscript/manuscript_editorial_completion_0_1.md`:

- Ntogramatzidis & Padula (2017) completed;
- Tabuada & Pappas (2005) year added;
- Li & Bose (1995) authors added;
- obsolete TODO removed.

No claim-level bibliography blocker remains. Venue-specific bibliography style remains downstream and should be applied only after venue selection.

## 8. Venue-dependency assessment

Venue selection can be deferred safely for one more step.

The following tasks are genuinely venue-neutral and should be completed first:

- render the four already frozen conceptual/schematic figure roles in a portable vector format;
- materialise existing tables without scientific changes;
- complete the supplement from frozen canonical material;
- assemble a reproducibility/artifact manifest;
- create a coherent submission-neutral source directory/package retaining Markdown as the canonical content source.

Venue selection becomes necessary **after** this pass for page/word limits, figure placement constraints, appendix/supplement split, bibliography style, LaTeX/Word template choice, anonymisation requirements, author metadata, data/code-availability wording required by the venue, and submission-system fields.

No venue is selected or implied by this gate.

## 9. Exact remaining blockers

No current scientific, claim, numerical, or claim-level bibliography blocker is identified.

Remaining blockers are artifact/submission mechanics only:

1. no rendered venue-neutral Figure 1–4 files;
2. no complete supplement artifact;
3. no reproducibility/artifact manifest;
4. no frozen venue-neutral submission package combining manuscript source, supplement, figures and manifest;
5. venue selection and venue-specific formatting/administrative metadata remain downstream after those artifacts exist.

## 10. Decision

**GO — VENUE-NEUTRAL ARTIFACT COMPLETION ONLY**.

Reject `GO — VENUE SELECTION / FORMAT SPECIFICATION REQUIRED` at this stage because none of the enumerated venue-neutral artifacts depends on page limits, publisher templates or submission-system rules.

Reject `REVISE` because no concrete presentational defect requires changing the frozen editorial manuscript before artifact creation.

Reject `STOP` because scientific and claim readiness remain intact.

## 11. Next task and branch recommendation

Create rollback point:

`RP-025 — Manuscript Submission Readiness & Artifact Packaging Freeze 0.1`.

Re-open exactly one branch:

`90 – MANUSCRIPT – Manuskript & Figuren`

for exactly one task:

`Manuscript Venue-Neutral Artifact Completion 0.1`.

The task may create only:

- venue-neutral vector/schematic Figure 1–4 files consistent with Section 3 above;
- a complete supplement compiled from frozen canonical text/results;
- a reproducibility/artifact manifest with existing paths/commits and frozen test-state statements;
- a submission-neutral artifact index/package that references the frozen editorial manuscript and newly created venue-neutral artifacts.

It may not select a venue, modify scientific content, rerun code, create trajectory data, introduce new metrics, add literature, change claims, repair WEAK/FAIL outcomes, create submission correspondence, or submit anything.

All scientific branches remain frozen/waiting or parked.

## 12. Exact next user command

Open/return to `90 – MANUSCRIPT – Manuskript & Figuren` and enter exactly:

`GO`

No novelty promotion is authorised.
