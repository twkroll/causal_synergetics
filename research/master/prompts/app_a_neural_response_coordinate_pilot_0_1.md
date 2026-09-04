# Prompt — Neural Response Coordinate Pilot 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-04
Dependencies:
- `RP-007 — Neural Vertical Slice Decision Freeze 0.1`
- `research/master/neural_response_coordinate_specification_gate_0_1.md` (`SPECIFICATION FROZEN / APP-A READY`)

## Start / execution rule

Git is the single source of truth. Before execution read:

- `research/master/PROJECT_GOVERNANCE_0_1.md`;
- `research/app_a/STATUS.md`;
- `research/master/neural_response_coordinate_specification_gate_0_1.md`;
- this prompt.

Execute only when the current APP-A STATUS points to this task and the user enters exactly:

`GO`

If no authorised next step exists, return:

`STOP — RETURN TO MASTER`

---

# Authorised task

## Name

`Neural Response Coordinate Pilot 0.1`

## Purpose

Execute exactly the pre-frozen deterministic benchmark defined in `research/master/neural_response_coordinate_specification_gate_0_1.md`.

The sole scientific question is:

> Does the frozen two-dimensional response-aware coordinate predict held-out one-step learning interventions materially better than the frozen non-response-aware baselines?

This is not a novelty test and does not authorise broader neural scaling.

## Frozen specification — do not alter

Implement exactly the canonical specification file. The following summary is controlling but does not replace the full specification.

### Model/state family

- factorised linear model `f_{U,v}(x)=v^T Ux`;
- `d=4`, `h=5`, `v=e1`;
- first row of `U` zero;
- rows 2–5 diagonal with entries `sqrt(q1)...sqrt(q4)`;
- `rho=0.5`;
- `q1=1+rho z1`, `q2=1-rho z1`, `q3=1+rho z2`, `q4=1-rho z2`;
- `z1,z2` on the fixed 9-value grid `{-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1}`;
- 81 total states;
- checkerboard train/test state split exactly as frozen.

### Intervention / response

- `L_c(w)=1/2||w-c||^2`;
- exactly one simultaneous full-batch GD step in `(U,v)`;
- `eta=0.1`;
- response `Gamma=Delta w=w^+`;
- no momentum, noise, weight decay, stochasticity, clipping, optimizer state, or extra steps.

### Calibration interventions

Exactly the four normalized Hadamard directions frozen in the specification.

### Held-out interventions

Exactly the eight frozen directions `h1...h8` in their frozen order.

### Candidate coordinate

- build the 16D calibration fingerprint from the four calibration responses;
- fit PCA only on train-state fingerprints;
- deterministic float64 full SVD;
- retain exactly `k=2`;
- project train/test calibration fingerprints;
- standardize the two scores from train-state statistics only;
- no dimension sweep or alternate construction.

### Decoder

Use the frozen bilinear feature map

`phi(r,c)=[c,r1 c,...,rk c]`

and float64 `numpy.linalg.lstsq(..., rcond=None)` without regularization.

Fit only on `S_train x C_cal`.

Generate predictions for `S_test x C_hold` before held-out responses are supplied to the evaluator.

### Mandatory baselines

Implement exactly:

- B0 current-function baseline;
- B1 six-scalar simple norm/state-summary baseline;
- B2 equal-dimensional 2D raw-parameter PCA baseline.

Do not add/remove competitive baselines.

### Mandatory ceilings/controls

Implement exactly:

- C0 full 16D calibration-fingerprint ceiling;
- C1 analytical `P=U^T U+||v||^2 I` oracle;
- N0 deterministic one-position cyclic state-association null.

### Metrics/classification

Use exactly the frozen aggregate and per-intervention `R2_state`, secondary NRMSE, sanity conditions, and PASS/WEAK/NULL/FAIL thresholds in the specification file.

No threshold or metric change is allowed.

## Leakage discipline

The fitting/prediction code must not consume held-out responses.

Implement prediction and held-out evaluation as separate callable stages. Tests must verify that fit/predict APIs receive no held-out response array.

Held-out truth may be generated only by the evaluator after predictions are fixed in memory or a deterministic result structure.

Do not inspect held-out values manually before the complete frozen pipeline is executed.

## Required analytical/autograd audit

For all 81 states and all 12 interventions (4 calibration + 8 held-out), verify the analytical one-step response against an independent PyTorch autograd one-step implementation in float64.

Maximum absolute discrepancy must be reported and must satisfy the frozen `1e-12` sanity threshold.

## Required tests

Create `tests/test_neural_response_coordinate_pilot.py` covering at minimum:

1. 81-state construction and deterministic ordering;
2. exact current-function equality;
3. frozen Frobenius/readout norm identities;
4. exact state split counts `41/40`;
5. exact calibration and held-out intervention lists;
6. analytical/autograd agreement;
7. exact oracle agreement;
8. PCA dimension exactly 2 for response and raw-state PCA;
9. no held-out-response arguments in fit/predict stage;
10. metric/classification logic against frozen thresholds;
11. deterministic cyclic null construction;
12. unchanged prior APP-A regression tests still pass.

Do not weaken existing tests.

## Required implementation path

`src/causal_synergetics/benchmarks/neural_response_coordinate.py`

## Required result file

Create:

`research/app_a/neural_response_coordinate_pilot_0_1.md`

It must contain:

1. Executive verdict and exact classification: PASS / WEAK / NULL / FAIL.
2. Reproduction of the frozen specification identifiers.
3. Invariant/sanity table.
4. Analytical/autograd audit result.
5. Aggregate metric table for response coordinate, B0, B1, B2, C0, C1, N0.
6. Per-held-out-intervention `R2_state` for the response coordinate and principal baselines.
7. Secondary NRMSE table.
8. Exact threshold comparison showing why the classification follows mechanically.
9. Leakage-control confirmation.
10. Regression-test result.
11. No-retuning declaration.
12. Claim ceiling and forbidden interpretations.
13. Open issues.
14. Implementation/test/result commit hashes and CI status if applicable.

## Classification discipline

Apply the frozen classification mechanically.

- `PASS` only if every PASS condition is met.
- `WEAK` only under the frozen WEAK rule.
- `NULL` is an admissible scientific result and must not trigger repair.
- `FAIL` is reserved for frozen sanity/implementation/leakage/regression invalidity.

If the response coordinate ties or fails to beat B2 under the frozen rule, do not modify the raw-state baseline or redefine success.

## Forbidden actions

Do not:

- change model/state family/grid/rho;
- change train/test states;
- change calibration/held-out interventions;
- change optimizer, learning rate, horizon, or response;
- change coordinate dimension/construction;
- sweep PCA dimensions;
- change decoder;
- add/remove/tune baselines;
- change metrics or thresholds;
- inspect results and then introduce a second coordinate;
- create a second state family if result is WEAK/NULL/FAIL;
- open nonlinear scaling, real-data, realistic-history, LoRA, power-grid, state-preparation, literature, or manuscript work;
- promote novelty.

## Final handoff

After execution:

1. commit implementation/tests/result;
2. update `research/app_a/STATUS.md` with exact frozen result classification and commit hashes;
3. set `Next instruction: RETURN TO MASTER`;
4. report CI status if applicable;
5. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
