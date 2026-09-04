# STATUS — 50 – APP-A – Neuronaler Minimalbenchmark

Current Gate: `Neural Response Coordinate Nuisance-Invariance Pilot 0.1`
Status: PARKED / FROZEN / WAIT
Latest canonical result: `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`
Latest frozen result decision: `FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION`
MASTER integration: `research/master/neural_response_coordinate_nuisance_fail_integration_0_1.md`
MASTER decision: `STOP / PARK RESPONSE-COORDINATE DIRECTION — CLAIM-RESTRICTED / NO NOVELTY PROMOTION`
Latest rollback point: `RP-013 — Neural Response Coordinate Nuisance FAIL Integration Freeze 0.1`
Implementation commit: `988db41bad5d46615b00defe2da8964c15a5203f`
Test commit: `2d7ac6171323607bfeeec12f3657b56b162e0406`
Canonical result-freeze commit: `8f2be1871605b39d9e851d1b47ed9c30ec7bf21f`
Next instruction: `WAIT FOR MASTER`
STOP boundary: Do not alter or rerun the frozen nuisance result, repair N0/classifier, open a replacement response coordinate/nuisance/state family, or start nonlinear/multi-step/real-data/realistic-history/LoRA/power-grid/state-preparation/literature/manuscript work without new MASTER authorisation.

## Frozen result

Decision: **FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP / NO NOVELTY PROMOTION**.

All mandatory scientific/numerical sanity conditions pass. Direct frozen observations include:

- candidate response coordinate `R2_state=1.0` on nuisance-only, latent-only and joint held-out partitions;
- minimum joint per-intervention candidate `R2=1.0`;
- candidate `J_nuis=5.596227006606825e-32`;
- naive B2 raw PCA joint `R2_state=2.220446049250313e-16`, `J_nuis=1.0`;
- gauge-aware B3 Gram-PCA joint `R2_state=1.0`, `J_nuis=2.692209973425601e-32`;
- N0 joint `R2_state=0.6999999999999995`;
- analytical/autograd maximum error over all 7776 pairs `1.6653345369377348e-16`;
- leakage separation passed;
- combined unchanged APP-A regression suite `36 passed`.

PASS and WEAK fail because the frozen N0 thresholds are violated. None of the explicitly enumerated NULL conditions applies. The pre-specified classifier is non-total for the realised metric vector. The result remains a specification/classification FAIL, not a numerical FAIL and not a scientific NULL.

## MASTER integration

The response-coordinate direction is parked. A prospective orbit-level/null repair was rejected because it would have low incremental scientific value and would not change the strongest comparator ceiling: the explicitly symmetry-aware 2D Gram-PCA control already matches the response coordinate exactly on predictive and gauge-invariance metrics.

The failed nuisance gate remains canonical and may not be reclassified. The earlier response-coordinate pilot remains independently `WEAK`.

## Claim ceiling

Allowed statement only:

> In the frozen synthetic gauge-control family, the 2D response-aware coordinate is numerically gauge invariant and exactly predictive; naive equal-dimensional raw-parameter PCA fails under held-out gauge orientations; a gauge-invariant equal-dimensional Gram-PCA control remains equally predictive; and the frozen N0/classifier does not assign a scientific class to the realised metric vector. The gate remains a specification-classification FAIL, and the response-coordinate direction is parked under the current synthetic programme framing.

No PASS/WEAK/NULL relabelling, unique response-specific information claim, generally useful coordinate claim, nonlinear/real-data/LoRA/state-preparation claim, novelty promotion, or established causal-synergetics claim is authorised.

## CI status

For test commit `2d7ac6171323607bfeeec12f3657b56b162e0406`, GitHub reports no commit status checks. Repository CI is not configured; frozen local combined tests report `36 passed`.

STOP — WAIT FOR MASTER
