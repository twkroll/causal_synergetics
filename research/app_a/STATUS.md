# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Minimal Benchmark 0.1`
Status: READY / AWAIT GO
Latest canonical file: `research/master/prompts/app_a_neural_minimal_benchmark_0_1.md`
Dependencies: `CORE Synergetic Sufficiency Boundary 0.1` COMPLETE / PASS — CLAIM-RESTRICTED
Next instruction: Execute only the frozen task in `research/master/prompts/app_a_neural_minimal_benchmark_0_1.md` after the chat start text is installed and the user enters `GO`.
STOP boundary: Do not change the frozen model, state pair, tasks, learning rate, horizon, response metrics, or success criteria; do not open nonlinear, historical-reachability, learned-representation, LoRA, power-grid, or manuscript work without new MASTER authorisation.

## Frozen benchmark specification

- Model: factorised linear network `f_{U,v}(x)=v^T U x`, `d=h=2`.
- State A: `v=(1,0)`, `U=[[0,0],[1,0]]`.
- State B: `v=(1,0)`, `U=[[0,0],[0,1]]`.
- Current effective function: `w=U^T v=0` for both.
- Tasks: `c_C=e1`, `c_D=e2`, loss `0.5||w-c||^2`.
- Intervention: one simultaneous full-batch GD step in `(U,v)`.
- Learning rate: `eta=0.1`.
- Horizon: one optimizer step.
- Primary response: `w^+`.
- Secondary response: post-step task loss.
- No parameter/task/model search permitted.

## Pre-specified expected values

- Task C: `w_A^+=(0.2,0)`, `w_B^+=(0.1,0)`; losses `0.32` and `0.405`.
- Task D: `w_A^+=(0,0.1)`, `w_B^+=(0,0.2)`; losses `0.405` and `0.32`.

These values are frozen before execution and must not be changed if code disagrees.

## Claim ceiling

This gate is a reproducible feasibility benchmark only. It carries no novelty promotion and does not establish causal synergetics, a universal causal/plasticity coordinate, nonlinear generalisation, or historical reachability.

STOP — AWAIT GO
