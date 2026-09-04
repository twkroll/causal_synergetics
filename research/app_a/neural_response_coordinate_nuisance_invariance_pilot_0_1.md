# Neural Response Coordinate Nuisance-Invariance Pilot 0.1

Status: EXECUTED
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-04
Specification: `research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`
Execution prompt: `research/master/prompts/app_a_neural_response_coordinate_nuisance_invariance_pilot_0_1.md`
Decision: **FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The frozen nuisance-invariance benchmark executed successfully at the numerical, leakage, oracle, gauge-invariance, predictive, B3-control, and regression levels. The candidate 2D response coordinate is exactly predictive on nuisance-only, latent-only, and joint held-out partitions and is numerically gauge invariant. Naive 2D raw-parameter PCA collapses under the held-out gauge orientations, while the explicitly gauge-invariant 2D Gram-PCA control remains exactly predictive.

However, the frozen deterministic state-association null `N0` attains a high joint `R2_state = 0.6999999999999995`. This violates both the PASS null threshold (`<=0.10`) and the WEAK null threshold (`<=0.25`). At the same time, none of the explicitly enumerated NULL conditions in the frozen specification is true: candidate prediction is exact, candidate nuisance invariance is essentially exact, and candidate joint prediction strictly exceeds B2.

Therefore the frozen PASS/WEAK/NULL rules are not total on the observed metric vector. APP-A is not authorised to add a post-hoc NULL condition for `R_null>0.25`, change the null construction, or otherwise repair the classifier. Because the required execution must return one of `PASS / WEAK / NULL / FAIL`, the gate is frozen as **FAIL due to a specification/classification-validity gap**, not due to numerical invalidity and not as a scientific NULL result.

The prior `Neural Response Coordinate Pilot 0.1` remains independently frozen as `WEAK`; this gate does not repair or overwrite it.

---

## 2. Frozen specification identifiers

The execution used exactly:

- factorised linear model `f_{U,v}(x)=v^T Ux`, `d=4`, `h=5`;
- canonical `9x9` response-latent grid with `rho=0.5`;
- hidden gauge `Q(phi)=R(phi)⊕I3`;
- eight angles `phi_j=j*pi/4`, `j=0,...,7`;
- exactly 648 states;
- partitions `164/164/160/160` for `S_train/S_nuis/S_latent/S_joint`;
- four frozen Hadamard calibration interventions and eight frozen held-out interventions;
- exactly one simultaneous full-batch GD step at `eta=0.1`;
- response `Gamma=w^+`;
- candidate 16D calibration fingerprint compressed by train-only PCA to exactly 2D;
- fixed bilinear OLS decoder;
- B0, B1, B2, B3, C0, C1, and N0 exactly as frozen;
- frozen `J_nuis`, R2, NRMSE, thresholds, and `1e-12` numerical tolerance;
- float64 NumPy/PyTorch implementation.

No alternative nuisance, state family, coordinate, dimension, baseline, null, decoder, metric, threshold, or tolerance was tried.

---

## 3. Analytical gauge-invariance checks

For every frozen orthogonal hidden rotation `Q(phi)`, the transformed state is

`U'=QU`, `v'=Qv`.

Because `Q^TQ=I`,

`w'=(QU)^T(Qv)=U^TQ^TQv=U^Tv=w`,

`U'^TU'=U^TQ^TQU=U^TU`,

`||v'||^2=v^TQ^TQv=||v||^2`.

Hence

`P'=U'^TU'+||v'||^2 I=P`,

and for the frozen one-step response,

`Gamma(s,c)=eta P(s)c`,

so `Gamma` is exactly invariant over each frozen gauge orbit.

The numerical audit confirms these identities within the frozen tolerance.

---

## 4. Mandatory sanity table

| Sanity condition | Frozen observation | Result |
|---|---:|---|
| State count / partitions | `648`; `164/164/160/160` | PASS |
| Current-function max error | `8.433854195116819e-17` | PASS |
| `||U||_F=2` max error | `2.220446049250313e-16` | PASS |
| `||v||_2=1` max error | `0.0` | PASS |
| `Q^TQ=I` max error | `2.220446049250313e-16` | PASS |
| Within-orbit `P` max component error | `8.881784197001252e-16` | PASS |
| Within-orbit analytical-response max error | `8.326672684688674e-17` | PASS |
| Analytical/autograd max error over `648x12=7776` pairs | `1.6653345369377348e-16` | PASS |
| C1 oracle max error | `<=1.6653345369377348e-16` | PASS |
| C0 joint aggregate R2 | `1.0` | PASS |
| B3 joint aggregate R2 | `1.0` | PASS |
| B3 `J_nuis` | `2.692209973425601e-32` | PASS |
| Leakage separation | fit/predict accept no held-out truth; truth generated only by evaluator | PASS |
| Prior APP-A regression plus new tests | `36 passed` | PASS |

All mandatory scientific/numerical sanity conditions pass.

---

## 5. Aggregate prediction metrics

### `S_nuis` — nuisance-only generalisation

| Model | `R2_state` | NRMSE |
|---|---:|---:|
| Response 2D PCA | `1.0` | `1.4276353317265007e-15` |
| B0 current function | `0.0` | `0.16119450179536882` |
| B1 simple summaries | `0.05804069725771965` | `0.15644665939329863` |
| B2 raw-parameter PCA 2D | `0.0` | `0.16119450179536882` |
| B3 Gram-PCA 2D | `1.0` | `1.941676549270116e-15` |
| C0 full fingerprint | `1.0` | `1.9306257176501446e-15` |
| C1 oracle | `1.0` | `2.761743272059772e-16` |
| N0 cyclic association null | `0.7071428571428566` | `0.08723246298464095` |

### `S_latent` — latent-only generalisation

| Model | `R2_state` | NRMSE |
|---|---:|---:|
| Response 2D PCA | `1.0` | `1.3827128803937375e-15` |
| B0 current function | `0.0` | `0.15735915849388862` |
| B1 simple summaries | `0.06639245797723059` | `0.15204572023100094` |
| B2 raw-parameter PCA 2D | `0.0` | `0.15735915849388862` |
| B3 Gram-PCA 2D | `1.0` | `1.9200809787532476e-15` |
| C0 full fingerprint | `1.0` | `1.9193067624670278e-15` |
| C1 oracle | `1.0` | `9.595717457890077e-17` |
| N0 cyclic association null | `0.6999999999999995` | `0.08618916073713352` |

### `S_joint` — primary joint held-out generalisation

| Model | `R2_state` | NRMSE |
|---|---:|---:|
| Response 2D PCA | `1.0` | `1.4190705384814486e-15` |
| B0 current function | `0.0` | `0.15735915849388862` |
| B1 simple summaries | `0.03933505243106106` | `0.15423324524823528` |
| B2 raw-parameter PCA 2D | `2.220446049250313e-16` | `0.15735915849388862` |
| B3 Gram-PCA 2D | `1.0` | `1.941469126436537e-15` |
| C0 full fingerprint | `1.0` | `1.9306201195232773e-15` |
| C1 oracle | `1.0` | `2.7453911730087413e-16` |
| N0 cyclic association null | `0.6999999999999995` | `0.08618916073713352` |

---

## 6. Per-held-out-intervention R2

Held-out order is frozen as `h1,...,h8`.

### Candidate response coordinate

- `S_nuis`: `[1,1,1,1,1,1,1,1]`
- `S_latent`: `[1,1,1,1,1,1,1,1]`
- `S_joint`: `[1,1,1,1,1,1,1,1]`

Thus the frozen joint minimum is

`R_min = 1.0`.

### B2 raw-parameter PCA on `S_joint`

`[-2.220446049250313e-16, 2.220446049250313e-16, 2.220446049250313e-16, 0.0, 0.0, 0.0, 0.0, -2.220446049250313e-16]`.

### B3 Gram-PCA on `S_joint`

`[1,1,1,1,1,1,1,1]`.

### N0 on `S_joint`

`[0.9307692307692308, 0.9307692307692307, 0.4692307692307671, 0.4692307692307681, 0.6999999999999997, 0.6999999999999988, 0.7000000000000002, 0.6999999999999995]`.

---

## 7. Frozen nuisance-fraction metric

| Representation | `J_nuis` |
|---|---:|
| Response 2D PCA | `5.596227006606825e-32` |
| B2 raw-parameter PCA 2D | `1.0` |
| B3 Gram-PCA 2D | `2.692209973425601e-32` |

Therefore:

- candidate gauge-invariance threshold `J_resp<=1e-8` is passed by a large margin;
- `J_B2-J_resp >=0.05` is passed by a large margin;
- B3 mandatory gauge-invariant control passes.

This supports only the intended comparison against naive raw PCA; B3 demonstrates that response measurements are not uniquely required to quotient this known symmetry.

---

## 8. Exact mechanical threshold audit

### PASS rule

| Requirement | Observed | Result |
|---|---:|---|
| `R_resp>=0.95` | `1.0` | PASS |
| `R_nuis>=0.95` | `1.0` | PASS |
| `R_lat>=0.95` | `1.0` | PASS |
| `R_min>=0.90` | `1.0` | PASS |
| `R_resp-R_raw2>=0.10` | approximately `1.0` | PASS |
| `J_resp<=1e-8` | `5.596227006606825e-32` | PASS |
| `J_raw2-J_resp>=0.05` | approximately `1.0` | PASS |
| `R_null<=0.10` | `0.6999999999999995` | **FAIL** |

PASS therefore does not apply.

### WEAK rule

All predictive and candidate-invariance floors pass, but WEAK explicitly also requires

`R_null<=0.25`.

Observed:

`0.6999999999999995 > 0.25`.

WEAK therefore does not apply.

### NULL rule

The frozen NULL list is triggered only if at least one of:

- `R_resp<0.90`;
- `R_nuis<0.90`;
- `R_lat<0.90`;
- `R_min<0.75`;
- `J_resp>1e-4`;
- `R_resp<=R_raw2`.

None is true. Therefore NULL also does not apply under the exact frozen text.

### Classification gap

The observed state therefore satisfies no frozen scientific branch: PASS false, WEAK false, NULL false, while all mandatory sanity conditions are true.

The high N0 score is structurally explained by the frozen finite design, without changing the result: each response-latent state appears at four held-out nuisance orientations with identical response coordinates and identical true responses. A one-state cyclic shift therefore maps most states to another gauge copy of the same latent state, preserving substantial correct state association. This explanation does not authorise a different null construction.

Because the execution prompt requires one of `PASS/WEAK/NULL/FAIL` and APP-A may not amend the frozen scientific rules after inspection, the result is frozen as:

**FAIL — SPECIFICATION CLASSIFICATION GAP**.

This FAIL means that the frozen classifier is not exhaustive for the realised metric vector. It must not be misreported as a numerical failure, leakage failure, failed gauge-invariance result, or scientific NULL.

---

## 9. Leakage-control confirmation

The execution separates:

1. construction/fitting/prediction using only `S_train`, calibration responses, state parameters permitted to the baselines, and intervention descriptors;
2. evaluator-only generation of held-out autograd truth after the prediction bundle exists.

`fit_decoder`, `predict_decoder`, and `build_predictions` accept no held-out response/truth argument. Leakage tests pass.

---

## 10. Regression and numerical execution

New nuisance-invariance tests:

`12 passed`.

Combined execution of all four prior unchanged APP-A test files plus the new nuisance-invariance test file:

`36 passed`.

The full analytical/autograd audit covered exactly

`648 x 12 = 7776`

state/intervention pairs in float64, with maximum absolute discrepancy

`1.6653345369377348e-16`.

---

## 11. No-retuning declaration

No alternative base family, grid, `rho`, gauge subgroup, rotation plane, angle set, angle split, partition, intervention, coordinate, PCA dimension, decoder, baseline, null construction, invariance metric, optimizer, learning rate, horizon, metric, threshold, or tolerance was tried after execution began.

The high N0 result was not repaired by changing the cyclic shift or deduplicating gauge copies.

---

## 12. Interpretation ceiling

The observed scientific metrics may be described only as follows:

> In this frozen factorised-linear gauge-control family, the 2D response-aware coordinate is numerically gauge invariant and predicts nuisance-only, latent-only and joint held-out one-step responses essentially exactly, while naive 2D raw-parameter PCA fails under the held-out gauge orientations and an explicitly gauge-invariant 2D Gram-PCA control remains equally predictive. However, the frozen one-state cyclic null retains high predictive score because of repeated gauge-equivalent copies, and the pre-specified PASS/WEAK/NULL classifier does not define a scientific class for this realised metric combination. The gate is therefore frozen as a specification-classification FAIL rather than post-hoc repaired.

Do not claim:

- a PASS of the frozen nuisance gate;
- a scientific NULL result;
- unique information unavailable to symmetry-aware raw-state quotients;
- a generally useful causal/plasticity coordinate;
- generic nonlinear or multi-step scaling;
- realistic SGD-history reachability;
- real-data, LoRA, transformer, or controlled-state-preparation relevance;
- novelty;
- established causal synergetics.

---

## 13. Open issues

The only immediate programme-level issue exposed by this frozen execution is the non-total scientific classifier caused by the pre-specified N0 construction on repeated gauge-equivalent states. Any amendment of the null, addition of an explicit `R_null>0.25 -> NULL` clause, deduplication, orbit-level null, alternate gauge family, alternate coordinate, or new state family requires a new MASTER-authorised gate. APP-A may not choose among these options.

---

## 14. Code, tests, commits, and CI

Implementation:

`src/causal_synergetics/benchmarks/neural_response_coordinate_nuisance.py`

Implementation commit:

`988db41bad5d46615b00defe2da8964c15a5203f`

Tests:

`tests/test_neural_response_coordinate_nuisance.py`

Test commit:

`2d7ac6171323607bfeeec12f3657b56b162e0406`

Local execution:

`PYTHONPATH=src pytest -q tests`

Frozen local result:

`36 passed`.

For test commit `2d7ac6171323607bfeeec12f3657b56b162e0406`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

The canonical result-freeze commit is the commit creating this result file and is registered in `research/app_a/STATUS.md` after creation.

---

STOP — RETURN TO MASTER
