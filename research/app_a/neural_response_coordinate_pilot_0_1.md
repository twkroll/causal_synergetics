# Neural Response Coordinate Pilot 0.1

Status: EXECUTED
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-04
Specification: `research/master/neural_response_coordinate_specification_gate_0_1.md`
Execution prompt: `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`
Decision: **WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The frozen response-coordinate pilot is **WEAK**, mechanically under the pre-specified thresholds.

All mandatory sanity, numerical, leakage, ceiling, and regression conditions pass. The frozen two-dimensional response-aware coordinate predicts every held-out intervention on held-out states essentially exactly:

- aggregate `R2_state = 1.0`;
- minimum per-held-out-intervention `R2_state(c) = 1.0`;
- `NRMSE = 7.30513741157965e-16`.

It strongly beats the current-function baseline B0 and the simple-summary baseline B1, and the cyclic state-association null fails as intended. However, the equal-dimensional raw-parameter PCA baseline B2 is also nearly perfect:

`R2_state(B2) = 0.999883026432542`.

Therefore the response-coordinate advantage over B2 is only

`1.0 - 0.999883026432542 = 0.000116973567458323`,

far below the frozen PASS requirement `>=0.05`. Because all frozen WEAK conditions are nevertheless satisfied, the classification is **WEAK**, not PASS and not NULL.

No coordinate, state family, baseline, threshold, metric, split, intervention, or horizon was changed after held-out inspection.

---

## 2. Frozen specification identifiers

This execution used exactly the frozen specification:

- factorised linear model `f_{U,v}(x)=v^T Ux`;
- `d=4`, `h=5`, fixed `v=e1`;
- 81 lexicographically ordered states on the frozen `9 x 9` `(z1,z2)` grid;
- `rho=0.5` and the frozen diagonal rows 2–5 of `U`;
- checkerboard state split: 41 train / 40 test;
- four normalized Hadamard calibration interventions;
- eight frozen held-out interventions in the frozen order;
- one simultaneous full-batch GD step at `eta=0.1`;
- primary response `Gamma(s,c)=w^+`;
- 16D calibration fingerprint;
- train-only float64 SVD PCA with exactly `k=2`;
- train-standardized PCA scores;
- frozen bilinear OLS decoder `phi(r,c)=[c,r1 c,...,rk c]`;
- B0, B1, B2 baselines exactly as frozen;
- C0, C1 and N0 controls exactly as frozen;
- frozen `R2_state`, per-intervention `R2_state(c)`, NRMSE and PASS/WEAK/NULL/FAIL thresholds.

No second coordinate or alternate family was executed.

---

## 3. Invariant and sanity table

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| State count | exactly `81` | `81` | PASS |
| Train/test split | exactly `41/40` | `41/40` | PASS |
| Current-function equality | max error `<=1e-12` | `0.0` | PASS |
| `||U||_F=2` | max error `<=1e-12` | `2.220446049250313e-16` | PASS |
| `||v||_2=1` | max error `<=1e-12` | `0.0` | PASS |
| `q_i in [0.5,1.5]` | no violation | `0.0` violation | PASS |
| Analytical/autograd audit | max error `<=1e-12` | `2.7755575615628914e-17` | PASS |
| C1 oracle agreement | max error `<=1e-12` | `2.7755575615628914e-17` | PASS |
| C0 full-fingerprint ceiling | aggregate `R2_state >=0.99` | `1.0` | PASS |
| Leakage controls | no failure | fit/predict APIs consume no held-out truth | PASS |
| Prior APP-A regressions | unchanged tests pass | combined run `24 passed` | PASS |

No mandatory sanity condition failed; therefore the result is not FAIL.

---

## 4. Analytical/autograd audit

For every one of the 81 frozen states and all 12 interventions (4 calibration plus 8 held-out), the exact audit response

`Gamma(s,c)=eta (U^T U + ||v||^2 I)c`

was compared against an independent PyTorch float64 autograd implementation of the one simultaneous `(U,v)` gradient step.

Total audited state/intervention pairs:

`81 x 12 = 972`.

Maximum observed absolute component discrepancy:

`2.7755575615628914e-17`.

This is well below the frozen `1e-12` tolerance.

The analytical C1 oracle compared against evaluator-generated autograd held-out truth has the same maximum absolute discrepancy:

`2.7755575615628914e-17`.

---

## 5. Aggregate held-out metrics

| Model/control | Aggregate `R2_state` | NRMSE | Role |
|---|---:|---:|---|
| Response coordinate | `1.000000000000000` | `7.30513741157965e-16` | candidate |
| B0 current function | approximately `0.0` | `0.157359158493889` | competitive baseline |
| B1 simple summaries | `0.070803629370716` | `0.151686097038027` | competitive baseline |
| B2 raw-parameter PCA, 2D | `0.999883026432542` | `0.00170190726453134` | principal competitive baseline |
| C0 full 16D fingerprint | `1.000000000000000` | `1.34721603562732e-15` | ceiling |
| C1 analytical operator | `1.000000000000000` | `9.25714380520572e-17` | oracle |
| N0 cyclic association null | `-0.200000000000001` | `0.172378321474267` | null control |

The response coordinate is therefore predictive, but it does not show the frozen material advantage over an equal-dimensional raw-state PCA representation.

---

## 6. Per-held-out-intervention `R2_state(c)`

Held-out interventions are reported in the exact frozen order `h1,...,h8`.

| Intervention | Response | B0 | B1 | B2 |
|---|---:|---:|---:|---:|
| `h1=e1` | `1.000000000000` | `0.000000000000` | `0.024598095949` | `0.999883026433` |
| `h2=e2` | `1.000000000000` | `0.000000000000` | `0.024598095949` | `0.999883026433` |
| `h3=e3` | `1.000000000000` | `0.000000000000` | `0.117009162793` | `0.999883026433` |
| `h4=e4` | `1.000000000000` | `0.000000000000` | `0.117009162793` | `0.999883026433` |
| `h5=(e1+e3)/sqrt(2)` | `1.000000000000` | `0.000000000000` | `0.070803629371` | `0.999883026433` |
| `h6=(e2+e4)/sqrt(2)` | `1.000000000000` | approximately `0.0` | `0.070803629371` | `0.999883026433` |
| `h7=(e1-e4)/sqrt(2)` | `1.000000000000` | `0.000000000000` | `0.070803629371` | `0.999883026433` |
| `h8=(e2-e3)/sqrt(2)` | `1.000000000000` | `0.000000000000` | `0.070803629371` | `0.999883026433` |

Thus

`R_min = 1.0`.

For reference, N0 per-intervention values in the same order are:

`[0.723076923077, 0.723076923077, -1.123076923077, -1.123076923077, -0.2, -0.2, -0.2, -0.2]`.

---

## 7. Exact threshold comparison

Define the frozen quantities:

- `R_resp = 1.0`;
- `R_func ≈ 0.0`;
- `R_norm = 0.070803629370716`;
- `R_raw2 = 0.999883026432542`;
- `R_null = -0.200000000000001`;
- `R_min = 1.0`.

Derived margins:

- `R_resp - R_func ≈ 1.0`;
- `R_resp - R_norm = 0.929196370629284`;
- `R_resp - R_raw2 = 0.000116973567458323`.

### PASS rule

| PASS condition | Required | Observed | Satisfied? |
|---|---:|---:|---|
| `R_resp` | `>=0.95` | `1.0` | yes |
| `R_min` | `>=0.90` | `1.0` | yes |
| `R_resp-R_func` | `>=0.25` | `~1.0` | yes |
| `R_resp-R_norm` | `>=0.20` | `0.929196370629284` | yes |
| `R_resp-R_raw2` | `>=0.05` | `0.000116973567458323` | **no** |
| `R_null` | `<=0.10` | `-0.200000000000001` | yes |

PASS is therefore not satisfied.

### WEAK rule

| WEAK condition | Required | Observed | Satisfied? |
|---|---:|---:|---|
| `R_resp` | `>=0.90` | `1.0` | yes |
| `R_min` | `>=0.75` | `1.0` | yes |
| `R_resp-R_func` | `>=0.10` | `~1.0` | yes |
| `R_resp-R_norm` | `>=0.10` | `0.929196370629284` | yes |
| `R_resp-R_raw2` | `>-0.05` | `0.000116973567458323` | yes |
| `R_null` | `<=0.25` | `-0.200000000000001` | yes |

All WEAK conditions are satisfied.

**Mechanical classification: WEAK — RESULT FROZEN.**

---

## 8. Leakage-control confirmation

The pipeline separates prediction generation from held-out evaluation.

The fit/predict stage accepts only:

- frozen states/raw parameters where authorised;
- calibration responses;
- calibration intervention descriptors;
- held-out intervention descriptors for prediction generation.

It does not accept held-out response truth.

The evaluator generates held-out autograd truth only after the deterministic prediction bundle has been produced. Tests inspect the fit/predict function signatures and verify the absence of held-out-truth arguments. No held-out response was used for PCA, preprocessing, decoder fitting, baseline construction, threshold selection, or prediction generation.

---

## 9. Regression and software execution

Permitted stack only was used:

- Python 3;
- NumPy;
- PyTorch;
- pytest;
- standard library.

Float64 was used throughout the frozen benchmark calculations.

New coordinate-pilot tests:

`12 passed`.

Combined coordinate-pilot plus unchanged prior APP-A regression tests:

`24 passed`.

Execution command used locally:

`PYTHONPATH=src pytest -q tests`

---

## 10. No-retuning declaration

No alternative model dimensions, state family, latent grid, `rho`, state split, calibration or held-out intervention, learning rate, optimizer, horizon, response, PCA dimension, coordinate construction, decoder, baseline, ceiling, null, preprocessing rule, metric, threshold, tolerance, or second candidate was tried after result inspection.

The near-tie with B2 was accepted as the frozen scientific outcome and was not repaired.

---

## 11. Interpretation ceiling

The strongest allowed interpretation is:

> In this frozen synthetic factorised-linear family, a two-dimensional response-aware coordinate learned from four calibration interventions predicts eight held-out one-step interventions essentially exactly on held-out states, but it does not materially outperform an equal-dimensional raw-parameter PCA baseline; under the pre-specified discriminator the result is therefore WEAK rather than PASS.

This result does **not** establish:

- a generally useful low-dimensional causal/plasticity coordinate;
- special value of response-aware coordinates beyond equally compact raw-state representations in general;
- generic nonlinear scaling;
- realistic SGD history or reachability;
- real-data usefulness;
- LoRA/transformer relevance;
- controlled state preparation;
- novelty;
- established causal synergetics.

No novelty promotion is authorised.

---

## 12. Open issues

The principal unresolved issue exposed by this frozen result is discriminative value beyond raw parameter geometry: the frozen state family is intrinsically two-dimensional enough that a 2D raw-parameter PCA almost completely recovers the same predictive structure.

Any attempt to test a different family, different coordinate, nonlinear scaling, multi-step prediction, real data, realistic training history, LoRA/adapters, controlled state preparation, literature positioning, or manuscript implications requires a new MASTER-authorised gate.

---

## 13. Code, tests, commits, and CI

Implementation:

`src/causal_synergetics/benchmarks/neural_response_coordinate.py`

Implementation commit:

`86715dfb9de78220964e137759c66785373f6de8`

Tests:

`tests/test_neural_response_coordinate_pilot.py`

Test commit:

`48d850c22ca156af892db11cbbdb95b20693bb08`

Canonical result file:

`research/app_a/neural_response_coordinate_pilot_0_1.md`

The canonical result-freeze commit is registered in `research/app_a/STATUS.md` after this result file is committed.

For test commit `48d850c22ca156af892db11cbbdb95b20693bb08`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

---

STOP — RETURN TO MASTER
