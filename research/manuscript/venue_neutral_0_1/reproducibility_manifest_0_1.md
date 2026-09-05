# Reproducibility / Artifact Manifest 0.1

Scope: venue-neutral packaging of frozen results only. No scientific code, simulation, benchmark, test, or analysis was rerun during this artifact task.

Repository: `twkroll/causal_synergetics`

Canonical editorial manuscript: `research/manuscript/manuscript_editorial_completion_0_1.md`

## 1. Canonical scientific result files

- CORE: `research/core/synergetic_sufficiency_boundary_0_1.md`
- Neural minimal: `research/app_a/neural_minimal_benchmark_0_1.md`
- Neural historical reachability: `research/app_a/neural_historical_reachability_0_1.md`
- Neural nonlinear ReLU: `research/app_a/neural_nonlinear_relu_pilot_0_1.md`
- Neural response-coordinate pilot: `research/app_a/neural_response_coordinate_pilot_0_1.md`
- Neural nuisance-invariance pilot: `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`
- Neural nuisance FAIL integration/PARK decision: `research/master/neural_response_coordinate_nuisance_fail_integration_0_1.md`
- Power-grid minimal benchmark: `research/app_b/power_grid_minimal_benchmark_0_1.md`
- Controlled state preparation: `research/app_c/controlled_state_preparation_0_1.md`
- Final claim-level literature revalidation: `research/literature/claim_level_theorem_level_prior_art_revalidation_0_1.md`
- Manuscript claim/architecture freeze: `research/master/manuscript_claim_freeze_architecture_0_1.md`

## 2. Scientific source modules and tests

| Scientific item | Source module(s) | Test file(s) |
|---|---|---|
| Neural linear + history | `src/causal_synergetics/benchmarks/neural_linear.py` | `tests/test_neural_linear_benchmark.py`; `tests/test_neural_linear_history.py` |
| Neural ReLU | `src/causal_synergetics/benchmarks/neural_relu.py` | `tests/test_neural_relu_pilot.py` |
| Neural response coordinate | `src/causal_synergetics/benchmarks/neural_response_coordinate.py` | `tests/test_neural_response_coordinate_pilot.py` |
| Neural nuisance invariance | `src/causal_synergetics/benchmarks/neural_response_coordinate_nuisance.py` | `tests/test_neural_response_coordinate_nuisance.py` |
| Power-grid two-machine | `src/causal_synergetics/benchmarks/power_grid_two_machine.py` | `tests/test_power_grid_two_machine.py` |
| Controlled state preparation | `src/causal_synergetics/benchmarks/controlled_state_preparation.py` | `tests/test_controlled_state_preparation.py` |

The CORE result is an analytic manuscript/result file rather than a benchmark module in the frozen record.

## 3. Frozen commits and local execution statements

### CORE Synergetic Sufficiency Boundary 0.1

- Canonical result-freeze commit: `1cad9c78c4f76484cb5e2197ce9c128c5f94f4ff`.
- Result type: analytic theorem/counterexample/bound derivation; no benchmark rerun in this artifact task.

### Neural Minimal Benchmark 0.1

- Implementation/test execution commit: `649a187125c4ad410e0b16b77accbfacfb577371`.
- Result-freeze commit: `f5f02c871093129ef012780dbfcbcf55ef4de6f3`.
- Frozen local result: `4 passed in 1.01s`.
- Frozen analytical/autograd maximum component discrepancy: `0.0`.

### Neural Historical Reachability 0.1

- Historical test-addition commit: `ad9cc18a0519ffcfc4e6bc2e919e82f40bf54208`.
- Implementation commit completing historical functionality: `e342ef5c5cefae30df45e23bc667f149e818238c`.
- Result-freeze commit: `0e345fbb7b5a8ccc3c3f8bd4c958132c1b130d7c`.
- Frozen local result: `8 passed in 1.08s`.
- Frozen analytical/autograd maximum discrepancy: `0.0`.

### Neural Nonlinear ReLU Pilot 0.1

- Implementation commit: `b5ba5da30d869d160eab0a7801bcfa324860b19a`.
- Test commit: `3b42bf8c9a3e1a56a031654576b9c9f25b70bdbc`.
- Result-freeze commit: `ff9f575839848e80705cd73062d431b20ca4eb10`.
- Frozen local combined result: `12 passed in 1.01s`.
- Frozen analytical/autograd maximum discrepancy: `0.0`.

### Neural Response Coordinate Pilot 0.1

- Implementation commit: `86715dfb9de78220964e137759c66785373f6de8`.
- Test commit: `48d850c22ca156af892db11cbbdb95b20693bb08`.
- Result-file freeze commit: `18618368991d818b3bfe883975b3ab2573bed0c6`.
- WEAK result/status freeze commit: `00dd60692268763b48252b81c5b69327ef06a0b3`.
- Frozen local combined result: `24 passed`.
- Frozen analytical/autograd audit: 972 state/intervention pairs, maximum discrepancy `2.7755575615628914e-17`.
- Frozen scientific classification: `WEAK — RESULT FROZEN`.

### Neural Response Coordinate Nuisance-Invariance Pilot 0.1

- Implementation commit: `988db41bad5d46615b00defe2da8964c15a5203f`.
- Test commit: `2d7ac6171323607bfeeec12f3657b56b162e0406`.
- Canonical result-freeze commit: `8f2be1871605b39d9e851d1b47ed9c30ec7bf21f`.
- Frozen local combined result: `36 passed`.
- Frozen analytical/autograd audit: 7776 state/intervention pairs, maximum discrepancy `1.6653345369377348e-16`.
- Frozen scientific classification: `FAIL — RESULT FROZEN / SPECIFICATION CLASSIFICATION GAP`.
- MASTER integration: `STOP / PARK RESPONSE-COORDINATE DIRECTION`.

### Power-Grid Minimal Benchmark 0.1

- Implementation commit: `a98c9447aa50b6bb8974b2522543d72784be24ce`.
- Test commit: `5774dac821fc3d4878feee32a4fe13b7553abe33`.
- Result creation commit: `c0c24c2a3266eb69daaa12340e8b7dc68248956f`.
- APP-B status update commit recorded in result file: `c27d359350e64e90b759e088df2205172d60d276`.
- Frozen local new-test result: `5 passed`.
- Frozen predecessor regression evidence: `36 passed`; APP-B changed none of those prior source/test files.
- Frozen numerical convergence error: `8.1601392309949e-15`.
- Frozen mean/COI closure error: `3.885780586188048e-14`.

### Controlled State Preparation 0.1

- Implementation commit: `3d4b06f417b4d81cbeaa93f27683a1c799d426b4`.
- Test commit: `04765a8dac61f4f657659d2bde03f5ef76c307d5`.
- Result creation commit: `14c82045ee187f825d8340d93cd1bde34216f7d4`.
- Result metadata finalisation commit: `fd3326703a8d6652df5561584b47bf8dd20da8c6`.
- Frozen local deterministic result: `5 passed`.
- Frozen primary/audit convergence error: `5.738465258531278e-15`.

## 4. CI state

The frozen result records report no configured GitHub commit-status contexts/workflow runs for the queried scientific execution commits. Repository CI is therefore treated as **not configured / not applicable for these frozen executions**. No CI success is claimed or inferred.

This artifact-completion task did not rerun tests or query scientific code for new results. It only compiled already frozen statements and existing repository pointers.

## 5. Venue-neutral package artifacts

- Supplement: `research/manuscript/venue_neutral_0_1/supplement_0_1.md`
- Figure 1: `research/manuscript/venue_neutral_0_1/figures/figure_1_diagnostic_schematic.svg`
- Figure 2: `research/manuscript/venue_neutral_0_1/figures/figure_2_cross_domain_witness_schematic.svg`
- Figure 3: `research/manuscript/venue_neutral_0_1/figures/figure_3_power_grid_schematic.svg`
- Figure 4: `research/manuscript/venue_neutral_0_1/figures/figure_4_preparation_protocol.svg`
- Package index: `research/manuscript/venue_neutral_0_1/README.md`
- Artifact change log: `research/manuscript/venue_neutral_0_1/CHANGELOG.md`

## 6. Reproducibility limitations

This manifest records the reproducibility evidence already frozen in Git. It does not certify external reproducibility, cross-platform identity, realistic-domain generalisation, robustness, or scientific validity beyond the stated benchmark assumptions. The absence of repository CI does not invalidate the frozen local executions, but no automated CI verification is claimed.
