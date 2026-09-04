# STATUS — 00 – MASTER – Projektplan & Status

Current Gate: `Post-Specification Integration / Neural Response Coordinate Pilot 0.1`
Status: COMPLETE / WAIT FOR APP-A
Latest canonical file: `research/master/project_status.md`
Dependencies: `Neural Response Coordinate Specification Gate 0.1` COMPLETE / SPECIFICATION FROZEN
Next instruction: User returns to existing `50 – APP-A – Neuronaler Minimalbenchmark` and enters exactly `GO`; that chat must execute only `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.
STOP boundary: MASTER must not execute the pilot itself, change any frozen coordinate/baseline/split/metric/threshold, or open multi-step/real-data/realistic-history/nonlinear-scaling/LoRA/power-grid/state-preparation/literature/manuscript work before APP-A returns.

## Freeze state

- Governance: FROZEN v0.1
- MASTER baseline: FROZEN
- Prior-art audit: FROZEN / PASS — CLAIM-RESTRICTED
- CORE boundary: FROZEN / PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION
- Neural Minimal Benchmark 0.1: FROZEN / PASS
- Neural Historical Reachability 0.1: FROZEN / PASS
- Neural Nonlinear ReLU Pilot 0.1: FROZEN / PASS
- Neural Vertical Slice Decision 0.1: FROZEN / GO — CLAIM-RESTRICTED
- Neural Response Coordinate Specification 0.1: FROZEN / APP-A READY
- Latest rollback point: `RP-008 — Neural Response Coordinate Specification Freeze 0.1`

## Current scientific state

No response-coordinate result exists yet.

The next benchmark is fully pre-specified: 81 exactly function-equivalent factorised-linear states, deterministic 41/40 state split, four calibration and eight held-out interventions, a fixed 2D response-PCA coordinate, fixed bilinear decoder, current-function/norm/raw-state-PCA baselines, ceilings/null controls, fixed metrics, and disjoint PASS/WEAK/NULL/FAIL thresholds.

The principal falsification criterion is whether the 2D response-aware coordinate materially beats the equal-dimensional raw-parameter PCA baseline on held-out interventions.

## Claim ceiling

No novelty promotion is authorised.

The project still may not claim existence/usefulness of a low-dimensional causal/plasticity coordinate, held-out intervention prediction, generic nonlinear scaling, realistic SGD histories, LoRA/transformer relevance, real-data usefulness, controlled state preparation, or established causal synergetics.

## Branch state

- 00 – MASTER: COMPLETE / WAIT FOR APP-A
- 10 – CORE: COMPLETE / FROZEN / WAIT
- 20/30/40 – THEORY-*`: UNOPENED
- 50 – APP-A: READY / AWAIT GO — Neural Response Coordinate Pilot 0.1
- 60/70 – APP-*`: UNOPENED
- 80 – LIT: COMPLETE / FROZEN / WAIT
- 90 – MANUSCRIPT: UNOPENED

## Active blocker

Operational only: APP-A has not yet executed the frozen response-coordinate pilot.

## Return protocol

After APP-A reaches `STOP — RETURN TO MASTER`, the next MASTER command is:

`Status?`

STOP — WAIT
