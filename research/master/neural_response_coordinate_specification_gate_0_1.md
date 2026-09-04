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

A full PASS requires not merely accurate held-out prediction, but a material advantage over the equal-dimensional raw-parameter PCA baseline. A near-tie with that baseline is WEAK; a clear loss to it is NULL.

## 2. Frozen model and state family

Use the factorised linear model

`f_{U,v}(x)=v^T Ux`

with input dimension `d=4`, hidden width `h=5`, `U in R^{5x4}`, and fixed readout

`v=e1=(1,0,0,0,0)^T`.

For every state, the first row of `U` is zero. Rows 2–5 are diagonal in the four input coordinates:

`U(z1,z2)[1:5,:] = diag(sqrt(q1),sqrt(q2),sqrt(q3),sqrt(q4))`,

with

`rho=0.5`,
`q1=1+rho z1`,
`q2=1-rho z1`,
`q3=1+rho z2`,
`q4=1-rho z2`.

The latent grid is fixed as

`z1,z2 in {-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1}`,

for exactly `9x9=81` states, ordered lexicographically by `(z1,z2)`.

Frozen consequences:

- `w=U^T v=0` for all states;
- all `qi in [0.5,1.5]`;
- `||U||_F=2` for all states;
- `||v||_2=1` for all states;
- raw parameter dimension is 25.

No alternative state family or `rho` is allowed.

## 3. Frozen state split

Index the 9 values of each latent coordinate by `i,j in {0,...,8}` in ascending order.

Training states:

`S_train = {(i,j): (i+j) mod 2 = 0}`

for exactly 41 states.

Test states:

`S_test = {(i,j): (i+j) mod 2 = 1}`

for exactly 40 states.

No random or alternate split is allowed.

## 4. Frozen learning intervention and response

For intervention vector `c in R^4`, use

`L_c(w)=1/2 ||w-c||_2^2`.

Intervention semantics: exactly one simultaneous full-batch gradient-descent step on `(U,v)` with

`eta=0.1`,

with no momentum, weight decay, stochasticity, clipping, noise, optimizer state, or extra step.

Horizon: exactly one optimizer step.

Primary response:

`Gamma(s,c)=Delta w=w^+`.

Because every frozen state has `w=0`, the exact analytical audit relation is

`Gamma(s,c)=eta P(s)c`,

where

`P(s)=U^T U + ||v||^2 I`

and

`P(z1,z2)=diag(2+rho z1,2-rho z1,2+rho z2,2-rho z2)`.

This is an oracle/audit relation, not the candidate learned coordinate.

## 5. Frozen intervention split

### Calibration interventions

Use exactly the four normalized Hadamard directions:

`t1=(1,1,1,1)/2`
`t2=(1,1,-1,-1)/2`
`t3=(1,-1,1,-1)/2`
`t4=(1,-1,-1,1)/2`.

Call this set `C_cal`.

### Held-out interventions

Use exactly, in order:

`h1=e1`
`h2=e2`
`h3=e3`
`h4=e4`
`h5=(e1+e3)/sqrt(2)`
`h6=(e2+e4)/sqrt(2)`
`h7=(e1-e4)/sqrt(2)`
`h8=(e2-e3)/sqrt(2)`.

Call this set `C_hold`.

No intervention may move between sets.

## 6. Frozen response coordinate

For every state, form the 16D calibration fingerprint

`F(s)=concat[Gamma(s,t1),Gamma(s,t2),Gamma(s,t3),Gamma(s,t4)]`.

Fit PCA only on training-state fingerprints:

1. subtract the train mean;
2. deterministic full SVD in float64;
3. retain exactly `k=2` right-singular directions;
4. no explained-variance selection and no `k` sweep;
5. project train/test calibration fingerprints;
6. standardize retained scores with training-state mean and population standard deviation; zero-variance scale is 1.

The resulting 2D vector is `z_resp(s)`.

PCA sign/order ambiguity is not outcome-tuned and does not alter the downstream subspace prediction because both coordinates are retained.

## 7. Frozen decoder

For any state feature vector `r in R^k` and intervention `c in R^4`, use

`phi(r,c)=[c,r1 c,...,rk c]`.

Fit multi-output OLS from `phi` to `Gamma(s,c)` using only `S_train x C_cal`.

Implementation: float64 `numpy.linalg.lstsq(..., rcond=None)`, no regularization, no hyperparameter tuning, no additional intercept beyond the explicit base `c` block.

The response-coordinate model has exactly 12 decoder input features.

Predictions for `S_test x C_hold` must be generated before held-out responses are supplied to the evaluator.

## 8. Frozen non-response-aware baselines

All baselines use the same state split, intervention split, bilinear feature construction, OLS solver, and metrics.

### B0 — current-function baseline

State features: current effective weights `w in R^4`, identically zero here.

### B1 — simple norm/state-summary baseline

Use exactly six scalar summaries:

1. `||U||_F`;
2. `||v||_2`;
3. spectral norm `||U||_2`;
4. nuclear norm `||U||_*`;
5. maximum row Euclidean norm of `U`;
6. minimum nonzero row Euclidean norm of `U`.

Center/population-standardize from train states only; zero-variance columns use scale 1. No extra summary may be added.

### B2 — equal-dimensional raw-parameter PCA baseline

Flatten

`theta=[vec(U),v] in R^25`.

Fit deterministic train-only PCA exactly as for the response coordinate, retain exactly `k=2`, project train/test states, standardize from train statistics, and use the same bilinear OLS decoder.

No nonlinear raw-state features or dimension sweep are allowed.

## 9. Frozen ceilings and controls

### C0 — full calibration-fingerprint ceiling

Use the complete centered/standardized 16D calibration fingerprint without PCA and the same bilinear OLS decoder. This is response-aware and not a competitive baseline.

### C1 — analytical operator oracle

Predict

`Gamma_oracle=eta (U^T U + ||v||^2 I)c`.

Maximum absolute error versus autograd truth must be `<=1e-12`.

### N0 — state-association null

For lexicographically ordered test states, cyclically shift fitted `z_resp` assignments by exactly one position and evaluate using the already-fitted response-coordinate decoder. No random permutation.

## 10. Leakage rule

Coordinate construction and decoder fitting may access only:

- raw train-state parameters for baselines;
- calibration responses `C_cal` for train and test states where required to construct `z_resp`;
- intervention descriptors.

Held-out responses may not be used for PCA, preprocessing, fitting, threshold selection, baseline design, or prediction generation.

Prediction generation and held-out evaluation must be separate callable stages.

## 11. Frozen metrics

Primary metric:

`R2_state = 1 - SSE/SST`,

with

`SSE = sum_{c in C_hold} sum_{s in S_test} ||Gamma_hat(s,c)-Gamma(s,c)||^2`,

`SST = sum_{c in C_hold} sum_{s in S_test} ||Gamma(s,c)-mean_{s' in S_test} Gamma(s',c)||^2`.

The held-out mean is evaluation-only.

Also report per-held-out-intervention `R2_state(c)`.

Secondary metric:

`NRMSE = sqrt(SSE / sum ||Gamma||^2)`

over all held-out state/intervention pairs.

## 12. Frozen classification thresholds

Mandatory sanity conditions:

- current-function equality error over all states `<=1e-12`;
- frozen norm identities within `1e-12`;
- analytical/autograd one-step responses agree within `1e-12` for all 81 states x 12 interventions;
- oracle C1 maximum absolute error `<=1e-12`;
- full fingerprint ceiling C0 aggregate `R2_state >=0.99`;
- no leakage test fails;
- unchanged prior APP-A regression tests pass.

Any failed sanity condition => `FAIL`.

Define:

`R_resp` = response-coordinate aggregate `R2_state`;
`R_func` = B0;
`R_norm` = B1;
`R_raw2` = B2;
`R_null` = N0;
`R_min` = minimum per-held-out-intervention response-coordinate `R2_state(c)`.

Classification is applied in this precedence order after sanity: `PASS`, then `WEAK`, otherwise `NULL`.

### PASS

All of:

- `R_resp >=0.95`;
- `R_min >=0.90`;
- `R_resp-R_func >=0.25`;
- `R_resp-R_norm >=0.20`;
- `R_resp-R_raw2 >=0.05`;
- `R_null <=0.10`.

### WEAK

PASS is not satisfied, but all of:

- `R_resp >=0.90`;
- `R_min >=0.75`;
- `R_resp-R_func >=0.10`;
- `R_resp-R_norm >=0.10`;
- `R_resp-R_raw2 > -0.05`;
- `R_null <=0.25`.

Interpretation: compact held-out prediction works, but special value beyond the equal-dimensional raw-state baseline or across every intervention is not strong enough for PASS.

### NULL

All sanity conditions pass, but neither PASS nor WEAK applies. In particular, a clear raw-state loss of `R_resp-R_raw2 <= -0.05`, poor aggregate/intervention prediction, inadequate advantage over B0/B1, or a failed association null produces NULL.

Interpretation: the frozen compact response-coordinate direction does not provide the intended predictive advantage and is materially weakened.

### FAIL

Any mandatory sanity, implementation, leakage, regression, or numerical-validity condition fails.

No threshold may change after held-out inspection.

## 13. Numerical/software freeze

Permitted stack only:

- Python 3;
- NumPy;
- PyTorch;
- pytest;
- Python standard library.

Use float64 throughout.

No scikit-learn dependency. No random seed is required because the entire pipeline is deterministic.

## 14. Required paths

Execution prompt:
`research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`

Implementation:
`src/causal_synergetics/benchmarks/neural_response_coordinate.py`

Tests:
`tests/test_neural_response_coordinate_pilot.py`

Canonical result:
`research/app_a/neural_response_coordinate_pilot_0_1.md`

## 15. Anti-retuning freeze

After execution begins, APP-A may not change model dimensions, state family/grid/rho/split, intervention sets, response, optimizer, learning rate, horizon, coordinate dimension/PCA, decoder, baselines, ceilings/null, preprocessing, metrics, thresholds, or numerical tolerances.

No second coordinate or alternative state family is authorised after WEAK/NULL/FAIL.

## 16. Claim ceiling

This specification does not establish a causal/plasticity coordinate and carries no novelty promotion.

Even a future PASS supports only the frozen synthetic-family statement. It does not establish generic nonlinear scaling, natural SGD history, real-data usefulness, LoRA/transformer relevance, controlled state preparation, or field-level causal synergetics.

## 17. Decision

**SPECIFICATION FROZEN / APP-A READY**

The next execution must use only the versioned APP-A prompt and return to MASTER after result freeze.
