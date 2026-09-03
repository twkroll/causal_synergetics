# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Historical Reachability 0.1`
Status: COMPLETE / PASS — RESULT FROZEN
Latest canonical result: `research/app_a/neural_historical_reachability_0_1.md`
Latest frozen result decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`
Dependencies: Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
Historical test-addition commit: `ad9cc18a0519ffcfc4e6bc2e919e82f40bf54208`
Historical implementation commit: `e342ef5c5cefae30df45e23bc667f149e818238c`
Canonical result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`
Next instruction: `RETURN TO MASTER`
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

## Frozen historical result

### Neural Historical Reachability 0.1

Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

Frozen preparation protocol:

- Common hidden initialization: `U_0=[[0,0],[0,0]]`.
- Fixed main readout: `v=e1`.
- Fixed temporary auxiliary readout: `a=e2`.
- History A target: `c_A=e1`.
- History B target: `c_B=e2`.
- Exactly one full-batch gradient step on `U` only.
- Historical learning rate: `eta_hist=1`.
- No retuning or alternative history was tried.

Frozen observations:

- History A reaches exactly `U_A=[[0,0],[1,0]]`.
- History B reaches exactly `U_B=[[0,0],[0,1]]`.
- Both histories start from the same `U_0` and `v`.
- Main function is `w=(0,0)` before and after preparation for both histories.
- Historical analytical/autograd maximum observed difference: `0.0` in float64.
- Historical loss is `0.5` before and `0.0` after the step for both histories.
- The already-frozen C/D evaluation is reproduced exactly within `1e-12`:
  - A/C: `w^+=(0.2,0)`, loss `0.32`.
  - B/C: `w^+=(0.1,0)`, loss `0.405`.
  - A/D: `w^+=(0,0.1)`, loss `0.405`.
  - B/D: `w^+=(0,0.2)`, loss `0.32`.
- Local combined frozen test run: `8 passed`.

## CI status

For historical implementation commit `e342ef5c5cefae30df45e23bc667f149e818238c`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

## Claim ceiling

Allowed interpretation only:

> The exact function-equivalent state pair used in the frozen linear benchmark can be generated from a common hidden initialization by two symmetric one-step auxiliary gradient histories while the main readout and current main function remain unchanged; the resulting states retain the previously frozen opposite one-step adaptation preferences.

This does not establish ordinary single-head SGD reachability, generic SGD reachability, nonlinear or real-data generalisation, novelty, uniqueness/necessity of auxiliary preparation, or causal synergetics.

## Open issues

Ordinary single-head reachability, nonlinear extension, learned representations, LoRA/adapters, real-data scaling, robustness/genericity of the historical construction, state preparation, and any manuscript work remain blocked pending new MASTER authorisation.

STOP — RETURN TO MASTER
