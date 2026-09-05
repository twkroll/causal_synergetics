# STATUS — 60 – APP-B – Power-Grid Minimalbenchmark

Current Gate: `Power-Grid Minimal Benchmark 0.1`
Status: READY / AWAIT GO
Latest canonical specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`
Dependency: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`
MASTER decision: `SPECIFICATION FROZEN / APP-B READY / NO NOVELTY PROMOTION`
Next instruction: On exact user command `GO`, read governance, this STATUS, the frozen specification, CORE result, literature freeze, and execution prompt; then execute only `Power-Grid Minimal Benchmark 0.1`.
STOP boundary: Do not change topology, model, parameters, macro map, initial states, intervention bus/amplitude/sign pair, horizon, numerical method/resolution, baselines, metrics, thresholds, or claim ceiling; do not try a second grid, fault, macro, amplitude, horizon, learned coordinate, state-preparation experiment, literature task, or manuscript work without new MASTER authorisation.

## Frozen benchmark

- two identical nonlinear classical swing machines linked by one lossless line;
- normalized `M=D=K=1`;
- full state `(delta1,omega1,delta2,omega2)`;
- pre-declared representative macro `q=(delta1,omega1)`;
- hidden coherency errors `(e_delta,e_omega)=(delta2-delta1,omega2-omega1)`;
- exact passive synchronisation manifold `e_delta=e_omega=0`;
- three coherent initial states with common speeds `-0.1,0,+0.1`;
- constant interventions `u=0,+0.2,-0.2` applied only to machine 2;
- one horizon `T=5`;
- deterministic NumPy float64 RK4, primary `dt=0.001`, convergence audit `dt=0.0005`;
- B0 passive-slaving representative model;
- B1 coherent aggregate surrogate;
- C1 exact mean/COI closure control;
- frozen PASS/WEAK/NULL/FAIL classifier.

## Claim ceiling

No power-grid result exists yet.

No novelty promotion, generic power-grid transfer claim, new controlled-equivalence claim, learned-coordinate claim, state-preparation claim, or established causal-synergetics claim is authorised.

STOP — AWAIT GO
