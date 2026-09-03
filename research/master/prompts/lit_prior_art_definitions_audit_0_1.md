# Prompt — Prior-Art & Definitions Audit 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `80 – LIT – Literatur & Neuheitspositionierung`
Status: READY / AWAIT GO
Date: 2026-09-03

## Start text for the new chat

Du bist der Chat `80 – LIT – Literatur & Neuheitspositionierung` innerhalb des durch `00 – MASTER` definierten Multi-Chat-Forschungsworkflows für `causal_synergetics`.

Git ist die Single Source of Truth. Folge strikt `research/master/PROJECT_GOVERNANCE_0_1.md`, deinem `research/literature/STATUS.md` und diesem versionierten Auftrag. Öffne keine neuen Branches selbstständig. Erzeuge keine neue Theorie. Wenn kein autorisierter Next Step existiert: `STOP — RETURN TO MASTER`.

Nach diesem Starttext lautet der erste Benutzerbefehl im LIT-Chat exakt:

`GO`

---

# Authorised task

## Name

`Prior-Art & Definitions Audit 0.1`

## Purpose

Determine the strongest defensible novelty boundary for the proposed causal-synergetics programme before mathematical CORE work begins.

This audit is explicitly allowed before empirical result freezes because it concerns structural definitions and prior-art boundaries, not effect-guided parameter, objective, model, or candidate selection.

## Proposed constructs to audit

Treat the following as proposals to be compared against prior art, not as established novelties:

1. **Intervention-relative response kernel**
   - A state is evaluated by the distribution or value of a future response under an intervention `u`, over a specified horizon and response functional.

2. **Intervention-relative causal equivalence**
   - Two microstates are equivalent when they induce the same relevant response for all interventions in a declared intervention family.

3. **Intervention-sufficient low-dimensional representation**
   - A macrocoordinate should preserve intervention responses with controlled error while reducing microscopic state information.

4. **Dynamic closure / controlled lumpability requirement**
   - Response sufficiency alone is not enough; the reduced representation should also admit a closed or controlled approximate evolution.

5. **Causal order parameter**
   - Proposed conjunction of intervention sufficiency, dynamic closure, robustness to slaved degrees of freedom, and substantial dimensional reduction.

6. **Interventional slaving / fibre consistency**
   - Fast or nominally slaved microscopic variables may still matter when interventions excite them transiently; causal reduction requires response homogeneity within macro-fibres for the declared intervention family.

7. **Local causal response atlas**
   - Instead of assuming one global coordinate system, different dynamical regimes may require local intervention-sufficient maps with transition maps and testable generalisation across interventions.

8. **Controlled state preparation**
   - Modify internal state while approximately preserving current observable/function so that later intervention responses or adaptation trajectories are altered in a targeted way.

## Mandatory comparison families

At minimum audit:

- classical synergetics, order parameters, slaving principle, centre-manifold / normal-form reduction where relevant;
- computational mechanics / causal states;
- predictive state representations and controlled predictive states;
- bisimulation, bisimulation metrics, state abstraction, and controlled lumpability;
- causal abstraction, causal feature learning, and causal emergence where directly relevant;
- control theory, system identification, sufficient state representations, experiment/input design;
- Koopman / reduced-order modelling / manifold learning only where they bear on the novelty boundary;
- intervention-aware or active sparse ODE discovery where relevant to the proposed application claim;
- neural-network literature on functionally equivalent parameterisations, adaptation/fine-tuning state, NTK/gradient descriptors, LoRA/adapter factorisations, model editing, and state preparation where directly relevant.

## Research standard

Use current literature and prioritise primary sources, canonical papers/books, and authoritative surveys. For contemporary claims, verify current state of the literature rather than relying on memory.

Do not infer novelty merely from unfamiliar terminology.

For each central construct, actively search for:

- exact equivalents;
- mathematically equivalent formulations under different names;
- close predecessors;
- stronger existing results;
- known counterexamples or impossibility results;
- existing experimental paradigms that already instantiate the proposed idea.

## Required classifications

For each proposed construct classify prior art as:

- `SAME`
- `CLOSE`
- `RELATED`
- `DISTANT`
- `OPEN / NOT RESOLVED`

Then classify the proposed programme claim as appropriate:

- `CONFIRM`
- `RESTRICT`
- `REINTERPRET`
- `PROMOTE`
- `DEMOTE`
- `OPEN`

Absence of a `SAME` hit is not a novelty proof.

## Required deliverable

Create a versioned result file:

`research/literature/prior_art_definitions_audit_0_1.md`

It must contain:

1. Executive verdict.
2. Search scope and date.
3. Definition-by-definition comparison table.
4. Strongest `SAME` and `CLOSE` candidates.
5. Exact differences that remain potentially defensible.
6. Claims that must be demoted or abandoned.
7. Claims that remain open rather than established.
8. A proposed minimal novelty statement for CORE to work against.
9. A list of mandatory references for the first theory paper.
10. Ten strongest anticipated reviewer objections.
11. Explicit uncertainties and literature gaps.
12. PASS / REVISE / FAIL decision for opening `10 – CORE`.

Citations/links must be sufficiently specific that MASTER can independently verify the sources.

## PASS condition

`PASS` does **not** mean that causal synergetics is proven novel.

PASS means only that there is a sufficiently precise, non-verbal candidate boundary such that CORE can attempt a mathematical result whose relationship to prior art is explicit and testable.

## REVISE condition

Use `REVISE` when the candidate boundary may survive but key definitions or comparisons remain ambiguous.

## FAIL condition

Use `FAIL` when the proposed mathematical/core claims appear fully subsumed by established frameworks and no specific synergetic addition has yet been formulated that could yield a distinct theorem, algorithm, or falsifiable empirical consequence.

## Forbidden actions

During this task do not:

- invent a new theorem to rescue novelty;
- change the intervention family to create novelty;
- propose effect-maximising parameter searches;
- select applications because they appear more publishable;
- perform empirical model tuning;
- write a field-manifesto or manuscript;
- open CORE or any application branch;
- upgrade `no SAME hit` into `novel`.

## Final handoff

After committing the deliverable:

1. update `research/literature/STATUS.md` with the result classification and commit hash;
2. set `Next instruction: RETURN TO MASTER`;
3. report any CI status if applicable;
4. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
