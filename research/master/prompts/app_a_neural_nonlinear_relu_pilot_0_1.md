# Prompt — Neural Nonlinear ReLU Pilot 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `50 – APP-A – Neuronaler Minimalbenchmark`
Status: READY / AWAIT GO
Date: 2026-09-04
Dependencies satisfied by:
- `research/app_a/neural_minimal_benchmark_0_1.md` (`PASS — RESULT FROZEN`)
- `research/app_a/neural_historical_reachability_0_1.md` (`PASS — RESULT FROZEN`)

## Start / continuation rule

This task is executed in the existing APP-A chat. On `GO`, read `research/app_a/STATUS.md` first and execute only this versioned prompt.

Git is the Single Source of Truth. Do not open a new branch or chat. Do not change any frozen model, state pair, task, learning rate, probe set, horizon, metric, tolerance, or success criterion after inspecting results. Do not promote novelty.

---

# Authorised task

## Name

`Neural Nonlinear ReLU Pilot 0.1`

## Purpose

Test whether the already-demonstrated principle — function-equivalent parameter states can have different frozen learning responses — survives in a genuinely nonlinear neural model under a fully pre-specified symmetry construction.

This is a nonlinear feasibility pilot only. Positive-homogeneity symmetries and parameterisation-dependent gradient dynamics have prior art; success carries `NO NOVELTY PROMOTION`.

## Frozen nonlinear model

Use the bias-free two-layer scalar-output ReLU network

`f_{U,v}(x) = v^T ReLU(Ux)`

with input dimension `d=2`, hidden width `h=2`, rows of `U` denoted `u_1^T,u_2^T`, and elementwise ReLU.

All numerical work must use PyTorch float64.

## Frozen function-equivalent states

State A:

`U_A = [[2,0],[0,1]]`

`v_A = (1/2, 1)^T`

State B:

`U_B = [[1,0],[0,2]]`

`v_B = (1, 1/2)^T`

By positive homogeneity of ReLU, both states represent exactly the same global current function

`f_A(x)=f_B(x)=ReLU(x_1)+ReLU(x_2)`

for all `x in R^2`.

Simple norms are also frozen and matched:

`||U_A||_F = ||U_B||_F = sqrt(5)`

`||v_A||_2 = ||v_B||_2 = sqrt(5/4)`.

No alternative state pair may be tried.

## Frozen tasks

Task C consists of the single regression sample

`x_C=(1,-1)^T`, `y_C=2`.

Task D consists of the single regression sample

`x_D=(-1,1)^T`, `y_D=2`.

Loss for either task:

`L = 1/2 (f(x)-y)^2`.

At the frozen initial states, exactly one hidden unit is active on each task with a strict activation margin; no ReLU derivative at zero is involved.

## Frozen intervention

Exactly one simultaneous full-batch gradient-descent step on all entries of `(U,v)`.

Learning rate:

`eta = 0.1`.

No momentum, weight decay, stochastic minibatching, optimizer state, clipping, noise, or extra step.

Horizon: exactly one optimizer step.

## Frozen probe set and response

After the one-step task intervention, evaluate the network on the ordered probe set

1. `x_C=(1,-1)`
2. `x_D=(-1,1)`
3. `x_S=(1,1)`
4. `x_N=(-1,-1)`.

Primary response:

`Gamma_primary(state, task) = [f^+(x_C), f^+(x_D), f^+(x_S), f^+(x_N)]`.

Secondary response:

post-step loss on the task sample.

Before any update, both states must give the common probe vector

`[1,1,2,0]`.

## Frozen analytical predictions

For an active hidden unit with positive scaling `a`, current contribution `v ReLU(u^T x)=1`, `u=a e_j`, `v=1/a`, and frozen task input norm `||x||^2=2`, the one-step task output is

`f^+(x)=1 + eta (a^2 + 2/a^2) + 2 eta^2`.

With `eta=0.1`:

- high scaling `a=2` gives task output `1.47` and post-step loss `0.14045`;
- low scaling `a=1` gives task output `1.32` and post-step loss `0.2312`.

Therefore the frozen expected responses are:

### Task C

State A:

`Gamma_primary = [1.47, 1.0, 2.4, 0.0]`

post-step loss `0.14045`.

State B:

`Gamma_primary = [1.32, 1.0, 2.1, 0.0]`

post-step loss `0.2312`.

### Task D

State A:

`Gamma_primary = [1.0, 1.32, 2.1, 0.0]`

post-step loss `0.2312`.

State B:

`Gamma_primary = [1.0, 1.47, 2.4, 0.0]`

post-step loss `0.14045`.

Directed loss advantage magnitude is frozen at

`0.2312 - 0.14045 = 0.09075`

in both directions.

## Required implementation

Add a minimal implementation and tests without modifying the frozen linear/history results.

Suggested paths:

`src/causal_synergetics/benchmarks/neural_relu.py`

`tests/test_neural_relu_pilot.py`

The implementation must include:

1. construction of frozen states A/B;
2. exact current-function/probe verification;
3. an independently coded analytical one-step update for the frozen tasks;
4. a PyTorch autograd one-step update;
5. frozen probe-vector evaluation;
6. regression checks that the prior linear/history tests still pass.

## Frozen tolerances

Absolute tolerance for analytic/autograd equality and all frozen expected values:

`1e-12`.

No tolerance widening is allowed after execution begins.

## Frozen success criteria

PASS requires all of the following:

1. **Global current-function equivalence is analytically proved** by ReLU positive homogeneity, and the frozen probe vectors agree numerically within `1e-12`.
2. **Simple norm symmetry** matches the frozen values within `1e-12`.
3. **Activation-margin check:** the intended active unit has strictly positive preactivation and the inactive unit strictly negative preactivation on each frozen task before and after the step.
4. **Analytic/autograd agreement:** every tested updated parameter/probe component agrees within `1e-12`.
5. **Directed nonlinear crossing:** on Task C, A has lower post-step loss than B; on Task D, B has lower post-step loss than A, with the exact frozen expected values above.
6. **Symmetry:** the two directed loss advantages agree within `1e-12` and equal `0.09075` within tolerance.
7. **No retuning:** no alternative states, tasks, learning rates, probe sets, horizons, optimizers, or response definitions are tried.
8. **Regression safety:** all previously frozen APP-A tests still pass unchanged.

If any criterion fails, record `FAIL — RESULT FROZEN`. Do not repair the pilot by changing the specification.

## Required deliverable

Create:

`research/app_a/neural_nonlinear_relu_pilot_0_1.md`

It must contain:

1. executive verdict;
2. exact reproduction of frozen specification;
3. analytical function-equivalence proof;
4. analytical one-step derivation;
5. numerical/autograd results;
6. frozen probe-response table;
7. success-criteria table;
8. PASS/FAIL classification;
9. explicit interpretation ceiling;
10. code/test paths and commit hashes;
11. CI status;
12. explicit STOP.

## Interpretation ceiling

If PASS, the strongest allowed statement is:

> In this frozen two-unit ReLU pilot, two globally function-equivalent and simple-norm-matched parameterisations exhibit different one-step learning responses under symmetric tasks, with the preferred state reversing across the task pair.

This does not establish novelty, generic nonlinear behaviour, realistic training-history reachability, learned causal/plasticity coordinates, LoRA/transformer claims, or causal synergetics.

## Forbidden actions

Do not:

- change the ReLU architecture or add bias;
- search alternative scaling factors;
- change tasks or probe points;
- alter `eta=0.1` or the one-step horizon;
- use multiple random seeds or parameter sweeps;
- add regularisation or another optimizer;
- run real-data experiments;
- learn a representation;
- open LoRA, power-grid, state-preparation, or manuscript work;
- promote novelty.

## Final handoff

After committing the deliverable:

1. update `research/app_a/STATUS.md` with the result classification and commit hash;
2. set `Next instruction: RETURN TO MASTER`;
3. report CI status if applicable;
4. end exactly with:

`STOP — RETURN TO MASTER`

The user then returns to `00 – MASTER` and enters:

`Status?`
