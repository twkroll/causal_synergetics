# Testing Synergetic Macrostates for Intervention Sufficiency: Controlled Projectability, Frozen Minimal Witnesses, and Output-Preserving Preparation

## Abstract

Classical synergetic reduction asks whether a small set of order parameters can describe a system whose remaining degrees of freedom are slaved or rapidly relaxing. That passive or present-state sufficiency need not, by itself, determine the response to a declared family of interventions. For the full retained-trajectory response considered here, exact homogeneity along the fibres of a pre-declared macro map is the standard controlled-projectability/closure condition. We use that established condition diagnostically: given a classical slaving/order-parameter map, we ask whether the same map remains sufficient for a frozen intervention family, and we express finite-horizon deviations using standard fast-slow stability and error-estimation ingredients. We then assemble prospectively frozen minimal witnesses. In a factorised linear neural model and a two-unit ReLU model, function-equivalent parameter states can exhibit different one-step learning responses, while later learned-coordinate pilots provide explicit negative evidence: a response-aware coordinate is WEAK against equal-dimensional raw PCA, a nuisance-invariance gate ends in a specification-classification FAIL, and an exact symmetry-aware Gram representation matches the response coordinate. In a symmetric two-machine swing benchmark, a representative-machine coherent surrogate is exact on the passive coherent set but loses accuracy under a localized disturbance, whereas the arithmetic mean/center-of-inertia coordinate remains exactly closed. In the same physical fibre, a bounded finite-duration output-preserving preparation moves the hidden coherency state to the known forced relative equilibrium; after preparation is removed, the matched condition follows the coherent aggregate and outperforms no preparation and an equal-cost sign-mismatched condition. The manuscript claims neither an original quotient criterion nor a universal cross-domain law nor a generic preparation/control method. Its contribution is a restricted synergetics-centered diagnostic synthesis of established criteria, frozen witnesses, successful countercontrols, and one active preparation benchmark.

## 1. Introduction

Synergetics formalizes the reduction of high-dimensional dynamics near organized regimes through order parameters and slaving relations: a small set of slow or unstable coordinates parametrizes degrees of freedom that relax more rapidly [Haken, 1996]. Such reductions are naturally read as statements about passive dynamics, invariant or attracting manifolds, and the ability of a reduced description to reproduce selected trajectories. Control and abstraction theory ask a complementary question. If external inputs are admitted, when does a quotient or reduced coordinate evolve consistently under those inputs, and when do states identified by the reduction remain behaviorally indistinguishable? Controlled projectability, bisimulation, homomorphism, predictive-state representations, input-output computational mechanics, and causal abstraction all provide established languages for versions of that question [Tabuada and Pappas, 2005; Littman et al., 2001; Givan et al., 2003; Ravindran and Barto, 2003; Barnett and Crutchfield, 2015; Girard and Pappas, 2007; Chalupka et al., 2015, 2016; Rubenstein et al., 2017; Beckers and Halpern, 2019; Li et al., 2025; Xia and Bareinboim, 2025; Geiger et al., 2025].

The central question of this manuscript is therefore deliberately restricted: **given a pre-declared classical synergetic macro/slaving map, is that particular map sufficient for a declared intervention family and response horizon?** For the full retained-variable trajectory used here, this question reduces exactly to the established controlled-projectability/closure condition. The point is not to replace the abstraction literature. Rather, the condition supplies a precise diagnostic boundary for a synergetic reduction that was selected independently of the intervention-response test.

The contribution of the manuscript is a restricted synergetics-centered diagnostic synthesis. We connect a pre-declared slaving/order-parameter map to the established controlled-projectability criterion, test the resulting intervention-sufficiency diagnostic under prospectively frozen minimal examples in two domains, retain exact successful countercontrols, and show in the physical example how an output-preserving hidden-state preparation can alter the subsequent intervention response. We do not claim ownership of a generic state-equivalence criterion or a generic control method. The ingredients are individually close to or subsumed by established work; the manuscript contribution lies in their explicit synergetics-centered organization and in the frozen evidence chain.

Two features of that evidence chain are important. First, negative and limiting controls remain visible. In the neural branch, a learned two-dimensional response coordinate predicts held-out responses essentially exactly but is only WEAK relative to an equal-dimensional raw-parameter PCA baseline; a later nuisance-invariance gate is frozen as a specification-classification FAIL; and a symmetry-aware two-dimensional Gram representation is equally predictive and invariant. The learned-coordinate direction is therefore parked rather than promoted. In the power-grid branch, the representative-machine macro fails under a localized hidden-machine disturbance, but the arithmetic mean/center-of-inertia (COI) coordinate is exactly closed. The grid result is consequently coordinate-specific, not an argument against low-dimensional aggregation.

Second, the examples were prospectively specified before execution. Model classes, interventions, horizons, primary metrics, comparators, numerical methods, and decision thresholds were frozen before result inspection. Weak and failed outcomes were retained rather than repaired, and successful countercontrols were not omitted. This process discipline is part of the evidential interpretation, not a scientific claim by itself.

Section 2 positions the manuscript against the closest parent literatures. Section 3 states the diagnostic framework and the standard projectability boundary, including the frozen finite-horizon bridge. Sections 4 and 5 give the neural and power-grid witnesses with their mandatory negative and successful controls. Section 6 presents the output-preserving preparation benchmark in the same physical fibre. Section 7 synthesizes the evidence and limitations, and Section 8 concludes with the restricted diagnostic question.

> **Figure 1 — Diagnostic schematic (conceptual; no quantitative data).** Full-state fibre → pre-declared synergetic macro/slaving map → frozen intervention family and retained response → standard controlled-projectability test → either sufficient macro or hidden-mode leakage. This figure is to be rendered only from the definitions in Section 3.

## 2. Related Work and Claim Positioning

### 2.1 Synergetics, slaving, and controlled reduction

Haken's slaving principle provides the classical reference point for the manuscript [Haken, 1996]. Near an organized regime, fast degrees of freedom may become functions of a smaller set of order parameters, yielding a reduced dynamics on an invariant or attracting relation. That structure is not, by itself, a statement about a controlled quotient over an entire fibre. Singular-perturbation and control theory have long treated fast-slow reduction in the presence of inputs, disturbances, and stability estimates [Kokotović et al., 1976; Christofides and Teel, 1996]. Accordingly, neither fast relaxation nor the fact that forcing can expose fast modes is treated here as a contribution.

The manuscript uses the synergetic map as an externally given candidate: it is not learned or optimized from the intervention responses. This ordering is central to the diagnostic interpretation. The question is whether an already chosen order-parameter/slaving description satisfies the stronger controlled condition required by the declared response.

### 2.2 Controlled quotients, bisimulation, predictive states, and abstraction

The closest exact control-theoretic predecessor is the quotient/projectability framework of Tabuada and Pappas [2005], which develops nonlinear control-system quotients and relates projectability to controlled invariance. Approximate bisimulation supplies established error and precision language for controlled reductions [Girard and Pappas, 2007]. Related discrete and stochastic frameworks include MDP equivalence and minimization [Givan et al., 2003], SMDP homomorphisms [Ravindran and Barto, 2003], bisimulation metrics [Ferns et al., 2004], predictive-state representations [Littman et al., 2001], and input-output computational mechanics through ε-transducers [Barnett and Crutchfield, 2015].

Causal feature learning and causal abstraction likewise group microvariables or states according to interventional behavior and study consistency across levels [Chalupka et al., 2015, 2016; Rubenstein et al., 2017; Beckers and Halpern, 2019]. Recent work on identifiability and lossy abstraction makes the relevance of intervention sets and non-homogeneous low-level fibres especially explicit [Li et al., 2025; Xia and Bareinboim, 2025; Geiger et al., 2025]. The present framework is therefore not a replacement for these notions. For the response functional used here, the exact criterion is intentionally recognized as part of this established controlled-abstraction family.

### 2.3 Neural parameter symmetries and training dynamics

Function-preserving neural parameter transformations are well established. Path-SGD explicitly targets optimization geometry that is invariant to output-preserving rescalings [Neyshabur et al., 2015], while Dinh et al. [2017] use ReLU parameter symmetries to show that functionally equivalent networks can have strongly altered parameter-space geometry. Most directly for our qualitative neural witness, Lebeurrier, Vayer, and Gribonval [2026] show that properly rescaled ReLU parameterizations can represent the same function while displaying substantially different training dynamics. We therefore treat the qualitative same-function/different-learning-response phenomenon as SAME-level prior art. The linear and ReLU examples in Section 4 are frozen illustrations, not neural-method contribution claims.

Function-preserving network morphisms, parameter-efficient adaptation, and editing further reinforce the need for restraint when interpreting internal-state manipulations [Chen et al., 2016; Wei et al., 2016; Jacot et al., 2018; Hu et al., 2022; Meng et al., 2022].

### 2.4 Power-system coherency and dynamic equivalents

Coherency-based equivalents and aggregate generators are longstanding tools for transient-stability analysis. Berg and Ghafurian [1983] construct coherency-based equivalents with representative/equivalent generators; Sankaranarayanan et al. [1983] study coherency identification and equivalents; and Kai et al. [2022] review dynamic equivalents for transient-stability studies. The two-machine example in Section 5 is placed inside this established domain. Its role is to provide an analytically transparent witness in which a pre-declared representative-machine macro is exact on a coherent passive set, loses accuracy under a specific localized disturbance, and is accompanied by an exact mean/COI closure control.

### 2.5 Output-nulling, preview/feedforward, and preventive control

Moving internal state while constraining an output belongs to the established traditions of output-nulling controlled-invariant subspaces, output-nulling reachability, and zero dynamics [Isidori, 2013; Ntogramatzidis and Padula, 2017]. Preview/feedforward control explicitly uses information about future references or disturbances to prepare the system response [Goodwin et al., 2011]. In power systems, preventive rescheduling and related pre-contingency control modify the operating state to improve the response to anticipated contingencies [Verma and Niazi, 2013; Li and Bose, 1995]. Section 6 is interpreted as a benchmark instantiation of those ideas in the same physical fibre exposed by Section 5, not as a generic control-method claim.

### 2.6 Exact claim hierarchy and what is not claimed

The claim-level literature revalidation assigns distinct manuscript roles to the programme components. Table 1 records those roles because they constrain the prose throughout the paper.

**Table 1 — Claim / prior-art / manuscript-role matrix.**

| Item | LIT class | Action | Manuscript role | Mandatory predecessor families | Prohibited interpretation |
|---|---|---|---|---|---|
| C1: slaving / controlled-projectability boundary + finite-horizon packaging | CLOSE | RETAIN-RESTRICTED | Diagnostic bridge for a pre-declared synergetic map | Haken; Tabuada–Pappas; Girard–Pappas; singular perturbation/ISS; controlled abstraction | Ownership of projectability, lumpability, or standard fast-slow bounds |
| C2: cross-domain feasibility package | RELATED | REINTERPRET | Evidential organization of two frozen minimal domains | controlled abstraction; neural symmetry; coherency reduction | Universal cross-domain law |
| C3: two-machine representative mismatch + mean/COI control | CLOSE | RETAIN-RESTRICTED | Exact minimal power-grid witness with successful countercontrol | coherency-based equivalents; aggregate/COI reductions | General failure of low-dimensional grid aggregation |
| C4: same-current-macro hidden-state preparation | CLOSE | REINTERPRET | Benchmark instantiation of output-constrained steering, preview/feedforward, preventive control | zero dynamics/output nulling; preview; preventive control | Generic preparation method, optimality, robustness, or broad grid capability |
| C5: same-function neural states with different one-step responses | SAME | DEMOTE | Illustration only | Path-SGD; ReLU symmetry/geometry; path-conditioned training | Neural-method contribution or uniquely response-specific state coordinate |
| Package P | DISTINCT-ENOUGH-FOR-RESTRICTED-CLAIM | RETAIN-RESTRICTED | Sole contribution-bearing framing: synergetics-centered diagnostic synthesis | all groups above | Field-establishment, generic state-equivalence ownership, or ingredient-level priority |

## 3. Diagnostic Framework

### 3.1 Pre-declared macro/slaving map and intervention family

Let the microscopic state be

`x=(q,r) ∈ D ⊂ R^m × R^n`,

where `q` is a pre-declared candidate synergetic order parameter and `r` collects nominally slaved or fast degrees of freedom. The candidate macro map is

`π(q,r)=q`.

The controlled dynamics are

`q_dot = f(q,r,u)`,

`r_dot = g(q,r,u)`,

with locally Lipschitz dynamics sufficient for unique trajectories over the fixed horizon. Controls belong to a compact instantaneous set `A`, and the admissible family is the piecewise-continuous set

`U = {u:[0,T]→A}`,

including constant controls. The intervention family and horizon are part of the diagnostic specification; changing them can change the resulting equivalence classes and therefore cannot be treated as an innocuous afterthought.

The classical slaving structure is represented by a fixed graph

`M = {(q,r): r=h(q)}`,

with unforced invariance

`g(q,h(q),0)=Dh(q) f(q,h(q),0)`

and, when required, normal attraction or a quantitative relaxation estimate for

`e=r-h(q)`.

This is the classical synergetic object [Haken, 1996]. The diagnostic asks whether it is also sufficient for the declared interventions.

### 3.2 Full retained-trajectory fibre response

For initial state `x0` and admissible intervention `u`, define the retained response

`Γ(x0,u)=q^u_x0(·) ∈ C([0,T],R^m)`

with metric

`d_Γ(Γ1,Γ2)=sup_{0≤t≤T} ||q1(t)-q2(t)||`.

The macro is intervention-response sufficient for this frozen response if two states in the same fibre have identical retained trajectories for every admissible intervention:

`π(x1)=π(x2)  =>  Γ(x1,u)=Γ(x2,u)  for every u∈U`.

This is not introduced as a generic state definition; action-conditioned predictive equivalence and controlled abstraction are established in the literatures reviewed in Section 2.

### 3.3 Standard controlled-projectability/closure criterion

**Proposition 1 (standard controlled-projectability equivalence; included for self-containment).** Assume unique solutions over `[0,T]` and that the intervention family contains every constant control `u(t)=a`, `a∈A`. For the full retained-trajectory response above, the following are equivalent:

1. every pair of states on the same `q`-fibre has the same retained trajectory for every admissible intervention;
2. for every instantaneous control `a`, the projected vector field is constant along each fibre,
   `f(q,r1,a)=f(q,r2,a)`;
3. there exists a closed projected vector field `f_bar(q,a)` satisfying
   `f(q,r,a)=f_bar(q,a)` on the relevant domain.

The implication from 3 to 1 is ordinary uniqueness of the closed `q` initial-value problem. For 1 to 2, apply any constant control to two same-`q` states and differentiate their identical retained trajectories at `t=0`. The equivalence of 2 and 3 is the definition of projectability through the quotient map. This statement is structurally subsumed by controlled quotient/projectability and exact abstraction theory [Tabuada and Pappas, 2005; Girard and Pappas, 2007]. Its role here is translational: it identifies the extra standard property a pre-declared synergetic macro must satisfy to be exact for the selected intervention response.

A controlled-invariant slaving graph is weaker than global fibre closure. If

`g(q,h(q),u)=Dh(q)f(q,h(q),u)`

for all admissible controls, trajectories initialized on the graph remain on it and obey `q_dot=f(q,h(q),u)`. But this does not imply that off-graph states with the same `q` have the same projected vector field.

### 3.4 Why unforced slaving alone is insufficient

Unforced slaving constrains the vector field on or toward `M` at `u=0`; Proposition 1 requires fibrewise constancy of the projected controlled vector field for all relevant hidden coordinates and all admissible controls. These statements are logically distinct. An intervention can therefore expose two failure mechanisms:

- **fibre memory:** different hidden initial coordinates on the same current macro fibre can produce different retained responses;
- **control leakage:** an intervention can push a state away from an unforced slaving graph, invalidating a naive reduced extension even when the initial state lies on the graph.

The distinction between invariant-manifold reduction and controlled quotient closure is standard. The synergetic use is to make the distinction explicit for an order-parameter map selected before the controlled test.

### 3.5 Finite-horizon diagnostic from standard fast-slow/error ingredients

The frozen CORE analysis provides both exact model-specific expressions and a general comparison bound. The scalar witness

`q_dot = u r`,

`r_dot = -λ r + u`

has slaving graph `r=0`. For two same-`q` states under the same admissible input, the hidden-state difference decays exactly as

`Δr(t)=Δr0 exp(-λt)`.

Consequently,

`d_Γ ≤ U |Δr0| (1-exp(-λT))/λ`,

and the bound is sharp for a constant sign-aligned intervention. Starting exactly on the slaving graph, the naive graph-restricted model predicts constant `q`, whereas the true intervention-induced retained error obeys

`d_Γ(q,q_red) ≤ U^2 [T/λ - (1-exp(-λT))/λ^2]`,

again attained by constant `|u|=U` in the frozen scalar model.

For a general pre-declared graph, let `e=r-h(q)` and `f_bar(q,u)=f(q,h(q),u)`. Assume the standard comparison conditions

`D^+||e|| ≤ -λ||e|| + δ + β||u||`,

`||f(q,r,u)-f(q,h(q),u)|| ≤ L_e ||e||`,

`||f_bar(q1,u)-f_bar(q2,u)|| ≤ L_q ||q1-q2||`.

Here `λ` is the fast relaxation rate, `δ` an unforced slaving defect, and `β` the intervention leakage into the fast deviation. For `||u||_∞≤U`, define

`c=(δ+βU)/λ`,

`Φ(L_q,t)=(exp(L_q t)-1)/L_q` for `L_q>0` and `Φ(0,t)=t`,

`Ψ(L_q,λ,t)=(exp(L_q t)-exp(-λt))/(L_q+λ)`.

The frozen comparison/Grönwall calculation yields

`||q(t)-q_bar(t)|| ≤ L_e [ ||e0|| Ψ(L_q,λ,t) + c(Φ(L_q,t)-Ψ(L_q,λ,t)) ]`,

and therefore the same expression at `T` bounds `d_Γ`. For a tube `||e0||≤ρ`, two states in the same fibre have the conservative response-diameter estimate

`d_Γ(Γ(x1,u),Γ(x2,u)) ≤ 2 B_T(ρ)`,

with

`B_T(ρ)=L_e [ ρ Ψ(L_q,λ,T) + ((δ+βU)/λ)(Φ(L_q,T)-Ψ(L_q,λ,T)) ]`.

These are standard singular-perturbation/ISS-style ingredients and comparison methods [Kokotović et al., 1976; Christofides and Teel, 1996]. The retained value is diagnostic packaging: a pre-existing relaxation estimate can be translated into the same intervention-response metric used to test the candidate synergetic macro.

### 3.6 Minimal CORE witness

The scalar system above is the minimal coordinate-count witness used by the programme: one retained coordinate, one hidden fast coordinate, and one intervention. For `u=0`, `q(t)=q0` for every initial `r0`, while `r(t)=r0 exp(-λt)` and the graph `r=0` is globally attracting in the fast direction. Under a constant nonzero intervention `u=a`,

`r(t)=r0 exp(-λt)+(a/λ)(1-exp(-λt))`,

`q(t)=q0+(a r0/λ)(1-exp(-λt))+a^2[t/λ-(1-exp(-λt))/λ^2]`.

Thus passive retained behavior can be exact across an entire fibre even though a declared intervention immediately reveals hidden-state dependence and drives the system off the unforced graph. This witness motivates the two application sections without being promoted as an original control phenomenon.

## 4. Neural Illustration and Negative Coordinate Evidence

The neural branch serves two different manuscript roles. The exact linear and ReLU constructions illustrate the distinction between current functional equivalence and response to a one-step learning intervention. The later coordinate pilots are negative/limiting evidence that prevents promotion of a learned response representation.

### 4.1 Linear same-function/different-response witness

Consider the factorised linear scalar-output network

`f_{U,v}(x)=v^T Ux`,

with `d=h=2` and effective function parameter `w=U^T v`. The frozen states are

`v_A=v_B=(1,0)^T`,

`U_A=[[0,0],[1,0]]`,

`U_B=[[0,0],[0,1]]`.

Both have `w=(0,0)^T`, `||U||_F=1`, and `||v||_2=1`. For quadratic task loss

`L_c(w)=1/2 ||w-c||_2^2`

and one simultaneous full-batch gradient step at `η=0.1`, the effective update is

`w^+ = w - η(U^T U + ||v||^2 I)g + η^2 g(v^T U g)`,

where `g=w-c`. In the frozen states `w=0`, so the second-order correction vanishes and `w^+=ηPc` with `P=U^TU+||v||^2I`. State A has `P_A=diag(2,1)` and state B has `P_B=diag(1,2)`.

On task C, `c=e1`, state A reaches `w^+=(0.2,0)` with loss `0.32`, while state B reaches `(0.1,0)` with loss `0.405`. On task D, `c=e2`, the preference reverses: state A reaches `(0,0.1)` with loss `0.405`, while state B reaches `(0,0.2)` with loss `0.32`. The directed loss advantage is `0.085` in both directions, and the frozen analytical and autograd implementations agree componentwise with maximum observed discrepancy `0.0` in float64.

These numbers are a feasibility illustration only. The qualitative phenomenon is already established by the neural optimization and rescaling literature [Neyshabur et al., 2015; Dinh et al., 2017; Lebeurrier et al., 2026].

### 4.2 Historical reachability as artificial provenance only

A separate frozen construction shows that the linear endpoints can be generated from the same hidden initialization under a deliberately artificial auxiliary-gradient protocol. Both histories begin at `U0=0` with fixed main readout `v=e1`; a temporary auxiliary readout `a=e2` is used with loss

`H_c(U)=1/2 ||U^T a-c||_2^2`.

One gradient step with `η_hist=1` gives `U^+=a c^T`. Targets `c=e1` and `c=e2` therefore reach exactly `U_A` and `U_B`, while the main function stays `w=U^Tv=0` because `a^Tv=0`. The auxiliary head is discarded before the frozen C/D evaluation, which reproduces the linear benchmark values exactly.

This establishes provenance only under the stated auxiliary mechanism. It is not evidence of natural reachability under ordinary single-head SGD, and it is not used to elevate the neural claim.

### 4.3 Two-unit ReLU illustration

The frozen nonlinear pilot uses

`f_{U,v}(x)=v^T ReLU(Ux)`

with

`U_A=[[2,0],[0,1]],   v_A=(1/2,1)^T`,

`U_B=[[1,0],[0,2]],   v_B=(1,1/2)^T`.

Positive homogeneity gives global current-function equivalence:

`f_A(x)=f_B(x)=ReLU(x1)+ReLU(x2)`

for all inputs. The simple norms also match. The frozen tasks are C: `x=(1,-1)`, `y=2`, and D: `x=(-1,1)`, `y=2`, with one simultaneous gradient step at `η=0.1`. The activation margins stay away from zero throughout the frozen step.

On task C, state A reaches post-step loss `0.14045` and state B `0.2312`; on task D the values reverse. The symmetric directed advantage is `0.09075`. Analytical and autograd updates again agree componentwise with maximum observed discrepancy `0.0`. This is a nonlinear minimal witness of an established rescaling/training-dynamics phenomenon, with Lebeurrier et al. [2026] treated as SAME-level prior art for the qualitative claim.

### 4.4 Response-coordinate WEAK result

The subsequent `Neural Response Coordinate Pilot 0.1` asked whether a two-dimensional response-aware coordinate learned from four calibration interventions could predict eight held-out one-step interventions on held-out states in a frozen `d=4`, `h=5` factorised-linear family. The candidate performs essentially exactly:

- aggregate held-out `R2_state = 1.0`;
- minimum per-held-out-intervention `R2_state(c)=1.0`;
- `NRMSE = 7.30513741157965e-16`.

It strongly exceeds the current-function and simple-summary baselines. However, the equal-dimensional raw-parameter PCA baseline B2 reaches

`R2_state(B2)=0.999883026432542`,

so the candidate advantage is only

`0.000116973567458323`,

well below the prospectively frozen PASS margin `0.05`. Under the pre-specified discriminator, the result is therefore **WEAK**, not PASS. This near-tie was retained without changing the state family, coordinate, baseline, threshold, split, intervention set, or horizon.

### 4.5 Nuisance-invariance FAIL, Gram control, and PARK decision

A later frozen nuisance-invariance gate applied hidden-basis gauge rotations to 648 states. The two-dimensional response coordinate is numerically gauge invariant and exactly predictive on nuisance-only, latent-only, and joint held-out partitions; on the joint partition `R2_state=1.0` and `J_nuis=5.596227006606825e-32`. Naive two-dimensional raw-parameter PCA collapses under unseen gauge orientations (`R2_state≈2.220446049250313e-16`, `J_nuis=1.0`).

The decisive successful countercontrol is an explicitly gauge-invariant two-dimensional Gram-PCA representation. It is equally predictive (`R2_state=1.0`) and equally invariant (`J_nuis=2.692209973425601e-32`). Response measurements are therefore not uniquely required to quotient this known symmetry.

The frozen one-state cyclic null attains joint `R2_state=0.6999999999999995`, violating the PASS and WEAK null thresholds while none of the prospectively enumerated NULL conditions applies. The classifier is thus non-total for the realized metric vector. The gate is frozen as **FAIL — SPECIFICATION CLASSIFICATION GAP**, not as a numerical failure and not as a scientific NULL. No post-hoc null repair or classifier amendment was performed.

Given the earlier WEAK result and the exact Gram comparator, the programme decision is **STOP / PARK RESPONSE-COORDINATE DIRECTION**. The manuscript therefore makes no claim that the learned coordinate is superior to symmetry-aware raw-state quotients.

**Table 2 — Frozen evidence and countercontrols.** Only canonical frozen values are shown.

| Evidence item | Frozen observation | Manuscript interpretation |
|---|---|---|
| CORE exact full-trajectory criterion | fibre response homogeneity iff controlled projectability/closure | standard criterion used diagnostically for a pre-declared synergetic map |
| CORE scalar witness | `d_Γ ≤ U|Δr0|(1-e^{-λT})/λ`; graph-start error `≤U²[T/λ-(1-e^{-λT})/λ²]` | exact minimal illustration; standard fast-slow mechanism |
| Neural linear minimal | C: A `0.32`, B `0.405`; D reversed; advantage `0.085` | illustrative SAME-level phenomenon |
| Historical reachability | exact A/B endpoints from common `U0=0`; main `w=0` preserved | artificial provenance only |
| Two-unit ReLU | C: A `0.14045`, B `0.2312`; D reversed; advantage `0.09075` | nonlinear illustration only |
| Response-coordinate pilot | candidate `R2=1.0`, B2 `R2=0.999883026432542` | WEAK versus equal-dimensional raw PCA |
| Nuisance pilot | candidate joint `R2=1.0`; null `0.6999999999999995` | FAIL — specification-classification gap |
| Symmetry-aware neural control | Gram-PCA joint `R2=1.0`, `J_nuis=2.692209973425601e-32` | exact equal-dimensional gauge-aware countercontrol |
| Response-coordinate integration | STOP / PARKED | no learned-coordinate promotion |
| APP-B representative macro | minimum controlled B0 `d_inf=0.3549858420076152` | material mismatch for the frozen representative macro |
| APP-B coherent aggregate surrogate | minimum controlled B1 `d_inf=0.06534774384333092` | much closer to representative machine, but still not exact for it |
| APP-B mean/COI control | closure error `3.885780586188048e-14` | exact low-dimensional successful countercontrol |
| APP-C matched PT | `E_B1=2.076727044536923e-15` | matched preparation follows frozen aggregate target |
| APP-C P0 / PM | P0 `0.06534774384334105`; PM `0.1307357122731585` | no-prep and equal-cost sign-mismatch remain separated |

> **Figure 2 — Cross-domain witness schematic (conceptual).** Panel A: identical current neural function → same learning task → different one-step parameter-induced function response, with the Gram-PCA countercontrol shown beside the parked coordinate direction. Panel B: passive coherent two-machine representative macro → localized machine-2 step → representative mismatch, with exact arithmetic mean/COI closure shown as the successful control. The two panels are feasibility witnesses, not a universality claim.

## 5. Power-Grid Minimal Witness

### 5.1 Symmetric two-machine swing model and coherent set

The frozen power-system benchmark uses two identical classical swing machines with normalized `M=D=K=1` and a lossless tie line:

`delta1_dot = omega1`,

`omega1_dot = -omega1 + sin(delta2-delta1)`,

`delta2_dot = omega2`,

`omega2_dot = -omega2 + sin(delta1-delta2) + u(t)`.

The pre-declared representative macro is

`q=(delta1,omega1)`,

and the hidden coherency coordinates are

`e_delta=delta2-delta1`,

`e_omega=omega2-omega1`.

The exact transverse dynamics are

`e_delta_dot=e_omega`,

`e_omega_dot=-e_omega-2 sin(e_delta)+u`.

For `u=0`, the coherent set `e_delta=e_omega=0` is invariant. Its transverse Jacobian is

`[[0,1],[-2,-1]]`,

with eigenvalues `(-1 ± i sqrt(7))/2`, so the coherent set is locally exponentially attracting around synchrony. The benchmark does not infer a broader attraction statement.

The frozen interventions are `u=0,+0.2,-0.2`, the horizon is `T=5`, and the initial coherent speeds are `-0.1,0,+0.1` with zero angles. Simulation used deterministic float64 RK4 at primary `dt=0.001` with audit `dt=0.0005`; the maximum primary/half-step discrepancy was `8.1601392309949e-15`.

### 5.2 Representative-machine passive exactness

On the coherent passive set, the representative macro obeys exactly

`delta1_dot=omega1`,

`omega1_dot=-omega1`.

The frozen passive-slaving representative model B0 is therefore exact for all three declared passive coherent initial states: `E_pass=0`.

This is precisely the setting in which a passive/current description appears maximally favorable: the chosen representative reduction is not merely approximate on the declared passive set; it is exact.

### 5.3 Localized hidden-machine disturbance and representative mismatch

Under a nonzero local input, the coherent set is not controlled invariant. On `e_delta=e_omega=0`,

`(e_delta_dot,e_omega_dot)=(0,u)`.

The hidden-machine step immediately drives relative motion, while B0 continues to enforce the passive substitution and contains no direct `u` term.

Across the frozen initial states and both step signs, the minimum controlled B0 full-trajectory max error is

`E_B0_min=0.3549858420076152`.

For the zero-speed initial condition and either sign, the representative-machine error is `0.354985842007615`, while the full-model coherency maxima are approximately

`max|e_delta|=0.130695487686682`,

`max|e_omega|=0.0895420239369532`.

The physical-admissibility condition remains comfortably inside the frozen `|e_delta|<π/2` bound.

A coherent aggregate surrogate B1 is much closer to the representative machine than B0, with minimum controlled representative mismatch

`E_B1_min=0.06534774384333092`,

but B1 is not exact for the representative-machine coordinate under the localized disturbance.

### 5.4 Exact arithmetic mean/COI closure countercontrol

For the arithmetic mean/COI coordinates

`delta_mean=(delta1+delta2)/2`,

`omega_mean=(omega1+omega2)/2`,

the antisymmetric line-power terms cancel exactly:

`delta_mean_dot=omega_mean`,

`omega_mean_dot=-omega_mean+u/2`.

This is exactly the B1 aggregate dynamics. The frozen full-model versus mean/COI closure error is

`3.885780586188048e-14`,

at numerical precision. The identities

`delta1-delta_mean=-e_delta/2`,

`omega1-omega_mean=-e_omega/2`

also explain why B1 is close to, but not exact for, the representative machine.

The mean/COI control is scientifically essential. The benchmark demonstrates that the pre-declared representative-machine coherent surrogate is intervention-insufficient under this localized step; it does not show that low-dimensional power-grid aggregation generally fails. This interpretation is consistent with the established coherency/dynamic-equivalent literature [Berg and Ghafurian, 1983; Sankaranarayanan et al., 1983; Kai et al., 2022].

### 5.5 Interpretation within established coherency theory

The grid witness mirrors the CORE diagnostic in a physical ODE. Passive coherence supplies an invariant and attracting relation, and a localized intervention violates controlled invariance of that relation. The representative coordinate then loses the exactness it had on the passive coherent set. At the same time, another two-dimensional aggregate is exactly closed under the same disturbance. The result is therefore best read as an exact coordinate-specific witness inside established coherency theory, not as a general verdict on coherent reduction.

> **Figure 3 — Power-grid frozen result.** If already stored frozen trajectory artifacts are available, render only those artifacts and annotate the exact mean/COI closure control. Otherwise use a schematic of representative versus aggregate coordinates together with Table 3; do not regenerate trajectories for this figure.

## 6. Output-Preserving Preparation Benchmark

### 6.1 Same physical fibre and known later disturbance

The preparation benchmark uses the same normalized two-machine model and the same representative macro `q=(delta1,omega1)`. The initial state is the synchronous equilibrium `x_init=(0,0,0,0)`. The later evaluation disturbance is a known local machine-2 step `a=+0.2` or `a=-0.2`.

For a constant later step, the hidden relative equilibrium satisfies

`2 sin(e_delta*)=a`,

so

`e_delta*=asin(a/2)`, `e_omega*=0`.

For `|a|=0.2`, `|e_delta*|=asin(0.1)=0.1001674211615598`.

The benchmark asks whether the system can be moved within the same present representative-macro fibre so that, after preparation has ended, the subsequent localized disturbance produces the coherent-aggregate response. This is framed as output-constrained hidden-state steering with preview of the known later disturbance [Isidori, 2013; Ntogramatzidis and Padula, 2017; Goodwin et al., 2011; Verma and Niazi, 2013; Li and Bose, 1995].

### 6.2 Frozen bounded quintic/inverse-dynamics preparation

For preparation sign `b`, the desired relative path is the quintic smoothstep

`e_d(t;b)=e_star(b)[10 ξ^3 - 15 ξ^4 + 6 ξ^5]`,

with `ξ=t/2` over the frozen preparation duration `τ_prep=2`. Exact inverse dynamics defines

`p1(t;b)=-sin(e_d(t;b))`,

`p2(t;b)=e_d_ddot(t;b)+e_d_dot(t;b)+sin(e_d(t;b))`.

The resulting trajectory holds the representative macro fixed to numerical precision while moving the hidden relative state to the target. The matched preparation has terminal hidden-target error

`4.6079385647875116e-15`,

and macro-preservation error

`P_q=3.580739551835791e-15`.

The frozen peak input is

`0.20881049376163438 ≤ 0.35`,

and preparation energy is

`0.04006381839386479 ≤ 0.25`.

Sign reversal produces identical cost and exact input sign symmetry in the frozen implementation. Preparation is switched off before evaluation; during the evaluation phase the inputs are exactly `p1=0`, `p2=a`.

### 6.3 P0/PT/PM comparator design

Three conditions are frozen:

- **P0:** no preparation;
- **PT:** matched preparation using the sign corresponding to the known later disturbance;
- **PM:** equal-cost sign-mismatched preparation.

The purpose of PM is directional control: it uses the same preparation magnitude and energy as PT but moves the hidden state toward the opposite forced relative equilibrium. This prevents the interpretation that any pre-motion of the hidden state would suffice.

No additional policy, feedback controller, optimizer, or comparator was introduced.

### 6.4 Frozen PASS metrics

For both later disturbance signs, PT matches the coherent aggregate B1 to numerical precision:

`E_target_max=2.076727044536923e-15`.

By contrast,

`E_no_min=0.06534774384334105`,

`E_mismatch_min=0.1307357122731585`.

The corresponding improvement fractions are

`B0_min=0.9999999999999682`,

`BM_min=0.9999999999999841`.

The maximum absolute relative angle over all preparation/evaluation trajectories is `0.16130400338475567`, below the frozen coherent-regime safety threshold `π/2`. Primary/audit numerical discrepancy is `5.738465258531278e-15`.

The P0 condition reproduces the APP-B `I_zero` coherent-aggregate mismatch within `5.551115123125783e-17`, linking the preparation benchmark directly to the same physical witness rather than to a separately tuned system.

**Table 3 — Frozen power-grid and preparation metrics.**

| Quantity | Frozen value | Role |
|---|---:|---|
| APP-B passive representative error `E_pass` | `0` | representative macro exact on declared passive coherent set |
| APP-B controlled B0 minimum `d_inf` | `0.3549858420076152` | localized-disturbance representative mismatch |
| APP-B controlled B1 minimum representative mismatch | `0.06534774384333092` | coherent aggregate is closer but not exact for representative machine |
| APP-B maximum `|e_delta|` | `0.13069548768668177` | hidden coherency excursion |
| APP-B maximum controlled `|e_omega|` | `0.08954202393695339` | hidden coherency-speed excursion |
| APP-B mean/COI closure error | `3.885780586188048e-14` | exact low-dimensional countercontrol |
| APP-B primary/half-step discrepancy | `8.1601392309949e-15` | numerical convergence audit |
| APP-C target `|e_delta*|` | `0.1001674211615598` | forced hidden relative equilibrium |
| APP-C macro preservation `P_q` | `3.580739551835791e-15` | present representative macro preserved during prep |
| APP-C terminal hidden-target error | `4.6079385647875116e-15` | target reached |
| APP-C peak preparation input | `0.20881049376163438` | below frozen `0.35` cap |
| APP-C preparation energy | `0.04006381839386479` | below frozen `0.25` budget |
| APP-C PT `E_B1` | `2.076727044536923e-15` | matched prep follows aggregate target |
| APP-C P0 `E_B1` | `0.06534774384334105` | no preparation comparator |
| APP-C PM `E_B1` | `0.1307357122731585` | equal-cost sign-mismatched comparator |
| APP-C maximum absolute relative angle | `0.16130400338475567` | coherent-regime safety audit |
| APP-C primary/audit discrepancy | `5.738465258531278e-15` | numerical convergence audit |

### 6.5 Relation to output-nulling, preview/feedforward, and preventive control

The preparation result should be interpreted narrowly. Geometric control already formalizes internal-state motion under output constraints, and zero dynamics provide a standard language for internal behavior compatible with constrained output [Isidori, 2013; Ntogramatzidis and Padula, 2017]. Preview/feedforward methods use known future disturbance information to shape the current trajectory [Goodwin et al., 2011], while preventive power-system control changes the pre-contingency state in anticipation of a future event [Verma and Niazi, 2013; Li and Bose, 1995].

The retained value here is the alignment of those established ideas with the diagnostic fibre from Section 5: the output held fixed is exactly the representative macro that was insufficient; the hidden coordinate moved is exactly the coherency mode exposed by the localized disturbance; the target is the forced relative equilibrium; preparation is bounded and finite-duration; preparation is removed before evaluation; and the matched condition is compared with both no preparation and an equal-cost directionally wrong preparation.

> **Figure 4 — Preparation protocol (conceptual).** Preparation phase: hold `q=(delta1,omega1)` fixed while moving `(e_delta,e_omega)` along the frozen quintic path → preparation inputs off → apply known localized step `a` → compare P0/PT/PM against the coherent aggregate B1. Only frozen analytic path formulas and scalar outcomes may be visualized.

## 7. Synthesis and Limitations

### 7.1 Package-level synthesis versus ingredient-level prior art

The manuscript's organizing statement is modest: a classical synergetic macro selected for passive/slaving reasons can be subjected to the established controlled-projectability test for a declared intervention family. Exact failure means that the selected fibre does not determine the chosen controlled response; approximate failure can be bounded with standard fast-slow ingredients when suitable contraction and Lipschitz estimates are available. Minimal frozen examples then make the diagnostic concrete, and the power-grid fibre is used constructively in an output-preserving preparation benchmark.

Every ingredient has close or SAME-level predecessors. Controlled projectability and abstraction are established; fast-slow comparison bounds are established; function-equivalent neural states with different training dynamics are established; coherency-based aggregation is established; and output-constrained steering, preview/feedforward, and preventive control are established. The manuscript therefore does not infer contribution from the absence of an exact literature match. Its contribution is the restricted organization of these ingredients around a pre-declared synergetic map, together with a prospectively frozen evidence chain that retains countercontrols and negative outcomes.

### 7.2 Prospective freezing and anti-cherry-picking discipline

The examples were specified before effect inspection. In the neural coordinate branch, the near-tie with raw PCA was accepted as WEAK. The nuisance null/classifier problem was accepted as FAIL rather than repaired, and the exact symmetry-aware Gram control was retained. The coordinate direction was then parked. In the grid branch, the model, disturbance, horizon, metric, numerical method, and comparator set were fixed before execution, and the exact mean/COI closure was retained in the same analysis. In the preparation branch, exactly one matched construction and the P0/PT/PM comparator set were executed under frozen budgets and metrics.

This process increases the credibility of the reported boundaries but does not elevate any claim. Weak and failed results are scientifically informative here precisely because they prevent stronger interpretation.

### 7.3 Neural limitations

The positive neural witnesses are synthetic and small. The linear example is factorised, quadratic, and one-step. The historical reachability mechanism uses an artificial auxiliary head rather than ordinary single-head training. The ReLU example has two units, a constructed positive-homogeneity symmetry, and one optimizer step. None of these establishes behavior for realistic multi-step training, large networks, stochastic optimization, adapters, language models, or real datasets.

The learned-coordinate evidence is especially restrictive. The first coordinate pilot is WEAK because equal-dimensional raw PCA is nearly exact. The nuisance pilot does show that response coordinates automatically quotient a frozen hidden-basis gauge symmetry relative to naive raw PCA, but an explicitly symmetry-aware two-dimensional Gram representation is exactly as predictive and invariant. Moreover, the pre-specified null/classifier is non-total for the realized metric vector. The response-coordinate direction is therefore parked, and the manuscript does not treat learned response coordinates as a contribution.

### 7.4 Power-grid limitations

The physical witness is a normalized, symmetric two-machine system with one lossless line and a single localized mechanical/injection step. It is an exact minimal example, not a statement about realistic grid-scale dynamic equivalents. The representative-machine macro is intentionally specific. Under the same disturbance, the mean/COI coordinate is exactly closed, demonstrating that the failure is not an intrinsic consequence of low dimension.

Coherency and dynamic-equivalent theory contain richer machine models, operating conditions, disturbance classes, and aggregation schemes [Berg and Ghafurian, 1983; Sankaranarayanan et al., 1983; Kai et al., 2022]. No claim is made that the representative failure observed here persists across those settings.

### 7.5 Preparation limitations

The preparation benchmark assumes exact model knowledge and preview of the later disturbance sign and magnitude. The control is open-loop inverse dynamics over a fixed two-second preparation phase, and the target is analytically chosen from the known forced relative equilibrium. The benchmark does not test uncertainty, stochastic events, robustness, feedback design, actuator constraints beyond the frozen amplitude and energy budgets, or optimality. It does not establish a broadly useful power-system strategy.

The scientifically retained statement is narrower: in this exact model, two states with the same present representative macro can be deliberately distinguished by hidden coherency position, and that hidden position changes the later response under the known localized step. The matched direction follows the coherent aggregate after preparation is removed, while no preparation and equal-cost sign-mismatched preparation do not.

### 7.6 Response choice and closure

The exact equivalence between fibre response homogeneity and controlled closure in Section 3 depends on the frozen response being the entire retained trajectory `q(·)`. A coarser response—such as a terminal scalar, threshold event, or integral observable—could be homogeneous over a fibre even if the full `q` dynamics is not closed. The manuscript therefore does not identify response sufficiency with dynamic closure outside the specified response functional.

### 7.7 Cross-domain scope

The neural and grid examples instantiate a common diagnostic pattern: a description sufficient for current/passive behavior can fail to determine a specified intervention response. They do not establish a universal law. The domains differ in semantics, intervention mechanism, and evidential role; only the diagnostic organization is shared.

### 7.8 Terminology and scope

The programme label `causal_synergetics` is useful internally for the synthesis, but the manuscript does not present it as an established field. Likewise, the paper does not introduce a generic causal-state construct, a generic controlled preparation primitive, or an alternative to existing abstraction/control theories. Its claims remain tied to the frozen response, intervention families, models, and comparators reported here.

## 8. Conclusion

A synergetic order parameter can be excellent for passive dynamics and still require an additional check before it is used as a sufficient description under intervention. For the full retained-trajectory response considered here, that check is simply the established controlled-projectability/closure condition. The useful diagnostic question is therefore concrete: **does the pre-declared synergetic fibre remain homogeneous for the intervention family and response horizon we actually intend to use?**

The frozen evidence illustrates both answers and their limits. The CORE witness shows analytically how an intervention can expose a slaved coordinate and how standard fast-slow quantities bound the resulting finite-horizon error. The neural examples make same-current-function/different-learning-response behavior explicit but, consistently with direct prior art, remain illustrations; learned response-coordinate work is constrained by a WEAK raw-PCA comparison, a specification-classification FAIL, an exact Gram control, and a PARK decision. The two-machine grid example gives a physically distinct witness in which a representative coherent macro is passively exact yet intervention-insufficient under a localized disturbance, while the arithmetic mean/COI coordinate remains exactly closed. Finally, bounded output-preserving preparation in that same physical fibre shows that the hidden coherency state can be repositioned, with the matched state changing the later response after preparation has ended.

Taken together, these results support a restricted synergetics-centered diagnostic synthesis: start from the macro one already intends to use, declare the intervention and response, test controlled sufficiency, retain successful countercontrols and negative evidence, and interpret any hidden-mode preparation inside established control theory. The evidence does not support a generic state-equivalence theory, a universal cross-domain claim, or a generic control method.

---

# Appendices / Supplement Outline

## Appendix A. CORE derivations, proofs, and finite-horizon bound details

A full supplement should preserve the exact assumptions and proof steps from the frozen CORE result.

### A.1 State, intervention, and response specification

- `x=(q,r)`, `π(q,r)=q`.
- Piecewise-continuous interventions over a compact instantaneous control set, including constants.
- Full retained trajectory `Γ=q(·)` over the fixed horizon and sup-norm response metric.
- Slaving graph `r=h(q)`, unforced invariance, and the distinction between controlled graph invariance and global fibre projectability.

### A.2 Standard projectability equivalence

Reproduce the self-contained proof of Proposition 1, clearly labelled as structurally subsumed by controlled quotient/projectability theory. Preserve the constant-control differentiation argument for the direction from response homogeneity to fibrewise vector-field equality.

### A.3 Scalar witness

Preserve the exact solution of

`q_dot=ur`, `r_dot=-λr+u`,

including the constant-intervention trajectory, the same-fibre difference, the graph-start reduced-model error, and the separation between fibre memory and control leakage.

### A.4 Exact and general bounds

Preserve:

`d_Γ ≤ U|Δr0|(1-e^{-λT})/λ`,

`d_Γ(q,q_red) ≤ U²[T/λ-(1-e^{-λT})/λ²]`,

and the general comparison bound in terms of `(λ,δ,β,L_e,L_q,U,T)`, including definitions of `Φ`, `Ψ`, and the tube-diameter consequence `2B_T(ρ)`. State explicitly that the proof uses standard comparison and Grönwall machinery.

## Appendix B. Neural exact constructions and regression details

### B.1 Factorised linear benchmark

Preserve the exact A/B matrices, `v=e1`, tasks C/D, `η=0.1`, the derivation of

`w^+=w-η(U^TU+||v||²I)g+η²g(v^TUg)`,

and all four post-step weights/losses. Record analytical/autograd maximum discrepancy `0.0` and the frozen test result `4 passed` for the original benchmark.

### B.2 Historical reachability

Preserve the common `U0=0`, auxiliary `a=e2`, `η_hist=1`, exact update `U^+=ac^T`, main-function preservation `w=0`, and reproduction of the C/D benchmark. Emphasize that this is an artificial auxiliary-gradient provenance construction.

### B.3 ReLU construction

Preserve A/B parameterizations, global equivalence by positive homogeneity, activation margins, frozen probe order, four post-step response vectors, losses `0.14045/0.2312`, and analytical/autograd discrepancy `0.0`.

## Appendix C. Response-coordinate WEAK/FAIL audits and classifier limitation

### C.1 WEAK pilot

Preserve the 81-state `9×9` family, 41/40 split, four calibration interventions, eight held-out interventions, two-dimensional response PCA, bilinear decoder, B0/B1/B2 controls, and the exact aggregate metrics:

- response `R2=1.0`, `NRMSE=7.30513741157965e-16`;
- B2 `R2=0.999883026432542`, `NRMSE=0.00170190726453134`;
- response-minus-B2 margin `0.000116973567458323`;
- classification WEAK.

### C.2 Nuisance-invariance pilot

Preserve the 648-state gauge family and the exact candidate/B2/B3/null metrics, especially:

- candidate joint `R2=1.0`, `J_nuis=5.596227006606825e-32`;
- naive B2 joint `R2=2.220446049250313e-16`, `J_nuis=1.0`;
- Gram-PCA B3 joint `R2=1.0`, `J_nuis=2.692209973425601e-32`;
- N0 joint `R2=0.6999999999999995`;
- classification `FAIL — SPECIFICATION CLASSIFICATION GAP`.

Document why the frozen PASS/WEAK/NULL rules do not assign a scientific class to the metric vector and why no post-hoc repair was permitted. Preserve the integration decision STOP / PARK RESPONSE-COORDINATE DIRECTION.

## Appendix D. Power-grid numerical specification and convergence audit

Preserve the exact two-machine equations, normalized constants `M=D=K=1`, macro/hidden transform, three coherent initial states, interventions `0,±0.2`, horizon `T=5`, float64 RK4 primary/audit steps, and all nine trajectory metrics from the canonical APP-B result.

The supplement should include the exact B0/B1/C1 definitions, primary/half-step discrepancy `8.1601392309949e-15`, odd-symmetry audit, and mean/COI closure error `3.885780586188048e-14`.

## Appendix E. Preparation inverse-dynamics derivation, budgets, and convergence audit

Preserve the quintic smoothstep path, analytical derivatives, inverse-dynamics controls `p1,p2`, sign symmetry, preparation duration `2.0`, amplitude cap `0.35`, energy budget `0.25`, P0/PT/PM definitions, evaluation horizon `5.0`, and the exact sign/condition tables from the frozen APP-C result.

In particular preserve:

- `P_q=3.580739551835791e-15`;
- terminal target error `4.6079385647875116e-15`;
- peak input `0.20881049376163438`;
- energy `0.04006381839386479`;
- PT `E_B1=2.076727044536923e-15`;
- P0 `E_B1=0.06534774384334105`;
- PM `E_B1=0.1307357122731585`;
- primary/audit discrepancy `5.738465258531278e-15`.

Record explicitly that preparation controls are absent during evaluation.

## Appendix F. Prospective-freeze / governance table

If venue policy permits a reproducibility/governance supplement, include a compact table listing for each scientific gate: pre-result specification freeze, model/intervention/horizon freeze, comparator freeze, outcome (`PASS`, `WEAK`, `FAIL`, or PARK), and no-retuning statement. The table should record negative results rather than only successful gates. It should not be used as a substitute for scientific validation.

---

# References

Barnett, N., & Crutchfield, J. P. (2015). Computational Mechanics of Input–Output Processes: Structured Transformations and the ε-Transducer. *Journal of Statistical Physics*, 161. https://doi.org/10.1007/s10955-015-1327-5

Beckers, S., & Halpern, J. Y. (2019). Abstracting Causal Models. *AAAI 2019*. https://doi.org/10.1609/aaai.v33i01.33012678

Berg, G. J., & Ghafurian, A. (1983). Representation of coherency-based equivalents in transient stability studies. *Electric Power Systems Research*, 6(4), 235–241. https://doi.org/10.1016/0378-7796(83)90035-4

Chalupka, K., Perona, P., & Eberhardt, F. (2015). Visual Causal Feature Learning. *UAI 2015*. https://arxiv.org/abs/1412.2309

Chalupka, K., Perona, P., & Eberhardt, F. (2016). Multi-Level Cause-Effect Systems. *AISTATS 2016*. https://proceedings.mlr.press/v51/chalupka16.html

Chen, T., Goodfellow, I., & Shlens, J. (2016). Net2Net: Accelerating Learning via Knowledge Transfer. *ICLR 2016*. https://research.google/pubs/net2net-accelerating-learning-via-knowledge-transfer/

Christofides, P. D., & Teel, A. R. (1996). Singular perturbations and input-to-state stability. *IEEE Transactions on Automatic Control*, 41(11), 1645–1650. https://doi.org/10.1109/9.544001

Crutchfield, J. P., & Young, K. (1989). Inferring Statistical Complexity. *Physical Review Letters*, 63, 105. https://doi.org/10.1103/PhysRevLett.63.105

Dinh, L., Pascanu, R., Bengio, S., & Bengio, Y. (2017). Sharp Minima Can Generalize For Deep Nets. *ICML 2017, PMLR 70*, 1019–1028. https://proceedings.mlr.press/v70/dinh17b.html

Ferns, N., Panangaden, P., & Precup, D. (2004). Metrics for Finite Markov Decision Processes. *UAI 2004*, 162–169. https://mlanthology.org/uai/2004/ferns2004uai-metrics/

Geiger, A., et al. (2025). Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability. *Journal of Machine Learning Research*, 26(83). https://jmlr.org/papers/v26/23-0058.html

Girard, A., & Pappas, G. J. (2007). Approximate bisimulation relations for constrained linear systems. *Automatica*, 43, 1307–1317. https://doi.org/10.1016/j.automatica.2007.01.019

Givan, R., Dean, T., & Greig, M. (2003). Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence*, 147, 163–223. https://doi.org/10.1016/S0004-3702(02)00376-4

Goodwin, G. C., Seron, M. M., & De Doná, J. A. (2011). Feedforward model predictive control. *Annual Reviews in Control*, 35(2), 199–206. https://doi.org/10.1016/j.arcontrol.2011.10.007

Haken, H. (1996). Slaving principle revisited. *Physica D*, 97, 95–103. https://doi.org/10.1016/0167-2789(96)00080-2

Hu, E. J., et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models. *ICLR 2022*. https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/

Isidori, A. (2013). The zero dynamics of a nonlinear system: From the origin to the latest progresses of a long successful story. *European Journal of Control*, 19(5), 369–378. https://doi.org/10.1016/j.ejcon.2013.05.014

Jacot, A., Gabriel, F., & Hongler, C. (2018). Neural Tangent Kernel: Convergence and Generalization in Neural Networks. *NeurIPS 2018*. https://arxiv.org/abs/1806.07572

Kai, S., et al. (2022). A review of power system dynamic equivalents for transient stability studies. *The Journal of Engineering*, 2022, 761–772. https://doi.org/10.1049/tje2.12157

Kokotović, P. V., O’Malley, R. E., Jr., & Sannuti, P. (1976). Singular perturbations and order reduction in control theory — An overview. *Automatica*, 12, 123–132. https://doi.org/10.1016/0005-1098(76)90076-5

Lebeurrier, A., Vayer, T., & Gribonval, R. (2026). Path-conditioned training: a principled way to rescale ReLU neural networks. *ICML 2026 / PMLR 306*. arXiv:2602.19799. https://arxiv.org/abs/2602.19799

Li, W., & Bose, A. (1995). Preventive Control for Dynamic Security of Power Systems. *IFAC Proceedings Volumes*, 28(26), 379–383. https://doi.org/10.1016/S1474-6670(17)44787-2

Li, X., Kaba, S.-O., & Ravanbakhsh, S. (2025). On the Identifiability of Causal Abstractions. *AISTATS 2025*. https://proceedings.mlr.press/v258/li25g.html

Littman, M. L., Sutton, R. S., & Singh, S. (2001). Predictive Representations of State. *NeurIPS 2001*. https://proceedings.neurips.cc/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html

Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. *NeurIPS 2022*. https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html

Neyshabur, B., Salakhutdinov, R., & Srebro, N. (2015). Path-SGD: Path-Normalized Optimization in Deep Neural Networks. *NeurIPS 2015*. https://papers.neurips.cc/paper_files/paper/2015/hash/eaa32c96f620053cf442ad32258076b9-Abstract.html

Ntogramatzidis, L., & Padula, F. (2017). A general approach to the eigenstructure assignment for reachability and stabilizability subspaces. *Systems & Control Letters*, 106, 58–67. https://doi.org/10.1016/j.sysconle.2017.06.003

Ravindran, B., & Barto, A. G. (2003). SMDP Homomorphisms: An Algebraic Approach to Abstraction in Semi-Markov Decision Processes. *IJCAI 2003*, 1011–1016. https://www.cse.iitm.ac.in/~ravi/papers/IJCAI03.pdf

Rubenstein, P. K., et al. (2017). Causal Consistency of Structural Equation Models. https://arxiv.org/abs/1707.00819

Sankaranarayanan, V., Venugopal, M., Elangovan, S., & Dharma Rao, N. (1983). Coherency identification and equivalents for transient stability studies. *Electric Power Systems Research*, 6(1), 51–60. https://doi.org/10.1016/0378-7796(83)90031-7

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational Mechanics: Pattern and Prediction, Structure and Simplicity. *Journal of Statistical Physics*, 104. https://arxiv.org/abs/cond-mat/9907176

Tabuada, P., & Pappas, G. J. (2005). Quotients of Fully Nonlinear Control Systems. *SIAM Journal on Control and Optimization*, 43(5), 1844–1866. https://doi.org/10.1137/S0363012901399027

Verma, K., & Niazi, K. R. (2013). A coherency based generator rescheduling for preventive control of transient stability in power systems. *International Journal of Electrical Power & Energy Systems*, 45(1), 10–18. https://doi.org/10.1016/j.ijepes.2012.08.072

Wei, T., Wang, C., Rui, Y., & Chen, C. W. (2016). Network Morphism. *ICML 2016*. https://proceedings.mlr.press/v48/wei16.html

Xia, K. M., & Bareinboim, E. (2025). Causal Abstraction Inference under Lossy Representations. *ICML 2025*. https://proceedings.mlr.press/v267/xia25a.html

---

# Editorial Change Log — Manuscript Editorial Completion 0.1

This editorial version preserves the frozen scientific content, numerical values, claim hierarchy, negative evidence, countercontrols, and figure/table restrictions of `manuscript_initial_draft_0_1.md`. The following claim-neutral editorial changes were made:

1. Completed the already cited Ntogramatzidis geometric-control reference as Lorenzo Ntogramatzidis and Fabrizio Padula, *Systems & Control Letters* 106 (2017), 58–67, DOI `10.1016/j.sysconle.2017.06.003`, and normalized the corresponding in-text citations.
2. Added the 2005 publication year to the already cited Tabuada & Pappas article and normalized its in-text author–year citations.
3. Completed the already cited 1995 IFAC preventive-control record as W. Li & A. Bose, with the existing title, volume/issue, pages, and DOI, and replaced title-led in-text citations with author–year form.
4. Removed the obsolete bibliography-formatting TODO associated with the now-completed Ntogramatzidis record.
5. Made no scientific, evidential, numerical, figure-inventory, claim-strength, novelty, priority, genericity, robustness, or optimality changes.