# Prompt — Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-04
Dependency: `RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1`

## Name

`Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1`

## Purpose

Select and pre-specify exactly one minimal power-system benchmark that tests the branch-independent CORE question in a physically distinct domain:

> Can a pre-declared passive/macroscopic description that is adequate for unforced or nominal dynamics fail to be sufficient for predicting a frozen class of control/load interventions, and can that failure or its finite-horizon bound be measured without inventing a new state-equivalence concept?

This is a MASTER feasibility/specification gate only. It must not execute the benchmark, inspect effect magnitudes, open APP-B before the specification is frozen, or promote novelty.

The motivation is cross-domain transfer of the already frozen CORE boundary, not repair of the parked neural response-coordinate direction.

## Frozen evidence and claim ceiling

Use only canonical project state through:

`RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1`.

Preserve:

- prior-art restrictions on controlled/intervention-relative state equivalence and low-dimensional sufficient representations;
- CORE result that unforced synergetic slaving does not imply controlled response sufficiency and that exact full-trajectory fibre sufficiency is controlled projectability/closure;
- all frozen neural results, including the parked response-coordinate direction;
- no novelty promotion.

The power-grid branch may test transfer of the CORE diagnostic but may not claim a new equivalence, new causal state formalism, or field-level novelty.

## Required gate decision

End with exactly one of:

- `SPECIFICATION FROZEN / APP-B READY`
- `REVISE SPECIFICATION`
- `STOP / PARK POWER-GRID DIRECTION`

If no scientifically neutral, minimal, reproducible benchmark can be fixed without effect-guided candidate search, choose STOP/PARK rather than trying multiple topologies or observables.

## Mandatory design requirements

Before any execution, the gate must freeze exactly:

1. one standard power-system dynamical model class, preferably a minimal swing-equation / network-reduced form with explicit physical units or normalized conventions;
2. exactly one fixed network topology and parameter set, justified by canonical simplicity rather than anticipated effect size;
3. full microstate variables and one pre-declared passive/macroscopic map to be tested;
4. nominal/unforced dynamics and the meaning of passive adequacy/slaving/aggregation in this benchmark;
5. exactly one admissible intervention family, such as bounded step/pulse changes in mechanical power, load, or controllable injection, with geometry and amplitudes frozen before execution;
6. response functional, observed channels and finite horizon(s);
7. whether the benchmark is an exact counterexample, bounded mismatch test, or both;
8. deterministic initial-state construction and any same-macro/different-hidden-state pairing rule;
9. any reachability/physical-admissibility constraints on initial states;
10. numerical integrator, tolerances, time resolution and software stack;
11. baselines, including at minimum the passive macro prediction and any standard physically informed reduced model required for fairness;
12. primary and secondary metrics;
13. null/sanity controls and conservation/symmetry checks where applicable;
14. PASS/WEAK/NULL/FAIL criteria that are exhaustive and disjoint;
15. explicit anti-retuning rule;
16. exact claim ceiling for every possible outcome.

## Anti-cherry-picking constraints

Do not:

- compare multiple grids/topologies and keep the strongest;
- tune damping, inertia, coupling, operating point, intervention amplitude, horizon, or observable after effect inspection;
- choose a macro map because it is known empirically to fail most strongly;
- import a response-coordinate objective from parked APP-A;
- use learned coordinates in this gate;
- open multiple power-grid candidates in parallel.

A single canonical minimal candidate must be selected before execution.

## Preferred scientific structure

The specification should, if cleanly possible, align the physical model with the frozen CORE notation:

`q_dot=f(q,r,u)`
`r_dot=g(q,r,u)`

where `q` is the pre-declared macro/observed sector, `r` is hidden/slaved structure, and `u` is the admissible intervention.

This alignment is for testability and cross-domain comparison only. It does not make the power-grid variables a novel `causal order parameter`.

## Required deliverables

Create:

`research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`

If and only if the specification is frozen, also create:

`research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`

and then initialise/update the canonical APP-B status for:

`60 – APP-B – Power-Grid Minimalbenchmark`

Do not open APP-B before the specification is frozen.

Update after the gate:

- `research/master/STATUS.md`;
- `research/master/project_status.md`;
- `research/master/decision_branch_log.md`;
- APP-B status only if execution becomes authorised.

## Alternatives explicitly deferred

This gate does not authorise:

- reopening neural response coordinates;
- broader neural nonlinear/multi-step scaling;
- realistic neural histories;
- LoRA/adapters/transformers;
- controlled state preparation;
- new literature positioning;
- manuscript drafting.

These remain waiting until MASTER integrates the power-grid gate result.

## Final handoff

After the gate is executed and committed, end with exactly one next user action consistent with its decision.
