# Neural Response Coordinate Specification Gate 0.1

Status: COMPLETE / SPECIFICATION FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-04
Dependency: `RP-007 — Neural Vertical Slice Decision Freeze 0.1`
Decision: **SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION**

## 1. Executive decision

Exactly one falsifiable held-out neural response-coordinate benchmark is frozen before execution.

The benchmark asks whether a fixed two-dimensional response-aware coordinate, constructed only from four calibration learning interventions, predicts eight held-out learning interventions on held-out states materially better than pre-declared non-response-aware baselines.

No benchmark execution, held-out response inspection, representation sweep, baseline tuning, or alternative state-family search was performed during this specification gate.

The benchmark deliberately uses an analytically auditable factorised-linear family rather than another hand-picked two-state crossing. It contains 81 exactly function-equivalent states with a two-dimensional latent response geometry, a deterministic state split, a fixed calibration/held-out intervention split, a fixed 2D PCA construction, a common bilinear decoder family, weak baselines, an equal-dimensional raw-parameter PCA baseline, and response-aware ceilings/null controls.

A full PASS requires not merely accurate held-out prediction, but a material advantage over the equal-dimensional raw-parameter PCA baseline. If the response coordinate predicts well but does not materially beat that baseline, the correct result is WEAK rather than PASS.

## 2. Frozen model and state family

Use the factorised linear model

`f_{U,v}(x)=v^T Ux`

with input dimension `d=4`, hidden width `h=5`, `U in R^{5x4}`, and fixed readout

`v=e1=(1,0,0,0,0)^T`.

For every state, the first row of `U` is zero. Rows 2–5 are diagonal in the four input coordinates:

`U(z1,z2)[1:5,:] = diag(sqrt(q1),sqrt(q2),sqrt(q3),sqrt(q4))`,

using zero-based conceptual row indexing after the all-zero first row, with

`rho=0.5`,

`q1=1+rho z1`,
`q2=1-rho z1`,
`q3=1+rho z2`,
`q4=1-rho z2`.

The latent grid is fixed as

`z1,z2 in {-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1}`,

for exactly `9x9=81` states, ordered lexicographically by `(z1,z2)`.

Consequences frozen before execution:

- `w=U^T v=0` for all 81 states, so the current function is exactly identical;
- all `qi` lie in `[0.5,1.5]`;
- `||U||_F=2` for all states because `sum_i qi=4`;
- `||v||_2=1` for all states;
- raw parameter dimension is 25 (`20` entries of `U` plus `5` of `v`).

No alternative state family or `rho` is allowed.

## 3. Frozen state split

Index the 9 values of each latent coordinate by `i,j in {0,...,8}` in ascending order.

Training states:

`S_train = {(i,j): (i+j) mod 2 = 0}`

for exactly 41 states.

Test states:

`S_test = {(i,j): (i+j) mod 2 = 1}`

for exactly 40 states.

No random split and no alternate split are allowed.

## 4. Frozen learning intervention and response

For intervention vector `c in R^4`, use

`L_c(w)=1/2 ||w-c||_2^2`.

Intervention semantics: exactly one simultaneous full-batch gradient-descent step on `(U,v)` with

`eta=0.1`,

no momentum, weight decay, stochasticity, clipping, noise, optimizer state, or extra step.

Horizon: exactly one optimizer step.

Primary response:

`Gamma(s,c) = Delta w = w^+ - w = w^+`.

Because every frozen state has `w=0`, the exact analytical response is

`Gamma(s,c)=eta P(s)c`,

where

`P(s)=U^T U + ||v||^2 I`

and therefore

`P(z1,z2)=diag(2+rho z1, 2-rho z1, 2+rho z2, 2-rho z2)`.

This formula is an analytical audit relation and oracle sanity check, not the candidate learned coordinate.

## 5. Frozen intervention split

### Calibration / coordinate-construction interventions

Use exactly four unit vectors forming the normalized 4x4 Hadamard basis:

`t1=(1,1,1,1)/2`
`t2=(1,1,-1,-1)/2`
`t3=(1,-1,1,-1)/2`
`t4=(1,-1,-1,1)/2`.

Call this set `C_cal`.

### Held-out interventions

Use exactly the following eight unit vectors, in this order:

`h1=e1`
`h2=e2`
`h3=e3`
`h4=e4`
`h5=(e1+e3)/sqrt(2)`
`h6=(e2+e4)/sqrt(2)`
`h7=(e1-e4)/sqrt(2)`
`h8=(e2-e3)/sqrt(2)`.

Call this set `C_hold`.

No intervention may move between sets after execution begins.

## 6. Frozen response coordinate

For every state `s`, form the 16-dimensional calibration fingerprint

`F(s)=concat[Gamma(s,t1),Gamma(s,t2),Gamma(s,t3),Gamma(s,t4)]`.

Fit PCA only on `{F(s): s in S_train}`:

1. subtract the training-state mean fingerprint;
2. compute deterministic full SVD in float64;
3. retain exactly the first `k=2` right-singular directions;
4. do not choose `k` from explained variance and do not sweep `k`;
5. project both train and test calibration fingerprints into this fixed 2D subspace;
6. standardize each retained score using training-state mean and population standard deviation; zero-variance handling is scale `1`, though zero variance is not expected.

The resulting two numbers are the frozen candidate response/plasticity coordinate `z_resp(s) in R^2`.

PCA sign/order ambiguity does not affect downstream predictions because both coordinates are retained and the decoder is refit; no result-based rotation is permitted.

## 7. Frozen decoder

For any state feature vector `r in R^k` and intervention `c in R^4`, use the fixed bilinear feature map

`phi(r,c) = [c, r1 c, ..., rk c]`.

Fit a multi-output ordinary least-squares map from `phi` to `Gamma(s,c)` using only

`S_train x C_cal`.

Implementation: float64 `numpy.linalg.lstsq(..., rcond=None)`, no regularization, no hyperparameter tuning, no intercept beyond the explicit base `c` block.

The response-coordinate model uses `r=z_resp` and hence exactly 12 decoder input features.

Predictions are then generated for `S_test x C_hold` before held-out responses are supplied to the evaluator.

## 8. Frozen non-response-aware baselines

All competitive baselines use the same state split, intervention split, bilinear feature construction, OLS solver, and evaluation metric.

### B0 — current-function baseline

State features are the current effective weights `w in R^4`.

They are identically zero in this family. The decoder therefore has only state-independent predictive power through the base `c` block.

### B1 — simple norm/state-summary baseline

Use exactly these six scalar summaries:

1. `||U||_F`;
2. `||v||_2`;
3. spectral norm `||U||_2`;
4. nuclear norm `||U||_*`;
5. maximum row Euclidean norm of `U`;
6. minimum nonzero row Euclidean norm of `U`.

Center and population-standardize each summary on training states; zero-variance columns receive scale `1` and become zero after centering.

No additional summary statistic may be added.

### B2 — equal-dimensional raw-parameter PCA baseline

Flatten the raw parameter state as

`theta=[vec(U),v] in R^25`.

Fit PCA on training-state `theta` values using the same deterministic centering/SVD procedure as the response coordinate, retain exactly `k=2`, project train/test states, standardize the two scores from training statistics, and use the same bilinear OLS decoder.

This is the strongest mandatory non-response-aware comparison and is the principal baseline for the material-advantage criterion.

No raw-parameter nonlinear features or dimension sweep are allowed.

## 9. Frozen ceilings and controls

### C0 — full calibration-fingerprint ceiling

Use the complete centered/standardized 16D calibration fingerprint `F(s)` without PCA and the same bilinear OLS decoder. This is response-aware and is not a competitive baseline; it verifies that the calibration interventions contain enough predictive information.

### C1 — analytical operator oracle

Use the exact pre-declared matrix

`P=U^T U + ||v||^2 I`

and predict

`Gamma_oracle=eta P c`.

The oracle must agree with autograd truth to absolute tolerance `1e-12`; otherwise the execution is invalid (`FAIL`).

### N0 — state-association null

For test states ordered lexicographically, cyclically shift the fitted `z_resp` assignments by exactly one position while keeping interventions and true responses fixed. Evaluate this misassigned coordinate with the already fitted response-coordinate decoder.

No random permutation is used.

## 10. Leakage rule

Coordinate construction and decoder fitting may access only:

- raw train-state parameters for baselines;
- calibration responses `C_cal` for train and test states where required to construct `z_resp`;
- intervention descriptors themselves.

Held-out responses for `C_hold` may not be passed to PCA, preprocessing, decoder fitting, threshold selection, baseline design, or prediction generation.

Implementation must separate prediction generation from held-out evaluation in code.

## 11. Frozen metrics

Primary metric: aggregate state-conditioned coefficient of determination

`R2_state = 1 - SSE/SST`,

where

`SSE = sum_{c in C_hold} sum_{s in S_test} ||Gamma_hat(s,c)-Gamma(s,c)||^2`,

and

`SST = sum_{c in C_hold} sum_{s in S_test} ||Gamma(s,c)-mean_{s' in S_test} Gamma(s',c)||^2`.

The held-out mean is used only for evaluation normalization, never for fitting.

Also report per-held-out-intervention `R2_state(c)` using the analogous denominator.

Secondary metric:

`NRMSE = sqrt(SSE / sum ||Gamma||^2)` over all held-out state/intervention pairs.

Report every baseline/control under the same metrics.

## 12. Frozen classification thresholds

All sanity conditions below are mandatory before scientific classification:

- current-function equality error over all states `<=1e-12`;
- frozen norm identities within `1e-12`;
- analytical one-step and autograd one-step responses agree within `1e-12` on all calibration and held-out state/intervention pairs;
- oracle C1 maximum absolute error `<=1e-12`;
- full fingerprint ceiling C0 has aggregate `R2_state >= 0.99`;
- no held-out leakage test fails;
- unchanged previous APP-A regression tests continue to pass.

If any sanity condition fails, classify `FAIL` and do not reinterpret as a scientific null.

Let

`R_resp` = aggregate `R2_state` of the 2D response coordinate;
`R_func` = B0;
`R_norm` = B1;
`R_raw2` = B2;
`R_null` = N0.

### PASS

All sanity conditions pass, and all of:

- `R_resp >= 0.95`;
- every held-out intervention has `R2_state(c) >= 0.90`;
- `R_resp - R_func >= 0.25`;
- `R_resp - R_norm >= 0.20`;
- `R_resp - R_raw2 >= 0.05`;
- `R_null <= 0.10`.

Interpretation: in this frozen synthetic family, a 2D response-aware coordinate predicts held-out interventions accurately and materially better than the pre-declared non-response-aware baselines, including an equal-dimensional raw-state PCA baseline.

### WEAK

All sanity conditions pass, `R_resp >= 0.90`, and the response coordinate clearly beats B0/B1 (`>=0.10` aggregate margin over each), but at least one PASS condition fails because either:

- the margin over B2 is `<0.05`, or
- some per-intervention `R2_state(c)` lies in `[0.75,0.90)`, or
- the null control lies in `(0.10,0.25]`.

Interpretation: compact held-out prediction works, but special value beyond simpler state information is not established strongly enough.

### NULL

All sanity conditions pass, but either:

- `R_resp <0.90`, or
- `R_resp <= R_raw2`, or
- response-coordinate advantage over B0 or B1 is `<0.10`.

Interpretation: the frozen response coordinate does not provide the intended predictive advantage. This materially weakens the neural programme's compact-response-coordinate direction.

### FAIL

Any mandatory sanity, implementation, leakage, regression, or numerical-validity condition fails.

No threshold may be changed after held-out results are inspected.

## 13. Numerical and software freeze

Permitted stack:

- Python 3;
- NumPy;
- PyTorch;
- pytest;
- Python standard library.

Use float64 throughout numerical model, PCA, OLS, and comparison calculations.

No scikit-learn dependency is required or authorised for this gate.

No random seed is needed because the state grid, splits, interventions, PCA solver, OLS solver, and null control are deterministic.

## 14. Required implementation and result paths

Execution prompt:

`research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`

Implementation:

`src/causal_synergetics/benchmarks/neural_response_coordinate.py`

Tests:

`tests/test_neural_response_coordinate_pilot.py`

Canonical result:

`research/app_a/neural_response_coordinate_pilot_0_1.md`

## 15. Anti-retuning freeze

After execution begins, APP-A may not change:

- model dimensions;
- state family, grid, `rho`, or state split;
- calibration or held-out interventions;
- response functional, optimizer, learning rate, or horizon;
- coordinate dimension or PCA construction;
- decoder family;
- any baseline, ceiling, or null control;
- preprocessing;
- metrics;
- classification thresholds;
- numerical tolerances.

No second candidate coordinate or alternative synthetic family is authorised if the result is WEAK, NULL, or FAIL.

## 16. Claim ceiling

This specification does not establish a learned causal/plasticity coordinate and carries no novelty promotion.

Even a future PASS may support only the frozen synthetic-family statement. It will not establish generic nonlinear scaling, natural SGD history, real-data usefulness, LoRA/transformer relevance, causal-synergetics field novelty, or controlled state preparation.

## 17. Decision

**SPECIFICATION FROZEN / APP-A READY**

The next execution must use only the versioned APP-A prompt and must return to MASTER after result freeze.
