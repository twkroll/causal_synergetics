# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Nonlinear ReLU Pilot 0.1`
Status: COMPLETE / PASS — RESULT FROZEN
Latest canonical result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`
Latest frozen result decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`
Dependencies:
- Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
- Neural Historical Reachability 0.1 COMPLETE / FROZEN
ReLU implementation commit: `b5ba5da30d869d160eab0a7801bcfa324860b19a`
ReLU test commit: `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`
Next instruction: `RETURN TO MASTER`
STOP boundary: Do not alter the frozen ReLU result or open learned-representation, multi-step/real-data, LoRA, power-grid, state-preparation, realistic nonlinear-history, or manuscript work without new MASTER authorisation.

## Frozen prior results

### Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.

Frozen observations include identical current function `w_A=w_B=(0,0)`, matched simple norms, opposite symmetric one-step adaptation preferences, exact analytic/autograd agreement, and no retuning.

### Neural Historical Reachability 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_historical_reachability_0_1.md`.

Frozen observations include a common start `U_0=0`, fixed main readout `v=e1`, symmetric one-step auxiliary histories reaching the exact linear A/B states while preserving the main function, exact analytic/autograd agreement, reproduction of the frozen C/D responses, and no retuning.

## Frozen nonlinear result

### Neural Nonlinear ReLU Pilot 0.1

Decision: **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**

Frozen model:

`f_{U,v}(x)=v^T ReLU(Ux)`, `d=h=2`, no bias.

Frozen states:

- A: `U_A=[[2,0],[0,1]]`, `v_A=(1/2,1)`;
- B: `U_B=[[1,0],[0,2]]`, `v_B=(1,1/2)`.

Frozen observations:

- Global current-function equivalence is proved analytically: `f_A(x)=f_B(x)=ReLU(x_1)+ReLU(x_2)` for all `x`.
- Simple norms match: `||U_A||_F=||U_B||_F=sqrt(5)` and `||v_A||_2=||v_B||_2=sqrt(5/4)`.
- Common pre-update probe vector: `[1,1,2,0]`.
- Activation signs remain strict before and after every frozen task step.
- Task C:
  - A probe response `[1.47,1.0,2.4,0.0]`, loss `0.14045`;
  - B probe response `[1.32,1.0,2.1,0.0]`, loss `0.2312`.
- Task D:
  - A probe response `[1.0,1.32,2.1,0.0]`, loss `0.2312`;
  - B probe response `[1.0,1.47,2.4,0.0]`, loss `0.14045`.
- Directed symmetric loss advantage: `0.09075` in both directions.
- ReLU analytical/autograd maximum observed tested component difference: `0.0` in float64.
- Combined unchanged linear/history plus ReLU regression run: `12 passed`.
- No retuning, alternative scaling, task, probe, optimizer, tolerance, or horizon was tried.

## CI status

For ReLU test commit `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`, GitHub reports no commit status checks and no workflow runs. Repository CI is therefore not configured / not applicable for this execution commit.

## Claim ceiling

Allowed interpretation only:

> In this frozen two-unit ReLU pilot, two globally function-equivalent and simple-norm-matched parameterisations exhibit different one-step learning responses under symmetric tasks, with the preferred state reversing across the task pair.

This does not establish novelty, generic nonlinear behaviour, realistic nonlinear training-history reachability, learned causal/plasticity coordinates, multi-step or real-data scaling, LoRA/transformer behaviour, or causal synergetics.

## Open issues

Generic nonlinear scaling, realistic nonlinear history/reachability, learned representations, multi-step/real-data experiments, LoRA/adapters, power-grid work, controlled state preparation, and manuscript work remain blocked pending new MASTER authorisation.

STOP — RETURN TO MASTER
