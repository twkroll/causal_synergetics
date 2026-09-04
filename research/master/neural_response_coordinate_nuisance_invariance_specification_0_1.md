# Neural Response Coordinate Nuisance-Invariance Specification 0.1

Status: COMPLETE / SPECIFICATION FROZEN
Assigned chat: `00 – MASTER – Projektplan & Status`
Date: 2026-09-04
Dependency: `RP-010 — Neural Response Coordinate WEAK Integration Freeze 0.1`
Decision: **SPECIFICATION FROZEN / APP-A READY / NO NOVELTY PROMOTION**

## 1. Executive decision

A scientifically neutral nuisance-invariance benchmark can be specified without effect-guided family search.

The nuisance is the exact orthogonal hidden-basis gauge symmetry of the factorised linear model. For any orthogonal hidden-space matrix `Q`,

`(U,v) -> (QU,Qv)`

leaves both the current function

`w=U^T v`

and the exact one-step response operator

`P=U^T U + ||v||^2 I`

unchanged, while generally changing the raw parameter vector nontrivially.

This symmetry exists independently of any anticipated PCA result. It therefore satisfies the anti-cherry-picking requirement of the authorised gate.

The new pilot freezes one canonical one-parameter subgroup `SO(2)` acting in the first two hidden coordinates, sampled at eight equally spaced angles over one full orbit. No alternative nuisance family or amplitude is permitted.

The benchmark is designed to distinguish three claims:

1. whether the response-aware coordinate remains predictive under unseen gauge orientations;
2. whether naive equal-dimensional raw-parameter PCA remains equally predictive;
3. whether an explicitly gauge-aware raw-state representation can recover the same information, preventing any false claim that response measurements contain uniquely unavailable information.

A future PASS may support only gauge-invariance value relative to naive raw-parameter coordinates. It will not establish unique superiority over all raw-state representations, because a symmetry-aware Gram baseline is frozen as a strong control.

No benchmark was executed and no held-out outcome was inspected during this specification gate.

## 2. Frozen model and canonical response-relevant family

Use the same factorised linear model class as the prior response-coordinate pilot:

`f_{U,v}(x)=v^T Ux`,

with input dimension `d=4`, hidden width `h=5`, `U in R^{5x4}` and `v in R^5`.

Define the canonical base state for response latents `(z1,z2)` by

`v0=e1`,

first row of `U0` equal to zero, and rows 2–5 given by

`diag(sqrt(q1),sqrt(q2),sqrt(q3),sqrt(q4))`,

with

`rho=0.5`,

`q1=1+rho z1`,
`q2=1-rho z1`,
`q3=1+rho z2`,
`q4=1-rho z2`.

The response-latent grid is frozen as

`z1,z2 in {-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1}`,

for 81 distinct response-relevant base states, ordered lexicographically by `(z1,z2)`.

As before:

- `w=U0^T v0=0`;
- `||U0||_F=2`;
- `||v0||_2=1`;
- `P0(z1,z2)=diag(2+rho z1,2-rho z1,2+rho z2,2-rho z2)`.

No alternative base state family, grid or `rho` is allowed.

## 3. Frozen nuisance/gauge family

Use exactly the hidden-space rotation

`Q(phi)=R(phi) ⊕ I_3`,

where

`R(phi)=[[cos(phi),-sin(phi)],[sin(phi),cos(phi)]]`.

For every canonical base state define

`U(z1,z2,phi)=Q(phi) U0(z1,z2)`,

`v(phi)=Q(phi) v0`.

Freeze exactly eight nuisance levels:

`phi_j = j*pi/4`, for `j=0,...,7`.

These are the eight equally spaced orientations on one complete `SO(2)` orbit. They are selected as a canonical finite discretisation of the exact gauge orbit, not from any empirical comparison.

Total state count:

`81 x 8 = 648` states.

## 4. Exact nuisance invariants

For every frozen `(z1,z2,phi)` state, because `Q(phi)^T Q(phi)=I`,

`w(phi)=(QU0)^T(Qv0)=U0^T v0=0`.

Also

`U(phi)^T U(phi)=U0^T Q^T Q U0=U0^T U0`,

and

`||v(phi)||_2=||v0||_2=1`.

Therefore

`P(phi)=U(phi)^T U(phi)+||v(phi)||^2 I=P0`.

Thus the exact frozen one-step response semantics defined below are independent of `phi` for all interventions.

These invariance identities are mandatory analytical sanity checks, not empirical hypotheses.

## 5. Frozen state partitions

Index response-latent grid points by `(i,j) in {0,...,8}^2` in ascending coordinate order.

Define response-latent parity:

`E_z = {(i,j): (i+j) mod 2 = 0}` with 41 latent states;

`O_z = {(i,j): (i+j) mod 2 = 1}` with 40 latent states.

Define nuisance parity:

`E_phi={0,2,4,6}` corresponding to `phi in {0,pi/2,pi,3pi/2}`;

`O_phi={1,3,5,7}` corresponding to `phi in {pi/4,3pi/4,5pi/4,7pi/4}`.

Freeze four disjoint partitions:

- `S_train = E_z x E_phi`: 164 states;
- `S_nuis = E_z x O_phi`: 164 states, nuisance-only generalisation;
- `S_latent = O_z x E_phi`: 160 states, latent-only generalisation;
- `S_joint = O_z x O_phi`: 160 states, joint held-out generalisation.

Only `S_train` may be used to fit PCA directions, preprocessing statistics or decoder parameters.

Primary scientific prediction evaluation is on `S_joint`.

`S_nuis` and `S_latent` are mandatory secondary diagnostic partitions and may not be promoted to primary after inspection.

## 6. Frozen intervention family and response

Use exactly the same learning intervention semantics as the prior response-coordinate pilot.

For `c in R^4`,

`L_c(w)=1/2 ||w-c||_2^2`.

Intervention: exactly one simultaneous full-batch gradient-descent step on all entries of `(U,v)` with

`eta=0.1`.

No momentum, weight decay, stochasticity, clipping, noise, optimizer state or extra step.

Horizon: exactly one optimizer step.

Primary response:

`Gamma(s,c)=Delta w=w^+` because `w=0` initially.

Exact audit relation:

`Gamma(s,c)=eta P(s)c`.

Because `P` is gauge invariant, `Gamma` is exactly nuisance invariant for fixed `(z1,z2,c)`.

## 7. Frozen intervention split

Calibration interventions `C_cal` are exactly the normalized Hadamard basis:

`t1=(1,1,1,1)/2`
`t2=(1,1,-1,-1)/2`
`t3=(1,-1,1,-1)/2`
`t4=(1,-1,-1,1)/2`.

Held-out interventions `C_hold`, in fixed order:

`h1=e1`
`h2=e2`
`h3=e3`
`h4=e4`
`h5=(e1+e3)/sqrt(2)`
`h6=(e2+e4)/sqrt(2)`
`h7=(e1-e4)/sqrt(2)`
`h8=(e2-e3)/sqrt(2)`.

No intervention may move between sets.

## 8. Frozen candidate response-aware coordinate

For every state, form the same 16D calibration fingerprint

`F(s)=concat[Gamma(s,t1),Gamma(s,t2),Gamma(s,t3),Gamma(s,t4)]`.

Fit PCA using only fingerprints from `S_train`:

1. subtract the `S_train` mean fingerprint;
2. deterministic full float64 SVD;
3. retain exactly `k=2` right-singular directions;
4. no explained-variance choice and no dimension sweep;
5. project all four state partitions using these fixed directions;
6. standardize retained scores by `S_train` population mean/std; zero-variance scale is `1`.

Call the resulting coordinate `z_resp(s) in R^2`.

Because the calibration responses are analytically gauge invariant, nuisance invariance of `z_resp` is expected from the model identity but must still be numerically audited.

## 9. Frozen decoder

For any state representation `r in R^k` and intervention `c in R^4`, use

`phi(r,c)=[c,r1*c,...,rk*c]`.

Fit a multi-output ordinary least-squares decoder to `Gamma` using only

`S_train x C_cal`.

Use float64 `numpy.linalg.lstsq(..., rcond=None)` with no regularization and no tuned intercept beyond the explicit base `c` block.

Use the same decoder family for candidate and competitive baselines.

## 10. Frozen raw-state baselines

### B0 — current-function baseline

State feature: current `w in R^4`, identically zero.

### B1 — simple summary baseline

Exactly six features:

1. `||U||_F`;
2. `||v||_2`;
3. spectral norm `||U||_2`;
4. nuclear norm `||U||_*`;
5. maximum row Euclidean norm of `U`;
6. minimum nonzero row Euclidean norm of `U`.

Center/standardize on `S_train`; zero-variance scale `1`.

### B2 — naive equal-dimensional raw-parameter PCA

Flatten

`theta=[vec(U),v] in R^25`.

Fit train-only PCA by the same centering/full-SVD procedure, retain exactly `k=2`, project all partitions, and standardize using `S_train` statistics.

This is the principal generic raw-coordinate comparator.

### B3 — symmetry-aware equal-dimensional Gram PCA control

Construct the explicitly gauge-invariant raw-state feature

`g(s)=[vech(U^T U), ||v||_2^2] in R^11`,

where `vech` lists the upper triangle of the symmetric `4x4` matrix in fixed row-major upper-triangular order.

Fit train-only PCA on `g`, retain exactly `k=2`, project all partitions and standardize from `S_train` statistics.

Use the same bilinear decoder.

B3 is a mandatory strong control, not a target to be defeated by construction. It tests whether an explicitly symmetry-aware raw-state quotient can remain equally adequate. A future PASS may therefore claim advantage over naive raw parameter coordinates under gauge nuisance, but not unique information unavailable from symmetry-aware raw-state features.

No other raw-state baseline may be added after execution.

## 11. Frozen ceilings and null controls

### C0 — full calibration fingerprint ceiling

Use the complete centered/standardized 16D `F(s)` with the same decoder.

### C1 — analytical response operator oracle

Predict `Gamma_oracle=eta P c` using exact `P=U^T U+||v||^2 I`.

Maximum absolute oracle/autograd discrepancy must be `<=1e-12`.

### N0 — state-association null

On each evaluation partition separately, order states lexicographically by `(z1,z2,phi-index)` and cyclically shift fitted `z_resp` assignments by exactly one state while keeping interventions and true responses fixed. Use the already fitted response-coordinate decoder.

No random permutation is used.

## 12. Frozen leakage rule

Candidate coordinate construction may use calibration responses for any state whose coordinate is being formed, but no held-out `C_hold` response may enter:

- PCA fitting;
- standardization fitting;
- decoder fitting;
- baseline construction;
- threshold definition;
- prediction generation.

Only `S_train` may determine PCA directions and preprocessing/decoder parameters.

The evaluator must generate held-out response truth only after prediction bundles are fixed.

## 13. Frozen predictive metrics

For each evaluation partition `D in {S_nuis,S_latent,S_joint}`, compute aggregate

`R2_state(D)=1-SSE_D/SST_D`

across all `C_hold` interventions and states in `D`, with the held-out-state mean response computed separately for each intervention only for evaluation normalization.

Also report:

- per-held-out-intervention `R2_state(c;D)`;
- `NRMSE(D)=sqrt(SSE_D/sum ||Gamma||^2)`.

Primary predictive metric is candidate aggregate `R2_state(S_joint)`.

## 14. Frozen nuisance-invariance metric

For any 2D state representation `r(z,phi)` defined for all 648 states, compute

`mu_z = mean_phi r(z,phi)`,

`mu = mean_z mu_z`,

`W = mean_{z,phi} ||r(z,phi)-mu_z||^2`,

`B = mean_z ||mu_z-mu||^2`.

Define the nuisance fraction

`J_nuis(r)=W/(W+B)`.

If both `W` and `B` are numerically zero, classify the representation as non-informative and set `J_nuis=1` for this metric.

Interpretation:

- `J_nuis=0`: perfect invariance across gauge orbit with nonzero between-latent variation;
- larger values: more representation variance is spent on nuisance orientation.

Report `J_nuis` for candidate `z_resp`, B2 raw PCA and B3 Gram PCA.

No post-hoc rotation or Procrustes alignment is permitted before computing `J_nuis`.

## 15. Frozen sanity conditions

All must pass before scientific classification:

1. exactly 648 states and exact partition counts `164/164/160/160`;
2. current-function equality max error `<=1e-12`;
3. `||U||_F=2`, `||v||_2=1` within `1e-12`;
4. `Q(phi)^TQ(phi)=I` max error `<=1e-12`;
5. within-orbit `P` invariance max component error `<=1e-12`;
6. within-orbit analytical response invariance max component error `<=1e-12` for all 12 interventions;
7. analytical/autograd response agreement `<=1e-12` for all `648 x 12` state/intervention pairs;
8. C1 oracle error `<=1e-12`;
9. C0 aggregate `R2_state(S_joint)>=0.99`;
10. B3 symmetry-aware Gram PCA aggregate `R2_state(S_joint)>=0.95` and `J_nuis(B3)<=1e-8`;
11. leakage tests pass;
12. all prior APP-A regression tests remain unchanged and pass.

If any sanity condition fails, classification is `FAIL` rather than scientific NULL.

## 16. Frozen scientific classification

Let

`R_resp = R2_state_candidate(S_joint)`;

`R_raw2 = R2_state_B2(S_joint)`;

`R_nuis = R2_state_candidate(S_nuis)`;

`R_lat = R2_state_candidate(S_latent)`;

`R_min = minimum candidate per-intervention R2 over S_joint`;

`J_resp=J_nuis(z_resp)`;

`J_raw2=J_nuis(B2)`;

`R_null=R2_state_N0(S_joint)`.

### PASS

All sanity conditions pass and all of:

- `R_resp >= 0.95`;
- `R_nuis >= 0.95`;
- `R_lat >= 0.95`;
- `R_min >= 0.90`;
- `R_resp - R_raw2 >= 0.10`;
- `J_resp <= 1e-8`;
- `J_raw2 - J_resp >= 0.05`;
- `R_null <= 0.10`.

Interpretation ceiling for PASS:

> In this frozen factorised-linear gauge-control family, the 2D response-aware coordinate remains predictive and gauge invariant under held-out `SO(2)` reparameterisations and materially outperforms naive equal-dimensional raw-parameter PCA. An explicitly gauge-aware 2D Gram representation remains a mandatory successful control, so PASS does not establish uniquely response-specific information beyond all raw-state quotients.

### WEAK

All sanity conditions pass, candidate remains strongly predictive/invariant

- `R_resp >=0.90`;
- `R_nuis >=0.90`;
- `R_lat >=0.90`;
- `R_min >=0.75`;
- `J_resp <=1e-4`;
- `R_null <=0.25`;

but at least one PASS discriminator fails because either

- `R_resp-R_raw2 <0.10`, or
- `J_raw2-J_resp <0.05`, or
- one candidate predictive PASS threshold is missed while remaining above the WEAK floor.

Interpretation: the response coordinate is robust to gauge nuisance, but material advantage over naive raw coordinates is not established strongly enough.

### NULL

All sanity conditions pass but any of:

- `R_resp <0.90`;
- `R_nuis <0.90`;
- `R_lat <0.90`;
- `R_min <0.75`;
- `J_resp >1e-4`;
- `R_resp <= R_raw2`.

Interpretation: the frozen nuisance control does not support the intended invariance/predictive advantage and materially weakens the response-coordinate direction.

### FAIL

Any mandatory sanity, leakage, oracle, numerical or regression condition fails.

No threshold may change after held-out inspection.

## 17. Numerical/software freeze

Permitted stack only:

- Python 3;
- NumPy;
- PyTorch;
- pytest;
- Python standard library.

Use float64 throughout.

No randomness is needed; all state grids, angles, partitions, interventions, PCA procedures, OLS fits and null controls are deterministic.

## 18. Required implementation and result paths

Execution prompt:

`research/master/prompts/app_a_neural_response_coordinate_nuisance_invariance_pilot_0_1.md`

Implementation:

`src/causal_synergetics/benchmarks/neural_response_coordinate_nuisance.py`

Tests:

`tests/test_neural_response_coordinate_nuisance.py`

Canonical result:

`research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`

## 19. Anti-retuning freeze

After APP-A execution begins, do not change:

- base state family, latent grid or `rho`;
- gauge subgroup, rotation plane, angle grid or angle parity split;
- state partitions;
- intervention sets;
- learning rate, optimizer semantics or horizon;
- response functional;
- candidate dimension/construction;
- B0/B1/B2/B3 definitions;
- decoder;
- invariance metric;
- ceilings/nulls;
- metrics, thresholds or tolerances;
- software semantics.

No alternative gauge group, rotation plane, nuisance amplitude, second coordinate or second family is authorised after WEAK/NULL/FAIL.

## 20. Claim ceiling

This specification does not repair the prior WEAK result and does not establish a useful causal/plasticity coordinate.

Even a future PASS is restricted to the frozen synthetic gauge-control statement. It does not establish generic nonlinear scaling, realistic training-history relevance, real-data/LoRA/transformer usefulness, controlled state preparation, novelty, or established causal synergetics.

## 21. Decision

**SPECIFICATION FROZEN / APP-A READY**

The next execution must use only the versioned APP-A prompt and must return to MASTER after result freeze.
