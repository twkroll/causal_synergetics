# Prior-Art & Definitions Audit 0.1

Status: EXECUTED
Assigned chat: `80 – LIT – Literatur & Neuheitspositionierung`
Authorised by: `00 – MASTER – Projektplan & Status`
Search date: 2026-09-03
Decision: **PASS — CLAIM-RESTRICTED**

> **Interpretation of PASS.** This is not a novelty proof. It means only that, after substantial demotion of the original verbal claims, a sufficiently precise candidate boundary remains for CORE to test mathematically against named prior-art frameworks.

## 1. Executive verdict

The proposed programme cannot defensibly claim novelty for the generic ideas that a state should be characterized by intervention/action-conditioned future responses, that states with identical controlled responses should be equivalent, that a low-dimensional representation should preserve those responses, or that such a representation should have a closed/approximately closed controlled evolution. Those ideas have strong, often structurally equivalent predecessors in predictive state representations (PSRs), computational mechanics of input-output processes, MDP/SMDP bisimulation and homomorphisms, state aggregation/lumpability, causal abstraction, causal feature learning, input-output realization, and control-oriented model reduction.

The strongest novelty boundary that survives this audit is therefore **not a new controlled-state equivalence or a new sufficient representation**. A potentially defensible CORE target is much narrower: an explicit mathematical comparison between **classical synergetic order-parameter/slaving reductions** and **intervention-relative behavioral sufficiency/closure**. In particular, CORE may ask whether, and under what assumptions, the fibres induced by a pre-existing synergetic order-parameter/slaving map are homogeneous with respect to a frozen intervention family, response functional, and horizon, and whether failure can be attributed or bounded when nominally slaved modes are transiently excited by interventions. This is a candidate bridge/problem statement, not an established novelty claim.

The phrase **causal order parameter** may remain useful as project terminology for a conjunction of requirements, but terminology or conjunction alone is not scientific novelty. Any future novelty claim must arise from a theorem, bound, impossibility result, algorithm, or falsifiable consequence that is demonstrably not already a restatement of PSR/bisimulation/lumpability/causal-abstraction/singular-perturbation results.

Construct 7 (local causal response atlas) and construct 8 (controlled state preparation) remain possible secondary directions, but both require severe restriction. Local charts/atlases are standard mathematical machinery and are active in current manifold learning; adding intervention sufficiency is not by itself a novelty result. Function-preserving neural-network transformations, later continued training, parameter-efficient adaptation, and model editing already instantiate substantial parts of controlled state preparation. Any surviving claim must specify a narrower measurable property.

**Programme-level classification:** `RESTRICT` and `REINTERPRET`.

**Gate decision for opening 10 – CORE:** `PASS — CLAIM-RESTRICTED`, conditional on CORE treating the minimal novelty statement in Section 8 as a hypothesis boundary to test, not as a pre-established novel theory.

---

## 2. Search scope and date

### Date

Search frozen for this audit on **2026-09-03**.

### Families audited

The audit covered the mandatory comparison families:

- classical synergetics, order parameters, slaving, centre-manifold/adiabatic-elimination context;
- computational mechanics and causal states, including controlled/input-output extensions;
- predictive state representations;
- MDP/SMDP bisimulation, homomorphism, state abstraction, approximate bisimulation, aggregation/lumpability;
- causal feature learning, causal abstraction, causal representation learning, and causal emergence where directly relevant;
- control theory, singular perturbation, input-output realization, system identification, model reduction, experiment/input design;
- Koopman methods with control and control-oriented reduced-order modelling;
- sparse dynamics discovery with inputs/control;
- neural-network function-preserving transformations, training-dynamics descriptors, LoRA/adaptation, and model editing;
- atlas/manifold representations where relevant to the local-atlas proposal.

### Search method

For each construct, searches targeted exact phrases and mathematical analogues rather than project terminology alone. Priority was given to primary papers, canonical sources, publisher records, and current conference/journal proceedings. The audit explicitly looked for exact equivalence classes, action/intervention-conditioned predictive states, quotient/aggregation conditions, recursive closure, approximate metrics/error bounds, lossy abstraction consistency, fast/slow controlled reductions, and function-preserving internal-state changes.

This was a broad prior-art audit, not a systematic review with a registered bibliographic protocol. Absence of a `SAME` hit is therefore never interpreted as novelty.

---

## 3. Definition-by-definition comparison

| # | Proposed construct | Strongest prior-art match | Prior-art class | Programme action | Audit conclusion |
|---|---|---|---|---|---|
| 1 | Intervention-relative response kernel | Predictive state representations; ε-transducers/input-output computational mechanics; controlled input-output maps | **SAME** at structural level | **DEMOTE / REINTERPRET** | Action/intervention-conditioned distributions or values of future responses are established state descriptors. A particular choice of response functional/horizon is an application specification, not generic novelty. |
| 2 | Intervention-relative causal equivalence | Causal feature learning causal partitions; MDP/SMDP bisimulation/homomorphism; ε-transducer causal states; behavioral/input-output equivalence | **SAME** | **DEMOTE** | Equating microstates when they induce the same relevant interventional/controlled behavior is established under several names. |
| 3 | Intervention-sufficient low-dimensional representation | PSRs; state abstraction/homomorphism; causal abstraction; balanced/control-oriented reduction; approximate bisimulation metrics | **SAME / CLOSE** | **DEMOTE / RESTRICT** | Sufficient compressed controlled states and reduced models with preservation/error guarantees are established goals. Novelty cannot be claimed generically. |
| 4 | Dynamic closure / controlled lumpability requirement | Markov lumpability/state aggregation; MDP bisimulation/homomorphism; recursive predictive states; reduced controlled dynamics | **SAME** | **DEMOTE** | Closure under the reduced dynamics is a core requirement of established aggregation and realization frameworks. |
| 5 | Causal order parameter | Synergetic order parameters/slaving plus controlled state abstraction/model reduction criteria | **CLOSE** | **RESTRICT / OPEN** | The conjunction/name was not found as a canonical single object, but each ingredient has strong prior art. A named conjunction is not enough; a distinct result is required. |
| 6 | Interventional slaving / fibre consistency | Controlled lumpability/bisimulation; causal abstraction consistency; projected/lossy causal abstraction; singular perturbation/control of fast modes | **CLOSE**, with parts effectively **SAME** | **REINTERPRET / RESTRICT** | Fibre homogeneity under interventions is an established abstraction concern; fast modes becoming relevant under forcing/control is also established. The potentially defensible residue is the explicit theorem-level relation to *classical synergetic slaving fibres*. |
| 7 | Local causal response atlas | Differential-geometric atlases; local manifold learning; switched/local reduced models; controlled Koopman/ROM | **RELATED / CLOSE** | **RESTRICT / OPEN** | Local charts and transition maps are standard. No reviewed source established the exact proposed package of local intervention-sufficient charts plus cross-intervention generalisation, but this remains unresolved, not novel. |
| 8 | Controlled state preparation | Net2Net/network morphism; parameter symmetries/function-preserving transformations; NTK/training-dynamics descriptors; LoRA; model editing | **CLOSE** | **RESTRICT / OPEN** | Preserving current function while changing internal parameterisation and then continuing training is established. A narrower claim about targeted future intervention/adaptation response at fixed observable/function would need formal separation from these literatures. |

### Notes on classification

`SAME` here means that the central mathematical idea of the proposal is already explicitly represented in a prior framework; it does not mean all notation, domains, horizons, or semantics are identical. Conversely, `CLOSE` does not imply novelty: it means the proposed object may combine established pieces in a way that still requires a precise non-verbal distinction.

---

## 4. Strongest SAME and CLOSE candidates

### 4.1 Predictive state representations — strongest SAME for constructs 1 and 3

Littman, Sutton and Singh represent state by **multi-step, action-conditional predictions of future observations**, explicitly including stochasticity and controls. They show that systems admit predictive state representations no larger than corresponding minimal POMDP state descriptions in their linear setting. This is a direct predecessor of an intervention-relative future-response descriptor and a strong predecessor of intervention-sufficient state compression.

Primary source:
- M. L. Littman, R. S. Sutton, S. Singh, “Predictive Representations of State,” NeurIPS 2001. https://proceedings.neurips.cc/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html

### 4.2 ε-transducers — strongest SAME for controlled predictive equivalence

Barnett and Crutchfield extend computational mechanics from passive stochastic processes to input-output processes and construct the ε-transducer as a minimal optimal model of a stochastic mapping with inputs. This places input-conditioned predictive equivalence and minimal predictive state squarely within prior art.

Primary source:
- N. Barnett, J. P. Crutchfield, “Computational Mechanics of Input–Output Processes: Structured Transformations and the ε-Transducer,” *Journal of Statistical Physics* 161 (2015). https://doi.org/10.1007/s10955-015-1327-5

Background causal-state sources:
- J. P. Crutchfield, K. Young, “Inferring Statistical Complexity,” *Physical Review Letters* 63, 105 (1989). https://doi.org/10.1103/PhysRevLett.63.105
- C. R. Shalizi, J. P. Crutchfield, “Computational Mechanics: Pattern and Prediction, Structure and Simplicity,” *Journal of Statistical Physics* 104 (2001); preprint: https://arxiv.org/abs/cond-mat/9907176

### 4.3 MDP bisimulation, homomorphism, and lumpability — strongest SAME for constructs 2–4

Givan, Dean and Greig formalize equivalence and model minimization for MDPs by aggregating equivalent states into a reduced MDP with the relevant properties of the original. Ravindran and Barto develop SMDP homomorphisms as a rigorous abstraction/minimization framework. Ferns, Panangaden and Precup make equivalence quantitative through bisimulation metrics and relate those metrics to value differences. Approximate bisimulation for controlled systems further supplies explicit precision notions.

Primary sources:
- R. Givan, T. Dean, M. Greig, “Equivalence notions and model minimization in Markov decision processes,” *Artificial Intelligence* 147 (2003), 163–223. https://doi.org/10.1016/S0004-3702(02)00376-4
- B. Ravindran, A. G. Barto, “SMDP Homomorphisms: An Algebraic Approach to Abstraction in Semi-Markov Decision Processes,” IJCAI 2003, 1011–1016. https://www.cse.iitm.ac.in/~ravi/papers/IJCAI03.pdf
- N. Ferns, P. Panangaden, D. Precup, “Metrics for Finite Markov Decision Processes,” UAI 2004, 162–169. https://mlanthology.org/uai/2004/ferns2004uai-metrics/
- A. Girard, G. J. Pappas, “Approximate bisimulation relations for constrained linear systems,” *Automatica* 43 (2007), 1307–1317. https://doi.org/10.1016/j.automatica.2007.01.019

Implication: a claim such as “two states are equivalent if no allowed intervention can distinguish their relevant future response, and the quotient should evolve consistently” is not a new generic definition.

### 4.4 Causal feature learning and causal abstraction — strongest SAME/CLOSE for constructs 2, 3, and 6

Chalupka, Perona and Eberhardt construct causal macrovariables by grouping micro-level values according to interventional behavior. Their programme explicitly constructs causal variables from microvariables rather than assuming them. Rubenstein et al. formalize consistency between causal models at different levels by requiring agreement about intervention effects. Beckers and Halpern develop increasingly strong forms of causal abstraction, with explicit attention to which interventions are allowed or induced by the abstraction map.

Recent work makes the overlap with fibre consistency even sharper. Xia and Bareinboim (ICML 2025) identify an **abstract invariance condition** that fails when multiple low-level interventions map to one high-level intervention but have different effects; their projected abstractions are designed to handle lossy representations in precisely this setting. Li, Kaba and Ravanbakhsh (AISTATS 2025) analyze identifiability up to an abstraction determined by the intervention set. Geiger et al. (JMLR 2025) give a broad causal-abstraction foundation for mechanistic interpretability and graded faithfulness.

Primary sources:
- K. Chalupka, P. Perona, F. Eberhardt, “Visual Causal Feature Learning,” UAI 2015; preprint https://arxiv.org/abs/1412.2309
- K. Chalupka, P. Perona, F. Eberhardt, “Multi-Level Cause-Effect Systems,” AISTATS 2016. https://proceedings.mlr.press/v51/chalupka16.html
- P. K. Rubenstein et al., “Causal Consistency of Structural Equation Models,” 2017. https://arxiv.org/abs/1707.00819
- S. Beckers, J. Y. Halpern, “Abstracting Causal Models,” AAAI 2019. https://doi.org/10.1609/aaai.v33i01.33012678
- K. M. Xia, E. Bareinboim, “Causal Abstraction Inference under Lossy Representations,” ICML 2025. https://proceedings.mlr.press/v267/xia25a.html
- X. Li, S.-O. Kaba, S. Ravanbakhsh, “On the Identifiability of Causal Abstractions,” AISTATS 2025. https://proceedings.mlr.press/v258/li25g.html
- A. Geiger et al., “Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability,” *JMLR* 26(83), 2025. https://jmlr.org/papers/v26/23-0058.html

Implication: “interventional fibre consistency” cannot be presented as a generic new requirement. The remaining possible distinction must be tied specifically to synergetic slaving/order-parameter fibres or another precisely delimited structure.

### 4.5 Synergetics and singular perturbation/control — strongest CLOSE for constructs 5 and 6

Haken’s slaving principle parametrizes the state near instabilities by a small set of order parameters and derives order-parameter dynamics. Separately, singular perturbation and control theory have treated order reduction, time-scale separation, fast modes, controlled forcing, and the hazards of reducing fast subsystems for decades. Thus neither “few slow/order variables slave fast variables” nor “fast variables may matter under forcing/control” is a new observation.

Primary/canonical sources:
- H. Haken, “Slaving principle revisited,” *Physica D* 97 (1996), 95–103. https://doi.org/10.1016/0167-2789(96)00080-2
- P. V. Kokotović, R. E. O’Malley Jr., P. Sannuti, “Singular perturbations and order reduction in control theory — An overview,” *Automatica* 12 (1976), 123–132. https://doi.org/10.1016/0005-1098(76)90076-5

The defensible question is therefore not whether interventions can reveal hidden fast modes in general, but whether **classical synergetic slaving hypotheses imply, fail to imply, or quantitatively approximate a declared intervention-response equivalence/closure criterion**.

### 4.6 Control-oriented reduction and Koopman with inputs — strongest CLOSE for construct 3

Balanced truncation and related control-oriented reductions explicitly target low-order models based on controllability/observability and supply approximation guarantees in established settings. Koopman-with-control methods likewise construct reduced predictive descriptions for actuated nonlinear systems.

Sources:
- S. Gugercin, A. C. Antoulas, “A Survey of Model Reduction by Balanced Truncation and Some New Results,” *International Journal of Control* 77 (2004), 748–766. https://doi.org/10.1080/00207170410001713448
- J. L. Proctor, S. L. Brunton, J. N. Kutz, “Generalizing Koopman Theory to Allow for Inputs and Control,” *SIAM Journal on Applied Dynamical Systems* 17 (2018), 909–930. https://doi.org/10.1137/16M1062296

### 4.7 Controlled sparse dynamics discovery — prior art for intervention-aware discovery claims

Sparse identification with control already generalizes sparse governing-equation discovery to external inputs, forcing, and feedback control. Designed input/experiment selection is also a mature system-identification topic. Therefore intervention-aware/active discovery is not a viable standalone novelty claim.

Source:
- S. L. Brunton, J. L. Proctor, J. N. Kutz, “Sparse Identification of Nonlinear Dynamics with Control (SINDYc),” *IFAC-PapersOnLine* 49(18), 2016, 710–715. https://doi.org/10.1016/j.ifacol.2016.10.249

### 4.8 Neural controlled state preparation — strongest CLOSE for construct 8

Net2Net and network morphism explicitly provide **function-preserving transformations** of neural networks followed by continued training. NTK theory formalizes that training evolution depends on parameter-derivative structure, not only the instantaneous input-output function. LoRA alters adaptation through restricted low-rank parameter updates, while ROME directly edits internal weights to change targeted behavior while testing specificity/generalization.

Sources:
- T. Chen, I. Goodfellow, J. Shlens, “Net2Net: Accelerating Learning via Knowledge Transfer,” ICLR 2016. https://research.google/pubs/net2net-accelerating-learning-via-knowledge-transfer/
- T. Wei, C. Wang, Y. Rui, C. W. Chen, “Network Morphism,” ICML 2016. https://proceedings.mlr.press/v48/wei16.html
- A. Jacot, F. Gabriel, C. Hongler, “Neural Tangent Kernel: Convergence and Generalization in Neural Networks,” NeurIPS 2018. https://arxiv.org/abs/1806.07572
- E. J. Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models,” ICLR 2022. https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/
- K. Meng, D. Bau, A. Andonian, Y. Belinkov, “Locating and Editing Factual Associations in GPT,” NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html

Implication: “change internal state while keeping current function approximately fixed so that future learning differs” is already substantially instantiated. A viable future claim must be narrower, e.g. a formally specified targeted future-response property under a fixed architecture/observable and frozen intervention/adaptation protocol.

---

## 5. Exact differences that remain potentially defensible

These are **candidate distinctions to be tested**, not established novelties.

### 5.1 Explicit bridge from synergetic slaving fibres to controlled behavioral equivalence

The reviewed synergetics sources define order-parameter parametrization/slaving near instabilities. The reviewed PSR/bisimulation/causal-abstraction sources define controlled/predictive equivalence and abstraction consistency. The audit did **not** identify a canonical source that proves a general implication of the form:

> a classical Haken-type slaving/order-parameter map automatically yields fibres that are homogeneous for a declared intervention family and response horizon.

Nor was a canonical source found proving the converse. This precise relationship is therefore an admissible question for CORE.

### 5.2 Failure mode induced by intervention-excited slaved degrees of freedom, tied specifically to a synergetic map

Control and singular perturbation already know that fast modes and reduction error can matter under forcing. The potentially distinct element is not that phenomenon, but a theorem-level or diagnostic relationship between that phenomenon and **failure of a specific pre-existing synergetic order-parameter quotient to satisfy controlled response equivalence/closure**.

### 5.3 One frozen criterion combining response sufficiency, closure, and dimensional reduction for a synergetic candidate

The ingredients individually have prior art. A future result might still be distinct if it establishes a nontrivial compatibility/incompatibility theorem for a *given synergetic reduction* under all three simultaneously, with quantitative error and a frozen intervention family. The audit found no basis for claiming that the conjunction itself is new.

### 5.4 Local atlas only if global controlled quotient failure is formal and transition compatibility is nontrivial

A differentiable atlas is standard, and current work explicitly learns atlases for manifold representations (e.g. AISTATS 2026). A local causal response atlas is therefore potentially defensible only if CORE can formalize a property beyond ordinary local coordinates: local intervention-response sufficiency plus transition compatibility, accompanied by a reason a global sufficient quotient/coordinate cannot satisfy the criterion.

Current atlas reference:
- R. A. Robinett et al., “Atlas-based Manifold Representations for Interpretable Riemannian Machine Learning,” AISTATS 2026. https://proceedings.mlr.press/v300/robinett26a.html

### 5.5 Neural state preparation only under a narrower future-response target

A possible application-level distinction would require all of the following to be explicit: what observable/function is held fixed; what internal state class is changed; what future intervention/adaptation protocol is frozen; what response is targeted; and how the claim differs from function-preserving morphisms, parameter symmetries, model editing, and ordinary fine-tuning/adapters. This is not yet a CORE novelty claim.

---

## 6. Claims that must be demoted or abandoned

The following claims should not appear as novelty claims in CORE or a first theory paper unless later evidence radically changes the audit:

1. **“We introduce intervention-conditioned future response as a new definition of state.”** Abandon. PSRs and ε-transducers are direct predecessors.
2. **“We introduce causal equivalence by equality of responses under interventions.”** Abandon. Causal feature learning, causal abstraction, bisimulation, and behavioral equivalence cover this idea.
3. **“We introduce intervention-sufficient state compression.”** Abandon as a generic claim. State abstraction, PSRs, homomorphisms, causal abstraction, and control-oriented ROM already pursue it.
4. **“We add the novel requirement of dynamic closure.”** Abandon. Lumpability, homomorphism, bisimulation, recursive predictive states, and realization theory make closure central.
5. **“A causal order parameter is novel because it combines sufficiency, closure, robustness, and low dimension.”** Demote. A bundle of established properties is terminology until a distinct result exists.
6. **“Classical slaving overlooks that fast variables can matter under interventions/forcing.”** Demote strongly. Singular perturbation and control theory have long studied controlled fast modes and reduction error.
7. **“Interventional fibre consistency is a new abstraction principle.”** Abandon generically. Causal abstraction and especially lossy/projected abstraction already confront non-homogeneous low-level interventions mapped to one macro intervention.
8. **“Local atlases are a new way to represent reduced dynamics.”** Abandon. Atlases/local charts are standard and active in modern manifold learning.
9. **“Intervention-aware sparse dynamics discovery is new.”** Abandon. SINDYc and system-identification/input-design literatures are direct predecessors.
10. **“Changing neural internal state while preserving current function is new.”** Abandon generically. Function-preserving network transformations and related parameterization methods predate the programme.

---

## 7. Claims that remain OPEN rather than established

1. Whether a standard Haken-type slaving map satisfies intervention-response homogeneity for a declared intervention family and finite horizon under identifiable assumptions.
2. Whether failure of that property admits a useful quantitative bound tied to excitation of nominally slaved modes that is not already an instance of a known singular-perturbation/bisimulation bound.
3. Whether simultaneous intervention sufficiency + controlled closure + substantial dimensional reduction imposes a distinct obstruction or structural condition for synergetic order parameters.
4. Whether a local atlas of controlled-response-sufficient charts yields a theorem or algorithm not subsumed by switched/local ROM, manifold learning, or local causal abstraction.
5. Whether a fixed-architecture neural state can be deliberately moved within an approximately function-equivalent fibre to control a precisely frozen future adaptation/intervention response in a way not reducible to known reparameterization, NTK, editing, or adapter results.
6. How broadly any synergetics-specific theorem would extend beyond near-instability regimes without becoming a generic state-abstraction theorem.

All six are `OPEN / NOT RESOLVED`; none is a novelty statement.

---

## 8. Proposed minimal novelty statement for CORE

### Admissible candidate boundary

> **Minimal candidate statement:** Existing predictive-state, bisimulation/lumpability, causal-abstraction, and control-reduction frameworks already define intervention/action-relative state equivalence, sufficient reduced states, and closed/approximately closed quotient dynamics. The remaining candidate contribution for `causal_synergetics` is therefore restricted to the relationship between these controlled behavioral criteria and a *pre-existing classical synergetic order-parameter/slaving reduction*. CORE should determine whether the fibres of such a reduction are necessarily, conditionally, approximately, or generally not homogeneous in their declared intervention responses, while simultaneously supporting reduced controlled dynamics; any surviving claim must be stated as an explicit theorem, bound, counterexample/impossibility result, or falsifiable criterion relative to named prior art.

### What CORE must not claim at entry

CORE must not enter with “causal order parameters are new” as a premise. It must enter with a comparison problem:

- frozen microscopic dynamics;
- frozen candidate synergetic map/order parameter;
- frozen intervention family;
- frozen response functional and horizon;
- explicit exact or approximate response-equivalence criterion;
- explicit closure criterion;
- explicit relation to PSR/bisimulation/lumpability/causal abstraction/singular perturbation.

If the resulting mathematics collapses to a known quotient, realization, bisimulation, or singular-perturbation theorem under relabeling, the novelty claim fails and should be recorded as such.

---

## 9. Mandatory references for a first theory paper

The following references are mandatory starting points; omission would create a serious novelty-positioning risk.

### Synergetics / fast-slow reduction

1. H. Haken, “Slaving principle revisited,” *Physica D* 97 (1996), 95–103. https://doi.org/10.1016/0167-2789(96)00080-2
2. P. V. Kokotović, R. E. O’Malley Jr., P. Sannuti, “Singular perturbations and order reduction in control theory — An overview,” *Automatica* 12 (1976), 123–132. https://doi.org/10.1016/0005-1098(76)90076-5

### Computational mechanics / predictive states

3. J. P. Crutchfield, K. Young, “Inferring Statistical Complexity,” *Physical Review Letters* 63 (1989), 105. https://doi.org/10.1103/PhysRevLett.63.105
4. C. R. Shalizi, J. P. Crutchfield, “Computational Mechanics: Pattern and Prediction, Structure and Simplicity,” *Journal of Statistical Physics* 104 (2001). https://arxiv.org/abs/cond-mat/9907176
5. M. L. Littman, R. S. Sutton, S. Singh, “Predictive Representations of State,” NeurIPS 2001. https://proceedings.neurips.cc/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
6. N. Barnett, J. P. Crutchfield, “Computational Mechanics of Input–Output Processes: Structured Transformations and the ε-Transducer,” *Journal of Statistical Physics* 161 (2015). https://doi.org/10.1007/s10955-015-1327-5

### Bisimulation / aggregation / abstraction

7. R. Givan, T. Dean, M. Greig, “Equivalence notions and model minimization in Markov decision processes,” *Artificial Intelligence* 147 (2003). https://doi.org/10.1016/S0004-3702(02)00376-4
8. B. Ravindran, A. G. Barto, “SMDP Homomorphisms: An Algebraic Approach to Abstraction in Semi-Markov Decision Processes,” IJCAI 2003. https://www.cse.iitm.ac.in/~ravi/papers/IJCAI03.pdf
9. N. Ferns, P. Panangaden, D. Precup, “Metrics for Finite Markov Decision Processes,” UAI 2004. https://mlanthology.org/uai/2004/ferns2004uai-metrics/
10. A. Girard, G. J. Pappas, “Approximate bisimulation relations for constrained linear systems,” *Automatica* 43 (2007). https://doi.org/10.1016/j.automatica.2007.01.019

### Causal feature learning / causal abstraction

11. K. Chalupka, P. Perona, F. Eberhardt, “Visual Causal Feature Learning,” UAI 2015. https://arxiv.org/abs/1412.2309
12. K. Chalupka, P. Perona, F. Eberhardt, “Multi-Level Cause-Effect Systems,” AISTATS 2016. https://proceedings.mlr.press/v51/chalupka16.html
13. P. K. Rubenstein et al., “Causal Consistency of Structural Equation Models,” 2017. https://arxiv.org/abs/1707.00819
14. S. Beckers, J. Y. Halpern, “Abstracting Causal Models,” AAAI 2019. https://doi.org/10.1609/aaai.v33i01.33012678
15. B. Schölkopf et al., “Toward Causal Representation Learning,” *Proceedings of the IEEE* 109 (2021). https://doi.org/10.1109/JPROC.2021.3058954
16. X. Li, S.-O. Kaba, S. Ravanbakhsh, “On the Identifiability of Causal Abstractions,” AISTATS 2025. https://proceedings.mlr.press/v258/li25g.html
17. A. Geiger et al., “Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability,” *JMLR* 26(83), 2025. https://jmlr.org/papers/v26/23-0058.html
18. K. M. Xia, E. Bareinboim, “Causal Abstraction Inference under Lossy Representations,” ICML 2025. https://proceedings.mlr.press/v267/xia25a.html

### Control-oriented/model reduction and discovery

19. S. Gugercin, A. C. Antoulas, “A Survey of Model Reduction by Balanced Truncation and Some New Results,” *International Journal of Control* 77 (2004). https://doi.org/10.1080/00207170410001713448
20. J. L. Proctor, S. L. Brunton, J. N. Kutz, “Generalizing Koopman Theory to Allow for Inputs and Control,” *SIAM Journal on Applied Dynamical Systems* 17 (2018). https://doi.org/10.1137/16M1062296
21. S. L. Brunton, J. L. Proctor, J. N. Kutz, “Sparse Identification of Nonlinear Dynamics with Control (SINDYc),” *IFAC-PapersOnLine* 49(18), 2016. https://doi.org/10.1016/j.ifacol.2016.10.249

### Neural-network application boundary

22. T. Chen, I. Goodfellow, J. Shlens, “Net2Net: Accelerating Learning via Knowledge Transfer,” ICLR 2016. https://research.google/pubs/net2net-accelerating-learning-via-knowledge-transfer/
23. T. Wei, C. Wang, Y. Rui, C. W. Chen, “Network Morphism,” ICML 2016. https://proceedings.mlr.press/v48/wei16.html
24. A. Jacot, F. Gabriel, C. Hongler, “Neural Tangent Kernel: Convergence and Generalization in Neural Networks,” NeurIPS 2018. https://arxiv.org/abs/1806.07572
25. E. J. Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models,” ICLR 2022. https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/
26. K. Meng, D. Bau, A. Andonian, Y. Belinkov, “Locating and Editing Factual Associations in GPT,” NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html

### Local atlas boundary

27. R. A. Robinett et al., “Atlas-based Manifold Representations for Interpretable Riemannian Machine Learning,” AISTATS 2026. https://proceedings.mlr.press/v300/robinett26a.html

These references are a mandatory minimum for positioning, not a complete bibliography.

---

## 10. Ten strongest anticipated reviewer objections

1. **“Constructs 1–4 are renamings.”** A reviewer can map response kernels to PSRs/ε-transducers, equivalence to bisimulation/causal partitions, and closure to lumpability/homomorphism. The paper must state this mapping before making any claim.
2. **“Causal equivalence under interventions already exists.”** Chalupka-style causal coarsenings and later causal-abstraction frameworks directly undermine any first-definition claim.
3. **“Your fibre-consistency condition is already causal abstraction consistency.”** Recent projected/lossy abstraction work explicitly addresses multiple low-level interventions with different effects mapping to a common high-level intervention.
4. **“Causal order parameter is branding, not a result.”** Combining sufficiency, closure, robustness, and dimension reduction does not establish a new object unless a nontrivial property follows.
5. **“Fast/slaved modes under control are old singular-perturbation territory.”** Any claim based only on transiently exciting fast modes will appear decades late unless the synergetic-specific relation is mathematically new.
6. **“Control-oriented model reduction already preserves what inputs can excite and outputs can reveal.”** Balanced truncation and related methods force a direct comparison of objectives, assumptions, and guarantees.
7. **“The equivalence is arbitrary because it depends on chosen interventions, horizon, and response.”** The intervention family, horizon, functional, and error metric must be frozen and scientifically motivated; otherwise equivalence classes can be engineered post hoc.
8. **“The local atlas adds standard differential geometry to an existing abstraction problem.”** Local charts/transition maps alone are not a contribution; an intervention-specific compatibility theorem or necessity result is required.
9. **“The neural state-preparation idea overlaps function-preserving morphisms, training dynamics, adapters, and editing.”** A neural application needs a sharply measurable target not already captured by these techniques.
10. **“The programme is too broad to support one novelty claim.”** A theorem about a restricted near-instability synergetic regime cannot automatically justify claims about generic dynamical systems or neural networks. MASTER must keep branch-dependent applications separate from CORE claims.

---

## 11. Explicit uncertainties and literature gaps

1. **No exhaustive theorem-to-theorem equivalence audit was performed.** Some constructs may be exactly subsumed by additional work in stochastic realization, controlled Markov-process lumping, formal methods, or nonlinear behavioral systems not captured in the minimum reference list.
2. **Input-output realization literature needs a dedicated follow-up if CORE selects that mathematical language.** Nerode/behavioral equivalence and nonlinear realization are likely additional close prior art.
3. **Controlled lumpability terminology is fragmented.** MDP aggregation, probabilistic bisimulation, Markov lumpability, homomorphisms, and formal abstraction use different assumptions; CORE must select the correct comparison class before theorem drafting.
4. **Causal abstraction is rapidly developing.** The 2025 literature already narrows the available fibre-consistency claim. A CORE manuscript will require a fresh literature update before submission.
5. **The exact relationship between Haken-style slaving manifolds and modern controlled bisimulation/abstraction was not found in a canonical single source.** This is the principal gap motivating the claim-restricted PASS, but it may exist under different terminology.
6. **Local atlas novelty is especially unresolved.** Current atlas/manifold and local reduced-order modelling literatures were sampled rather than exhaustively audited. Construct 7 must not be promoted without a dedicated search.
7. **Neural parameter equivalence is vast.** Permutation symmetries, mode connectivity, gauge-like reparameterizations, fine-tuning geometry, model editing, adapters, and continual learning all bear on construct 8; the present audit establishes only that the broad claim is not new.
8. **Causal emergence is conceptually related but not an exact substitute.** Macro-level intervention-based effectiveness measures should be cited when discussing causal macrostates, but they do not by themselves settle controlled dynamical closure.
9. **Approximation/error metrics matter.** “Approximately same response” can induce materially different theories depending on probability metric, norm, horizon scaling, and policy/intervention quantification. CORE must freeze these before inspecting desired consequences.
10. **Domain transfer is not automatic.** A result in deterministic smooth dynamical systems, controlled Markov systems, or neural optimization states cannot be generalized to the others without separate arguments.

---

## 12. Gate decision for opening `10 – CORE`

### Decision: **PASS — CLAIM-RESTRICTED**

This audit satisfies the prompt’s PASS condition only in the narrow sense that a non-verbal candidate boundary is now available for mathematical testing.

The PASS is contingent on the following restrictions:

- CORE begins from the explicit prior-art mappings above.
- Constructs 1–4 are treated as established structural ingredients, not new definitions.
- “Causal order parameter” is provisional terminology, not a novelty claim.
- The primary candidate question is the compatibility or incompatibility between **classical synergetic slaving/order-parameter fibres** and **frozen intervention-relative response equivalence plus controlled closure**.
- Fast-mode intervention sensitivity is not claimed as new; only a distinct synergetics-specific formal result could survive.
- Local-atlas and neural state-preparation ideas remain secondary `OPEN` directions and may not be used to rescue CORE novelty post hoc.
- Failure to obtain a distinct theorem/bound/counterexample/criterion relative to PSR, bisimulation/lumpability, causal abstraction, and singular perturbation must be preserved as a legitimate negative result.

### Final classification by construct

- 1 response kernel: `SAME` → `DEMOTE / REINTERPRET`
- 2 causal equivalence: `SAME` → `DEMOTE`
- 3 sufficient representation: `SAME / CLOSE` → `DEMOTE / RESTRICT`
- 4 dynamic closure: `SAME` → `DEMOTE`
- 5 causal order parameter: `CLOSE` → `RESTRICT / OPEN`
- 6 interventional slaving/fibre consistency: `CLOSE` with `SAME` components → `REINTERPRET / RESTRICT`
- 7 local causal response atlas: `RELATED / CLOSE` → `RESTRICT / OPEN`
- 8 controlled state preparation: `CLOSE` → `RESTRICT / OPEN`

**No construct is classified `CONFIRM` as novel by this audit.**

---

## Audit boundary

This document performs prior-art and definition positioning only. It does not introduce a new theory, theorem, model, intervention family, application selection, parameter search, or empirical result.
