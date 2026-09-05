# STATUS — 60 – APP-B – Power-Grid Minimalbenchmark

Current Gate: `Power-Grid Minimal Benchmark 0.1`
Status: COMPLETE / RESULT FROZEN / PASS
Latest canonical result: `research/app_b/power_grid_minimal_benchmark_0_1.md`
Specification: `research/master/power_grid_minimal_benchmark_feasibility_specification_0_1.md`
Execution prompt: `research/master/prompts/app_b_power_grid_minimal_benchmark_0_1.md`
Dependency: `RP-014 — Power-Grid Minimal Benchmark Specification Freeze 0.1`
Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`
Next instruction: Return to `00 – MASTER – Projektplan & Status` and enter exactly `Status?`.
STOP boundary: Do not retune or extend this benchmark; do not change topology, model, parameters, macro map, initial states, intervention bus/amplitude/sign pair, horizon, numerical method/resolution, baselines, metrics, thresholds, or claim ceiling; do not try a second grid, fault, macro, amplitude, horizon, learned coordinate, state-preparation experiment, literature task, or manuscript work without new MASTER authorisation.

## Frozen result

Mandatory sanity checks pass. Mechanical classifier returns `PASS` with:

- `E_pass = 0`;
- `E_B0_min = 0.3549858420076152`;
- `E_B1_min = 0.06534774384333092`;
- `H_delta = 0.13069548768668177 < pi/2`;
- maximum controlled `|e_omega| = 0.08954202393695339`;
- mean/COI closure error `3.885780586188048e-14`;
- primary/half-step convergence error `8.1601392309949e-15`;
- odd-sign symmetry error `3.83026943495679e-14`;
- new APP-B tests: `5 passed`;
- prior unchanged repository regression evidence: `36 passed` in the preceding frozen APP-A execution; APP-B modified none of those prior files.

## Interpretation ceiling

In this frozen normalized two-machine swing benchmark, the representative-machine coherent reduction is exact for the declared unforced coherent initial set but becomes intervention-insufficient under a localized step applied to the hidden machine; the mismatch persists even against a standard coherent aggregate surrogate. The true mean/COI coordinate remains exactly closed, so the result is specific to the pre-declared representative macro and does not show that all low-dimensional power-grid reductions fail.

No novelty promotion, generic power-grid transfer claim, new controlled-equivalence claim, learned-coordinate claim, state-preparation claim, or established causal-synergetics claim is authorised.

STOP — RETURN TO MASTER
