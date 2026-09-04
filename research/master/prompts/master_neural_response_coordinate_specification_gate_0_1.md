# Prompt — Neural Response Coordinate Specification Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-04
Dependency satisfied by: `research/master/neural_vertical_slice_go_revise_stop_0_1.md` (`GO — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`)

## Name

`Neural Response Coordinate Specification Gate 0.1`

## Purpose

Define and freeze exactly one falsifiable neural predictive benchmark for a compact response/plasticity representation before any learned-coordinate execution begins.

This is a MASTER specification gate only. It must not execute training/evaluation, inspect held-out results, search candidate representations by performance, open additional domains, or promote novelty.

## Frozen evidence and claim ceiling

Use only the already frozen programme state through:

`RP-007 — Neural Vertical Slice Decision Freeze 0.1`.

Preserve all existing claim restrictions. In particular, no generic novelty is allowed for intervention-conditioned state representations, behavioral equivalence, low-dimensional intervention-sufficient states, or controlled closure. The neural evidence remains tiny-scale, one-step, and feasibility-only.

## Required design objective

The next empirical gate must answer one question:

> Does a compact, pre-specified response/plasticity representation predict held-out learning interventions materially better than pre-declared non-response-aware baselines?

The benchmark must be designed so that failure is scientifically meaningful and cannot be repaired by changing representation dimensionality, intervention split, baselines, or metrics after held-out inspection.

## Mandatory items to freeze

Before any execution, define exactly:

1. neural model/state family;
2. how function-equivalent or near-equivalent states are generated;
3. sample size / number of states;
4. admissible intervention family;
5. training-versus-held-out intervention split;
6. response functional and horizon;
7. candidate coordinate dimensionality;
8. coordinate learning/construction rule;
9. information/features available to the learner;
10. all preprocessing/normalisation;
11. mandatory baselines, including at minimum current-function features and simple norm/state summaries;
12. any stronger baseline justified before execution;
13. prediction model from coordinate/baseline to response;
14. evaluation metric and aggregation rule;
15. null/control tests;
16. random seeds/splits if stochasticity is used;
17. success / weak / null / fail thresholds;
18. numerical tolerances;
19. permitted implementation stack;
20. explicit anti-retuning rule after any held-out result is inspected.

## Design principles

The specification should maximize information value while remaining small enough to be analytically or numerically auditable.

Prefer a controlled state family where:

- current function is exactly equal or equality error has a pre-frozen tolerance;
- simple baselines have a genuine chance to succeed;
- intervention directions are numerous enough to permit a real held-out test;
- the response coordinate is lower-dimensional than the raw state/response data it is intended to summarize;
- the held-out split is fixed before execution;
- a failed coordinate test materially weakens the neural programme.

Do not select a representation merely because the previous ReLU example suggests it will win.

## Required deliverable

Create a versioned execution prompt:

`research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`

The execution prompt must contain the full frozen specification, PASS/WEAK/NULL/FAIL criteria, forbidden actions, deliverable path, test requirements, and final STOP protocol.

Also update:

- `research/master/STATUS.md`;
- `research/master/project_status.md`;
- `research/master/decision_branch_log.md`;
- `research/app_a/STATUS.md` only after the specification is frozen and execution is authorised.

## Forbidden actions

During this specification gate do not:

- run the benchmark;
- inspect any held-out response result;
- sweep representation dimensions;
- search state families for stronger effects;
- tune baselines or metrics against outcomes;
- open LoRA, transformer, power-grid, state-preparation, real-data, or manuscript branches;
- reopen prior freezes;
- claim novelty.

## Decision

The gate should end with exactly one of:

- `SPECIFICATION FROZEN / APP-A READY`
- `REVISE SPECIFICATION`
- `STOP`

If the specification is frozen, the next user action is to return to the existing `50 – APP-A – Neuronaler Minimalbenchmark` chat and enter `GO`.
