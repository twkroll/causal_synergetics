# Prompt — APP-B Power-Grid Minimal Benchmark 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `60 – APP-B – Power-Grid Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-05
Dependency: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`

## Name

`Power-Grid Minimal Benchmark 0.1`

## Purpose

Execute exactly the frozen specification in:

`research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`

and return a mechanically classified `PASS`, `WEAK`, `NULL`, or `FAIL` result without changing the model, topology, macro map, intervention, horizon, baselines, resolution, metrics, thresholds, or claim ceiling.

This is a cross-domain transfer test of the already frozen CORE control-leakage mechanism. It is not a novelty test and does not reopen neural response-coordinate work.

## Mandatory pre-execution reads

Before any code or execution, read:

1. `research/master/PROJECT_GOVERNANCE_0_1.md`;
2. `research/app_b/STATUS.md`;
3. `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`;
4. `research/core/synergetic_sufficiency_boundary_0_1.md`;
5. `research/literature/prior_art_definitions_audit_0_1.md`.

If APP-B status does not explicitly authorise this gate, stop and return to MASTER.

## Frozen model

Use only the normalized two-machine nonlinear swing system:

`delta1_dot = omega1`

`omega1_dot = -omega1 + sin(delta2-delta1)`

`delta2_dot = omega2`

`omega2_dot = -omega2 + sin(delta1-delta2) + u`

with exactly:

`M=D=K=1`.

Pre-declared macro:

`q=(delta1,omega1)`.

Hidden coherency variables:

`e_delta=delta2-delta1`,

`e_omega=omega2-omega1`.

No alternative grid/model is permitted.

## Frozen initial states and interventions

Initial states, exactly:

- `I_minus=(0,-0.1,0,-0.1)`;
- `I_zero=(0,0,0,0)`;
- `I_plus=(0,+0.1,0,+0.1)`.

Interventions, exactly:

- `u0=0`;
- `u+=+0.2`;
- `u-=-0.2`.

Each is constant over exactly `T=5.0`.

No amplitude, sign, waveform, bus, horizon, or initial-state sweep.

## Frozen baselines and controls

### B0

Passive-slaving representative model:

`delta_dot=omega`,

`omega_dot=-omega`.

### B1

Coherent aggregate surrogate:

`delta_eq_dot=omega_eq`,

`omega_eq_dot=-omega_eq+u/2`.

### C0

Full four-state nonlinear swing system.

### C1

Exact mean/COI control:

`delta_mean=(delta1+delta2)/2`,

`omega_mean=(omega1+omega2)/2`,

which must match B1 within the frozen numerical tolerance.

## Frozen numerical method

Implement deterministic classical RK4 using NumPy float64 only.

Primary:

`dt=0.001`, `T=5`, exactly 5000 steps.

Convergence audit:

`dt=0.0005`; compare every second fine step to the primary grid.

No adaptive solver, alternative integrator, or tolerance repair.

Suggested implementation paths:

`src/causal_synergetics/benchmarks/power_grid_two_machine.py`

`tests/test_power_grid_two_machine.py`

Alternative paths are allowed only if necessary for the repository's existing import layout; scientific contents may not change.

## Mandatory implementation content

The implementation must expose/test at minimum:

- frozen constants and initial states;
- full RHS;
- `(q,r)` transformation;
- B0 RHS;
- B1 RHS;
- deterministic RK4;
- generation of all nine full trajectories and matching baselines;
- trajectory max/RMS/componentwise metrics;
- coherency error metrics;
- primary/half-step convergence audit;
- exact mean/COI closure audit;
- sign-symmetry audit;
- controlled-invariance defect on `M_sync`.

## Mandatory sanity hierarchy

Before scientific classification, enforce exactly the specification checks:

1. frozen constants/states/interventions;
2. exact trajectory counts;
3. finite states;
4. convergence max error `<=1e-8`;
5. passive coherency error `<=1e-12`;
6. passive full-vs-B0 `d_inf<=1e-10`;
7. mean/COI full-vs-B1 `d_inf<=1e-10`;
8. positive/negative controlled-increment odd symmetry `<=1e-10`;
9. on-manifold controlled-invariance defect exactly `(0,u)` to numerical precision;
10. new APP-B tests and all prior repository tests pass unchanged.

Any failure here => `FAIL`.

## Frozen scientific metrics

Compute exactly:

`E_pass`;

`E_B0_min`;

`E_B1_min`;

`H_delta`;

plus all pairwise B0/B1 errors, componentwise errors, RMS errors, maximum `|e_omega|`, mean-closure error, and convergence error.

Do not introduce replacement metrics.

## Frozen classification

After all mandatory sanity checks pass:

### PASS

- `H_delta < pi/2`;
- `E_pass <=1e-10`;
- `E_B0_min >=1e-4`;
- `E_B1_min >=1e-4`.

### WEAK

- `H_delta < pi/2`;
- `min(E_B0_min,E_B1_min)>1e-10`;
- PASS is false.

### NULL

All mandatory sanity checks pass, but neither PASS nor WEAK applies.

### FAIL

At least one mandatory sanity/implementation/convergence/regression condition fails.

Do not add or change branches in this classifier after inspection.

## No-retuning rule

No second topology, second amplitude, second macro map, second horizon, alternative integrator, alternative baseline, threshold adjustment, or follow-on fault experiment is allowed after execution begins.

WEAK, NULL, and FAIL are valid frozen returns.

## Required deliverable

Create:

`research/app_b/power_grid_minimal_benchmark_0_1.md`

It must contain:

1. verdict;
2. exact frozen specification identifiers;
3. analytic coherency/control-invariance derivation;
4. numerical sanity table;
5. full metric table for all initial-state/sign pairs;
6. B0/B1/C1 comparison;
7. mechanical classification audit;
8. no-retuning declaration;
9. claim ceiling;
10. code/test/result commits and CI state.

Update:

`research/app_b/STATUS.md`.

Commit implementation/tests/result/status. Query GitHub commit-status/CI state. Do not infer CI success from local tests.

## Claim ceiling

No novelty promotion.

A PASS may state only:

> In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

Do not claim generic power-grid transfer, a novel causal state, learned coordinates, controlled state preparation, or established causal synergetics.

## Final boundary

After the frozen result and status are committed, end:

`STOP — RETURN TO MASTER`
