# Supplement — Testing Synergetic Macrostates for Intervention Sufficiency

Version: `Manuscript Venue-Neutral Artifact Completion 0.1`

This supplement is compiled only from canonical frozen programme results. It introduces no new theorem, calculation, simulation, metric, baseline, classifier, interpretation, literature claim, or scientific result. The claim ceiling of the canonical editorial manuscript remains controlling: Package P is the sole contribution-bearing framing; C1–C4 remain restricted; C5 remains SAME-level illustration only.

Canonical manuscript source: `research/manuscript/manuscript_editorial_completion_0_1.md`.

---

# Appendix A. CORE assumptions, projectability proof, scalar witness, and finite-horizon bounds

Canonical source: `research/core/synergetic_sufficiency_boundary_0_1.md`.

## A.1 Frozen state, intervention, response, and slaving specification

Let the microscopic state be

`x=(q,r) ∈ D ⊂ R^m × R^n`,

with pre-declared macro map

`π(q,r)=q`.

The controlled ODE is

`q̇=f(q,r,u)`,

`ṙ=g(q,r,u)`,

with local Lipschitz regularity sufficient for unique solutions over the frozen horizon. Fix a compact instantaneous control set `A ⊂ R^p`, a horizon `T>0`, and the admissible family

`𝒰={u:[0,T]→A : u is piecewise continuous}`,

including every constant control `u(t)≡a`, `a∈A`.

The frozen response is the complete retained trajectory

`Γ(x0,u)=q^u_x0(·) ∈ C([0,T],R^m)`

with metric

`d_Γ(Γ1,Γ2)=sup_{0≤t≤T} ||q1(t)-q2(t)||`.

The pre-declared macro is intervention-response sufficient on the relevant domain if

`π(x1)=π(x2)  ⇒  Γ(x1,u)=Γ(x2,u)`

for every admissible `u`.

Exact controlled closure means that a projected vector field exists with

`q̇=f̄(q,u)`

independently of the hidden coordinate, equivalently

`f(q,r,u)=f̄(q,u)`.

The classical slaving relation is a fixed graph

`M={(q,r): r=h(q)}`

with unforced invariance

`g(q,h(q),0)=Dh(q)f(q,h(q),0)`

and, where invoked, normal attraction/fast relaxation for

`e=r-h(q)`.

Two distinct controlled properties must not be conflated:

1. controlled graph invariance requires
   `g(q,h(q),a)=Dh(q)f(q,h(q),a)` for every admissible instantaneous control `a`;
2. global fibre projectability requires
   `f(q,r,a)=f̄(q,a)` for all relevant hidden `r` in the fibre.

Neither follows from unforced slaving alone.

## A.2 Standard full-trajectory projectability equivalence

**Statement.** Under the frozen full retained-trajectory response, unique solutions on `[0,T]`, and an intervention family containing every constant control, the following are equivalent:

1. for every `(q,r1),(q,r2)` on the same `q` fibre and every admissible `u`, the retained trajectories are identical;
2. for every `a∈A`, `f(q,r1,a)=f(q,r2,a)` along each `q` fibre;
3. there exists `f̄(q,a)` with `f(q,r,a)=f̄(q,a)`.

This is included for self-containment and is structurally subsumed by established controlled quotient/projectability and exact-abstraction theory.

**Proof.** `(2)⇔(3)` follows by defining `f̄(q,a)` as the common fibre value. For `(3)⇒(1)`, two microscopic trajectories with the same initial `q` and the same intervention solve the same closed reduced IVP `q̇=f̄(q,u)`; uniqueness gives identical retained trajectories. For `(1)⇒(2)`, fix two states with the same `q` and any `a∈A`, apply the constant intervention `u(t)≡a`, and differentiate the identical retained trajectories at `t=0`:

`f(q,r1,a)=q̇1(0)=q̇2(0)=f(q,r2,a)`.

Thus the projected vector field is constant along every fibre. ∎

A controlled-invariant slaving graph gives closure only on the graph. It does not establish global fibre homogeneity if `f` still depends on off-graph hidden coordinates.

## A.3 Scalar minimal witness

The frozen scalar system is

`q̇=ur`,

`ṙ=-λr+u`,

with `λ>0`, `u(t)∈[-U,U]`, and slaving graph `M={r=0}`.

For `u=0`,

`q(t)=q0`,

`r(t)=r0 e^{-λt}`.

Hence the graph is invariant and globally exponentially attracting in `r`, and the retained passive trajectory is exact and independent of `r0` even off the graph.

For constant nonzero `u(t)≡a`,

`r(t)=r0 e^{-λt}+(a/λ)(1-e^{-λt})`,

`q(t)=q0+(a r0/λ)(1-e^{-λt})+a²[t/λ-(1-e^{-λt})/λ²]`.

For two same-`q` states with hidden coordinates `r1≠r2`,

`Δq(t)=(a(r1-r2)/λ)(1-e^{-λt})`,

so their retained responses differ for every nonzero admissible constant `a`. On the slaving graph itself,

`ṙ|_{r=0}=u`,

so every nonzero intervention immediately violates controlled invariance. The witness therefore separates two mechanisms already identified in the frozen CORE result:

- fibre memory: different initial hidden coordinates yield different controlled retained responses;
- control leakage: even exact initialization on the unforced graph does not protect the graph-restricted reduction when the intervention excites the hidden coordinate.

## A.4 Exact scalar finite-horizon bounds

For two same-`q` states under a common arbitrary admissible input,

`Δṙ=-λΔr`,

hence

`Δr(t)=Δr0 e^{-λt}`

and

`Δq(t)=Δr0 ∫_0^t u(s)e^{-λs} ds`.

Using `|u(s)|≤U` gives the sharp bound

`d_Γ ≤ U |Δr0| (1-e^{-λT})/λ`.

Equality is attained by a constant intervention whose sign is aligned with `Δr0`.

Starting on the slaving graph (`r0=0`),

`r(t)=∫_0^t e^{-λ(t-s)}u(s)ds`,

so

`|r(t)|≤U(1-e^{-λt})/λ`.

Because `|q̇|=|ur|`, the graph-restricted reduced-model error satisfies

`d_Γ(q,q_red) ≤ U²[T/λ-(1-e^{-λT})/λ²]`,

where `q_red(t)≡q0`. Constant `u=±U` attains this bound exactly in the frozen scalar model.

## A.5 General finite-horizon bridge bound

Let

`e(t)=r(t)-h(q(t))`,

`f̄(q,u)=f(q,h(q),u)`,

and let `q̄` solve

`q̄̇=f̄(q̄,u)`, `q̄(0)=q0`.

Assume uniformly on the relevant tube:

**B1 — fast deviation inequality**

`D⁺||e|| ≤ -λ||e|| + δ + β||u||`,

with `λ>0`, `δ≥0`, `β≥0`;

**B2 — tangential sensitivity**

`||f(q,r,u)-f(q,h(q),u)|| ≤ L_e||e||`;

**B3 — reduced tangential Lipschitz condition**

`||f̄(q1,u)-f̄(q2,u)|| ≤ L_q||q1-q2||`.

For `||u||∞≤U`, define

`c=(δ+βU)/λ`,

`Φ(L_q,t)=(e^{L_q t}-1)/L_q` for `L_q>0`, with `Φ(0,t)=t`,

`Ψ(L_q,λ,t)=(e^{L_q t}-e^{-λt})/(L_q+λ)`.

Scalar comparison gives

`||e(t)||≤e^{-λt}||e0||+c(1-e^{-λt})`.

With `z=q-q̄`, B2–B3 imply in the upper-Dini sense

`d/dt ||z|| ≤ L_q||z||+L_e||e||`.

Since `z(0)=0`, Grönwall yields

`||z(t)|| ≤ L_e ∫_0^t e^{L_q(t-s)}||e(s)||ds`.

Using

`∫_0^t e^{L_q(t-s)}e^{-λs} ds = Ψ(L_q,λ,t)`

and

`∫_0^t e^{L_q(t-s)}(1-e^{-λs}) ds = Φ(L_q,t)-Ψ(L_q,λ,t)`,

one obtains

`||q(t)-q̄(t)|| ≤ L_e[||e0||Ψ(L_q,λ,t)+c(Φ(L_q,t)-Ψ(L_q,λ,t))]`.

Thus

`d_Γ(q,q̄) ≤ L_e[||e0||Ψ(L_q,λ,T)+((δ+βU)/λ)(Φ(L_q,T)-Ψ(L_q,λ,T))]`.

For a tube `||e0||≤ρ`, the conservative same-fibre diameter bound is

`d_Γ(Γ(x1,u),Γ(x2,u)) ≤ 2B_T(ρ)`,

where

`B_T(ρ)=L_e[ρΨ(L_q,λ,T)+((δ+βU)/λ)(Φ(L_q,T)-Ψ(L_q,λ,T))]`.

This proof uses standard comparison/Grönwall and singular-perturbation/ISS-style ingredients. It is not a new control-theoretic theorem family.

---

# Appendix B. Frozen neural constructions

Canonical sources:

- `research/app_a/neural_minimal_benchmark_0_1.md`
- `research/app_a/neural_historical_reachability_0_1.md`
- `research/app_a/neural_nonlinear_relu_pilot_0_1.md`

These constructions are manuscript illustrations only. The qualitative same-function/different-training-response phenomenon is treated as SAME-level prior art.

## B.1 Factorised linear same-function/different-response construction

Use

`f_{U,v}(x)=v^TUx`, `d=h=2`, `w=U^Tv`.

Frozen states:

`v_A=v_B=(1,0)^T`,

`U_A=[[0,0],[1,0]]`,

`U_B=[[0,0],[0,1]]`.

Both satisfy

`w_A=w_B=(0,0)^T`,

`||U_A||_F=||U_B||_F=1`,

`||v_A||_2=||v_B||_2=1`.

Frozen tasks:

`c_C=e1`, `c_D=e2`,

with loss

`L_c(w)=1/2||w-c||²`

and exactly one simultaneous full-batch gradient step at `η=0.1`.

Writing `g=w-c`, the exact gradients are

`∇_U L=v g^T`,

`∇_v L=Ug`.

Thus

`U⁺=U-ηvg^T`,

`v⁺=v-ηUg`,

and

`w⁺=w-η(U^TU+||v||²I)g+η²g(v^TUg)`.

For both frozen states, `w=0` and `v^TU=0`, so the `η²` term vanishes and

`w⁺=ηPc`, `P=U^TU+||v||²I`.

The state-specific response operators are

`P_A=diag(2,1)`,

`P_B=diag(1,2)`.

Frozen outcomes:

| State | Task | `w⁺` | Post-step loss |
|---|---|---|---:|
| A | C | `(0.2,0)` | `0.32000000000000006` |
| B | C | `(0.1,0)` | `0.405` |
| A | D | `(0,0.1)` | `0.405` |
| B | D | `(0,0.2)` | `0.32000000000000006` |

The directed advantage is `0.085` in both directions. Analytical and PyTorch autograd updates agree componentwise with maximum observed absolute discrepancy `0.0`. Frozen local execution: `4 passed in 1.01s`.

## B.2 Historical reachability under the artificial auxiliary protocol

Both histories begin from

`U0=0`, `v=e1`.

A temporary auxiliary readout is fixed as

`a=e2`.

For historical target `c`, define

`H_c(U)=1/2||U^Ta-c||²`.

One full-batch gradient step on `U` only with `η_hist=1` gives

`∇_U H_c=a(U^Ta-c)^T`.

At `U0=0`,

`∇_U H_c(U0)=-ac^T`,

so

`U⁺=ac^T`.

For `c=e1`,

`U_A⁺=e2e1^T=[[0,0],[1,0]]`;

for `c=e2`,

`U_B⁺=e2e2^T=[[0,0],[0,1]]`.

These are exactly the frozen linear benchmark endpoints. Main-function preservation follows from

`w⁺=(U⁺)^Tv=c(a^Tv)=0`,

because `a^Tv=e2^Te1=0`.

Frozen verification:

| History | `U⁺` | `w_before` | `w_after` | `H_before` | `H_after` | max analytic/autograd difference |
|---|---|---|---|---:|---:|---:|
| A | `[[0,0],[1,0]]` | `(0,0)` | `(0,0)` | `0.5` | `0.0` | `0.0` |
| B | `[[0,0],[0,1]]` | `(0,0)` | `(0,0)` | `0.5` | `0.0` | `0.0` |

The auxiliary head is discarded before evaluation. The original C/D results are reproduced unchanged. Frozen combined local execution: `8 passed in 1.08s`.

This is artificial provenance only; it does not establish natural reachability under ordinary single-head SGD.

## B.3 Two-unit ReLU construction

Use the bias-free network

`f_{U,v}(x)=v^T ReLU(Ux)`

with frozen states

`U_A=[[2,0],[0,1]]`, `v_A=(1/2,1)^T`,

`U_B=[[1,0],[0,2]]`, `v_B=(1,1/2)^T`.

Positive homogeneity gives, for every `x∈R²`,

`f_A(x)=f_B(x)=ReLU(x1)+ReLU(x2)`.

The simple norms also match:

`||U_A||_F=||U_B||_F=sqrt(5)`,

`||v_A||_2=||v_B||_2=sqrt(5/4)`.

Frozen tasks:

C: `x=(1,-1)^T`, `y=2`;

D: `x=(-1,1)^T`, `y=2`.

Exactly one simultaneous full-batch step is taken at `η=0.1`.

For one sample, write `z=Ux`, `h=ReLU(z)`, residual `r=f(x)-y`, and activation indicator `m_i=1[z_i>0]`. The exact gradients are

`∇_vL=rh`,

`∇_UL=r(v⊙m)x^T`.

At each frozen initial state/task pair the task output is `1`, target is `2`, and `r=-1`. For an active unit of scale `a`,

`u⁺=u+(η/a)x`,

`v⁺=1/a+ηa`,

and, since `||x||²=2`,

`f⁺(x)=1+η(a²+2/a²)+2η²`.

At `η=0.1`, the high scaling `a=2` gives `f⁺=1.47` and loss `0.14045`; the low scaling `a=1` gives `f⁺=1.32` and loss `0.2312`.

Activation-margin audit:

| State | Task | Before | After |
|---|---|---|---|
| A | C | `(2,-1)` | `(2.1,-1)` |
| B | C | `(1,-2)` | `(1.2,-2)` |
| A | D | `(-2,1)` | `(-2,1.2)` |
| B | D | `(-1,2)` | `(-1,2.1)` |

Frozen probe-response table:

| State | Task | Post-step probe vector | Post-step loss |
|---|---|---|---:|
| A | C | `[1.47,1.0,2.4,0.0]` | `0.14045` |
| B | C | `[1.32,1.0,2.1,0.0]` | `0.2312` |
| A | D | `[1.0,1.32,2.1,0.0]` | `0.2312` |
| B | D | `[1.0,1.47,2.4,0.0]` | `0.14045` |

Directed advantage: `0.09075` in both directions. Maximum analytical/autograd discrepancy: `0.0`. Frozen combined local execution: `12 passed in 1.01s`.

---

# Appendix C. Response-coordinate WEAK, nuisance FAIL, Gram countercontrol, and PARK decision

Canonical sources:

- `research/app_a/neural_response_coordinate_pilot_0_1.md`
- `research/app_a/neural_response_coordinate_nuisance_invariance_pilot_0_1.md`
- `research/master/neural_response_coordinate_nuisance_fail_integration_0_1.md`

## C.1 Frozen response-coordinate pilot: WEAK

Specification identifiers include the factorised-linear model with `d=4`, `h=5`, 81 frozen states on a `9×9` latent grid, checkerboard split `41/40`, four frozen calibration interventions, eight frozen held-out interventions, one simultaneous full-batch GD step at `η=0.1`, a 16D calibration fingerprint compressed by train-only PCA to exactly 2D, a fixed bilinear OLS decoder, and pre-frozen B0/B1/B2/C0/C1/N0 controls and thresholds.

Aggregate held-out metrics:

| Model/control | `R2_state` | NRMSE | Role |
|---|---:|---:|---|
| Response coordinate | `1.0` | `7.30513741157965e-16` | candidate |
| B0 current function | approximately `0.0` | `0.157359158493889` | baseline |
| B1 simple summaries | `0.070803629370716` | `0.151686097038027` | baseline |
| B2 raw-parameter PCA, 2D | `0.999883026432542` | `0.00170190726453134` | principal equal-dimensional baseline |
| C0 full 16D fingerprint | `1.0` | `1.34721603562732e-15` | ceiling |
| C1 analytical operator | `1.0` | `9.25714380520572e-17` | oracle |
| N0 cyclic association null | `-0.200000000000001` | `0.172378321474267` | null control |

The candidate minimum per-held-out-intervention `R2_state(c)` is `1.0`. The decisive frozen margin is

`R_resp-R_raw2 = 0.000116973567458323`,

far below the PASS requirement `0.05`. All WEAK conditions are satisfied. Therefore the mechanical classification remains

**WEAK — RESULT FROZEN**.

The 972-state/intervention analytical/autograd audit has maximum component discrepancy `2.7755575615628914e-17`, and the frozen combined local test run reports `24 passed`.

## C.2 Nuisance-invariance gate: exact prediction and invariance, but specification-classification FAIL

The frozen gauge-control family contains 648 states with partitions `164/164/160/160` for train/nuisance-only/latent-only/joint, eight hidden-basis angles, four calibration interventions, eight held-out interventions, and the same one-step factorised-linear response structure.

Under hidden orthogonal rotations `U'=QU`, `v'=Qv`, orthogonality gives

`w'=U'^Tv'=U^Tv`,

`U'^TU'=U^TU`,

`||v'||²=||v||²`,

so

`P'=U'^TU'+||v'||²I=P`

and the frozen analytical response `Γ(s,c)=ηP(s)c` is invariant over each gauge orbit.

Primary joint metrics:

| Model | Joint `R2_state` | Joint NRMSE |
|---|---:|---:|
| Response 2D PCA | `1.0` | `1.4190705384814486e-15` |
| B0 current function | `0.0` | `0.15735915849388862` |
| B1 simple summaries | `0.03933505243106106` | `0.15423324524823528` |
| B2 raw-parameter PCA 2D | `2.220446049250313e-16` | `0.15735915849388862` |
| B3 Gram-PCA 2D | `1.0` | `1.941469126436537e-15` |
| C0 full fingerprint | `1.0` | `1.9306201195232773e-15` |
| C1 oracle | `1.0` | `2.7453911730087413e-16` |
| N0 cyclic association null | `0.6999999999999995` | `0.08618916073713352` |

Frozen nuisance-fraction values:

| Representation | `J_nuis` |
|---|---:|
| Response 2D PCA | `5.596227006606825e-32` |
| B2 raw-parameter PCA 2D | `1.0` |
| B3 Gram-PCA 2D | `2.692209973425601e-32` |

Thus the response coordinate is exactly predictive and numerically gauge invariant; naive raw PCA fails under unseen gauge orientations; and the explicitly gauge-invariant equal-dimensional Gram-PCA control is equally predictive and invariant.

However, frozen N0 gives joint `R2_state=0.6999999999999995`. This violates the PASS null threshold (`≤0.10`) and WEAK null threshold (`≤0.25`), while none of the enumerated NULL conditions is true. The pre-specified classifier is therefore non-total for the observed metric vector. No post-hoc NULL clause, orbit-level null, deduplication, or alternative state family was introduced.

The gate remains exactly:

**FAIL — SPECIFICATION CLASSIFICATION GAP**,

not a numerical failure, leakage failure, failed gauge-invariance result, or scientific NULL.

The full analytical/autograd audit covered `648×12=7776` pairs with maximum absolute discrepancy `1.6653345369377348e-16`; the frozen combined local test run reports `36 passed`.

## C.3 Programme integration: PARK

Because the earlier coordinate pilot was WEAK against equal-dimensional raw PCA, the nuisance classifier is non-total, and the symmetry-aware 2D Gram-PCA control matches the response coordinate exactly in predictive and invariance metrics, MASTER froze the decision

**STOP / PARK RESPONSE-COORDINATE DIRECTION**.

The manuscript and this supplement therefore make no claim of unique response-specific information or superiority over symmetry-aware raw-state quotients.

---

# Appendix D. Power-grid minimal benchmark: exact specification, full metrics, and audits

Canonical source: `research/app_b/power_grid_minimal_benchmark_0_1.md`.

## D.1 Frozen model and macro/hidden decomposition

Two identical nonlinear classical swing machines are coupled by one lossless line with normalized

`M=D=K=1`.

Full equations:

`δ̇1=ω1`,

`ω̇1=-ω1+sin(δ2-δ1)`,

`δ̇2=ω2`,

`ω̇2=-ω2+sin(δ1-δ2)+u(t)`.

Pre-declared representative macro:

`q=(δ1,ω1)`.

Hidden coherency coordinates:

`eδ=δ2-δ1`,

`eω=ω2-ω1`.

Exact transverse dynamics:

`ėδ=eω`,

`ėω=-eω-2sin(eδ)+u`.

For `u=0`, `eδ=eω=0` is invariant. Its transverse Jacobian is

`[[0,1],[-2,-1]]`,

with eigenvalues

`(-1±i sqrt(7))/2`,

hence local exponential attraction around synchrony.

On the coherent set under nonzero localized intervention,

`(ėδ,ėω)=(0,u)`,

so controlled invariance is immediately lost.

The passive representative B0 model is

`δ̇=ω`,

`ω̇=-ω`.

For the arithmetic mean/COI coordinate

`δ_mean=(δ1+δ2)/2`,

`ω_mean=(ω1+ω2)/2`,

the antisymmetric line terms cancel exactly:

`δ̇_mean=ω_mean`,

`ω̇_mean=-ω_mean+u/2`.

This is the B1 aggregate dynamics and is an exact low-dimensional closure for the mean/COI coordinate.

## D.2 Frozen numerical specification

- coherent initial speeds: `-0.1`, `0`, `+0.1`, all with zero angles;
- interventions: `u=0`, `+0.2`, `-0.2`;
- horizon: `T=5`;
- deterministic NumPy float64 classical RK4;
- primary `dt=0.001`, audit `dt=0.0005`;
- B0 passive representative model;
- B1 coherent aggregate surrogate;
- C1 arithmetic mean/COI exact-closure control.

No alternative topology, model, parameter, macro, state, intervention, amplitude, horizon, baseline, metric, threshold, or numerical method was tried.

## D.3 Numerical sanity and convergence audit

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| Full trajectory count | `9` | `9` | PASS |
| Primary/half-step convergence | `≤1e-8` | `8.1601392309949e-15` | PASS |
| Passive coherency | `≤1e-12` | `0` | PASS |
| Passive full representative vs B0 | `≤1e-10` | `0` | PASS |
| Mean/COI full vs B1 | `≤1e-10` | `3.88578058618805e-14` | PASS |
| Positive/negative odd symmetry | `≤1e-10` | `3.83026943495679e-14` | PASS |
| Controlled-invariance defect | `(0,u)` | exact float64 construction | PASS |
| New APP-B tests | pass | `5 passed` | PASS |

The only initial APP-B test failure concerned exact binary equality in a standalone coordinate-transform assertion for decimal `0.7`; that assertion was changed to `atol=1e-15`. No scientific benchmark tolerance, equation, parameter, metric, or classifier changed.

## D.4 Full frozen nine-case metric table

`d_inf` is the full-trajectory max metric. `E_delta` and `E_omega` are componentwise macro errors. RMS is over both macro components and all primary-grid times. `H_delta` and `H_omega` are full-model coherency maxima.

| Initial | Intervention | B0 d_inf | B0 E_delta | B0 E_omega | B0 RMS | B1 d_inf | B1 E_delta | B1 E_omega | B1 RMS | H_delta | H_omega |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| I_minus | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_minus | u_plus | 0.354985842007617 | 0.354985842007617 | 0.110139531935133 | 0.13350745641446 | 0.0653477438433406 | 0.0653477438433406 | 0.0447710119684765 | 0.03809399399337 | 0.130695487686682 | 0.0895420239369532 |
| I_minus | u_minus | 0.354985842007616 | 0.354985842007616 | 0.110139531935133 | 0.133507456414459 | 0.0653477438433309 | 0.0653477438433309 | 0.0447710119684767 | 0.0380939939933611 | 0.130695487686681 | 0.0895420239369534 |
| I_zero | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_zero | u_plus | 0.354985842007615 | 0.354985842007615 | 0.110139531935133 | 0.133507456414459 | 0.065347743843341 | 0.065347743843341 | 0.0447710119684767 | 0.0380939939933706 | 0.130695487686682 | 0.0895420239369532 |
| I_zero | u_minus | 0.354985842007615 | 0.354985842007615 | 0.110139531935133 | 0.133507456414459 | 0.065347743843341 | 0.065347743843341 | 0.0447710119684767 | 0.0380939939933706 | 0.130695487686682 | 0.0895420239369532 |
| I_plus | u0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_plus | u_plus | 0.354985842007616 | 0.354985842007616 | 0.110139531935133 | 0.133507456414459 | 0.0653477438433309 | 0.0653477438433309 | 0.0447710119684767 | 0.0380939939933611 | 0.130695487686681 | 0.0895420239369534 |
| I_plus | u_minus | 0.354985842007617 | 0.354985842007617 | 0.110139531935133 | 0.13350745641446 | 0.0653477438433406 | 0.0653477438433406 | 0.0447710119684765 | 0.03809399399337 | 0.130695487686682 | 0.0895420239369532 |

Frozen summary values:

- `E_pass=0`;
- `E_B0_min=0.3549858420076152`;
- `E_B1_min=0.06534774384333092`;
- `H_delta=0.13069548768668177`;
- maximum controlled `|e_omega|=0.08954202393695339`;
- mean/COI closure error `3.885780586188048e-14`;
- maximum primary/half-step discrepancy `8.1601392309949e-15`.

The exact identities

`δ1-δ_mean=-eδ/2`,

`ω1-ω_mean=-eω/2`

explain why B1 is close to, but not exact for, the representative macro under the localized disturbance.

## D.5 Frozen classification and interpretation ceiling

PASS conditions are satisfied:

- `H_delta<π/2`;
- `E_pass≤1e-10`;
- `E_B0_min≥1e-4`;
- `E_B1_min≥1e-4`.

The result is **PASS — RESULT FROZEN / NO NOVELTY PROMOTION**.

The exact mean/COI control is mandatory: the benchmark is specific to the pre-declared representative-machine macro and does not establish failure of all low-dimensional grid aggregates.

---

# Appendix E. Output-preserving preparation: inverse dynamics, budgets, comparators, and audits

Canonical source: `research/app_c/controlled_state_preparation_0_1.md`.

## E.1 Frozen system, target, and preparation path

The benchmark uses the same normalized two-machine model with `M=D=K=1`, initial state

`x_init=(0,0,0,0)`,

preserved present macro

`q=(δ1,ω1)`,

hidden state

`(eδ,eω)=(δ2-δ1,ω2-ω1)`,

and later local machine-2 steps

`a=+0.2,-0.2`.

The forced hidden target is

`eδ*=asin(a/2)`,

`eω*=0`.

For `|a|=0.2`,

`|eδ*|=asin(0.1)=0.1001674211615598`.

For preparation sign `b`, define

`e_star(b)=asin(b/2)`,

`e_d(t;b)=e_star(b)[10ξ³-15ξ⁴+6ξ⁵]`, `ξ=t/2`,

for frozen preparation duration `τ_prep=2.0`.

The exact inverse-dynamics inputs are

`p1(t;b)=-sin(e_d(t;b))`,

`p2(t;b)=ë_d(t;b)+ė_d(t;b)+sin(e_d(t;b))`.

Sign-symmetry audit:

`max_t max_i |p_i(t;-0.2)+p_i(t;+0.2)|=0.0`.

During evaluation, the implementation uses only

`p1=0`, `p2=a`.

The preparation-control function is not used after the preparation phase.

## E.2 Frozen budgets and numerical sanity

Frozen preparation constraints:

- peak amplitude cap `0.35`;
- energy budget `0.25`;
- primary RK4 `dt=0.001`;
- audit RK4 `dt=0.0005`;
- evaluation horizon `T_eval=5.0`.

Key audit values:

| Check | Frozen requirement | Observed | Result |
|---|---:|---:|---|
| Primary/audit convergence | `≤1e-8` | `5.738465258531278e-15` | PASS |
| PT macro preservation `P_q` | `≤1e-8` | `3.580739551835791e-15` | PASS |
| PM macro preservation `P_q` | `≤1e-8` | `3.580739551835791e-15` | PASS |
| PT terminal hidden-target error | `≤1e-8` | `4.6079385647875116e-15` | PASS |
| PM terminal sign-reversed target error | `≤1e-8` | `4.6079385647875116e-15` | PASS |
| Peak preparation amplitude | `≤0.35` | `0.20881049376163438` | PASS |
| Preparation energy | `≤0.25` | `0.04006381839386479` | PASS |
| PT/PM energy difference | `≤1e-10` | `0.0` | PASS |
| Analytical sign symmetry | `≤1e-12` | `0.0` | PASS |
| Matched initial relative vector field | `≤1e-12` | `4.6079385647875116e-15` | PASS |
| APP-B I_zero B1 regression | abs error `≤1e-10` | `5.551115123125783e-17` | PASS |
| PT representative vs B1 | `≤1e-8` | `2.076727044536923e-15` | PASS |
| Evaluation uses no preparation input | exact | `p1=0`, `p2=a` only | PASS |
| New APP-C tests | pass | `5 passed` | PASS |

Energy is the frozen composite-trapezoidal evaluation of `p1²+p2²` on the primary control grid. No energy rule was changed.

## E.3 P0/PT/PM design

- **P0:** no preparation;
- **PT:** matched preparation, sign `b` matched to later disturbance `a`;
- **PM:** equal-cost sign-mismatched preparation with `b=-a`.

PM has the same magnitude and energy as PT but moves the hidden coordinate toward the opposite forced relative equilibrium. No additional policy, feedback controller, optimizer, or comparator was introduced.

## E.4 Full frozen sign/condition metric table

`E_B1` is the full-trajectory max representative-to-B1 error. `H_delta=max|e_delta-asin(a/2)|`; `H_omega=max|e_omega|`.

| `a` | Condition | `E_B1` | RMS B1 | `H_delta` | `H_omega` | max `|e_delta|` over evaluation |
|---:|---|---:|---:|---:|---:|---:|
| `+0.2` | P0 | `0.06534774384334105` | `0.03809399399337059` | `0.1001674211615598` | `0.08954202393695318` | `0.13069548768668177` |
| `+0.2` | PT | `2.076727044536923e-15` | `9.481901258630277e-16` | `2.1649348980190553e-15` | `4.6079385647875116e-15` | `0.10016742116156196` |
| `+0.2` | PM | `0.1307357122731585` | `0.07621285244933236` | `0.20033484232311938` | `0.17919273392083204` | `0.16130400338475567` |
| `-0.2` | P0 | `0.06534774384334105` | `0.03809399399337059` | `0.1001674211615598` | `0.08954202393695318` | `0.13069548768668177` |
| `-0.2` | PT | `2.076727044536923e-15` | `9.481901258630277e-16` | `2.1649348980190553e-15` | `4.6079385647875116e-15` | `0.10016742116156196` |
| `-0.2` | PM | `0.1307357122731585` | `0.07621285244933236` | `0.20033484232311938` | `0.17919273392083204` | `0.16130400338475567` |

P0 reproduces the frozen APP-B `I_zero` B1 mismatch within `5.551115123125783e-17` absolute error.

## E.5 Frozen preparation cost table

| Future `a` | Condition | preparation sign `b` | `P_q` | terminal target error `P_r` | peak input | `C_prep` | max prep `|e_delta|` |
|---:|---|---:|---:|---:|---:|---:|---:|
| `+0.2` | PT | `+0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `+0.2` | PM | `-0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `-0.2` | PT | `-0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |
| `-0.2` | PM | `+0.2` | `3.580739551835791e-15` | `4.6079385647875116e-15` | `0.20881049376163438` | `0.04006381839386479` | `0.10016742116155959` |

Frozen aggregate comparison:

- `E_target_max=2.076727044536923e-15`;
- `E_no_min=0.06534774384334105`;
- `E_mismatch_min=0.1307357122731585`;
- `B0_min=0.9999999999999682`;
- `BM_min=0.9999999999999841`;
- `H_target=4.6079385647875116e-15`;
- maximum absolute relative angle over all preparation/evaluation trajectories `0.16130400338475567`.

## E.6 Frozen classification and interpretation ceiling

All frozen PASS requirements are met, including coherent-regime safety, target agreement, separation from P0 and PM, and amplitude/energy budgets. The result remains

**PASS — RESULT FROZEN / NO NOVELTY PROMOTION**.

It is a benchmark instantiation of established output-constrained state steering, preview/feedforward, and preventive-control ideas. It does not establish a generic preparation method, optimality, robustness to unknown interventions, or generic power-grid benefit.

---

# Appendix F. Prospective-freeze and governance record

Governance source: `research/master/PROJECT_GOVERNANCE_0_1.md` plus the canonical gate/result files listed below.

The project uses the sequence `GATE → FREEZE → EXECUTION → RESULT FREEZE` to separate pre-result choices from post-result interpretation. Weak and failed outcomes are retained. This governance improves auditability and guards against post-hoc retuning; **it does not substitute for scientific validation, external replication, generalisation, or novelty evidence**.

| Scientific stage | Pre-result frozen elements | Frozen outcome | Retuning after inspection | Manuscript role |
|---|---|---|---|---|
| Prior-Art & Definitions Audit 0.1 | literature scope / definitions / comparison families | PASS — CLAIM-RESTRICTED | none | claim boundary only |
| CORE Synergetic Sufficiency Boundary 0.1 | macro map, intervention family, horizon, response, assumptions | PASS — CLAIM-RESTRICTED | none | C1 restricted diagnostic bridge |
| Neural Minimal Benchmark 0.1 | model, A/B states, C/D tasks, η=0.1, one-step response | PASS | none | C5 illustration only |
| Neural Historical Reachability 0.1 | common init, auxiliary readout, targets, η_hist=1, one step | PASS | none | artificial provenance only |
| Neural Nonlinear ReLU Pilot 0.1 | two-unit states, symmetric tasks, η=0.1, probe set | PASS | none | C5 nonlinear illustration only |
| Neural Response Coordinate Pilot 0.1 | state family, splits, interventions, 2D coordinate, baselines, metrics, thresholds | WEAK | none; near-tie retained | negative/claim-limit evidence |
| Neural Nuisance-Invariance Pilot 0.1 | gauge family, partitions, baselines incl. B3, null, thresholds | FAIL — specification-classification gap | no null/classifier repair | negative/claim-limit evidence |
| Response-coordinate integration | frozen WEAK + FAIL + Gram control | STOP / PARK | direction not reopened | no learned-coordinate contribution |
| Power-Grid Minimal Benchmark 0.1 | two-machine model, representative macro, states, ±0.2, T=5, RK4, B0/B1/C1 | PASS | none | C3 restricted exact witness |
| Controlled State Preparation 0.1 | same grid model, target, quintic path, τ=2, budgets, P0/PT/PM, T_eval=5 | PASS | none | C4 benchmark instantiation |

Mandatory preserved countercontrols/negative evidence across the package are:

- response-coordinate WEAK versus equal-dimensional raw PCA;
- nuisance-invariance specification-classification FAIL;
- exact symmetry-aware 2D Gram-PCA successful control;
- response-coordinate STOP/PARK decision;
- exact APP-B arithmetic mean/COI closure control.

No scientific experiment, simulation, test, or analysis was rerun in `Manuscript Venue-Neutral Artifact Completion 0.1`.
