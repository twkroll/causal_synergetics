# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Response Coordinate Pilot 0.1`
Status: COMPLETE / WEAK — RESULT FROZEN
Latest canonical result: `research/app_a/neural_response_coordinate_pilot_0_1.md`
Latest frozen result decision: `WEAK — RESULT FROZEN / NO NOVELTY PROMOTION`
Dependencies:
- `Neural Minimal Benchmark 0.1` COMPLETE / FROZEN
- `Neural Historical Reachability 0.1` COMPLETE / FROZEN
- `Neural Nonlinear ReLU Pilot 0.1` COMPLETE / FROZEN
- `Neural Vertical Slice Go/Revise/Stop Gate 0.1` COMPLETE / GO / FROZEN
- `Neural Response Coordinate Specification Gate 0.1` COMPLETE / SPECIFICATION FROZEN
Implementation commit: `86715dfb9de78220964e137759c66785373f6de8`
Test commit: `48d850c22ca156af892db11cbbdb95b20693bb08`
Canonical result-freeze commit: `18618368991d818b3bfe883975b3ab2573bed0c6`
Next instruction: `RETURN TO MASTER`
STOP boundary: Do not alter the frozen result, coordinate, state family, baselines, metrics, or thresholds; do not open a second coordinate/family, multi-step/real-data/realistic-history/nonlinear-scaling/LoRA/power-grid/state-preparation/literature/manuscript work without new MASTER authorisation.

## Frozen prior chain

### Neural Minimal Benchmark 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### Neural Historical Reachability 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### Neural Nonlinear ReLU Pilot 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.

## Frozen response-coordinate result

### Neural Response Coordinate Pilot 0.1

Decision: **WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**

Frozen observations:

- 81 exact function-equivalent factorised-linear states; checkerboard split `41/40`.
- Candidate coordinate: exactly 2D train-only PCA of the 16D four-intervention calibration fingerprint.
- Aggregate candidate `R2_state = 1.0`.
- Minimum per-held-out-intervention candidate `R2_state(c) = 1.0`.
- Candidate `NRMSE = 7.30513741157965e-16`.
- B0 current-function aggregate `R2_state ≈ 0.0`.
- B1 simple-summary aggregate `R2_state = 0.070803629370716`.
- B2 equal-dimensional raw-parameter PCA aggregate `R2_state = 0.999883026432542`.
- Candidate advantage over B2: `0.000116973567458323`, below frozen PASS requirement `>=0.05`.
- C0 full-fingerprint ceiling aggregate `R2_state = 1.0`.
- C1 oracle maximum absolute error: `2.7755575615628914e-17`.
- N0 cyclic state-association null aggregate `R2_state = -0.200000000000001`.
- Analytical/autograd maximum absolute discrepancy over all `81 x 12 = 972` state/intervention pairs: `2.7755575615628914e-17`.
- Current-function error `0.0`; frozen Frobenius norm maximum error `2.220446049250313e-16`; readout norm error `0.0`.
- Leakage separation passed: fit/predict stages accept no held-out truth; evaluator generates truth only after prediction construction.
- New coordinate tests: `12 passed`.
- Combined unchanged APP-A regression plus coordinate tests: `24 passed`.
- No retuning, alternate coordinate, alternate state family, baseline repair, or threshold change was performed.

### Mechanical classification

PASS fails only because the material B2 advantage condition fails:

`R_resp - R_raw2 = 0.000116973567458323 < 0.05`.

All frozen WEAK conditions pass, including `R_resp >=0.90`, `R_min >=0.75`, required advantages over B0/B1, `R_resp-R_raw2 > -0.05`, and `R_null <=0.25`.

Therefore the exact frozen classification is `WEAK`.

## CI status

For test commit `48d850c22ca156af892db11cbbdb95b20693bb08`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

## Claim ceiling

Allowed interpretation only:

> In this frozen synthetic factorised-linear family, a two-dimensional response-aware coordinate learned from four calibration interventions predicts eight held-out one-step interventions essentially exactly on held-out states, but it does not materially outperform an equal-dimensional raw-parameter PCA baseline; under the pre-specified discriminator the result is therefore WEAK rather than PASS.

Do not claim a generally useful causal/plasticity coordinate, special response-coordinate value beyond raw-state geometry in general, generic nonlinear scaling, realistic SGD reachability, real-data usefulness, LoRA/transformer relevance, controlled state preparation, novelty, or established causal synergetics.

## Open issues

The frozen result shows that this state family is sufficiently low-dimensional in raw parameter geometry that 2D raw PCA almost recovers the predictive structure. Any different state family, alternate coordinate, nonlinear/multi-step/real-data extension, realistic history, LoRA/adapters, state preparation, literature positioning, or manuscript consequence requires a new MASTER-authorised gate.

STOP — RETURN TO MASTER
