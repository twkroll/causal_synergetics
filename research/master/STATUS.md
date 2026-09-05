# STATUS — 00 – MASTER – Projektplan & Status

Current Gate: `Post-Power-Grid-Specification Integration / Power-Grid Minimal Benchmark 0.1`
Status: COMPLETE / WAIT FOR APP-B
Latest canonical file: `research/master/project_status.md`
Dependencies: `Power-Grid Minimal Benchmark Feasibility & Specification Gate 0.1` COMPLETE / SPECIFICATION FROZEN
Specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`
Decision: `SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION`
Latest rollback point: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`
Next instruction: User opens/returns to `60 – APP-B – Power-Grid Minimalbenchmark` and enters exactly `GO`; APP-B must execute only `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`.
STOP boundary: MASTER must not execute the power-grid benchmark itself, alter the frozen topology/model/parameters/macro/interventions/horizon/numerics/baselines/metrics/thresholds, reopen parked APP-A response-coordinate work, or open state-preparation/literature/manuscript/other-domain work before APP-B returns.

## Freeze state

- Governance: FROZEN v0.1
- Prior-art audit: FROZEN / PASS — CLAIM-RESTRICTED
- CORE boundary: FROZEN / PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION
- Neural Minimal Benchmark 0.1: FROZEN / PASS
- Neural Historical Reachability 0.1: FROZEN / PASS
- Neural Nonlinear ReLU Pilot 0.1: FROZEN / PASS
- Neural Response Coordinate Pilot 0.1: FROZEN / WEAK
- Neural Response Coordinate Nuisance-Invariance Pilot 0.1: FROZEN / FAIL — SPECIFICATION CLASSIFICATION GAP
- Neural Response Coordinate direction: FROZEN / STOP — PARKED
- Power-Grid Minimal Benchmark Specification 0.1: FROZEN / APP-B READY
- Latest rollback point: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`

## Frozen power-grid specification

Exactly one candidate is authorised:

- two identical nonlinear classical swing machines coupled by one lossless tie line;
- normalized `M=D=K=1`;
- microstate `(delta1,omega1,delta2,omega2)`;
- pre-declared representative macro `q=(delta1,omega1)`;
- hidden coherency error `(e_delta,e_omega)`;
- passive synchronisation manifold `e_delta=e_omega=0`, locally exponentially attracting for `u=0`;
- local intervention applied only to machine 2 with frozen constant values `u=0,+0.2,-0.2`;
- three coherent initial speeds `-0.1,0,+0.1`;
- one horizon `T=5`, fixed from five damping time constants;
- deterministic NumPy float64 RK4 with `dt=0.001` and convergence audit `dt=0.0005`;
- B0 passive-slaving representative model;
- B1 coherent aggregate surrogate;
- exact mean/COI closure as mandatory strong control;
- exhaustive PASS/WEAK/NULL/FAIL rules frozen before execution.

The exact structural witness is already model-level: a nonzero local intervention gives `(e_delta_dot,e_omega_dot)=(0,u)` on the passive synchronisation manifold and therefore destroys controlled invariance. Numerical execution is authorised only to validate and quantify the frozen finite-horizon benchmark under the frozen physical-admissibility and comparator criteria.

No trajectory or effect magnitude was inspected during specification.

## Claim ceiling

No novelty promotion is authorised.

No power-grid result exists yet. The project may state only that a two-machine cross-domain benchmark has been pre-specified. It may not claim cross-domain replication, generic power-grid insufficiency, new controlled equivalence, generally useful causal coordinates, controlled state preparation, or established causal synergetics.

Even a future PASS is restricted to the representative-machine macro in this exact normalized two-machine system. The exact mean/COI control remains a successful low-dimensional closure and blocks any claim that all power-grid aggregates fail.

## Branch state

- 00 – MASTER: COMPLETE / WAIT FOR APP-B
- 10 – CORE: COMPLETE / FROZEN / WAIT
- 20/30/40 – THEORY-*`: UNOPENED
- 50 – APP-A: PARKED / FROZEN / WAIT
- 60 – APP-B: READY / AWAIT GO — Power-Grid Minimal Benchmark 0.1
- 70 – APP-C: UNOPENED
- 80 – LIT: COMPLETE / FROZEN / WAIT
- 90 – MANUSCRIPT: UNOPENED

## Active blocker

Operational only: APP-B has not yet executed the frozen power-grid benchmark.

## Return protocol

After APP-B reaches `STOP — RETURN TO MASTER`, return here and enter:

`Status?`

STOP — WAIT
