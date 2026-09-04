# Prompt — APP-A Neural Response Coordinate Nuisance-Invariance Pilot 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-04
Dependency: `research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md` (`SPECIFICATION FROZEN / APP-A READY`)

## Name

`Neural Response Coordinate Nuisance-Invariance Pilot 0.1`

## Purpose

Execute exactly the frozen nuisance-invariance benchmark specified in:

`research/master/neural_response_coordinate_nuisance_invariance_specification_0_1.md`.

Do not modify, optimize, repair, replace, or reinterpret the specification.

The scientific question is restricted to whether the already-fixed 2D response-aware coordinate remains predictive/invariant under the exact hidden-basis `SO(2)` gauge nuisance and whether it materially outperforms naive equal-dimensional raw-parameter PCA, while an explicitly gauge-aware Gram-PCA control is evaluated fairly.

No novelty promotion is permitted.

## Mandatory frozen specification

Use exactly:

- model `f_{U,v}(x)=v^T Ux`, `d=4`, `h=5`;
- canonical 9x9 response-latent grid, `rho=0.5`;
- canonical base states with `v0=e1`, first row `U0=0`, rows 2–5 `diag(sqrt(q1),...,sqrt(q4))`;
- hidden gauge `Q(phi)=R(phi)⊕I3` acting as `(U,v)->(QU,Qv)`;
- exactly eight angles `phi_j=j*pi/4`, `j=0,...,7`;
- total 648 states;
- exact four state partitions from latent parity and nuisance-angle parity: `164/164/160/160` for `S_train/S_nuis/S_latent/S_joint`;
- four frozen Hadamard calibration interventions;
- eight frozen held-out interventions in the frozen order;
- exactly one simultaneous full-batch GD step at `eta=0.1`;
- response `Gamma=Delta w=w^+`;
- exact 16D calibration fingerprint;
- train-only PCA to exactly `k=2` for candidate response coordinate;
- same fixed bilinear OLS decoder `phi(r,c)=[c,r1*c,...]`;
- B0 current-function baseline;
- B1 six fixed simple summaries;
- B2 naive 2D raw-parameter PCA on `theta=[vec(U),v]`;
- B3 symmetry-aware 2D Gram PCA on `g=[vech(U^TU),||v||^2]`;
- C0 full-fingerprint ceiling;
- C1 analytical-operator oracle;
- N0 deterministic cyclic state-association null;
- primary joint held-out `R2_state`, partition diagnostics, per-intervention R2, NRMSE;
- frozen nuisance fraction `J_nuis=W/(W+B)` exactly as specified;
- all frozen sanity conditions, thresholds and tolerances;
- float64 with Python/NumPy/PyTorch/pytest only.

The specification memo is controlling if any wording here is abbreviated.

## Required analytical checks

Before scientific classification, verify analytically and numerically:

`w(QU,Qv)=w(U,v)`;

`U'^T U'=U^T U`;

`||v'||=||v||`;

`P'=P`;

`Gamma(s,c)=eta P c` is invariant over the full frozen gauge orbit.

Compare analytical response to independent PyTorch autograd for all `648 x 12 = 7776` state/intervention pairs.

## Leakage discipline

Only `S_train` may fit PCA directions, standardization statistics and decoders.

Candidate calibration responses may be used to construct coordinates for evaluation states, exactly as frozen.

Held-out intervention response truth must not enter PCA, preprocessing, decoder fitting, baseline construction, thresholding or prediction generation.

Prediction bundles must be generated before held-out truth is supplied to the evaluator.

## Mechanical classification

Use exactly the frozen `PASS / WEAK / NULL / FAIL` rules in the specification memo.

In particular, full PASS requires all sanity conditions plus:

- candidate joint `R2_state >=0.95`;
- candidate nuisance-only `R2_state >=0.95`;
- candidate latent-only `R2_state >=0.95`;
- minimum joint per-intervention `R2>=0.90`;
- candidate minus B2 joint aggregate `R2 >=0.10`;
- `J_nuis(candidate)<=1e-8`;
- `J_nuis(B2)-J_nuis(candidate)>=0.05`;
- joint N0 `R2<=0.10`.

B3 is a mandatory strong symmetry-aware control and must satisfy its frozen sanity threshold. A PASS does not mean response information is uniquely superior to all raw-state representations.

Do not change thresholds after inspection.

## Required implementation

Create/update only as needed:

`src/causal_synergetics/benchmarks/neural_response_coordinate_nuisance.py`

Tests:

`tests/test_neural_response_coordinate_nuisance.py`

The tests must include at least:

1. state/partition counts;
2. exact gauge orthogonality and current-function invariance;
3. exact `P` and analytical-response invariance across nuisance orbit;
4. analytical/autograd audit;
5. train-only preprocessing/fitting leakage checks;
6. candidate/B0/B1/B2/B3/C0/C1/N0 execution under frozen rules;
7. nuisance metric implementation;
8. mechanical classification;
9. regression execution of all prior unchanged APP-A tests.

## Required result

Create:

`research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`

The result must report:

- all sanity checks;
- aggregate and per-intervention prediction metrics for required partitions;
- `J_nuis` for candidate, B2 and B3;
- all baseline/control results;
- exact mechanical classification;
- no-retuning declaration;
- implementation/test commit hashes;
- local test result;
- GitHub CI/status-check state;
- strict interpretation ceiling.

After committing the canonical result, update `research/app_a/STATUS.md` to `COMPLETE / <CLASSIFICATION> — RESULT FROZEN`, set Next instruction to `RETURN TO MASTER`, and stop.

## Forbidden actions

Do not:

- alter the base family or `rho`;
- change the gauge subgroup, rotation plane, angle levels or parity split;
- change any state partition;
- change calibration/held-out interventions;
- change horizon, learning rate, optimizer or response;
- sweep coordinate dimension;
- replace PCA or decoder;
- add/drop/repair baselines or controls;
- change nuisance metric, thresholds or tolerances;
- try another gauge/nuisance construction;
- try another coordinate or state family;
- open nonlinear/multi-step/real-data/LoRA/power-grid/state-preparation/literature/manuscript work;
- claim novelty.

WEAK, NULL and FAIL are admissible frozen outcomes and must not be repaired.

## Final STOP

After result freeze and status update:

`STOP — RETURN TO MASTER`
