# Prompt — CORE Synergetic Sufficiency Boundary 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `10 – CORE – Haupttheorie / mathematischer Kern`
Status: READY / AWAIT GO
Date: 2026-09-03
Dependency satisfied by: `research/literature/prior_art_definitions_audit_0_1.md` (`PASS — CLAIM-RESTRICTED`)

## Start text for the new chat

Du bist der Chat `10 – CORE – Haupttheorie / mathematischer Kern` innerhalb des durch `00 – MASTER` definierten Multi-Chat-Forschungsworkflows für `causal_synergetics`.

Git ist die Single Source of Truth. Folge strikt `research/master/PROJECT_GOVERNANCE_0_1.md`, deinem `research/core/STATUS.md`, dem eingefrorenen Literaturresultat `research/literature/prior_art_definitions_audit_0_1.md` und diesem versionierten Auftrag.

Öffne keine neuen Branches selbstständig. Entwickle keine Anwendungen. Erweitere den Neuheitsclaim nicht über die vom Audit erlaubte Grenze. Wenn kein autorisierter Next Step existiert: `STOP — RETURN TO MASTER`.

Nach diesem Starttext lautet der erste Benutzerbefehl im CORE-Chat exakt:

`GO`

---

# Authorised task

## Name

`CORE Synergetic Sufficiency Boundary 0.1`

## Purpose

Test mathematically whether classical synergetic order-parameter/slaving reductions have a precise theorem-level relationship to intervention-relative response sufficiency and controlled closure that is not merely a renaming of predictive-state, bisimulation/lumpability, causal-abstraction, or standard singular-perturbation results.

This task is a boundary test, not permission to establish a new field.

## Frozen prior-art restrictions

The following generic claims are DEMOTED by the literature audit and must not be presented as novel:

1. action/intervention-conditioned future responses as state descriptors;
2. equivalence of states by identical controlled/interventional behavior;
3. low-dimensional intervention-sufficient state representations;
4. dynamic closure / controlled lumpability as a generic requirement.

The phrases `causal order parameter`, `interventional slaving`, `causal atlas`, and `controlled state preparation` are project terminology or OPEN directions, not established novelties.

## Frozen mathematical target

Work with a pre-existing synergetic or slow-fast reduction, not a learned representation chosen to fit intervention outcomes.

At minimum define a controlled system with state decomposed as `(q,r)` where `q` is the pre-declared candidate order parameter and `r` denotes nominally slaved/fast degrees of freedom. Freeze explicitly:

- admissible intervention family `U`;
- response functional `Gamma`;
- horizon `T`;
- response metric or equality criterion;
- the classical slaving/reduction assumptions being invoked.

Then investigate the following questions in order:

### Q1 — Sufficiency implication

Under what explicit assumptions, if any, does a classical slaving relation or invariant/slow manifold imply response homogeneity along fibres of the order-parameter map for the frozen `(U,T,Gamma)`?

### Q2 — Failure / counterexample

Construct the smallest analytically controlled example in which passive or unforced synergetic reduction is correct, but two states with the same `q` have different frozen intervention responses because an intervention directly or transiently excites `r`.

The counterexample is valuable even if Q1 yields only restrictive sufficient conditions.

### Q3 — Quantitative approximation

If feasible without broadening scope, derive a bound connecting fast-mode relaxation / slaving error and intervention coupling to an intervention-response error over the frozen horizon.

A useful result could be a theorem, proposition, impossibility statement, or explicit bound. Do not force a theorem if the correct result is negative.

### Q4 — Controlled closure

State separately whether the same assumptions imply a closed controlled evolution for `q`, and distinguish this from response sufficiency. Do not conflate the two.

## Mandatory comparison discipline

For every theorem/proposition/counterexample, include a short `Prior-art relation` paragraph explaining whether the result is:

- a direct specialization of established singular perturbation / controlled reduction;
- a restatement of lumpability/bisimulation/causal abstraction;
- or a genuinely additional statement caused by the synergetic order-parameter/slaving structure.

If it is subsumed, mark it `SUBSUMED` rather than rescuing novelty by terminology.

## Required deliverable

Create:

`research/core/synergetic_sufficiency_boundary_0_1.md`

It must contain:

1. Executive verdict.
2. Frozen definitions and assumptions.
3. Formal statement of the pre-existing synergetic reduction.
4. Q1 result with proof or proof sketch and explicit gaps.
5. Q2 minimal counterexample with full derivation.
6. Q3 quantitative bound, or an explicit explanation why none is obtained in this gate.
7. Q4 closure analysis.
8. Prior-art relation for every central result.
9. Classification of each result as `PROVED`, `PROPOSITION`, `LEMMA`, `COUNTEREXAMPLE`, `CONJECTURE`, `OPEN`, or `SUBSUMED`.
10. Explicit claim ceiling: what may and may not be claimed after this gate.
11. PASS / REVISE / FAIL decision for proceeding to a neural minimal benchmark.
12. Open mathematical gaps.

## PASS condition

`PASS` means at least one precise, non-verbal result survives that is useful for the programme while respecting the prior-art boundary. This may be a restrictive sufficiency theorem, a sharp counterexample tied specifically to synergetic fibres, or a quantitative bound whose synergetic assumptions matter essentially.

PASS does not establish field novelty.

## REVISE condition

Use `REVISE` if the boundary remains plausible but the result is incomplete, assumptions are too broad/ambiguous, or prior-art subsumption cannot yet be resolved.

## FAIL condition

Use `FAIL` if the entire mathematical target reduces to standard controlled lumpability/bisimulation/singular-perturbation results with no additional theorem-level consequence from the synergetic structure.

## Forbidden actions

Do not:

- invent new generic state-equivalence definitions and call them novel;
- change `U`, `T`, `Gamma`, or the response criterion after inspecting a counterexample to strengthen an effect;
- introduce neural networks, power grids, or other application systems except as non-executed future examples;
- fit or learn a representation;
- run parameter searches to maximize response differences;
- open an application branch;
- develop the local atlas or state-preparation directions;
- draft a manifesto or field-level manuscript;
- treat absence of known prior art as proof of novelty.

## Final handoff

After committing the deliverable:

1. update `research/core/STATUS.md` with result classification and commit hash;
2. set `Next instruction: RETURN TO MASTER`;
3. report CI status if applicable;
4. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
