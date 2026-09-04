# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Nonlinear ReLU Pilot 0.1`
Status: READY / AWAIT GO
Latest canonical result: `research/app_a/neural_historical_reachability_0_1.md`
Dependencies:
- Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
- Neural Historical Reachability 0.1 COMPLETE / FROZEN
Next instruction: execute only `research/master/prompts/app_a_neural_nonlinear_relu_pilot_0_1.md` on `GO`.
STOP boundary: Do not alter the frozen ReLU model/state pair/tasks/probes/learning rate/horizon/tolerances; do not open learned-representation, LoRA, power-grid, state-preparation, or manuscript work without new MASTER authorisation.

## Frozen prior results

### Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_minimal_benchmark_0_1.md`.

Frozen observations include identical current function `w_A=w_B=(0,0)`, matched simple norms, opposite symmetric one-step adaptation preferences, exact analytic/autograd agreement, and no retuning.

### Neural Historical Reachability 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_historical_reachability_0_1.md`.
Historical test-addition commit: `ad9cc18a0519ffcfc4e6bc2e919e82f40bf54208`.
Historical implementation commit: `e342ef5c5cefae30df45e23bc667f149e818238c`.
Canonical result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`.

Frozen observations:

- common start `U_0=0`, fixed main readout `v=e1`;
- symmetric auxiliary targets `e1/e2` with fixed auxiliary readout `a=e2`;
- exactly one `U`-only gradient step at `eta_hist=1` reaches the previously frozen A/B states exactly;
- main function remains exactly `w=0` before and after both preparations;
- historical analytic/autograd maximum observed difference `0.0` in float64;
- previously frozen C/D responses reproduce unchanged;
- local combined frozen test run `8 passed`;
- no retuning or alternate history.

Allowed interpretation remains restricted to reachability under this explicit auxiliary-gradient mechanism; no ordinary-SGD or generic reachability claim is authorised.

## Current frozen task

### Neural Nonlinear ReLU Pilot 0.1

Canonical prompt:
`research/master/prompts/app_a_neural_nonlinear_relu_pilot_0_1.md`.

Frozen model:

`f_{U,v}(x)=v^T ReLU(Ux)`, `d=h=2`, no bias.

Frozen states:

- A: `U_A=[[2,0],[0,1]]`, `v_A=(1/2,1)`;
- B: `U_B=[[1,0],[0,2]]`, `v_B=(1,1/2)`.

They are analytically globally function-equivalent by positive homogeneity and have matched simple norms.

Frozen tasks:

- C: `x=(1,-1)`, target `2`;
- D: `x=(-1,1)`, target `2`.

Frozen intervention: exactly one simultaneous full-batch GD step on `(U,v)` at `eta=0.1`.

Frozen ordered probe set:
`[(1,-1),(-1,1),(1,1),(-1,-1)]`.

Frozen expected task losses:

- C: A `0.14045`, B `0.2312`;
- D: A `0.2312`, B `0.14045`;
- directed symmetric advantage `0.09075`.

No alternative nonlinear candidate may be tried if this pilot fails.

## CI status

For the historical implementation commit, GitHub reported no status checks/workflow runs. Repository CI is not configured; frozen local historical+linear tests reported `8 passed`.

## Claim ceiling

Even if the nonlinear pilot passes, it may support only the exact frozen two-unit ReLU feasibility statement. It does not establish generic nonlinear scaling, learned response/plasticity coordinates, novelty, realistic nonlinear history, LoRA/transformer behaviour, or causal synergetics.

STOP — AWAIT GO
