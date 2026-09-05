# Power-Grid Minimal Benchmark 0.1

Status: EXECUTED / RESULT FROZEN
Assigned chat: `60 – APP-B – Power-Grid Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`
Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

## 1. Verdict

The frozen `Power-Grid Minimal Benchmark 0.1` is mechanically classified **PASS**.

> In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

No broader power-grid, novelty, controlled-equivalence, learned-coordinate, state-preparation, or field-level claim is authorised.

## 2. Exact frozen specification identifiers

Executed exactly:

- two identical nonlinear classical swing machines linked by one lossless line;
- normalized `M=D=K=1`;
- full state `(delta1,omega1,delta2,omega2)`;
- representative macro `q=(delta1,omega1)`;
- hidden coherency errors `(e_delta,e_omega)=(delta2-delta1,omega2-omega1)`;
- coherent initial states with common speeds `-0.1,0,+0.1` and zero angles;
- constant machine-2 interventions `u=0,+0.2,-0.2`;
- exactly one horizon `T=5`;
- deterministic NumPy float64 classical RK4;
- primary `dt=0.001`, audit `dt=0.0005`;
- B0 passive-slaving representative model;
- B1 coherent aggregate surrogate;
- C1 exact arithmetic-mean/COI closure control;
- frozen `PASS/WEAK/NULL/FAIL` hierarchy and thresholds.

No alternative topology, model, parameter, macro, state, intervention, amplitude, horizon, baseline, metric, threshold, or numerical method was tried.

## 3. Analytic coherency / controlled-invariance derivation

With `e_delta=delta2-delta1` and `e_omega=omega2-omega1`, the exact transverse dynamics are

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)+u`.

For `u=0`, `e_delta=e_omega=0` is invariant. Its transverse Jacobian is `[[0,1],[-2,-1]]` with eigenvalues `(-1 ± i sqrt(7))/2`, hence local exponential attraction.

On that manifold under a nonzero localized intervention,

`(e_delta_dot,e_omega_dot)=(0,u)`,

so controlled invariance is immediately lost. B0 nevertheless keeps the passive substitution and predicts `delta_dot=omega`, `omega_dot=-omega` with no direct `u` term. This is the frozen control-leakage witness.

For the arithmetic mean/COI coordinate,

`delta_mean=(delta1+delta2)/2`, `omega_mean=(omega1+omega2)/2`,

the antisymmetric line-power terms cancel exactly and

`delta_mean_dot=omega_mean`, `omega_mean_dot=-omega_mean+u/2`.

Thus B1 is exact for C1 although it is only approximate for the representative-machine macro.

## 4. Numerical sanity table

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| Constants/states/interventions | exact freeze | exact | PASS |
| Full trajectory count | `9` | `9` | PASS |
| Finite states | all finite | all finite | PASS |
| Primary/half-step convergence | `<=1e-8` | `8.1601392309949e-15` | PASS |
| Passive coherency | `<=1e-12` | `0` | PASS |
| Passive full representative vs B0 | `<=1e-10` | `0` | PASS |
| Mean/COI full vs B1 | `<=1e-10` | `3.88578058618805e-14` | PASS |
| Positive/negative odd symmetry | `<=1e-10` | `3.83026943495679e-14` | PASS |
| Controlled-invariance defect | `(0,u)` | exact float64 construction | PASS |
| New APP-B tests | pass | `5 passed` | PASS |
| Prior unchanged repository regression | pass unchanged | frozen predecessor reports `36 passed`; APP-B changed none of those prior source/test files | PASS |

The initial APP-B unit-test run produced one failure only because a standalone `q/r` transform assertion demanded exact binary equality for the decimal `0.7`; the assertion was changed to `atol=1e-15`. No scientific benchmark tolerance, equation, parameter, metric, or classifier was changed. The rerun was `5 passed`.

## 5. Full metric table

`d_inf` is the frozen full-trajectory max metric. `E_delta` and `E_omega` are componentwise macro errors. RMS is over both macro components and all primary-grid times. `H_delta/H_omega` are full-model coherency maxima.

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

## 6. B0 / B1 / C1 comparison

Frozen summary metrics:

- `E_pass = 0`;
- `E_B0_min = 0.3549858420076152`;
- `E_B1_min = 0.06534774384333092`;
- `H_delta = 0.13069548768668177`;
- maximum controlled `|e_omega| = 0.08954202393695339`;
- mean/COI closure error `=3.885780586188048e-14`;
- maximum primary/half-step discrepancy `=8.1601392309949e-15`.

B0 is exact passively and materially wrong under both localized step signs. B1 is much closer to the representative machine than B0 but still exceeds the frozen `1e-4` mismatch floor by more than two orders of magnitude. C1 confirms that the same B1 dynamics is an exact low-dimensional closure for the true mean/COI coordinate.

The exact identities `delta1-delta_mean=-e_delta/2` and `omega1-omega_mean=-e_omega/2` are reflected numerically by the B1 component errors being one half of the coherency errors.

## 7. Mechanical classification audit

All mandatory sanity checks pass.

| PASS condition | Observed | Result |
|---|---:|---|
| `H_delta < pi/2` | `0.13069548768668177 < 1.5707963267948966` | PASS |
| `E_pass <= 1e-10` | `0` | PASS |
| `E_B0_min >= 1e-4` | `0.3549858420076152` | PASS |
| `E_B1_min >= 1e-4` | `0.06534774384333092` | PASS |

Therefore the frozen classifier returns **PASS**. WEAK and NULL are not reached; FAIL is not reached.

## 8. No-retuning declaration

After `GO`, no model class, topology, parameter, macro/hidden map, initial state, intervention bus, amplitude, sign pair, horizon, integrator, resolution, baseline, control, response functional, metric, physical-admissibility bound, threshold, or claim ceiling was changed.

No second grid, fault, macro, amplitude, horizon, learned coordinate, state-preparation experiment, literature task, or manuscript work was attempted.

## 9. Claim ceiling

The result supports only the frozen statement in Section 1.

It does **not** support novelty; generic power-grid transfer or generic power-grid insufficiency; a new controlled-equivalence or causal-state concept; failure of all low-dimensional grid aggregates; uniqueness or optimality of the representative-machine macro; learned-coordinate claims; controlled state preparation; or established causal synergetics.

The exact mean/COI closure is a mandatory counterexample to any claim that all two-dimensional grid aggregates fail.

## 10. Code / test / result commits and CI state

- Implementation commit: `a98c9447aa50b6bb8974b2522543d72784be24ce`.
- Test commit: `5774dac821fc3d4878feee32a4fe13b7553abe33`.
- Result creation commit: `c0c24c2a3266eb69daaa12340e8b7dc68248956f`.
- APP-B status update commit: `c27d359350e64e90b759e088df2205172d60d276`.
- Result metadata finalisation: this update commit; its SHA is available from Git history after the write completes.
- Local new-test execution: `5 passed`.
- Prior unchanged regression evidence: `36 passed` in the preceding frozen APP-A result; none of those prior source/test files was modified by APP-B.
- GitHub commit-status query for `c27d359350e64e90b759e088df2205172d60d276`: `statuses=[]`, `total_count=0`; the aggregate endpoint reports `state="pending"` because there are no status contexts.
- GitHub Actions query for the same head SHA: `total_count=0`, `workflow_runs=[]`.
- Therefore **no CI success is claimed or inferred**; no CI run/status exists for this commit at query time.

STOP — RETURN TO MASTER
