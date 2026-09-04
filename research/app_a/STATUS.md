# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`
Status: COMPLETE / FAIL — RESULT FROZEN
Latest canonical result: `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`
Latest frozen result decision: `FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION`
Dependencies:
- Neural Minimal Benchmark 0.1 COMPLETE / FROZEN
- Neural Historical Reachability 0.1 COMPLETE / FROZEN
- Neural Nonlinear ReLU Pilot 0.1 COMPLETE / FROZEN
- Neural Vertical Slice Go/Revise/Stop Gate 0.1 COMPLETE / GO / FROZEN
- Neural Response Coordinate Specification Gate 0.1 COMPLETE / FROZEN
- Neural Response Coordinate Pilot 0.1 COMPLETE / WEAK / FROZEN
- Neural Response Coordinate WEAK Integration Gate 0.1 COMPLETE / REVISE / FROZEN
- Neural Response Coordinate Nuisance-Invariance Specification Gate 0.1 COMPLETE / SPECIFICATION FROZEN
Implementation commit: `988db41bad5d46615b00defe2da8964c15a5203f`
Test commit: `2d7ac6171323607bfeeec12f3657b56b162e0406`
Canonical result-freeze commit: `8f2be1871605b39d9e851d1b47ed9c30ec7bf21f`
Next instruction: `RETURN TO MASTER`
STOP boundary: Do not alter the frozen nuisance result, null construction, classification rules, base family, gauge subgroup, partitions, coordinate, baselines, metrics, thresholds or tolerances; do not try another nuisance/coordinate/family or open nonlinear/multi-step/real-data/realistic-history/LoRA/power-grid/state-preparation/literature/manuscript work without new MASTER authorisation.

## Frozen prior response-coordinate result

`Neural Response Coordinate Pilot 0.1` remains:

**WEAK — RESULT FROZEN / NO NOVELTY PROMOTION**

- candidate aggregate held-out `R2_state=1.0`;
- B2 equal-dimensional raw PCA `R2_state=0.999883026432542`;
- candidate minus B2 `0.000116973567458323 < 0.05` frozen PASS margin;
- all validity controls passed;
- no retuning.

This prior WEAK result is not repaired or overwritten by the nuisance gate.

## Frozen nuisance-invariance result

### Neural Response Coordinate Nuisance-Invariance Pilot 0.1

Decision: **FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION**

All mandatory scientific/numerical sanity conditions pass:

- exact 648-state construction and partitions `164/164/160/160`;
- current-function max error `8.433854195116819e-17`;
- Frobenius norm max error `2.220446049250313e-16`;
- readout norm error `0.0`;
- gauge orthogonality max error `2.220446049250313e-16`;
- within-orbit `P` max component error `8.881784197001252e-16`;
- within-orbit analytical-response max error `8.326672684688674e-17`;
- analytical/autograd maximum error over all `648 x 12 = 7776` pairs `1.6653345369377348e-16`;
- C0 joint aggregate `R2_state=1.0`;
- B3 Gram-PCA joint aggregate `R2_state=1.0`;
- B3 `J_nuis=2.692209973425601e-32`;
- leakage separation passed;
- combined prior APP-A plus new regression execution: `36 passed`.

Frozen scientific metrics:

- candidate response coordinate:
  - `R2_state(S_nuis)=1.0`;
  - `R2_state(S_latent)=1.0`;
  - `R2_state(S_joint)=1.0`;
  - minimum joint per-intervention `R2=1.0`;
  - `J_nuis=5.596227006606825e-32`;
- B2 naive raw PCA:
  - joint `R2_state=2.220446049250313e-16`;
  - `J_nuis=1.0`;
- B3 gauge-invariant Gram-PCA:
  - joint `R2_state=1.0`;
  - `J_nuis=2.692209973425601e-32`;
- N0 cyclic state-association null:
  - nuisance `R2_state=0.7071428571428566`;
  - latent `R2_state=0.6999999999999995`;
  - joint `R2_state=0.6999999999999995`.

### Mechanical classification issue

PASS does not apply because frozen PASS requires `R_null<=0.10`.

WEAK does not apply because frozen WEAK requires `R_null<=0.25`.

The explicit frozen NULL list also does not apply because all of the following are false:

- `R_resp<0.90`;
- `R_nuis<0.90`;
- `R_lat<0.90`;
- `R_min<0.75`;
- `J_resp>1e-4`;
- `R_resp<=R_raw2`.

Thus the frozen PASS/WEAK/NULL rules are not total for the realised metric vector. APP-A is not authorised to add a post-hoc `R_null>0.25 -> NULL` clause or change N0 after inspection.

The gate is therefore recorded as **FAIL due to specification/classification validity**, not as numerical FAIL and not as scientific NULL.

The high N0 value is structurally attributable to the frozen one-state cyclic shift acting on four gauge-equivalent copies per response-latent state, so most shifted assignments remain within the same latent orbit. This diagnosis does not authorise a repair.

## CI status

For test commit `2d7ac6171323607bfeeec12f3657b56b162e0406`, GitHub reports no commit status checks and no workflow runs. Repository CI is not configured / not applicable for this execution commit.

## Claim ceiling

Allowed statement only:

> In the frozen synthetic gauge-control family, the 2D response-aware coordinate is numerically gauge invariant and predicts held-out responses essentially exactly, naive 2D raw-parameter PCA fails under held-out gauge orientations, and a gauge-invariant 2D Gram-PCA control remains equally predictive. However, the frozen N0 construction retains high predictive score and the pre-specified PASS/WEAK/NULL classifier does not assign a scientific class to the realised metric combination; the gate is therefore frozen as a specification-classification FAIL rather than repaired post hoc.

Do not claim a PASS, a scientific NULL, unique response-specific information beyond symmetry-aware raw-state quotients, generic nonlinear scaling, realistic SGD reachability, real-data/LoRA/transformer usefulness, controlled state preparation, novelty, or established causal synergetics.

## Open issues

Any amendment of N0, orbit-level/deduplicated null, explicit `R_null>0.25 -> NULL` rule, alternative gauge nuisance, alternate state family, new coordinate, or broader scaling experiment requires a new MASTER-authorised gate.

STOP — RETURN TO MASTER
