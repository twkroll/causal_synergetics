# Project Status — causal_synergetics

Version: 0.6
Date: 2026-09-04
Overall status: NONLINEAR RELU PILOT FROZEN / VERTICAL-SLICE DECISION READY
Governance status: FROZEN v0.1
Latest rollback point: `RP-006 — Neural Nonlinear ReLU Pilot Result Freeze 0.1`

## Central research question

Which macroscopic description of a complex system is sufficient not only for its spontaneous dynamics, but also for predicting and controlling a defined class of interventions?

The programme treats causal synergetics as a proposed research field to be tested, not as an already established theory.

## Frozen scientific results

### 80 – LIT

`Prior-Art & Definitions Audit 0.1`: `PASS — CLAIM-RESTRICTED`; programme action `RESTRICT / REINTERPRET`.

Generic novelty claims for intervention-conditioned state descriptors, controlled behavioral equivalence, intervention-sufficient representations, and controlled closure/lumpability remain demoted as prior-art territory.

### 10 – CORE

`CORE Synergetic Sufficiency Boundary 0.1`: `PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`.

Frozen conclusions include the controlled-projectability boundary, failure of classical unforced slaving to imply controlled sufficiency, a minimal slow/fast counterexample, and finite-horizon bridge bounds without novelty promotion.

### 50 – APP-A — Neural Minimal Benchmark 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

Two factorised-linear states with identical current function and matched simple norms exhibit opposite symmetric one-step learning preferences. Analytic/autograd agreement is exact in the frozen float64 run; local tests reported `4 passed`; no retuning occurred.

### 50 – APP-A — Neural Historical Reachability 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

One pre-specified symmetric auxiliary-gradient preparation from common initialization reaches the exact frozen A/B states while preserving the main function. Prior C/D responses reproduce; combined local tests reported `8 passed`; no alternative history was tried.

### 50 – APP-A — Neural Nonlinear ReLU Pilot 0.1

Decision: `PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`.
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.

Frozen observations:

- two bias-free two-unit ReLU parameterisations are globally function-equivalent by positive homogeneity;
- simple norms match;
- strict activation margins avoid derivative-at-zero ambiguity;
- Task C: A loss `0.14045`, B loss `0.2312`;
- Task D: A loss `0.2312`, B loss `0.14045`;
- symmetric directed advantage `0.09075`;
- analytical/autograd maximum observed component difference `0.0` in float64;
- combined unchanged linear/history/ReLU regression run: `12 passed`;
- no alternate scaling, task, state pair, optimizer, probe set, tolerance, or horizon was tried.

Allowed interpretation only: in this single frozen nonlinear symmetry pair, globally function-equivalent parameterisations can have different symmetric one-step learning responses. No generic nonlinear or novelty claim is licensed.

## Integration state

The first neural vertical slice now contains five frozen stages:

1. prior-art/definitions restriction;
2. theorem-level CORE boundary;
3. exact linear function-insufficiency benchmark;
4. one explicit historical reachability construction;
5. one exact nonlinear ReLU persistence pilot.

This is enough evidence to justify a formal programme-level Go/Revise/Stop review before opening a learned-coordinate or broader-scaling stage.

## Active gate

`00 – MASTER – Projektplan & Status`

Current gate: `Neural Vertical Slice Go/Revise/Stop Gate 0.1`.
Status: READY / AWAIT NAMED GATE.
Canonical prompt: `research/master/prompts/master_neural_vertical_slice_go_revise_stop_0_1.md`.

The gate must use only already-frozen evidence and choose exactly one of:

- `GO`
- `REVISE`
- `STOP`

If GO or REVISE is selected, exactly one next scientific gate may be recommended. No new experiment or branch is executed during the decision gate itself.

## Waiting / blocked branches

- `10 – CORE`: COMPLETE / FROZEN / WAIT.
- `50 – APP-A`: COMPLETE / FROZEN / WAIT.
- `20/30/40 – THEORY-*`: UNOPENED.
- `60/70 – APP-*`: UNOPENED.
- learned response/plasticity coordinates: BLOCKED pending vertical-slice decision.
- multi-step/real-data scaling: BLOCKED.
- realistic nonlinear history/reachability: BLOCKED.
- NTK/LoRA/adapter comparisons: BLOCKED.
- power-grid / ODE discovery: BLOCKED.
- controlled state preparation: BLOCKED.
- `80 – LIT`: COMPLETE / FROZEN / WAIT.
- `90 – MANUSCRIPT`: UNOPENED.

## Freeze check

OK.

The ReLU result is frozen as `RP-006`. No learned-coordinate or broader-scaling specification is yet authorised.

## Branching check

OK.

The correct next step is integration, not another empirical branch. Opening learned coordinates immediately would skip the programme-level Go/Revise/Stop checkpoint.

## Rollback

Latest stable savepoint:

`RP-006 — Neural Nonlinear ReLU Pilot Result Freeze 0.1`.

No prior freeze may be weakened by the vertical-slice decision.

## Manuscript

UNOPENED.

No manuscript claim freeze is justified.

## CI

Repository CI remains not configured. The frozen ReLU test commit had no GitHub status checks/workflow runs; the frozen local combined test run reported `12 passed`.

## Next global step

Remain in `00 – MASTER – Projektplan & Status` and enter exactly:

`Neural Vertical Slice Go/Revise/Stop Gate 0.1`

After that gate commits its integration memo and updates MASTER status, follow its single explicit handoff.
