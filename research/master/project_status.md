# Project Status — causal_synergetics

Version: 1.5
Date: 2026-09-05
Overall status: POWER-GRID SPECIFICATION FROZEN / APP-B READY / RESPONSE-COORDINATE DIRECTION PARKED
Governance status: FROZEN v0.1
Latest rollback point: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an established theory.

## Frozen scientific chain

- `Prior-Art & Definitions Audit 0.1`: PASS — CLAIM-RESTRICTED / RESTRICT / REINTERPRET.
- `CORE Synergetic Sufficiency Boundary 0.1`: PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION.
- `Neural Minimal Benchmark 0.1`: PASS — RESULT FROZEN.
- `Neural Historical Reachability 0.1`: PASS — RESULT FROZEN.
- `Neural Nonlinear ReLU Pilot 0.1`: PASS — RESULT FROZEN.
- `Neural Response Coordinate Pilot 0.1`: WEAK — RESULT FROZEN.
- `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`: FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP.
- `Neural Response Coordinate Nuisance-Invariance FAIL Integration Gate 0.1`: STOP / PARK RESPONSE-COORDINATE DIRECTION.
- `Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1`: **SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION**.

All prior claim ceilings remain controlling.

## Frozen neural conclusion

The neural response-coordinate/null/nuisance direction remains parked under `RP-013`. It may not be reopened to repair or relabel the frozen WEAK/FAIL results.

The earlier exact neural minimal/history/ReLU results remain independently frozen and valid only within their respective claim ceilings.

## Branch-independent scientific base

The strongest branch-independent result remains the CORE controlled-ODE boundary:

- passive/unforced slaving alone does not imply intervention-relative response sufficiency;
- exact full-trajectory fibre response homogeneity is controlled projectability/closure under the frozen response definition;
- the CORE includes an explicit control-leakage counterexample and finite-horizon mismatch bounds;
- these results are structurally prior-art/subsumed and support no generic novelty claim.

## Frozen power-grid specification

Canonical memo:

`research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`.

Execution prompt:

`research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`.

Exactly one physically distinct candidate is frozen before execution:

- two identical nonlinear classical swing machines coupled by one lossless tie line;
- normalized `M=D=K=1`;
- microstate `(delta1,omega1,delta2,omega2)`;
- pre-declared representative-machine macro `q=(delta1,omega1)`;
- hidden coherency errors `(e_delta,e_omega)`;
- unforced synchronisation manifold `e_delta=e_omega=0`, locally exponentially attracting;
- three coherent initial conditions with common speed `-0.1,0,+0.1`;
- constant local interventions on machine 2 only: `u=0,+0.2,-0.2`;
- one horizon `T=5`, fixed as five normalized damping time constants;
- deterministic NumPy float64 RK4, primary `dt=0.001`, convergence audit `dt=0.0005`;
- B0 passive-slaving representative model;
- B1 standard coherent aggregate surrogate;
- exact mean/COI closure as a mandatory fairness control;
- frozen trajectory metrics, physical-admissibility constraint, and exhaustive PASS/WEAK/NULL/FAIL classifier.

The choice `|u|=0.2` is frozen from model structure rather than inspected performance: the forced relative equilibrium satisfies `2 sin(e_delta*)=u`, so `|u|=0.2` is one tenth of the normalized existence limit `|u|<2` for the near-synchronous branch.

## Exact structural witness already frozen

In coherency coordinates,

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)+u`.

On the passive synchronisation manifold, a nonzero local input gives

`(e_delta_dot,e_omega_dot)=(0,u)`.

Thus the frozen intervention violates controlled invariance of the passive slaving/coherency manifold by construction. Starting from synchronous equilibrium, the representative-machine frequency has the exact local Taylor witness `omega1'''(0)=u`, whereas B0 has no controlled response term.

This is not yet counted as an empirical power-grid result. APP-B must execute and mechanically classify the full frozen finite-horizon benchmark.

## Fairness / claim control

The arithmetic mean/COI coordinate is exactly closed for the identical-machine model:

`delta_mean_dot=omega_mean`,

`omega_mean_dot=-omega_mean+u/2`.

Therefore a future PASS can only establish insufficiency of the pre-declared representative-machine coherent macro under a localized hidden-machine step. It cannot establish failure of all low-dimensional grid reductions.

## Active branch

`60 – APP-B – Power-Grid Minimalbenchmark`

Current gate: `Power-Grid Minimal Benchmark 0.1`.
Status: READY / AWAIT GO.

APP-B must execute only the frozen prompt and return without retuning.

## Waiting / parked branches

- `00 – MASTER`: COMPLETE / WAIT FOR APP-B.
- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: PARKED / FROZEN / WAIT.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `70 – APP-C`: UNOPENED.
- `90 – MANUSCRIPT`: UNOPENED.
- controlled state preparation: BLOCKED.
- new literature positioning: BLOCKED.
- broader neural scaling / realistic histories / LoRA: BLOCKED.

## Freeze check

OK.

`RP-014` freezes the power-grid topology, model equations, normalized parameters, macro/hidden map, initial states, intervention location/amplitude/sign pair, horizon, numerical method/resolution, B0/B1/C1 controls, metrics, physical-admissibility condition, thresholds, claim ceiling, and no-retuning rule before execution.

No second topology, fault, macro, amplitude, or horizon may be tried after a WEAK/NULL/FAIL result inside benchmark 0.1.

## Branching check

OK.

Exactly one scientific execution is authorised: the frozen APP-B minimal benchmark. APP-A remains parked.

## Rollback

Latest stable savepoint:

`RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`.

Any APP-B PASS/WEAK/NULL/FAIL return is frozen and integrated by MASTER rather than repaired in-place.

## Current claim ceiling

No empirical power-grid or cross-domain replication claim exists yet.

The project may state the exact frozen LIT/CORE/neural findings plus the fact that one power-grid benchmark has been prospectively specified.

It may not claim:

- generic power-grid intervention insufficiency;
- generic cross-domain transfer;
- a new state-equivalence or causal-state formalism;
- a generally useful learned causal/plasticity coordinate;
- controlled state preparation as established capability;
- field-level causal-synergetics novelty.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. The last executed APP-A suite remains frozen at `36 passed`; current power-grid changes are specification/governance only.

## Next global step

Open/return to:

`60 – APP-B – Power-Grid Minimalbenchmark`

and enter exactly:

`GO`

After APP-B reaches `STOP — RETURN TO MASTER`, return to MASTER and enter:

`Status?`
