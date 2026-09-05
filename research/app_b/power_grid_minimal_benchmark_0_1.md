# Power-Grid Minimal Benchmark 0.1

Status: EXECUTED / RESULT FROZEN
Assigned chat: `60 – APP-B – Power-Grid Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

## 1. Verdict

The frozen `Power-Grid Minimal Benchmark 0.1` is classified **PASS** under the pre-declared hierarchy.

In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

No broader power-grid, novelty, controlled-equivalence, learned-coordinate, state-preparation, or field-level claim is authorised.

## 2. Frozen specification identifiers

Executed exactly:

- two identical nonlinear swing machines with one lossless tie line;
- `M=D=K=1`;
- state `(delta1,omega1,delta2,omega2)`;
- macro `q=(delta1,omega1)`;
- hidden errors `(e_delta,e_omega)=(delta2-delta1,omega2-omega1)`;
- coherent initial speeds `-0.1,0,+0.1` at zero angles;
- constant machine-2 interventions `u=0,+0.2,-0.2`;
- horizon `T=5`;
- deterministic NumPy float64 classical RK4;
- primary `dt=0.001`, convergence audit `dt=0.0005`;
- B0 passive-slaving representative model;
- B1 coherent aggregate surrogate;
- C1 exact arithmetic-mean/COI closure control;
- frozen `PASS/WEAK/NULL/FAIL` thresholds.

No alternative topology, model, macro, state, intervention, amplitude, horizon, baseline, metric, threshold, or numerical method was tried.

## 3. Analytic coherency and controlled-invariance derivation

With

`e_delta=delta2-delta1`,

`e_omega=omega2-omega1`,

the exact transverse dynamics are

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)+u`.

For `u=0`, the synchronisation manifold `e_delta=e_omega=0` is exactly invariant. The transverse Jacobian at synchrony is

`[[0,1],[-2,-1]]`,

with eigenvalues `(-1 ± i sqrt(7))/2`, hence local exponential attraction.

On the manifold under a nonzero localized intervention,

`(e_delta_dot,e_omega_dot)=(0,u)`.

Thus controlled invariance is destroyed immediately for `u!=0`. B0 nevertheless keeps the passive slaving substitution and therefore predicts

`delta_dot=omega`, `omega_dot=-omega`,

with no direct `u` term. This is the pre-declared control-leakage witness.

For the exact arithmetic mean,

`delta_mean=(delta1+delta2)/2`,

`omega_mean=(omega1+omega2)/2`,

the line-power terms cancel exactly and

`delta_mean_dot=omega_mean`,

`omega_mean_dot=-omega_mean+u/2`.

Therefore B1 is exact for the mean/COI coordinate while only approximate for the representative-machine macro.

## 4. Numerical sanity table

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| Constants/states/interventions | exact freeze | exact | PASS |
| Full trajectory count | `9` | `9` | PASS |
| Finite states | all finite | all finite | PASS |
| Primary vs half-step max error | `<=1e-8` | `8.1601392309949e-15` | PASS |
| Passive coherency max error | `<=1e-12` | `0` | PASS |
| Passive full representative vs B0 | `<=1e-10` | `0` | PASS |
| Mean/COI full vs B1 | `<=1e-10` | `3.88578058618805e-14` | PASS |
| Odd sign symmetry | `<=1e-10` | `3.83026943495679e-14` | PASS |
| Controlled-invariance defect | `(0,u)` | exact float64 construction | PASS |
| APP-B tests | pass | `5 passed` | PASS |
| Prior unchanged repository regression | pass unchanged | prior frozen execution `36 passed`; no prior source/test file modified | PASS |

The pre-existing regression evidence is recorded in the immediately preceding frozen APP-A result. APP-B commits are additive only: one new benchmark module and one new test file.

## 5. Full metric table

`B0/B1 d_inf` is the frozen trajectory max metric. `E_delta`, `E_omega` are componentwise maxima; RMS is over both macro components and all primary-grid times. `H_delta/H_omega` are coherency maxima for the full trajectory.

| Initial | Intervention | B0 d_inf | B0 E_delta | B0 E_omega | B0 RMS | B1 d_inf | B1 E_delta | B1 E_omega | B1 RMS | H_delta | H_omega |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| I_minus | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_minus | u_plus | 0.354985842007617 | 0.354985842007617 | 0.110139531935133 | 0.13350745641446 | 0.0653477438433406 | 0.0653477438433406 | 0.0447710119684765 | 0.03809399399337 | 0.130695487686682 | 0.0895420239369532 |
| I_minus | u_minus | 0.354985842007616 | 0.354985842007616 | 0.110139531935133 | 0.133507456414459 | 0.0653477438433309 | 0.0653477438433309 | 0.0447710119684767 | 0.0380939939933611 | 0.130695487686681 | 0.0895420239369534 |
| I_zero | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_zero | u_plus | 0.354985842007615 | 0.354985842007615 | 0.110139531935133 | 0.133507456414459 | 0.065347743843341 | 0.065347743843341 | 0.0447710119684767 | 0.0380939939933706 | 0.130695487686682 | 0.0895420239369532 |
| I_zero | u_minus | 0.354985842007615 | 0.354985842007615 | 0.110139531935133 | 0.133507456414459 | 0.065347743843341 | 0.065347743843341 | 0.0447710119684767 | 0.0380939939933706 | 0.130695487686682 | 0.0895420239369532 |
| I_plus | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_plus | u_plus | 0.354985842007616 | 0.354985842007616 | 0.110139531935133 | 0.133507456414459 | 0.0653477438433309 | 0.0653477438433309 | 0.0447710119684767 | 0.0380939939933611 | 0.130695487686681 | 0.0895420239369534 |
| I_plus | u_minus | 0.354985842007617 | 0.354985842007617 | 0.110139531935133 | 0.13350745641446 | 0.0653477438433406 | 0.0653477438433406 | 0.0447710119684765 | 0.03809399399337 | 0.130695487686682 | 0.0895420239369532 |

## 6. B0/B1/C1 comparison

Frozen summary metrics:

- `E_pass = 0`;
- `E_B0_min = 0.3549858420076152`;
- `E_B1_min = 0.06534774384333092`;
- `H_delta = 0.13069548768668177`;
- maximum controlled `|e_omega| = 0.08954202393695339`;
- exact mean/COI closure numerical error `=3.885780586188048e-14`;
- maximum primary/half-step discrepancy `=8.1601392309949e-15`.

B0 is exact passively and materially wrong under both localized step signs. B1 is substantially closer to the representative machine than B0 but still exceeds the frozen `1e-4` mismatch floor by more than two orders of magnitude. C1 confirms that this B1 dynamics is nevertheless an exact low-dimensional closure for the true mean/COI coordinate.

The identities

`delta1-delta_mean=-e_delta/2`,

`omega1-omega_mean=-e_omega/2`

are numerically reflected by the B1 componentwise errors being one half of the coherency errors.

## 7. Mechanical classification audit

All mandatory sanity checks pass.

PASS conditions:

| Condition | Observed | Result |
|---|---:|---|
| `H_delta < pi/2` | `0.13069548768668177 < 1.5707963267948966` | PASS |
| `E_pass <= 1e-10` | `0` | PASS |
| `E_B0_min >= 1e-4` | `0.3549858420076152` | PASS |
| `E_B1_min >= 1e-4` | `0.06534774384333092` | PASS |

Therefore the frozen classifier returns:

**PASS**.

WEAK and NULL are not reached. FAIL is not reached because the mandatory numerical and regression checks pass.

## 8. No-retuning declaration

After `GO`, no model class, topology, parameter, macro/hidden map, initial state, intervention bus, amplitude, sign pair, horizon, integrator, resolution, baseline, control, response functional, metric, physical-admissibility bound, threshold, or claim ceiling was changed.

The only implementation correction during testing was changing a unit-test assertion tolerance for the standalone coordinate transform from exact binary equality to `atol=1e-15`; this did not alter any scientific object or benchmark tolerance.

No second grid, fault, macro, amplitude, horizon, learned coordinate, state-preparation experiment, or literature task was attempted.

## 9. Claim ceiling

The result supports only the frozen statement in Section 1.

Do not claim:

- novelty;
- generic power-grid transfer or generic power-grid insufficiency;
- a new controlled-equivalence or causal-state concept;
- that all low-dimensional grid aggregates fail;
- that the representative-machine macro is unique or optimal;
- learned coordinates;
- controlled state preparation;
- established causal synergetics.

The exact mean/COI closure is a mandatory counterweight to any such overclaim.

## 10. Code, tests, result and CI state

- Implementation commit: `a98c9447aa50b6bb8974b2522543d72784be24ce`.
- Test commit: `5774dac821fc3d4878feee32a4fe13b7553abe33`.
- Local APP-B test execution: `5 passed`.
- Prior unchanged regression evidence: `36 passed` in the preceding frozen APP-A execution; APP-B modified none of those files.
- Result file creation commit: recorded by Git after this file is created.
- Status update commit: recorded after `research/app_b/STATUS.md` is updated.
- GitHub commit-status/CI state: queried after result/status commits; no CI success is inferred locally.

STOP — RETURN TO MASTER
