# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Minimal Benchmark 0.1`
Status: COMPLETE / PASS — RESULT FROZEN
Latest canonical file: `research/app_a/neural_minimal_benchmark_0_1.md`
Dependencies: `CORE Synergetic Sufficiency Boundary 0.1` COMPLETE / PASS — CLAIM-RESTRICTED
Canonical implementation/test commit: `649a187125c4ad410e0b16b77accbfacfb577371`
Canonical result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`
Next instruction: `RETURN TO MASTER`
STOP boundary: Do not change the frozen model, state pair, tasks, learning rate, horizon, response metrics, or success criteria; do not open nonlinear, historical-reachability, learned-representation, LoRA, power-grid, or manuscript work without new MASTER authorisation.

## Frozen benchmark result

Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

- Current function: `w_A = w_B = (0,0)`.
- Matched norms: `||U_A||_F = ||U_B||_F = ||v_A||_2 = ||v_B||_2 = 1` in the stated pairwise sense.
- `P_A = diag(2,1)` and `P_B = diag(1,2)`.
- Task C: `w_A^+=(0.2,0)`, `w_B^+=(0.1,0)`; losses `0.32` and `0.405`.
- Task D: `w_A^+=(0,0.1)`, `w_B^+=(0,0.2)`; losses `0.405` and `0.32`.
- Symmetric loss advantage: `0.085` in both directions.
- Analytic/autograd maximum observed component difference: `0.0` in float64.
- Local frozen test run: `4 passed`.
- No retuning or alternative configuration was tried.

## CI status

For implementation commit `649a187125c4ad410e0b16b77accbfacfb577371`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

## Claim ceiling

Allowed interpretation only:

> In this frozen factorised linear neural benchmark, two parameter states with the same current function and matched simple norms can respond differently to the same one-step learning intervention; a symmetric task pair reverses which state adapts more strongly.

No novelty promotion, universal causal/plasticity coordinate claim, nonlinear generalisation, historical reachability claim, LoRA/transformer claim, or causal-synergetics establishment is authorised.

## Open issues

Historical reachability, nonlinear extension, learned representations, LoRA/adapters, real-data scaling, and any broader application remain blocked pending new MASTER authorisation.

STOP — RETURN TO MASTER
