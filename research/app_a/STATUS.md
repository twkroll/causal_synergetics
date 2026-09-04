# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Response Coordinate Pilot 0.1`
Status: COMPLETE / WEAK — RESULT FROZEN / WAIT
Latest canonical result: `research/app_a/neural_response_coordinate_pilot_0_1.md`
Latest frozen result decision: `WEAK — RESULT FROZEN / NO NOVELTY PROMOTION`
Dependencies:
- Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
- Neural Historical Reachability 0.1 COMPLETE / FROZEN
- Neural Nonlinear ReLU Pilot 0.1 COMPLETE / FROZEN
- Neural Vertical Slice Go/Revise/Stop Gate 0.1 COMPLETE / GO / FROZEN
- Neural Response Coordinate Specification Gate 0.1 COMPLETE / SPECIFICATION FROZEN
Implementation commit: `86715dfb9de78220964e137759c66785373f6de8`
Test commit: `48d850c22ca156af892db11cbbdb95b20693bb08`
Canonical result-freeze commit: `18618368991d818b3bfe883975b3ab2573bed0c6`
Next instruction: `WAIT FOR MASTER`
STOP boundary: Do not alter the frozen result, coordinate, state family, baselines, metrics, thresholds, split, interventions, or horizon; do not open a second coordinate/family, nonlinear/multi-step/real-data/realistic-history/LoRA/power-grid/state-preparation/literature/manuscript work without new MASTER authorisation.

## Frozen response-coordinate result

Decision: **WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**

- Candidate 2D response coordinate aggregate held-out `R2_state = 1.0`.
- Minimum held-out intervention `R2_state(c)=1.0`.
- B0 current-function baseline approximately `0.0`.
- B1 simple-summary baseline `0.070803629370716`.
- B2 equal-dimensional raw-parameter PCA baseline `0.999883026432542`.
- Candidate advantage over B2: `0.000116973567458323`, below frozen PASS requirement `>=0.05`.
- C0 full-fingerprint ceiling `R2_state=1.0`.
- C1 oracle maximum absolute error `2.7755575615628914e-17`.
- N0 cyclic association null `R2_state=-0.200000000000001`.
- Analytical/autograd maximum discrepancy over all 972 state/intervention pairs `2.7755575615628914e-17`.
- Leakage and all mandatory sanity checks passed.
- New coordinate tests `12 passed`; combined unchanged APP-A regression suite `24 passed`.
- No retuning or alternate coordinate/family was tried.

## Claim ceiling

Allowed interpretation only:

> In this frozen synthetic factorised-linear family, a two-dimensional response-aware coordinate learned from four calibration interventions predicts eight held-out one-step interventions essentially exactly on held-out states, but it does not materially outperform an equal-dimensional raw-parameter PCA baseline; under the pre-specified discriminator the result is therefore WEAK rather than PASS.

No generally useful causal/plasticity coordinate, special response-aware value beyond raw-state geometry in general, generic nonlinear scaling, realistic SGD reachability, real-data usefulness, LoRA/transformer relevance, controlled state preparation, novelty, or established causal synergetics may be claimed.

## CI status

For test commit `48d850c22ca156af892db11cbbdb95b20693bb08`, GitHub reports no commit status checks. Repository CI is therefore not configured / not applicable for this execution commit.

STOP — WAIT
