# Prompt — Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-04
Dependency: `research/master/neural_response_coordinate_weak_integration_0_1.md` (`REVISE — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`)

## Name

`Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1`

## Purpose

Define and freeze exactly one falsifiable control benchmark addressing the unresolved issue exposed by the frozen WEAK response-coordinate result: whether response-aware compression has predictive/invariance value beyond equally compact raw-parameter geometry when response-irrelevant parameterisation nuisance is present.

This is a MASTER specification gate only. It must not execute the benchmark, inspect new held-out results, search multiple nuisance constructions, alter the prior coordinate result, or promote novelty.

## Frozen evidence and claim ceiling

Use only the canonical project state through:

`RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`.

Preserve these facts:

- the prior 2D response coordinate predicted held-out interventions essentially exactly;
- equal-dimensional raw-parameter PCA also predicted essentially exactly;
- the prior result is `WEAK`, not PASS;
- no special response-aware value beyond raw-state geometry has been established;
- generic intervention-sufficient representations remain prior-art territory;
- no novelty promotion is authorised.

## Required scientific question

The next benchmark must answer exactly:

> Under a pre-declared, model-justified parameterisation nuisance that is irrelevant to the frozen intervention-response semantics, does a compact response-aware representation remain predictive while equally compact raw-state representations lose predictive sufficiency, or does raw-state geometry remain equally adequate?

The nuisance must be justified independently of anticipated baseline performance.

## Anti-cherry-picking requirement

The specification must not choose a nuisance transformation merely because it is expected to make raw PCA fail.

A valid nuisance family must satisfy all of:

1. derive from an explicit reparameterisation/gauge/symmetry or otherwise independently justified representation redundancy of the model;
2. preserve the current function exactly or within a pre-frozen tolerance;
3. preserve the target response semantics exactly or with a pre-frozen analytical bound;
4. vary raw parameters nontrivially;
5. be fixed before any execution and without comparing alternative nuisance families by effect size;
6. use exactly one nuisance construction in this gate.

If no such construction can be specified cleanly, the correct gate decision is `STOP / PARK COORDINATE DIRECTION` rather than inventing a favorable family.

## Mandatory items to freeze

Before any execution, define exactly:

1. model and state family;
2. response-relevant latent variables;
3. nuisance variables and their independent justification;
4. exact invariants under nuisance variation;
5. state count and deterministic/random generation rule;
6. state train/test split;
7. intervention family and calibration/held-out split;
8. response functional and horizon;
9. candidate response-aware coordinate and fixed dimension;
10. coordinate-construction rule and information access;
11. raw-state baselines, including at minimum equal-dimensional raw PCA;
12. at least one stronger raw-state baseline if scientifically justified before execution;
13. preprocessing and normalisation;
14. decoder/predictor family shared across methods where appropriate;
15. nuisance-specific invariance metric in addition to held-out prediction;
16. primary/secondary metrics;
17. null/control tests;
18. nuisance levels or amplitudes, frozen as a finite list rather than selected after results;
19. seeds/splits if stochasticity is used;
20. PASS/WEAK/NULL/FAIL thresholds;
21. numerical tolerances;
22. software stack;
23. explicit anti-retuning rule.

## Design principle

The benchmark should separate two questions:

- **predictive sufficiency** for held-out interventions;
- **invariance/efficiency** under response-irrelevant reparameterisation nuisance.

A full PASS should require both high predictive performance and a material, pre-declared advantage over equally compact raw-state representations under nuisance. A result where both response-aware and raw-state coordinates remain equally predictive should be WEAK/NULL according to pre-frozen rules, not reinterpreted after inspection.

## Required deliverable

Create a versioned execution prompt:

`research/master/prompts/app_a_neural_response_coordinate_nuisance_invariance_pilot_0_1.md`

Also create a MASTER specification memo:

`research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`

Update only after the specification is frozen:

- `research/master/STATUS.md`;
- `research/master/project_status.md`;
- `research/master/decision_branch_log.md`;
- `research/app_a/STATUS.md` if and only if APP-A execution is authorised.

## Forbidden actions

Do not:

- run the new benchmark;
- inspect held-out outcomes;
- compare multiple nuisance families experimentally;
- tune nuisance amplitude by performance;
- change the prior frozen response-coordinate result;
- sweep coordinate dimensions;
- add baselines after seeing results;
- open nonlinear/multi-step/real-data/realistic-history/LoRA/power-grid/state-preparation/literature/manuscript work;
- claim novelty.

## Decision

End with exactly one of:

- `SPECIFICATION FROZEN / APP-A READY`
- `REVISE SPECIFICATION`
- `STOP / PARK COORDINATE DIRECTION`

If frozen, the next user action is to return to the existing `50 – APP-A – Neuronaler Minimalbenchmark` chat and enter `GO`.
