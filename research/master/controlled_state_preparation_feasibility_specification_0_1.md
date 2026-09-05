# Controlled State Preparation Feasibility & Specification 0.1

Status: COMPLETE / SPECIFICATION FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Dependency: `RP-016 — Cross-Domain Intervention-Sufficiency Integration Freeze 0.1`
Decision: **SPECIFICATION FROZEN / PREPARATION EXECUTION READY / NO NOVELTY PROMOTION**

## 1. Executive decision

A single narrow controlled-state-preparation benchmark can be specified prospectively without reopening the parked neural response-coordinate direction, retuning the frozen power-grid benchmark, searching multiple candidate systems, or claiming novelty.

The selected domain is the already frozen normalized two-machine swing system, but the preparation benchmark is a new capability task assigned to APP-C rather than an extension or reclassification of APP-B.

The benchmark asks whether a bounded preparation action can keep the full pre-declared representative-machine macro exactly fixed while changing only the hidden coherency state, end before a known future localized disturbance, and thereby make the later representative-machine response match the standard coherent aggregate response. The future disturbance sign is known during preparation; robustness to unknown disturbances is not tested.

The preparation is not selected by effect-size search. For each frozen future step `a in {+0.2,-0.2}`, the hidden target is the exact forced relative equilibrium of the frozen swing equations,

`e_delta*(a)=asin(a/2)`, `e_omega*(a)=0`.

A deterministic quintic hidden-state path and exact inverse-dynamics feedforward inputs are fixed analytically. A sign-reversed preparation with exactly the same path magnitude and control cost is the mandatory strong comparator. No controller learning, trajectory optimization, feedback during evaluation, or parameter search is permitted.

This is a narrow anticipatory preparation/preconditioning benchmark. It is not claimed as a new control method or generic state-preparation theory.

## 2. Candidate selection and rejected alternatives

Exactly one candidate is selected: physical two-machine swing dynamics.

Reasons:

- It branches from the first physically distinct PASS while testing a genuinely new capability rather than another insufficiency witness.
- The current representative-machine macro and hidden coherency state are already physically defined and frozen.
- The preparation can be constructed analytically with an exact same-macro constraint, avoiding learned coordinates and avoiding performance-guided policy search.
- A sign-reversed, energy-symmetric preparation provides a strong directional comparator.
- The protocol is temporally separated: preparation ends before evaluation, and no feedback or compensating control is active during the future disturbance.

Not selected:

- Neural function-preserving rescaling, because it would be too close to ordinary parameter symmetry/reparameterisation and would add little beyond the frozen ReLU pair.
- Reuse of `Neural Historical Reachability 0.1`, because that gate already established only artificial auxiliary-gradient endpoint reachability and would not provide an independent new capability test.
- Learned preparation or response-coordinate methods, because the response-coordinate direction is parked under `RP-013`.
- A new grid topology or retuned APP-B setting, because APP-B is frozen under `RP-015`.

## 3. Frozen physical system

Use exactly the same normalized two-machine nonlinear swing equations as the frozen APP-B benchmark, but with two preparation-phase machine inputs `p1(t),p2(t)`:

`delta1_dot = omega1`,

`omega1_dot = -omega1 + sin(delta2-delta1) + p1(t)`,

`delta2_dot = omega2`,

`omega2_dot = -omega2 + sin(delta1-delta2) + p2(t)`.

Constants remain exactly

`M=D=K=1`.

State:

`x=(delta1,omega1,delta2,omega2)`.

Pre-declared current macro to preserve:

`q=(delta1,omega1)`.

Hidden coherency coordinates:

`r=(e_delta,e_omega)`,

`e_delta=delta2-delta1`,

`e_omega=omega2-omega1`.

No machine count, topology, inertia, damping, coupling, voltage model, governor model, load model, or operating point may be changed.

## 4. Frozen initial state and current-macro preservation objective

Use exactly one deterministic common initial state before preparation:

`x_init=(0,0,0,0)`.

Thus

`q_init=(0,0)`, `r_init=(0,0)`.

The preparation must preserve the representative-machine macro not only at the endpoint but throughout the entire preparation interval:

`q(t)=(0,0)` for `0<=t<=tau_prep`

in the exact continuous model.

Numerical preservation metric:

`P_q = max_{0<=t<=tau_prep} max(|delta1(t)|,|omega1(t)|)`.

Terminal hidden-target error:

`P_r = max(|e_delta(tau_prep)-e_delta*|, |e_omega(tau_prep)|)`.

This same-current-macro requirement is central. A method that improves future response by changing the present representative-machine macro does not satisfy the benchmark.

## 5. Frozen future evaluation interventions

Use exactly the sign-symmetric future disturbance family

`a in {+0.2,-0.2}`.

After the preparation interval ends, all preparation inputs are removed and the evaluation phase uses only

`p1(t)=0`,

`p2(t)=a`

for the full evaluation horizon.

No feedback, compensating action, ramp, pulse, topology change, or intervention adaptation is allowed during evaluation.

The future sign `a` is assumed known before preparation. Unknown-sign, distributional, robust, or adaptive preparation is outside benchmark 0.1.

Evaluation horizon:

`T_eval=5.0` normalized time units, reusing the five-damping-time-constant horizon frozen in APP-B.

## 6. Frozen target hidden state

For a constant future localized step `a`, the relative dynamics during evaluation are

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)+a`.

The near-synchronous forced relative equilibrium is therefore fixed analytically by

`e_omega*=0`,

`2 sin(e_delta*)=a`.

Hence

`e_delta*(a)=asin(a/2)`.

For the frozen amplitudes,

`|e_delta*|=asin(0.1)`.

This target is determined by the frozen future intervention and model equations, not by inspecting a preparation response or searching over hidden states.

## 7. Frozen preparation action family

Preparation duration:

`tau_prep=2.0` normalized time units, exactly two damping time constants.

For each future sign `a`, define

`xi=t/tau_prep`, `0<=xi<=1`,

`s(xi)=10 xi^3 - 15 xi^4 + 6 xi^5`.

The desired hidden path is

`e_d(t;a)=e_delta*(a) s(t/tau_prep)`.

Set

`e_omega,d(t;a)=d e_d/dt`.

The quintic satisfies zero first and second derivatives at both endpoints.

The frozen open-loop preparation inputs are

`p1,target(t;a) = -sin(e_d(t;a))`,

`p2,target(t;a) = d2 e_d/dt2 + d e_d/dt + sin(e_d(t;a))`.

With the exact model and common initial state, the trajectory

`delta1(t)=0`, `omega1(t)=0`,

`delta2(t)=e_d(t;a)`, `omega2(t)=d e_d/dt`

solves the full equations exactly. Therefore the current macro is exactly clamped while the hidden state is moved to

`r(tau_prep)=(e_delta*(a),0)`.

No numerical optimizer or learned policy is used to construct the preparation.

## 8. Frozen preparation admissibility, budget and cost

The smoothstep derivative bounds are fixed analytically:

`max |s'| = 15/8`,

`max |s''| = 10/sqrt(3)`.

For `tau_prep=2` and `|e_delta*|=asin(0.1)`, the frozen feedforward construction obeys the deterministic bounds

`|p1(t)| <= 0.1`,

`|p2(t)| <= asin(0.1) [(10/sqrt(3))/4 + (15/8)/2] + 0.1 < 0.339`.

Freeze the admissible per-machine preparation amplitude cap as

`max_t max(|p1|,|p2|) <= 0.35`.

Preparation energy/cost is

`C_prep = integral_0^tau_prep [p1(t)^2+p2(t)^2] dt`.

Using the frozen analytic amplitude bounds gives a conservative deterministic budget below `0.25`; therefore freeze

`C_prep <= 0.25`.

No amplitude, duration, cost weighting or trajectory shape may be retuned after execution begins.

## 9. Frozen conditions and strong comparator

For each future sign `a`, execute exactly three preparation conditions from the same `x_init`:

### P0 — no preparation

No preparation inputs. Evaluation begins from `x_init`.

This is the mandatory no-preparation baseline.

### PT — targeted preparation

Use the frozen preparation generated from the matched future sign `a`, reaching

`r=(asin(a/2),0)`

while preserving `q=(0,0)`.

### PM — sign-mismatched preparation

Use exactly the sign-reversed preparation generated for `-a`, then evaluate under `a`.

Because the system, path and controls are odd under sign reversal,

`p_i(t;-a)=-p_i(t;a)`

and therefore PT and PM have exactly equal preparation energy in the continuous model.

PM is the mandatory strong comparator. It tests directionality under identical duration, path magnitude, amplitude envelope and cost rather than comparing PT only with doing nothing.

No fourth preparation policy is permitted.

## 10. Frozen target response property

The standard coherent aggregate response B1 is retained as the physically informed target trajectory, initialized from the preserved representative macro `q=(0,0)`:

`delta_B1_dot=omega_B1`,

`omega_B1_dot=-omega_B1+a/2`.

For PT, because

`sin(e_delta*(a))=a/2`

and the hidden state is at an exact relative equilibrium, the continuous full model has

`e_delta(t)=e_delta*(a)`, `e_omega(t)=0`

during evaluation, so the representative machine obeys the same B1 equations. This exact structural prediction is part of the pre-result specification; the numerical benchmark must verify it without changing the target or thresholds.

Primary evaluation error for condition `X in {P0,PT,PM}`:

`E_B1(X,a)=max_{0<=t<=T_eval} max(|delta1_X(t)-delta_B1(t)|, |omega1_X(t)-omega_B1(t)|)`.

Primary targeted benefit relative to no preparation:

`B0(a)=1-E_B1(PT,a)/E_B1(P0,a)`.

Primary targeted benefit relative to the sign-mismatched comparator:

`BM(a)=1-E_B1(PT,a)/E_B1(PM,a)`.

If a denominator is `<=1e-12`, the corresponding benefit is undefined and the scientific classifier cannot PASS or WEAK; after mandatory numerical checks it falls to NULL.

The target property is therefore not hidden-state reachability alone. It is later agreement of the preserved representative macro with the physically informed coherent aggregate under the separately frozen future intervention.

## 11. Frozen secondary response and safety metrics

For evaluation under sign `a`, define relative-equilibrium transient errors

`H_delta(X,a)=max_t |e_delta_X(t)-asin(a/2)|`,

`H_omega(X,a)=max_t |e_omega_X(t)|`.

Also report

- full `e_delta(t),e_omega(t)` trajectories;
- representative macro trajectory `q(t)`;
- B1 trajectory;
- RMS representative-to-B1 trajectory error;
- preparation `P_q`, `P_r`, peak input amplitude and `C_prep`;
- maximum absolute relative angle over preparation plus evaluation.

Safety/admissibility condition:

`max |e_delta(t)| < pi/2`

for every PT/PM preparation and all P0/PT/PM evaluation trajectories.

Safety violation after otherwise valid numerical execution is a scientific NULL, not an implementation FAIL.

## 12. Frozen numerical method and software stack

Use the existing deterministic in-project classical RK4 implementation pattern from APP-B, with NumPy float64 only.

Preparation phase:

- `tau_prep=2.0`;
- primary `dt=0.001`;
- audit `dt=0.0005`;
- time-dependent preparation controls evaluated analytically at every RK4 stage time.

Evaluation phase:

- `T_eval=5.0`;
- primary `dt=0.001`;
- audit `dt=0.0005`;
- constant evaluation inputs.

Use pytest for tests. No SciPy optimizer, adaptive integration, controller tuning, random seed, learned model or stochastic component is allowed.

Convergence metric:

maximum componentwise difference between primary-grid trajectories and every second point of the audit-grid trajectories across all preparation, P0/PT/PM evaluation and B1 trajectories.

Frozen convergence tolerance:

`<=1e-8`.

## 13. Frozen mandatory sanity and regression checks

All must pass before scientific classification:

1. exact constants `M=D=K=1`, `tau_prep=2`, `T_eval=5`, `a=±0.2`, `x_init=0`;
2. exactly two future signs and exactly three preparation conditions `P0/PT/PM` per sign;
3. all primary and audit trajectories finite;
4. RK4 convergence discrepancy `<=1e-8`;
5. PT preparation macro-preservation error `P_q<=1e-8` for both signs;
6. PM preparation macro-preservation error `P_q<=1e-8` for both signs;
7. PT terminal target error `P_r<=1e-8` for both signs;
8. PM terminal target error relative to the sign-reversed target `<=1e-8`;
9. maximum preparation amplitude `<=0.35`;
10. PT and PM preparation energy `<=0.25`;
11. PT versus PM preparation energy difference `<=1e-10` for each future sign;
12. preparation sign symmetry `max_t |p_i(t;-a)+p_i(t;a)|<=1e-12` on the analytic control grid;
13. PT evaluation initial relative vector field equals zero within `1e-12` under the matched future intervention;
14. P0 evaluation reproduces the frozen APP-B `I_zero` B1 mismatch for both signs within absolute `1e-10` of `0.065347743843341` on the primary grid;
15. PT full representative response versus analytic B1 agrees within `1e-8` if the implementation is correct;
16. no preparation input remains active after evaluation begins;
17. all new APP-C tests pass and all existing repository tests are left unchanged.

If any mandatory sanity/regression condition fails, classification is `FAIL` rather than WEAK/NULL/PASS.

Condition 15 is an implementation/structural audit, not the scientific materiality criterion. Its expected exactness follows from the frozen equations before execution.

## 14. Frozen scientific metrics

Aggregate over both future signs:

`E_target_max = max_a E_B1(PT,a)`.

`E_no_min = min_a E_B1(P0,a)`.

`E_mismatch_min = min_a E_B1(PM,a)`.

`B0_min = min_a B0(a)`.

`BM_min = min_a BM(a)`.

`H_target = max_a max(H_delta(PT,a),H_omega(PT,a))`.

Also report every sign-specific value.

No alternative response metric may replace `E_B1` after execution.

## 15. Exhaustive frozen classification

Apply the following hierarchy only after every mandatory sanity/regression check in Section 13 passes.

### PASS

All of:

- safety condition holds for every trajectory;
- `E_target_max <= 1e-8`;
- `E_no_min >= 1e-4`;
- `E_mismatch_min >= 1e-4`;
- `B0_min >= 0.90`;
- `BM_min >= 0.90`;
- PT and PM each respect the frozen amplitude and energy budgets.

Interpretation ceiling:

> In this exact normalized two-machine swing model, a prospectively fixed bounded open-loop preparation can hold the representative-machine macro at the same present state while moving only the hidden coherency state to the forced relative equilibrium associated with a known later local step. After preparation ends, the representative-machine response under that step matches the standard coherent aggregate trajectory, while no preparation and an equal-cost sign-mismatched preparation remain materially different. This is a narrow model-based anticipatory preparation result, not a generic state-preparation or control-theory claim.

### WEAK

All mandatory checks pass, safety holds, PASS does not apply, and all of:

- `E_target_max < min(E_no_min,E_mismatch_min)`;
- `E_no_min > 1e-10`;
- `E_mismatch_min > 1e-10`;
- `B0_min > 0`;
- `BM_min > 0`.

Interpretation ceiling: the frozen bounded preparation directionally improves the later representative response over both no preparation and the equal-cost sign-mismatched control, but it does not meet the predeclared exactness/materiality requirements.

### NULL

All mandatory checks pass but neither PASS nor WEAK applies.

This includes any safety violation, any non-material no-preparation or comparator denominator, or absence of directional benefit over at least one required comparator.

NULL is a valid scientific result. It must not trigger another preparation path, duration, target, disturbance, model or domain inside benchmark 0.1.

### FAIL

One or more mandatory sanity/regression checks fail, including model construction, macro clamp, hidden target, control-budget audit, sign symmetry, convergence, APP-B regression, structural B1 audit, or new test failure.

These classes are ordered, disjoint and exhaustive.

## 16. Anti-retuning freeze

After APP-C receives `GO`, do not change:

- system/domain or topology;
- `M,D,K`;
- current macro or hidden coordinates;
- initial state;
- preparation duration or quintic path;
- analytic feedforward construction;
- preparation amplitude or energy budgets;
- future intervention signs or amplitudes;
- sign-mismatched comparator;
- B1 target trajectory;
- evaluation horizon;
- integrator or resolutions;
- tolerances;
- response metrics;
- PASS/WEAK/NULL/FAIL thresholds;
- claim ceiling.

No alternative preparation policy, optimizer, feedback controller, hidden target, duration, cost, disturbance, topology, neural candidate or second domain may be tried after effect inspection.

## 17. Prior-art separation and claim ceiling

The benchmark is operationally separated from the most obvious confounds:

- it is not a parameter reparameterisation or model edit;
- it starts from one fixed physical state rather than choosing a favourable initialization;
- the preparation is a bounded dynamical trajectory with explicit cost;
- the current representative macro is held fixed throughout preparation;
- the preparation ends before the future disturbance;
- no feedback, adaptation or compensating control acts during evaluation;
- the equal-cost sign-reversed preparation controls for generic pre-actuation and energy injection.

Nevertheless the method is recognisably related to established anticipatory feedforward control, equilibrium pre-positioning and preconditioning. No novelty is claimed for those control ideas.

For every outcome, prohibited claims include:

- generic controlled state preparation;
- optimality of the preparation;
- robustness to unknown or stochastic future interventions;
- realistic actuator feasibility beyond the normalized model;
- generic power-grid benefit;
- new controlled-state equivalence or causal-state formalism;
- learned causal/plasticity coordinates;
- established causal synergetics.

The only possible PASS claim is the exact benchmark statement in Section 15.

## 18. Gate outcome and branch recommendation

The candidate is scientifically neutral enough to freeze because its hidden target, preparation path, comparator, budgets, future interventions and evaluation metric are all determined before any new preparation response is inspected.

Decision:

**SPECIFICATION FROZEN / PREPARATION EXECUTION READY / NO NOVELTY PROMOTION**

Recommended execution branch:

`70 – APP-C – Controlled State Preparation`

This is a genuinely new two-phase preparation capability and therefore should not reopen APP-A or mutate the completed APP-B benchmark.

Rollback recommendation:

`RP-017 — Controlled State Preparation Specification Freeze 0.1`.
