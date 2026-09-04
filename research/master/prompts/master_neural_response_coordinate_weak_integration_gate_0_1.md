# Prompt — Neural Response Coordinate WEAK Integration Gate 0.1

Authorised by: `00 – MASTER – Projektplan & Status`
Assigned chat: `00 – MASTER – Projektplan & Status`
Status: READY / AWAIT NAMED GATE
Date: 2026-09-04
Dependency: `Neural Response Coordinate Pilot 0.1` COMPLETE / WEAK / RESULT FROZEN

## Name

`Neural Response Coordinate WEAK Integration Gate 0.1`

## Purpose

Integrate the frozen WEAK result of `Neural Response Coordinate Pilot 0.1` without repairing or re-running it, and choose exactly one programme action: `GO`, `REVISE`, or `STOP` for the neural response-coordinate direction.

This is an integration/governance gate only. It must not run experiments, search a new state family, change the coordinate, tune a baseline, alter thresholds, reopen prior freezes, or promote novelty.

## Frozen evidence

Use only the canonical frozen project state through:

`RP-009 — Neural Response Coordinate Result Freeze 0.1`.

Mandatory result facts to preserve:

- candidate 2D response coordinate aggregate held-out `R2_state = 1.0`;
- minimum held-out intervention `R2_state(c)=1.0`;
- B0 current-function baseline approximately `0.0`;
- B1 simple-summary baseline `0.070803629370716`;
- B2 equal-dimensional raw-parameter PCA baseline `0.999883026432542`;
- response-coordinate margin over B2 `0.000116973567458323`, below the frozen PASS requirement `0.05`;
- null control `R2_state=-0.2`;
- all sanity, leakage, oracle, numerical and regression conditions passed;
- classification mechanically `WEAK`, with no retuning.

## Required evaluation dimensions

Evaluate at least:

1. **Predictive success** — the response-aware coordinate predicts held-out interventions essentially exactly.
2. **Discriminative failure** — the equal-dimensional raw-state PCA baseline is also essentially exact, so special response-aware value is not established.
3. **Mechanistic diagnosis** — distinguish what is directly shown from the plausible explanation that the frozen synthetic state family has an intrinsically low-dimensional raw-parameter geometry.
4. **Claim ceiling** — preserve the prior-art restriction and forbid promotion to a generally useful causal/plasticity coordinate.
5. **Falsifiability** — decide whether there is one next pre-specifiable test whose failure would materially weaken the coordinate direction.
6. **Anti-cherry-picking** — reject any next step whose only rationale is to engineer a family where B2 is known in advance to fail.
7. **Value of information** — compare a stricter discriminative synthetic control, nonlinear/multi-step extension, realistic-history work, and stopping/parking the coordinate direction.
8. **Programme coherence** — determine whether the neural vertical slice remains worth continuing under its current claim-restricted framing.

## Required decision

Choose exactly one:

### GO

Use only if the WEAK result still justifies a separately frozen next scientific gate without first repairing the coordinate claim. Select exactly one next gate.

### REVISE

Use if the programme remains viable but one specific prerequisite must be addressed before any broader neural claim. Select exactly one prerequisite/gate.

### STOP

Use if the frozen evidence is insufficient to justify further investment in the response-coordinate direction under the current programme framing. Preserve all prior results and park the direction.

## Required deliverable

Create:

`research/master/neural_response_coordinate_weak_integration_0_1.md`

It must contain:

1. Executive decision: GO / REVISE / STOP.
2. Frozen evidence table.
3. What the WEAK result establishes.
4. What it explicitly does not establish.
5. Diagnosis of the near-tie with B2, clearly separating result from inference.
6. Updated claim ceiling.
7. Exactly one next scientific gate, or STOP.
8. Reasons for rejecting the main alternatives.
9. Rollback/branch recommendation.
10. Exact next user command.

## Forbidden actions

Do not:

- rerun or repair the frozen pilot;
- change its family, split, coordinate, dimensionality, decoder, baselines, metrics, thresholds, or nulls;
- inspect a new candidate family;
- open multiple parallel next steps;
- open LoRA, power-grid, state-preparation, literature, or manuscript work during this gate;
- claim novelty.

## Final handoff

After committing the integration memo, update MASTER status and Decision & Branch Log. End with exactly one next user action.
