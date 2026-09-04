# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Response Coordinate Pilot 0.1`
Status: READY / AWAIT GO
Latest frozen prior result: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`
Dependencies:
- `Neural Minimal Benchmark 0.1` COMPLETE / FROZEN
- `Neural Historical Reachability 0.1` COMPLETE / FROZEN
- `Neural Nonlinear ReLU Pilot 0.1` COMPLETE / FROZEN
- `Neural Vertical Slice Go/Revise/Stop Gate 0.1` COMPLETE / GO / FROZEN
- `Neural Response Coordinate Specification Gate 0.1` COMPLETE / SPECIFICATION FROZEN
Next instruction: execute only `research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md` when the user enters `GO`.
STOP boundary: Do not alter any frozen model/state/split/intervention/coordinate/baseline/metric/threshold; do not open multi-step/real-data/realistic-history/nonlinear-scaling/LoRA/power-grid/state-preparation/literature/manuscript work; after result freeze return to MASTER.

## Frozen prior chain

### Neural Minimal Benchmark 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### Neural Historical Reachability 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.

### Neural Nonlinear ReLU Pilot 0.1
`PASS — RESULT FROZEN / NO NOVELTY PROMOTION`.
Canonical result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.

## Current frozen execution specification

Canonical specification:
`research/master/neural_response_coordinate_specification_gate_0_1.md`.

Canonical execution prompt:
`research/master/prompts/app_a_neural_response_coordinate_pilot_0_1.md`.

Latest rollback point:
`RP-008 — Neural Response Coordinate Specification Freeze 0.1`.

Frozen essentials:

- 81 exactly function-equivalent factorised-linear states (`d=4,h=5`);
- deterministic 41/40 train/test state split;
- four calibration and eight held-out learning interventions;
- one full-batch GD step, `eta=0.1`;
- 16D calibration fingerprint compressed to exactly 2D by train-only PCA;
- fixed bilinear OLS decoder;
- mandatory B0 current-function, B1 simple-norm/state-summary, B2 equal-dimensional raw-parameter PCA baselines;
- full-fingerprint and analytical-operator ceilings;
- deterministic cyclic state-association null;
- fixed leakage rule, metrics, tolerances and disjoint PASS/WEAK/NULL/FAIL thresholds;
- no second coordinate/family or threshold repair after held-out inspection.

The principal PASS discriminator is a material `>=0.05` aggregate `R2_state` advantage over B2, in addition to the other frozen conditions.

## Claim ceiling

No response-coordinate result exists yet.

Do not claim a useful low-dimensional causal/plasticity coordinate, held-out intervention prediction, generic nonlinear scaling, realistic SGD reachability, LoRA/transformer relevance, real-data scaling, controlled state preparation, novelty, or established causal synergetics.

## Final protocol

After execution, commit implementation/tests/result, update this STATUS with exact PASS/WEAK/NULL/FAIL classification and commit hashes, set `Next instruction: RETURN TO MASTER`, report CI status if applicable, and end:

`STOP — RETURN TO MASTER`

STOP — AWAIT GO
