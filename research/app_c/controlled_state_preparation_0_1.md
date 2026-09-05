# Controlled State Preparation 0.1

Status: EXECUTED / RESULT FROZEN
Assigned chat: `70 – APP-C – Controlled State Preparation`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Specification: `research/master/controlled_state_preparation_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_c_controlled_state_preparation_0_1.md`
Dependency: `RP-017 — Controlled State Preparation Specification Freeze 0.1`
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

## 1. Exact verdict

The prospectively frozen `Controlled State Preparation 0.1` benchmark is mechanically classified **PASS**.

> In this exact normalized two-machine swing model, the frozen bounded open-loop preparation holds the representative-machine macro fixed while steering the hidden coherency mode to the forced relative equilibrium for a known later local step; after preparation ends, the later representative response matches the standard coherent aggregate and outperforms both no preparation and the equal-cost sign-mismatched preparation under the frozen metrics.

No novelty, optimality, robustness-to-unknown-disturbance, generic power-grid benefit, generic controlled-state-preparation capability, new controlled-equivalence claim, learned-coordinate claim, or established causal-synergetics claim is authorised.

## 2. Frozen specification identifiers

Executed exactly:

- normalized two-machine nonlinear swing system with `M=D=K=1`;
- `x_init=(0,0,0,0)`;
- preserved present macro `q=(delta1,omega1)`;
- hidden state `(e_delta,e_omega)=(delta2-delta1,omega2-omega1)`;
- future local machine-2 steps `a=+0.2,-0.2`;
- forced hidden target `e_delta*=asin(a/2)`, `e_omega*=0`;
- quintic smoothstep preparation path over `tau_prep=2.0`;
- exact open-loop inverse-dynamics inputs;
- amplitude cap `0.35`, energy budget `0.25`;
- conditions `P0`, `PT`, `PM` only;
- evaluation horizon `T_eval=5.0`;
- B1 coherent aggregate target;
- NumPy float64 fixed-step RK4 with primary `dt=0.001` and audit `dt=0.0005`;
- frozen exhaustive `PASS/WEAK/NULL/FAIL` classifier.

No model, topology, parameter, target, preparation duration/path, intervention sign/amplitude, comparator, horizon, metric, tolerance, or classifier clause was changed after `GO`.

## 3. Analytical preparation construction audit

For each preparation sign `b`, the implementation uses

`e_star(b)=asin(b/2)`,

`e_d(t;b)=e_star(b) [10 xi^3-15 xi^4+6 xi^5]`, `xi=t/2`,

with analytical first and second derivatives and

`p1(t;b)=-sin(e_d(t;b))`,

`p2(t;b)=e_d_ddot(t;b)+e_d_dot(t;b)+sin(e_d(t;b))`.

For `|b|=0.2`, `|e_star|=asin(0.1)=0.1001674211615598`.

The sign-symmetry audit gives

`max_t max_i |p_i(t;-0.2)+p_i(t;+0.2)| = 0.0`.

The matched PT terminal evaluation relative-vector-field defect is

`4.6079385647875116e-15`,

well below the frozen `1e-12` tolerance.

During evaluation the implementation hard-codes `p1=0` and `p2=a`; the preparation-control function is not used. The new test checks this separation directly.

## 4. Numerical sanity table

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| Constants / signs / condition count | exact | exact | PASS |
| Finite primary/audit trajectories | all finite | all finite | PASS |
| Primary/audit convergence | `<=1e-8` | `5.738465258531278e-15` | PASS |
| PT macro preservation `P_q` | `<=1e-8` | `3.580739551835791e-15` | PASS |
| PM macro preservation `P_q` | `<=1e-8` | `3.580739551835791e-15` | PASS |
| PT terminal hidden-target error | `<=1e-8` | `4.6079385647875116e-15` | PASS |
| PM terminal sign-reversed target error | `<=1e-8` | `4.6079385647875116e-15` | PASS |
| Peak preparation amplitude | `<=0.35` | `0.20881049376163438` | PASS |
| Preparation energy | `<=0.25` | `0.04006381839386479` | PASS |
| PT/PM energy difference | `<=1e-10` | `0.0` | PASS |
| Analytical preparation sign symmetry | `<=1e-12` | `0.0` | PASS |
| Matched initial relative vector field | `<=1e-12` | `4.6079385647875116e-15` | PASS |
| APP-B `I_zero` B1 regression | abs error `<=1e-10` | `5.551115123125783e-17` | PASS |
| PT full representative vs B1 | `<=1e-8` | `2.076727044536923e-15` | PASS |
| No preparation input during evaluation | exact | `p1=0`, `p2=a` only | PASS |
| New APP-C tests | pass | `5 passed` | PASS |
| Existing scientific source/test files | unchanged | none modified | PASS |

Preparation energy was evaluated deterministically on the frozen primary control grid by composite trapezoidal quadrature of `p1^2+p2^2`; sign reversal gives identical squared controls and therefore exact PT/PM equality on the grid.

## 5. Full sign / condition metric table

`E_B1` is the full-trajectory max representative-to-B1 error. RMS is over both representative macro components and all primary-grid times. `H_delta=max|e_delta-asin(a/2)|`; `H_omega=max|e_omega|`.

| `a` | Condition | `E_B1` | RMS B1 | `H_delta` | `H_omega` | max `|e_delta|` over evaluation |
|---:|---|---:|---:|---:|---:|---:|
| `+0.2` | P0 | `0.06534774384334105` | `0.03809399399337059` | `0.1001674211615598` | `0.08954202393695318` | `0.13069548768668177` |
| `+0.2` | PT | `2.076727044536923e-15` | `9.481901258630277e-16` | `2.1649348980190553e-15` | `4.6079385647875116e-15` | `0.10016742116156196` |
| `+0.2` | PM | `0.1307357122731585` | `0.07621285244933236` | `0.20033484232311938` | `0.17919273392083204` | `0.16130400338475567` |
| `-0.2` | P0 | `0.06534774384334105` | `0.03809399399337059` | `0.1001674211615598` | `0.08954202393695318` | `0.13069548768668177` |
| `-0.2` | PT | `2.076727044536923e-15` | `9.481901258630277e-16` | `2.1649348980190553e-15` | `4.6079385647875116e-15` | `0.10016742116156196` |
| `-0.2` | PM | `0.1307357122731585` | `0.07621285244933236` | `0.20033484232311938` | `0.17919273392083204` | `0.16130400338475567` |

The P0 value reproduces the frozen APP-B `I_zero` B1 mismatch `0.065347743843341` for both signs within `5.551115123125783e-17` absolute error.

## 6. Preparation cost / budget table

All four PT/PM preparations have the same magnitude by sign symmetry.

| Future `a` | Condition | preparation sign `b` | `P_q` | terminal target error `P_r` | peak input | `C_prep` | max prep `|e_delta|` |
|---:|---|---:|---:|---:|---:|---:|---:|
| `+0.2` | PT | `+0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `+0.2` | PM | `-0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `-0.2` | PT | `-0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `-0.2` | PM | `+0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |

Both frozen budgets are respected with substantial margin; no budget was changed.

## 7. Targeted versus no-prep versus sign-mismatched comparison

For both future signs:

- `B0(a)=0.9999999999999682` relative to P0;
- `BM(a)=0.9999999999999841` relative to PM.

Frozen aggregates:

- `E_target_max = 2.076727044536923e-15`;
- `E_no_min = 0.06534774384334105`;
- `E_mismatch_min = 0.1307357122731585`;
- `B0_min = 0.9999999999999682`;
- `BM_min = 0.9999999999999841`;
- `H_target = 4.6079385647875116e-15`;
- maximum absolute relative angle over all preparation/evaluation trajectories `=0.16130400338475567`.

Thus the matched preparation drives the later representative response to numerical agreement with B1, while both P0 and the equal-cost sign-mismatched PM condition remain materially separated under the frozen primary metric.

## 8. Mechanical classifier audit

All mandatory sanity/regression checks pass before scientific classification.

| PASS condition | Observed | Result |
|---|---:|---|
| Safety `max|e_delta|<pi/2` | `0.16130400338475567 < 1.5707963267948966` | PASS |
| `E_target_max<=1e-8` | `2.076727044536923e-15` | PASS |
| `E_no_min>=1e-4` | `0.06534774384334105` | PASS |
| `E_mismatch_min>=1e-4` | `0.1307357122731585` | PASS |
| `B0_min>=0.90` | `0.9999999999999682` | PASS |
| `BM_min>=0.90` | `0.9999999999999841` | PASS |
| amplitude budget | `0.20881049376163438 <= 0.35` | PASS |
| energy budget | `0.04006381839386479 <= 0.25` | PASS |

Therefore the frozen hierarchy returns **PASS**. `WEAK`, `NULL`, and `FAIL` are not reached.

## 9. No-retuning declaration

After `GO`, no system, topology, `M,D,K`, initial state, macro, hidden coordinate, preparation path, preparation duration, inverse-dynamics formula, amplitude/energy budget, future disturbance sign/amplitude, P0/PT/PM condition, B1 target, horizon, integrator, resolution, tolerance, metric, classifier clause, target state, optimizer, feedback controller, neural model, domain, literature task, or manuscript task was changed or added.

No second preparation policy or parameter search was attempted.

## 10. Exact claim ceiling

Only the frozen benchmark statement in Section 1 is supported.

This result does **not** establish novelty, optimality, robustness to unknown interventions, generic power-grid benefit, generic controlled state preparation, a new causal-state formalism, learned causal coordinates, a new controlled-equivalence theorem, or established causal synergetics.

The literature freeze remains controlling: controlled state preparation has close prior art and any broader claim requires a separately authorised and specifically delimited comparison. The CORE freeze remains controlling: exact intervention-response sufficiency for full retained trajectories is structurally controlled closure/projectability and is not a new generic equivalence theory.

## 11. Code / test / result commits and CI state

- Implementation commit: `3d4b06f417b4d81cbeaa93f27683a1c799d426b4`.
- Test commit: `04765a8dac61f4f657659d2bde03f5ef76c307d5`.
- Result creation commit: `14c82045ee187f825d8340d93cd1bde34216f7d4`.
- Result metadata finalisation: this update commit; its SHA is available from Git history after the write completes.
- Local deterministic execution of the exact APP-C source/test contents: `5 passed`.
- Existing prior scientific source/test files were not modified; APP-C added only its new benchmark module and new test file before this result file.
- GitHub commit-status query on test commit `04765a8dac61f4f657659d2bde03f5ef76c307d5`: `statuses=[]`, `total_count=0`; aggregate state is `pending` only because no status contexts exist.
- GitHub Actions query on the same head: `total_count=0`, `workflow_runs=[]`.
- Therefore **no CI success is claimed or inferred**; no CI run/status exists for the tested head at query time.

STOP — RETURN TO MASTER
