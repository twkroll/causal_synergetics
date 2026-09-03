# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Historical Reachability 0.1`
Status: READY / AWAIT GO
Latest canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`
Latest frozen result decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`
Dependencies: Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
Next instruction: Execute only `research/master/prompts/app_a_neural_historical_reachability_0_1.md` after user enters `GO`.
STOP boundary: Do not change the frozen historical protocol; do not open nonlinear, learned-representation, LoRA, power-grid, state-preparation, or manuscript work without new MASTER authorisation.

## Frozen prior result

### Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.
Implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.

Frozen observations:

- `w_A=w_B=(0,0)`.
- Matched simple norms.
- `P_A=diag(2,1)`, `P_B=diag(1,2)`.
- Task C: A adapts more strongly (`0.32` vs `0.405`).
- Task D: B adapts more strongly (`0.32` vs `0.405`).
- Analytic/autograd maximum observed component difference: `0.0` in float64.
- Local frozen test run: `4 passed`.
- No retuning.

## Active frozen specification

### Neural Historical Reachability 0.1

Canonical prompt:
`research/master/prompts/app_a_neural_historical_reachability_0_1.md`.

The gate freezes one common initialization `U_0=0`, main readout `v=e1`, temporary auxiliary readout `a=e2`, symmetric historical targets `e1/e2`, one `U`-only gradient step at `eta_hist=1`, followed by exact reproduction of the already-frozen C/D evaluation.

No alternative history construction may be tried in this gate.

## Claim ceiling

The benchmark remains a feasibility scaffold. Even if the historical gate passes, it may establish only reachability under the explicitly frozen auxiliary-gradient history. It may not establish ordinary single-head SGD reachability, generic neural plasticity coordinates, nonlinear generalisation, novelty, or causal synergetics.

STOP — AWAIT GO
