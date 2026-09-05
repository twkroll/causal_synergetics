# Prompt — Controlled State Preparation 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `70 – APP-C – Controlled State Preparation`
Status: READY / AWAIT GO
Date: 2026-09-05
Dependency: `RP-017 — Controlled State Preparation Specification Freeze 0.1`
Canonical specification: `research/master/controlled_state_preparation_feasibility_specification_0_1.md`

## Name

`Controlled State Preparation 0.1`

## Purpose

Execute exactly the prospectively frozen two-machine controlled-state-preparation benchmark and mechanically return `PASS`, `WEAK`, `NULL`, or `FAIL` under the frozen classifier.

The scientific question is narrow:

> Can the fixed bounded open-loop preparation keep the representative-machine macro at the same present state while moving only the hidden coherency mode to the forced relative equilibrium for a known later local step, so that after preparation ends the representative response matches the standard coherent aggregate better than both no preparation and an equal-cost sign-mismatched preparation?

This execution tests only this exact benchmark. It does not search for a preparation policy or claim a new control method.

## Mandatory reads before execution

Read:

1. `research/master/PROJECT_GOVERNANCE_0_1.md`;
2. `research/app_c/STATUS.md`;
3. `research/master/controlled_state_preparation_feasibility_specification_0_1.md`;
4. `research/app_b/power_grid_minimal_benchmark_0_1.md` for the frozen APP-B regression target;
5. `research/core/synergetic_sufficiency_boundary_0_1.md` for claim limits;
6. `research/literature/prior_art_definitions_audit_0_1.md` for prior-art restrictions.

If the STATUS does not authorise this exact gate, stop and return to MASTER.

## Frozen model

Use exactly

`delta1_dot = omega1`,

`omega1_dot = -omega1 + sin(delta2-delta1) + p1(t)`,

`delta2_dot = omega2`,

`omega2_dot = -omega2 + sin(delta1-delta2) + p2(t)`,

with `M=D=K=1` and initial state `x_init=(0,0,0,0)`.

Macro:

`q=(delta1,omega1)`.

Hidden coherency state:

`e_delta=delta2-delta1`, `e_omega=omega2-omega1`.

## Frozen future signs

Execute exactly

`a=+0.2`, `a=-0.2`.

For each sign execute exactly three conditions:

- `P0`: no preparation;
- `PT`: matched targeted preparation;
- `PM`: sign-mismatched preparation generated for `-a` and evaluated under `a`.

No fourth condition is allowed.

## Frozen preparation

Preparation duration:

`tau_prep=2.0`.

Define

`e_star(a)=asin(a/2)`.

`xi=t/tau_prep`.

`s(xi)=10 xi^3-15 xi^4+6 xi^5`.

`e_d(t;a)=e_star(a) s(xi)`.

Use analytical first and second time derivatives of `e_d`.

For the preparation sign `b` (`b=a` for PT and `b=-a` for PM), use exactly

`p1(t;b)=-sin(e_d(t;b))`,

`p2(t;b)=e_d_ddot(t;b)+e_d_dot(t;b)+sin(e_d(t;b))`.

No numerical optimization, feedback controller, learned policy, alternative smoothstep or alternative duration is allowed.

At the end of preparation, remove both preparation inputs completely.

## Frozen evaluation

Evaluation horizon:

`T_eval=5.0`.

During evaluation use exactly

`p1=0`,

`p2=a`.

B1 target trajectory starts from the preserved representative macro `(delta,omega)=(0,0)` and solves

`delta_B1_dot=omega_B1`,

`omega_B1_dot=-omega_B1+a/2`.

No evaluation feedback or compensation is allowed.

## Frozen numerics

Use NumPy float64 and deterministic fixed-step classical RK4 only.

Primary:

`dt=0.001`.

Audit:

`dt=0.0005`.

Evaluate time-dependent preparation controls at the exact RK4 stage times.

No adaptive solver, SciPy optimizer, stochasticity, seed search or resolution change is allowed.

## Required implementation

Create a minimal APP-C benchmark implementation under the existing package, preferably:

`src/causal_synergetics/benchmarks/controlled_state_preparation.py`

Create tests, preferably:

`tests/test_controlled_state_preparation.py`

Do not modify prior scientific implementation/test files except for unavoidable import/package plumbing. If plumbing is needed, document it explicitly and do not alter prior expected values or tests.

## Mandatory checks

Implement and record every Section 13 check from the frozen specification, including:

- exact constants/condition counts;
- finiteness;
- primary/audit convergence `<=1e-8`;
- PT/PM macro preservation `P_q<=1e-8`;
- PT/PM terminal hidden-target accuracy `<=1e-8`;
- preparation amplitude `<=0.35`;
- preparation energy `<=0.25`;
- PT/PM energy equality `<=1e-10`;
- analytical sign symmetry `<=1e-12`;
- matched evaluation relative vector field zero `<=1e-12`;
- P0 reproduction of frozen APP-B I_zero B1 mismatch `0.065347743843341` within `1e-10` for both signs;
- PT representative response versus B1 `<=1e-8`;
- proof in code/tests that no preparation input remains active during evaluation;
- all new APP-C tests pass;
- prior repository files remain unchanged.

Any mandatory failure gives `FAIL` immediately. Do not repair the specification.

## Required scientific metrics

For every sign and condition report:

`E_B1(X,a)` full-trajectory max representative-to-B1 error;

RMS representative-to-B1 error;

`H_delta(X,a)=max |e_delta-asin(a/2)|`;

`H_omega(X,a)=max |e_omega|`.

For PT/PM report:

`P_q`, terminal hidden-target error, peak input amplitude, and `C_prep`.

Aggregate:

`E_target_max`, `E_no_min`, `E_mismatch_min`, `B0_min`, `BM_min`, `H_target`.

Also report maximum absolute relative angle over preparation and evaluation for safety.

## Frozen classifier

After all mandatory checks pass, apply exactly the Section 15 hierarchy from the specification.

### PASS

Require all:

- every relative angle remains `<pi/2` in absolute value;
- `E_target_max<=1e-8`;
- `E_no_min>=1e-4`;
- `E_mismatch_min>=1e-4`;
- `B0_min>=0.90`;
- `BM_min>=0.90`;
- preparation amplitude and energy budgets respected.

### WEAK

Only if PASS does not apply, all mandatory checks and safety pass, and:

- `E_target_max < min(E_no_min,E_mismatch_min)`;
- `E_no_min>1e-10`;
- `E_mismatch_min>1e-10`;
- `B0_min>0`;
- `BM_min>0`.

### NULL

All mandatory checks pass but neither PASS nor WEAK applies, including safety violation or absence of directional benefit/material comparator denominator.

### FAIL

Any mandatory numerical, regression, construction, budget, symmetry, clamp, target, B1 structural audit or new-test failure.

Do not add classifier clauses after seeing results.

## Required result file

Create:

`research/app_c/controlled_state_preparation_0_1.md`

It must contain:

1. exact verdict;
2. frozen specification identifiers;
3. analytical preparation construction audit;
4. numerical sanity table;
5. full sign/condition metric table;
6. preparation cost/budget table;
7. targeted versus no-prep versus sign-mismatched comparison;
8. mechanical classifier audit;
9. no-retuning declaration;
10. exact claim ceiling;
11. code/test/result commits and CI state.

Update `research/app_c/STATUS.md` to COMPLETE / RESULT FROZEN and return to MASTER.

## Claim ceiling

Even on PASS, claim only:

> In this exact normalized two-machine swing model, the frozen bounded open-loop preparation holds the representative-machine macro fixed while steering the hidden coherency mode to the forced relative equilibrium for a known later local step; after preparation ends, the later representative response matches the standard coherent aggregate and outperforms both no preparation and the equal-cost sign-mismatched preparation under the frozen metrics.

Do not claim novelty, optimality, robustness to unknown interventions, generic power-grid benefit, generic controlled state preparation, a new causal-state formalism, learned causal coordinates, or established causal synergetics.

## Anti-retuning / STOP boundary

Do not change any frozen model, state, path, duration, control formula, budget, future intervention, comparator, target response, horizon, metric, threshold, integrator, resolution or claim after `GO`.

Do not try another preparation policy, optimizer, feedback controller, target state, topology, neural model or domain.

After result freeze:

`STOP — RETURN TO MASTER`
