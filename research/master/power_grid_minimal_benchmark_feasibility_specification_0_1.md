# Power-Grid Minimal Benchmark Feasibility & Specification 0.1

Status: COMPLETE / SPECIFICATION FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-05
Dependency: `RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1`
Decision: **SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION**

## 1. Executive decision

A scientifically neutral minimal power-system benchmark can be fixed without topology search, parameter tuning, learned coordinates, or effect inspection.

The benchmark is the canonical two-machine classical swing system: two identical synchronous-machine rotors coupled by one lossless tie line in normalized per-unit coordinates. The pre-declared passive macro is the state of machine 1 used as the representative of a perfectly coherent two-machine group. The hidden variables are the machine-2 minus machine-1 coherency errors.

For zero intervention, the exact synchronisation manifold is invariant and locally exponentially attracting. On that manifold, the representative-machine macro obeys an exact two-dimensional passive reduced model. A frozen local mechanical-power step applied only to machine 2 is then used as the intervention. This input directly violates controlled invariance of the synchronisation manifold, so the full representative-machine trajectory need not follow the naive controlled extension of the passive reduction.

The benchmark therefore transfers the already frozen CORE mechanism `control leakage out of an unforced slaving manifold` into a physically distinct controlled ODE setting. It does not test a new state-equivalence concept and does not reopen the parked neural response-coordinate direction.

A strong fairness control is mandatory: the true arithmetic-mean/COI coordinate of the two identical machines is exactly closed under the same local input and is predicted by the standard coherent aggregate model. Therefore even a future PASS can only establish failure of the pre-declared representative-machine coherent reduction under localized intervention, not failure of all low-dimensional power-system aggregates.

No benchmark trajectory or effect magnitude was inspected during this specification gate.

## 2. Frozen physical model

Use exactly two classical second-order synchronous-machine swing equations coupled by one lossless line.

Full microstate:

`x=(delta1, omega1, delta2, omega2)`.

Angles are rotor electrical angles relative to the synchronous rotating reference; frequencies are normalized rotor-speed deviations.

Use normalized per-unit/time conventions:

- inertia `M=1` for both machines;
- damping `D=1` for both machines;
- tie-line coupling `K=1`;
- nominal mechanical/electrical balance is absorbed into the synchronous reference, so the nominal offsets are zero.

The exact full nonlinear equations are

`delta1_dot = omega1`,

`omega1_dot = -omega1 + sin(delta2-delta1)`,

`delta2_dot = omega2`,

`omega2_dot = -omega2 + sin(delta1-delta2) + u(t)`.

Here `u(t)` is a normalized controllable mechanical-power/injection perturbation applied only to machine 2.

No alternative topology, machine count, inertia, damping, coupling, operating point, voltage model, governor model, load model, or linearisation is allowed in benchmark 0.1.

## 3. Frozen macro/hidden decomposition

Pre-declare the representative-machine macro

`q=(delta1, omega1)`.

Define hidden coherency coordinates

`r=(e_delta,e_omega)`

with

`e_delta=delta2-delta1`,

`e_omega=omega2-omega1`.

In `(q,r)` coordinates the exact dynamics are

`delta1_dot = omega1`,

`omega1_dot = -omega1 + sin(e_delta)`,

`e_delta_dot = e_omega`,

`e_omega_dot = -e_omega - 2 sin(e_delta) + u(t)`.

Thus the benchmark aligns directly with the frozen CORE notation `q_dot=f(q,r,u)`, `r_dot=g(q,r,u)` without introducing a new terminology or equivalence notion.

## 4. Frozen passive slaving/coherency structure

Define the synchronisation/coherency manifold

`M_sync={e_delta=0,e_omega=0}`.

For `u=0`, `M_sync` is exactly invariant. On it,

`delta1_dot=omega1`,

`omega1_dot=-omega1`.

This is the frozen passive reduced model.

The transverse unforced dynamics are

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)`.

The transverse Jacobian at synchrony is

`[[0,1],[-2,-1]]`,

whose eigenvalues are

`(-1 ± i sqrt(7))/2`.

Hence `M_sync` is locally exponentially attracting around the synchronous operating region.

The benchmark does not claim global attraction and does not call this manifold a novel order parameter construction.

## 5. Exact controlled-invariance witness

On `M_sync`, under a nonzero local intervention,

`e_delta_dot=0`,

`e_omega_dot=u`.

Therefore every frozen nonzero step immediately violates controlled invariance of the passive synchronisation manifold.

The naive controlled extension obtained by substituting `r=0` into the representative-machine projected dynamics contains no direct `u` term:

`delta_B0_dot=omega_B0`,

`omega_B0_dot=-omega_B0`.

Starting from the synchronous equilibrium and applying constant `u=a`, the exact local Taylor witness is

`omega1'(0)=0`,

`omega1''(0)=0`,

`omega1'''(0)=a`.

Thus the full representative-machine frequency cannot remain identical to B0 for any nonzero `a` over a nonzero time interval. This structural fact is derived from the frozen equations, not selected from a numerical effect size.

This is specifically a `control-leakage / graph-controlled-invariance` witness. The benchmark does not claim global fibre sufficiency of `q`; off `M_sync`, the unforced projected vector field already depends on `e_delta`.

## 6. Frozen intervention family

Use exactly three intervention conditions:

- passive control: `u0(t)=0`;
- positive local step: `u+(t)=+0.2`;
- negative local step: `u-(t)=-0.2`.

Each intervention is constant for the full horizon.

The two nonzero signs are a symmetry pair, not an amplitude sweep.

No pulse duration, alternative amplitude, alternative intervention bus, topology change, fault, or control waveform may be added after execution begins.

## 7. Frozen horizon and initial states

Use exactly one horizon:

`T=5.0` normalized time units.

Use exactly three coherent initial conditions, all on `M_sync`:

- `I_minus`: `delta1=delta2=0`, `omega1=omega2=-0.1`;
- `I_zero`: `delta1=delta2=0`, `omega1=omega2=0`;
- `I_plus`: `delta1=delta2=0`, `omega1=omega2=+0.1`.

These provide a deterministic small coherent operating set and are chosen symmetrically around the synchronous equilibrium.

No off-manifold same-macro/different-hidden pair is used in benchmark 0.1. The primary mechanism is intervention-induced departure from an exactly coherent initial state, not fibre-memory comparison.

Physical-admissibility condition for the intended coherent regime:

`max_t |e_delta(t)| < pi/2`

for every controlled trajectory. Violation is a scientific NULL condition, not a numerical implementation FAIL.

## 8. Frozen response functional

The primary response is the complete representative-machine macro trajectory

`Gamma(x0,u)=q(t)=(delta1(t),omega1(t))`, `t in [0,T]`.

Use the normalized trajectory max metric

`d_inf(q_a,q_b)=max_t max(|delta_a-delta_b|, |omega_a-omega_b|)`.

Also report componentwise maxima

`E_delta=max_t |delta_a-delta_b|`,

`E_omega=max_t |omega_a-delta_b*0-omega_b|`,

where the second expression means simply `max_t |omega_a-omega_b|`.

Report trajectory RMS error as a secondary descriptive metric. No scalar post-hoc observable may replace the frozen full `q(t)` response.

## 9. Frozen baselines and controls

### B0 — passive-slaving representative model

Use the exact unforced reduction on `M_sync` as the naive controlled extension:

`delta_dot=omega`,

`omega_dot=-omega`.

The hidden-machine input `u` has no direct term after substituting `r=0` into the projected `q` vector field.

B0 is the primary sufficiency diagnostic.

### B1 — standard coherent aggregate surrogate

Use a single equivalent two-machine coherent aggregate with total inertia `2M`, total damping `2D`, and total applied disturbance `u`:

`delta_eq_dot=omega_eq`,

`2 omega_eq_dot=-2 omega_eq+u`,

or equivalently

`omega_eq_dot=-omega_eq+u/2`.

For prediction of the representative machine, B1 uses `(delta_eq,omega_eq)` as the coherent-group approximation to `(delta1,omega1)`.

B1 is a mandatory physically informed fairness baseline.

### C0 — full nonlinear two-machine model

The full four-state equations are the reference truth.

### C1 — exact mean/COI closure control

Define

`delta_mean=(delta1+delta2)/2`,

`omega_mean=(omega1+omega2)/2`.

For the frozen identical-machine model, antisymmetric line power cancels exactly and

`delta_mean_dot=omega_mean`,

`omega_mean_dot=-omega_mean+u/2`.

Thus B1 is an exact closed model for the mean coordinate even though it is only an approximation to the representative-machine macro `q` under localized intervention.

This control is mandatory. It prevents any future claim that all two-dimensional grid aggregates fail or that response measurements are required to construct an adequate aggregate.

## 10. Frozen numerical method

Use only NumPy float64 and a deterministic fixed-step classical RK4 integrator implemented in-project.

Primary resolution:

- `dt=0.001`;
- uniform grid `t_n=n*dt` from `0` through `5.0` inclusive;
- exactly `5000` RK4 steps.

Convergence audit:

- repeat every full-model and baseline trajectory at `dt=0.0005`;
- compare the half-step solution at every second fine step to the primary grid;
- maximum state-component discrepancy must be `<=1e-8`.

No adaptive solver, tolerance tuning, alternative integrator, or post-result resolution change is allowed in benchmark 0.1.

## 11. Frozen mandatory numerical/sanity checks

All of the following must pass before scientific classification:

1. exact model constants `M=D=K=1`, `T=5`, amplitudes `0,±0.2`, and the three frozen initial states;
2. exactly nine full trajectories (`3 initial states x 3 interventions`) plus corresponding B0/B1 trajectories;
3. all state values finite at both resolutions;
4. primary/half-step convergence max error `<=1e-8` across all full and baseline trajectories;
5. for every passive trajectory, `max_t max(|e_delta|,|e_omega|)<=1e-12`;
6. passive full representative trajectory versus B0 `d_inf<=1e-10` for all three initial states;
7. exact mean/COI full trajectory versus B1 `d_inf<=1e-10` for all initial states and all three interventions;
8. positive/negative controlled increments satisfy odd sign symmetry within `1e-10` for every initial state;
9. the exact controlled-invariance defect on `M_sync` evaluates to `(e_delta_dot,e_omega_dot)=(0,u)`;
10. all frozen APP-B tests pass and all existing repository tests remain unchanged and pass.

If any mandatory check fails, classification is `FAIL` rather than scientific WEAK/NULL.

## 12. Frozen scientific metrics

Define

`E_pass = max over initial states d_inf(q_full(u0), q_B0(u0))`.

For the nonzero steps define

`E_B0_min = min over initial states and signs d_inf(q_full(u±), q_B0(u±))`.

`E_B1_min = min over initial states and signs d_inf(q_full(u±), q_B1(u±))`.

Define

`H_delta = max over controlled trajectories and time |e_delta(t)|`.

Also report:

- `E_B0` and `E_B1` for every initial-state/sign pair;
- componentwise `E_delta`, `E_omega`;
- RMS trajectory errors;
- maximum coherency frequency error `max |e_omega|`;
- exact mean/COI closure error;
- primary-versus-half-step convergence error.

No metric may be substituted after execution.

## 13. Exhaustive frozen classification

Apply the following hierarchy only after all mandatory numerical/sanity checks pass.

### PASS

All of:

- physical-admissibility condition `H_delta < pi/2`;
- `E_pass <= 1e-10`;
- `E_B0_min >= 1e-4`;
- `E_B1_min >= 1e-4`.

Interpretation ceiling:

> In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

### WEAK

All mandatory sanity checks pass, `H_delta < pi/2`, `E_pass <=1e-8`, and

`min(E_B0_min,E_B1_min) > 1e-10`,

but the full PASS conditions are not all met.

Interpretation ceiling: the control-induced mismatch is detectable but below the frozen materiality floor for at least one primary comparator or passive adequacy is only numerically approximate at the weaker tolerance.

### NULL

All mandatory sanity checks pass but neither PASS nor WEAK applies.

This includes any of:

- departure from the intended coherent regime (`H_delta >= pi/2`);
- passive representative reduction not adequate at the frozen weak tolerance (`E_pass >1e-8`);
- no controlled mismatch above numerical scale against at least one required comparator.

NULL is a valid scientific result and may not trigger candidate replacement.

### FAIL

One or more mandatory numerical/sanity checks fail, including implementation, convergence, mean-closure, symmetry, or regression checks.

These four classes are ordered, disjoint, and exhaustive.

## 14. Anti-retuning freeze

After APP-B receives `GO`, do not change:

- model class or topology;
- `M,D,K`;
- macro/hidden map;
- coherent manifold;
- operating point;
- initial states;
- intervention location, sign pair or amplitude;
- horizon;
- RK4 method or time steps;
- B0/B1/C1 definitions;
- metrics;
- materiality thresholds;
- physical-admissibility bound;
- claim ceiling.

If the result is WEAK, NULL, or FAIL, APP-B must freeze it and return to MASTER. No second grid, fault, amplitude, macro, or horizon may be tried inside benchmark 0.1.

## 15. Claim ceiling

For every outcome:

- no novelty promotion;
- no new controlled-equivalence or causal-state claim;
- no claim that power grids generically exhibit intervention-insufficient macrostates;
- no claim that the representative machine is a unique or optimal macro;
- no learned-coordinate claim;
- no state-preparation claim;
- no field-level `causal synergetics` claim.

A PASS supports only the exact frozen cross-domain statement in Section 13.

A WEAK supports only detectable but sub-threshold mismatch in this frozen model.

A NULL means this single predeclared power-grid candidate did not meet the frozen transfer criterion and must remain visible.

A FAIL means the execution/specification could not be validated and must not be converted into a scientific NULL or PASS.

## 16. Gate outcome

This specification is scientifically neutral, minimal, deterministic, physically interpretable, and tied directly to the frozen CORE mechanism without effect-guided search.

Decision:

**SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION**

Rollback recommendation:

`RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`.
