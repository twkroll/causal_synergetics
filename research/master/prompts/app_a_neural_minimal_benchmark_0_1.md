# Prompt — Neural Minimal Benchmark 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-03
Dependency satisfied by: `research/core/synergetic_sufficiency_boundary_0_1.md` (`PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`)

## Start text for the new chat

Du bist der Chat `50 – APP-A – Neuronaler Minimalbenchmark` innerhalb des durch `00 – MASTER` definierten Multi-Chat-Forschungsworkflows für `causal_synergetics`.

Git ist die Single Source of Truth. Folge strikt `research/master/PROJECT_GOVERNANCE_0_1.md`, deinem `research/app_a/STATUS.md`, dem eingefrorenen Literaturresultat `research/literature/prior_art_definitions_audit_0_1.md`, dem eingefrorenen CORE-Resultat `research/core/synergetic_sufficiency_boundary_0_1.md` und diesem versionierten Auftrag.

Öffne keine neuen Branches selbstständig. Ändere keine eingefrorenen Modell-, Interventions-, Horizon- oder Erfolgskriterien nach Ergebnisinspektion. Erzeuge keine neue Theorie und keine Novelty-Promotion. Wenn kein autorisierter Next Step existiert: `STOP — RETURN TO MASTER`.

Nach diesem Starttext lautet der erste Benutzerbefehl exakt:

`GO`

---

# Authorised task

## Name

`Neural Minimal Benchmark 0.1`

## Purpose

Build the smallest exact analytical + numerical neural benchmark showing that two parameter states with the same current function can have different responses to the same frozen learning intervention.

This gate is a **feasibility/benchmark gate**, not a novelty claim. Generic intervention-conditioned state insufficiency is already prior-art territory. The purpose is to create a reproducible, symmetry-controlled benchmark scaffold for later programme tests.

## Frozen model

Use a two-layer factorised linear scalar-output network

`f_{U,v}(x) = v^T U x`,

with input dimension `d=2`, hidden width `h=2`, `U in R^{2x2}`, `v in R^2`, and effective current function parameter

`w = U^T v`.

Freeze the two initial states exactly as

`v_A = (1,0)^T`,

`U_A = [[0,0],[1,0]]`,

and

`v_B = (1,0)^T`,

`U_B = [[0,0],[0,1]]`.

Therefore both states have exactly the same current effective function:

`w_A = w_B = (0,0)^T`.

They also have matched simple norms:

`||U_A||_F = ||U_B||_F = 1`,

`||v_A||_2 = ||v_B||_2 = 1`.

No alternative pair may be searched in this gate.

## Frozen intervention family

Use exactly two symmetric supervised linear-regression tasks.

For task `C`, target effective weight is

`c_C = e_1 = (1,0)^T`.

For task `D`, target effective weight is

`c_D = e_2 = (0,1)^T`.

The task loss is

`L_c(w) = 1/2 ||w-c||_2^2`.

This is equivalently the population squared-error loss for isotropic inputs with target `y=c^T x`.

The intervention is exactly **one simultaneous full-batch gradient-descent step in `(U,v)`** on the selected frozen task, with fixed learning rate

`eta = 0.1`.

No optimizer state, momentum, weight decay, stochastic minibatching, or noise is allowed in this gate.

## Frozen horizon and response

Horizon: `T = 1` optimizer step.

Primary response functional:

`Gamma_primary(s,c) = w^+`, the effective function parameter after the one frozen GD step.

Secondary response functional:

`Gamma_secondary(s,c) = L_c(w^+)`.

## Required analytical derivation

For `g = grad_w L_c(w)`, derive exactly

`U^+ = U - eta v g^T`,

`v^+ = v - eta U g`,

and

`w^+ = w - eta (U^T U + ||v||^2 I) g + eta^2 g (v^T U g)`.

Define

`P(U,v) = U^T U + ||v||^2 I`.

For the frozen states verify

`P_A = diag(2,1)`,

`P_B = diag(1,2)`.

Because the frozen current function is `w=0`, the `eta^2` term vanishes for both tasks.

The pre-specified analytical predictions are therefore:

Task `C`:

`w_A^+ = (0.2,0)^T`,

`w_B^+ = (0.1,0)^T`.

Task `D`:

`w_A^+ = (0,0.1)^T`,

`w_B^+ = (0,0.2)^T`.

And the corresponding post-step task losses are:

Task `C`:

`L_C(w_A^+) = 0.32`,

`L_C(w_B^+) = 0.405`.

Task `D`:

`L_D(w_A^+) = 0.405`,

`L_D(w_B^+) = 0.32`.

These numbers are frozen before execution. Do not alter the pair, tasks, or learning rate if the implementation disagrees.

## Numerical implementation

Implement a minimal reproducible benchmark in Python/PyTorch using float64.

Preferred paths:

- `src/causal_synergetics/benchmarks/neural_linear.py`
- `tests/test_neural_linear_benchmark.py`

If package scaffolding is absent, create only the minimal structure required for these files and tests. Do not build unrelated infrastructure.

Numerically verify both:

1. explicit analytical gradients/formulae;
2. PyTorch autograd + one optimizer-equivalent update.

## Frozen success criteria

Classify the gate `PASS` only if all hold:

1. **Current-function equality:** `w_A = w_B = 0` exactly analytically and within `1e-12` numerically.
2. **Norm symmetry:** the stated norm equalities hold within `1e-12`.
3. **Analytic/autograd agreement:** every component of `U^+`, `v^+`, and `w^+` agrees with the analytical update within `1e-12` in float64.
4. **Directed crossing:** `L_C(w_A^+) < L_C(w_B^+)` and `L_D(w_B^+) < L_D(w_A^+)`.
5. **Symmetry check:** the two loss advantages have equal magnitude within `1e-12`.
6. **No retuning:** no alternative `eta`, dimensions, state pair, task targets, optimizer, or response metric has been tried after inspecting the frozen result.

`FAIL` is a valid frozen result if any criterion fails. Do not repair the gate by searching a replacement configuration.

## Interpretation ceiling

If PASS, the allowed interpretation is only:

> In this frozen factorised linear neural benchmark, two parameter states with the same current function and matched simple norms can respond differently to the same one-step learning intervention; a symmetric task pair reverses which state adapts more strongly.

Do not claim from this gate that:

- the phenomenon is novel;
- current function is generally an order parameter;
- `P(U,v)` is a universal causal/plasticity coordinate;
- the result establishes causal synergetics;
- the result generalises to nonlinear networks, multi-step training, LoRA, transformers, or real datasets;
- historical training can reach the two states under a matched protocol.

## Required deliverables

Create:

`research/app_a/neural_minimal_benchmark_0_1.md`

It must contain:

1. Executive verdict.
2. Frozen specification reproduced exactly.
3. Full analytical derivation.
4. Numerical implementation summary.
5. Test results for every frozen success criterion.
6. PASS / FAIL classification.
7. Exact allowed interpretation and forbidden interpretations.
8. Open issues, especially historical reachability and nonlinear extension.
9. Code/test file paths and execution command.
10. Commit hash and CI status if applicable.

Commit the implementation, tests, result file, and updated `research/app_a/STATUS.md`.

## Forbidden actions

Do not:

- search for a stronger parameter pair;
- change `eta`, dimensions, tasks, horizon, optimizer, response metric, or success criteria;
- add a second benchmark after seeing results;
- introduce nonlinear networks;
- test historical reachability;
- learn a representation;
- add NTK, LoRA, adapters, model editing, or large-model experiments;
- perform a literature audit beyond citing the frozen claim ceiling;
- open another chat/branch;
- promote novelty.

## Final handoff

After committing the deliverables:

1. update `research/app_a/STATUS.md` with result classification and canonical commit hash;
2. set `Next instruction: RETURN TO MASTER`;
3. report CI status if applicable;
4. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
