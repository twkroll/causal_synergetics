# CORE Synergetic Sufficiency Boundary 0.1

Status: EXECUTED
Assigned chat: `10 – CORE – Haupttheorie / mathematischer Kern`
Authorised by: `00 – MASTER – Projektplan & Status`
Date: 2026-09-03
Dependency: `research/literature/prior_art_definitions_audit_0_1.md` (`PASS — CLAIM-RESTRICTED`)
Decision: **PASS — CLAIM-RESTRICTED / NO NOVELTY PROMOTION**

---

## 1. Executive verdict

The gate produces a precise boundary result, but not a new generic state-equivalence theory.

The main conclusions are:

1. **Classical slaving alone does not imply intervention-relative response sufficiency.** A pre-existing invariant or attracting graph `r=h(q)` constrains the dynamics on, or toward, that graph. It does not by itself constrain how the projected controlled vector field varies along the full fibres `q=const`.
2. For the frozen response functional in this gate — the complete retained-variable trajectory `q(·)` over a fixed horizon — **exact fibre response homogeneity is equivalent to exact controlled closure of `q`**, namely to projectability of the controlled vector field through the pre-declared order-parameter map. This is structurally the controlled-lumpability / abstraction criterion already identified by the literature audit and is therefore marked `SUBSUMED` rather than novel.
3. A two-dimensional scalar slow/fast system gives an explicit minimal counterexample in which the unforced synergetic reduction is exact and globally attracting, yet an admissible intervention directly excites the fast variable and makes two states on the same `q`-fibre produce different controlled `q` responses.
4. The same counterexample yields an exact finite-horizon fibre-response bound proportional to

   `U |Δr_0| (1-e^{-λT})/λ`,

   and an intervention-induced reduced-model error from the slaving manifold proportional to

   `U² [T/λ - (1-e^{-λT})/λ²]`.

5. More generally, a standard contraction/ISS-type assumption for the deviation `e=r-h(q)` gives an explicit bridge from **fast-mode relaxation rate**, **slaving defect**, and **intervention leakage into fast modes** to a finite-horizon intervention-response error. The proof uses standard comparison and Grönwall machinery; it is not presented as novel control theory. Its programme value is that it converts pre-existing synergetic quantities into a falsifiable intervention-sufficiency bound without learning a new representation.

Accordingly, this gate passes only in the restricted sense that a non-verbal mathematical boundary and a quantitative diagnostic survive. It does **not** establish novelty of controlled equivalence, causal order parameters, dynamic closure, or fast/slow reduction. Any publication-level novelty claim would require a later theorem-to-theorem prior-art comparison of the bridge statement itself.

---

## 2. Frozen definitions and assumptions

### 2.1 State and pre-declared order parameter

Let the microscopic state be

`x=(q,r) ∈ D ⊂ R^m × R^n`,

where:

- `q` is the **pre-declared candidate synergetic order parameter**;
- `r` collects nominally slaved / fast degrees of freedom;
- the order-parameter map is fixed as

`π(q,r)=q`.

No representation is learned or selected after inspecting controlled responses.

### 2.2 Controlled dynamics

Consider the controlled ODE

`q̇ = f(q,r,u)`,

`ṙ = g(q,r,u)`,

with `f,g` locally Lipschitz in `(q,r)` uniformly over admissible instantaneous controls `u∈A`, so that solutions are unique on the frozen horizon.

### 2.3 Frozen intervention family

Fix a compact instantaneous control set `A ⊂ R^p` and a horizon `T>0`.

The admissible intervention family is

`U := {u:[0,T]→A : u is piecewise continuous}`.

The family includes every constant control `u(t)≡a` with `a∈A`.

No change to `U` is made after inspecting the counterexample.

### 2.4 Frozen response functional

For initial state `x_0=(q_0,r_0)` and intervention `u∈U`, define

`Γ(x_0,u) := q^u_{x_0}(·) ∈ C([0,T],R^m)`.

Thus the frozen response is the **entire retained-variable trajectory** over `[0,T]`, not a post-hoc selected scalar statistic.

The response metric is

`d_Γ(Γ_1,Γ_2) := sup_{0≤t≤T} ||q_1(t)-q_2(t)||`.

Exact response equality means `d_Γ=0`.

### 2.5 Fibre response homogeneity

The pre-declared order parameter `q` is **intervention-response sufficient on D** for the frozen `(U,T,Γ)` if

`π(x_1)=π(x_2)` implies `Γ(x_1,u)=Γ(x_2,u)` for every `u∈U`.

Equivalently, every fibre

`π^{-1}(q) = {(q,r): (q,r)∈D}`

is homogeneous in its frozen controlled `q` response.

This is not claimed as a new definition; it is the frozen comparison criterion inherited from the literature audit.

### 2.6 Controlled closure

The coordinate `q` has **exact controlled closure on D** if there exists a vector field `f̄(q,u)` such that every controlled microscopic trajectory satisfies

`q̇(t)=f̄(q(t),u(t))`

independently of `r(t)`.

Equivalently,

`f(q,r,u)=f̄(q,u)`

for all admissible `(q,r,u)`.

### 2.7 Frozen classical slaving structure

A pre-existing classical slaving relation is represented by a graph

`M := {(q,r): r=h(q)}`

for some fixed `C^1` map `h`.

The minimal classical unforced assumptions invoked in this gate are:

- **unforced invariance** of `M` at `u=0`:

  `g(q,h(q),0) = Dh(q) f(q,h(q),0)`;

- **normal attraction / fast relaxation** in a tube around `M`, expressed when needed through an estimate on

  `e := r-h(q)`.

Importantly, these assumptions are unforced unless explicitly strengthened. They do not presuppose controlled invariance of `M` and do not presuppose fibre projectability of `f`.

---

## 3. Formal statement of the pre-existing synergetic reduction

The classical reduced unforced system associated with the graph `M` is

`q̇ = f(q,h(q),0)`.

If `M` is invariant and normally attracting, trajectories started on `M` remain on it, while nearby trajectories approach it in the fast directions. This is the usual structural content required here from a pre-existing slaving relation.

Two logically different extensions must be distinguished:

1. **Controlled invariance of the slaving graph** would require, for every admissible instantaneous control `a∈A`,

   `g(q,h(q),a) = Dh(q) f(q,h(q),a)`.

   This says interventions do not push a state off the graph.

2. **Global fibre projectability** would require

   `f(q,r,a)=f̄(q,a)`

   for all `r` in the fibre, not merely `r=h(q)`.

Controlled invariance is a statement about the graph. Fibre projectability is a statement about the quotient map `π(q,r)=q`. Neither follows from unforced slaving in general.

---

## 4. Q1 — Sufficiency implication

### Result Q1.1 — Exact criterion for the frozen full-trajectory response

**Classification:** `PROVED`

**Prior-art status:** `SUBSUMED` at the structural level by controlled lumpability / exact abstraction / projectability.

#### Theorem 1 — Fibre response homogeneity iff controlled projectability

Assume unique solutions on `[0,T]` and that `U` contains every constant control `u(t)≡a`, `a∈A`.

The following are equivalent on `D`:

1. For every pair `(q,r_1),(q,r_2)∈D` with the same `q`, and every `u∈U`,

   `Γ((q,r_1),u)=Γ((q,r_2),u)`.

2. For every `a∈A`, the projected vector field is constant along each `q`-fibre:

   `f(q,r_1,a)=f(q,r_2,a)`

   whenever `(q,r_1),(q,r_2)∈D`.

3. There exists `f̄(q,a)` such that

   `f(q,r,a)=f̄(q,a)`

   on `D×A`, and hence `q` has exact controlled closure.

#### Proof

`(2) ⇔ (3)` is immediate by defining `f̄(q,a)` as the common fibre value.

`(3) ⇒ (1)`: if `q̇=f̄(q,u)` independently of `r`, then two trajectories with the same `q_0` and the same intervention solve the same reduced initial-value problem for `q`. Uniqueness gives identical `q(t)` on `[0,T]`; hence their frozen responses are equal.

`(1) ⇒ (2)`: fix any admissible `(q,r_1)`, `(q,r_2)` and any `a∈A`. Apply the constant intervention `u(t)≡a`. By response homogeneity, the resulting retained trajectories satisfy `q_1(t)=q_2(t)` for all `t∈[0,T]`. Differentiating at `t=0` gives

`f(q,r_1,a)=q̇_1(0)=q̇_2(0)=f(q,r_2,a)`.

Thus the projected controlled vector field is constant along every fibre. ∎

#### Interpretation

For this gate's deliberately rich response functional, exact response sufficiency is not an extra concept beyond controlled closure. The full `q` trajectory exposes any instantaneous dependence of `q̇` on the hidden coordinate `r`.

This theorem therefore does **not** provide a novelty claim. It sharply locates the boundary: any exact global implication from classical synergetic slaving to intervention-response sufficiency would have to establish the already-familiar projectability condition from the synergetic assumptions.

#### Prior-art relation

The theorem is structurally a continuous-time exact controlled-lumpability / exact abstraction criterion. The literature freeze already classifies controlled state equivalence and dynamic closure as prior-art territory. Therefore this theorem is marked `SUBSUMED`; it is retained only to make the synergetic comparison explicit.

---

### Result Q1.2 — Classical slaving by itself is insufficient

**Classification:** `PROVED`

**Prior-art status:** `SUBSUMED` as a logical consequence of the distinction between invariant-manifold reduction and controlled quotient closure.

#### Corollary 1

Unforced invariance and normal attraction of `M={r=h(q)}` do not imply the equivalent conditions of Theorem 1.

#### Reason

The classical unforced slaving condition constrains `f` and `g` only on `M` at `u=0` together with transverse stability information. Theorem 1 requires `f(q,r,a)` to be independent of `r` over every relevant fibre and for every admissible control value `a`. Those are strictly stronger statements.

#### Special case: restriction to the slaving manifold

If initial states are restricted to `M`, then for each `q` there is only one admissible point `(q,h(q))`. Fibre homogeneity on that restricted state set is therefore trivial rather than a nontrivial compression statement.

If, in addition, `M` is controlled invariant for every admissible control, then a reduced controlled dynamics on `M` exists:

`q̇ = f(q,h(q),u)`.

This establishes closure **on the graph**. It still does not establish global fibre homogeneity in a tube around the graph.

#### Prior-art relation

This is a standard invariant-manifold versus quotient distinction. No novelty is claimed.

---

## 5. Q2 — Minimal counterexample

### Result Q2 — Exact passive slaving with controlled response failure

**Classification:** `COUNTEREXAMPLE` and `PROVED`

**Prior-art status:** conceptually `SUBSUMED` as an explicit controlled-lumpability failure / forced-fast-mode effect; retained because it is the requested sharp witness tied to a pre-existing slaving fibre.

Consider the scalar system

`q̇ = u r`,

`ṙ = -λ r + u`,

with fixed `λ>0`, control values `u(t)∈[-U,U]`, and frozen horizon `T>0`.

Take the pre-declared order parameter `π(q,r)=q` and the classical slaving graph

`M={r=0}`,

so `h(q)=0`.

### 5.1 Unforced reduction is exact

For `u=0`,

`q̇=0`,

`ṙ=-λr`.

Hence

`q(t)=q_0`,

`r(t)=r_0 e^{-λt}`.

Therefore:

- `M={r=0}` is invariant;
- `M` is globally exponentially attracting in `r` with rate `λ`;
- the reduced unforced dynamics on `M` is exactly `q̇=0`;
- more strongly, the unforced `q` trajectory is independent of `r_0` even off the manifold.

Thus passive correctness is not merely asymptotic in this example: the retained unforced response is exact for every initial `r_0`.

### 5.2 Constant intervention exposes hidden fast-state information

Choose an admissible constant intervention

`u(t)≡a`, with `0<|a|≤U`.

The fast variable solves

`r(t)=r_0 e^{-λt} + (a/λ)(1-e^{-λt})`.

Integrating `q̇=ar` gives

`q(t)=q_0 + (a r_0/λ)(1-e^{-λt}) + a²[t/λ - (1-e^{-λt})/λ²]`.

Now take two initial states on the same `q`-fibre,

`x_1=(q_0,r_1)`,

`x_2=(q_0,r_2)`,

with `r_1≠r_2`.

Their controlled retained trajectories differ by

`Δq(t)=q_1(t)-q_2(t)=(a(r_1-r_2)/λ)(1-e^{-λt})`.

Hence, for any `T>0`,

`d_Γ(Γ(x_1,a),Γ(x_2,a))`

`= |a| |r_1-r_2| (1-e^{-λT})/λ > 0`.

Therefore the pre-existing order parameter `q` is not intervention-response sufficient.

### 5.3 The intervention directly destroys controlled invariance

On the classical slaving graph `r=0`,

`ṙ|_{r=0}=u`.

Thus every nonzero intervention immediately pushes the state away from the unforced slaving manifold. The hidden fast variable is not merely passively present; it is directly excited by the intervention.

### 5.4 Failure even when starting exactly on the slaving manifold

Take `r_0=0` and constant `u(t)≡a`.

Then

`r(t)=(a/λ)(1-e^{-λt})`,

and

`q(t)-q_0=a²[t/λ-(1-e^{-λt})/λ²]`.

A naive controlled extension obtained by substituting the unforced slaving relation `r=0` into `q̇=ur` would predict

`q̇_red=0`,

so `q_red(t)=q_0`.

The actual controlled trajectory therefore differs from this naive reduced model even when initialized exactly on `M`.

This separates two failure mechanisms:

1. **fibre memory:** different initial fast coordinates `r_0` produce different controlled responses despite identical `q_0`;
2. **control leakage:** even `r_0=0` does not protect the reduction because the intervention drives the fast variable off the manifold.

### 5.5 Minimality statement

The example uses one retained scalar coordinate, one slaved scalar coordinate, and one scalar intervention. This is the smallest coordinate count that permits a nontrivial `q/r` decomposition with a hidden fast direction. No stronger universal minimality claim over all possible mathematical formalisms is made.

### Prior-art relation

The mechanism is not claimed as a new phenomenon. In control and abstraction language the projected controlled vector field `ur` is not fibre-projectable, and the control also violates invariance of the unforced slow manifold. The value of the example is diagnostic: it shows explicitly that an exact passive synergetic reduction can coexist with controlled insufficiency.

---

## 6. Q3 — Quantitative approximation

Two quantitative results are obtained: one sharp for the counterexample and one general bridge bound under explicit fast-mode assumptions.

### Result Q3.1 — Sharp fibre-response bound in the counterexample

**Classification:** `PROVED`

**Prior-art status:** `SUBSUMED` in method; exact formula retained as a model-specific bridge diagnostic.

Let two solutions of

`q̇=ur`, `ṙ=-λr+u`

start from `(q_0,r_1)` and `(q_0,r_2)` and be driven by the same arbitrary admissible `u∈U`.

The difference in fast coordinates satisfies exactly

`Δṙ=-λΔr`,

so

`Δr(t)=Δr_0 e^{-λt}`.

Therefore

`Δq(t)=Δr_0 ∫_0^t u(s)e^{-λs} ds`.

Using `|u(s)|≤U`,

`|Δq(t)| ≤ U |Δr_0| (1-e^{-λt})/λ`.

Hence

`d_Γ ≤ U |Δr_0| (1-e^{-λT})/λ`.

The bound is sharp: equality is attained for a constant intervention with sign aligned to `Δr_0`.

#### Scaling

- For `λT ≪ 1`,

  `(1-e^{-λT})/λ = T + O(λT²)`,

  so the hidden-mode response difference initially grows as `U|Δr_0|T`.

- For `λT ≫ 1`,

  `(1-e^{-λT})/λ ≈ 1/λ`,

  so fast relaxation suppresses the maximal fibre distinction as `O(U|Δr_0|/λ)`.

Fast slaving therefore yields approximate response homogeneity only quantitatively and only relative to intervention amplitude, hidden-state spread, and horizon.

---

### Result Q3.2 — Intervention-induced reduced-model error from the manifold

**Classification:** `PROVED`

For the same counterexample with initial state on the slaving manifold `r_0=0`,

`r(t)=∫_0^t e^{-λ(t-s)}u(s) ds`.

Thus

`|r(t)|≤U(1-e^{-λt})/λ`.

Since `|q̇|=|ur|`,

`|q(t)-q_0|`

`≤ U² ∫_0^t (1-e^{-λs})/λ ds`

`= U²[t/λ-(1-e^{-λt})/λ²]`.

Consequently,

`d_Γ(q,q_red) ≤ U²[T/λ-(1-e^{-λT})/λ²]`,

where `q_red(t)≡q_0` is the naive reduction obtained by imposing the unforced slaving relation `r=0` under control.

For constant `u(t)≡±U`, the bound is attained exactly.

This term is purely intervention-induced: it is nonzero even when the initial slaving error is zero.

---

### Result Q3.3 — General finite-horizon synergetic bridge bound

**Classification:** `PROPOSITION` with complete proof under the stated assumptions.

**Prior-art status:** direct specialization of standard comparison / input-to-state-stability / singular-perturbation estimates. It is not claimed as a new control-theoretic theorem. The programme-specific content is the interpretation of its constants relative to a pre-existing synergetic slaving graph and the frozen response metric.

Let

`e(t):=r(t)-h(q(t))`

be the deviation from the fixed slaving graph. Define the graph-restricted controlled vector field

`f̄(q,u):=f(q,h(q),u)`.

Let `q̄` solve the graph-restricted reduced system

`q̄̇=f̄(q̄,u)`,

`q̄(0)=q_0`.

Assume uniformly on the relevant tube and for all admissible controls:

**B1 — fast deviation inequality**

`D⁺||e|| ≤ -λ||e|| + δ + β||u||`,

with `λ>0`, `δ≥0`, `β≥0`.

Interpretation:

- `λ` is the fast relaxation / normal attraction rate;
- `δ` is an unforced slaving defect (`δ=0` for an exact invariant graph under the chosen unforced model);
- `β` measures intervention leakage into the fast deviation.

**B2 — tangential sensitivity to slaving error**

`||f(q,r,u)-f(q,h(q),u)|| ≤ L_e ||e||`.

**B3 — Lipschitz reduced tangential dynamics**

`||f̄(q_1,u)-f̄(q_2,u)|| ≤ L_q ||q_1-q_2||`,

with `L_q≥0`.

Let `||u||_∞≤U` and define

`c := (δ+βU)/λ`.

Then comparison for B1 gives

`||e(t)|| ≤ e^{-λt}||e_0|| + c(1-e^{-λt})`.

Define

`Φ(L_q,t) := (e^{L_q t}-1)/L_q` for `L_q>0`,

and `Φ(0,t):=t`.

Also define

`Ψ(L_q,λ,t) := (e^{L_q t}-e^{-λt})/(L_q+λ)`.

Then for all `t∈[0,T]`,

`||q(t)-q̄(t)||`

`≤ L_e [ ||e_0|| Ψ(L_q,λ,t) + c(Φ(L_q,t)-Ψ(L_q,λ,t)) ]`.

In particular, because the right-hand side is nondecreasing in `t` for the nonnegative constants above,

`d_Γ(q,q̄)`

`≤ L_e [ ||e_0|| Ψ(L_q,λ,T) + ((δ+βU)/λ)(Φ(L_q,T)-Ψ(L_q,λ,T)) ]`.

#### Proof

From B1 and scalar comparison,

`||e(t)|| ≤ E(t) := e^{-λt}||e_0|| + c(1-e^{-λt})`.

Set `z=q-q̄`. By B2 and B3,

`d/dt ||z|| ≤ L_q||z|| + L_e||e||`

in the usual upper-Dini sense. Since `z(0)=0`, Grönwall gives

`||z(t)|| ≤ L_e ∫_0^t e^{L_q(t-s)} ||e(s)|| ds`

`≤ L_e ∫_0^t e^{L_q(t-s)} E(s) ds`.

The two elementary integrals are

`∫_0^t e^{L_q(t-s)}e^{-λs} ds = Ψ(L_q,λ,t)`,

and

`∫_0^t e^{L_q(t-s)}(1-e^{-λs}) ds`

`= Φ(L_q,t)-Ψ(L_q,λ,t)`.

Substitution yields the bound. ∎

#### Consequences

1. **Exact controlled invariance and exact graph initialization.** If `e_0=0`, `δ=0`, and `β=0`, then the bound is zero. The slaving graph remains exact under the admissible intervention family and graph-restricted reduction is exact.
2. **Intervention leakage.** If `e_0=δ=0` but `β>0`, control alone creates a finite-horizon error. For large `λ`, the dominant prefactor scales at least as `O(βU/λ)` for fixed `T,L_q,L_e`.
3. **Initial fibre spread.** If intervention leakage and slaving defect vanish, the error due to an initial off-manifold displacement decays with the kernel `Ψ`, which inherits the fast relaxation rate `λ`.
4. **Counterexample specialization.** In the scalar model `q̇=ur`, `ṙ=-λr+u`, one may take `h=0`, `δ=0`, `β=1`, and `L_e=U`. The resulting scaling is `O(U²/λ)` for the control-induced graph-reduction error, consistent with the exact bound above.

### Approximate fibre diameter consequence

Suppose a tube around the slaving graph is restricted by `||e_0||≤ρ`. For any state in that tube, its frozen response lies within the above bound of the common graph-restricted response starting from the same `q_0`. Therefore two states on the same `q` fibre in that tube satisfy the conservative diameter estimate

`d_Γ(Γ(x_1,u),Γ(x_2,u)) ≤ 2 B_T(ρ)`,

where

`B_T(ρ) := L_e [ ρ Ψ(L_q,λ,T) + ((δ+βU)/λ)(Φ(L_q,T)-Ψ(L_q,λ,T)) ]`.

This is sufficient for an approximate response-homogeneity guarantee. It is not claimed to be sharp in general.

### Prior-art relation

The mathematical machinery is standard singular-perturbation / stability analysis. The statement is therefore not promoted as a new theorem family. Its role here is to make the synergetic-to-behavioral bridge explicit: a pre-existing fast relaxation estimate can be translated into the exact response metric fixed before the calculation.

---

## 7. Q4 — Controlled closure analysis

### Result Q4.1 — Global closure

**Classification:** `PROVED`

**Prior-art status:** `SUBSUMED`.

For the frozen full `q`-trajectory response, Theorem 1 already shows:

`exact fibre response sufficiency ⇔ exact controlled closure of q`.

The closure condition is

`f(q,r,u)=f̄(q,u)`

throughout the relevant state domain.

Classical unforced slaving does not imply this.

### Result Q4.2 — Closure on the slaving graph is weaker than global fibre closure

**Classification:** `PROVED`

If the graph `M={r=h(q)}` is controlled invariant,

`g(q,h(q),u)=Dh(q)f(q,h(q),u)`,

then trajectories initialized on `M` obey the graph-restricted controlled dynamics

`q̇=f(q,h(q),u)`.

This is a valid closed dynamics **on `M`**.

However, states off `M` with the same `q` may still have different `q̇` if `f` depends on `r`. Therefore controlled invariance of the graph does not by itself imply global response homogeneity along fibres.

### Result Q4.3 — Counterexample closure failure

**Classification:** `PROVED`

For

`q̇=ur`, `ṙ=-λr+u`,

the projected vector field depends explicitly on the hidden coordinate whenever `u≠0`. Hence no global `f̄(q,u)` exists.

Moreover `M={r=0}` is not controlled invariant because `ṙ=u` on `M`.

Thus both possible routes to a controlled reduction fail:

- no global fibre projectability;
- no controlled invariance of the unforced slaving graph.

### Why sufficiency and closure must still be conceptually distinguished

The equivalence in Theorem 1 is a consequence of the **specific frozen response functional** `Γ=q(·)` used in this gate. A coarser response — for example one terminal scalar, an integral observable, or a threshold event — could be homogeneous on fibres even when the full `q` dynamics is not closed.

Therefore the project must not generalize the current equivalence into a universal identity between response sufficiency and dynamic closure. Under this gate's response freeze they coincide; generically, response sufficiency depends on the chosen response functional.

---

## 8. Consolidated result classification

| Result | Mathematical status | Prior-art relation | Programme use |
|---|---|---|---|
| Theorem 1: full-trajectory fibre sufficiency iff controlled projectability/closure | `PROVED` | `SUBSUMED` by controlled lumpability / exact abstraction structure | Fixes the exact boundary; prevents renaming prior art |
| Corollary: unforced slaving does not imply controlled sufficiency | `PROVED` | Structurally standard / `SUBSUMED` | Separates classical slaving from controlled quotient requirements |
| Two-dimensional bilinear slow/fast counterexample | `COUNTEREXAMPLE`, `PROVED` | Conceptually controlled-lumpability failure; no novelty claim | Sharp witness that exact passive reduction can fail under interventions |
| Exact fibre-response bound `U|Δr_0|(1-e^{-λT})/λ` | `PROVED` | Standard linear estimate | Quantifies how fast relaxation suppresses hidden-state distinguishability |
| Exact control-induced graph-reduction error `U²[T/λ-(1-e^{-λT})/λ²]` | `PROVED` | Standard forced-fast-mode estimate | Shows intervention leakage can invalidate a reduction even from the manifold |
| General bridge bound from `(λ,δ,β,L_e,L_q)` to response error | `PROPOSITION` with proof | Direct specialization of standard comparison / singular perturbation / ISS methods | Provides a frozen quantitative criterion for approximate intervention sufficiency |
| Controlled-invariant graph gives closure only on the graph | `PROVED` | Standard invariant-manifold fact | Prevents conflation of manifold reduction with global fibre quotienting |

---

## 9. Explicit claim ceiling after this gate

### Claims that may be made

Subject to the exact assumptions in this document, the project may state:

1. A classical unforced synergetic slaving relation does **not by itself** guarantee intervention-relative response sufficiency or global controlled closure of the pre-declared order parameter.
2. For the frozen full retained-variable trajectory response, exact fibre response homogeneity is equivalent to controlled projectability of the microscopic vector field through the order-parameter map.
3. There exists an explicit two-dimensional slow/fast counterexample in which the passive reduction is exact but interventions reveal hidden fast-state dependence and destroy the naive controlled reduction.
4. Under explicit contraction, slaving-defect, and intervention-leakage assumptions, one can bound finite-horizon intervention-response error in terms of `λ`, `δ`, `β`, `L_e`, `L_q`, the intervention amplitude bound `U`, and the horizon `T`.
5. The bridge bound provides a falsifiable compatibility test between a **pre-existing** synergetic reduction and a **frozen** intervention-response criterion.

### Claims that may not be made

The project may **not** state on the basis of this gate that:

- intervention-relative state equivalence is new;
- intervention-sufficient representations are new;
- dynamic closure / controlled lumpability is new;
- `causal order parameter` is a new mathematical object merely by naming the conjunction;
- the counterexample mechanism is a newly discovered control phenomenon;
- the bridge bound is publication-level novel control theory;
- synergetic order parameters are generally intervention sufficient;
- failure under one intervention family implies failure under every possible intervention family;
- success of the bound in one deterministic smooth setting transfers automatically to stochastic systems, Markov systems, or neural optimization states.

The strongest defensible statement is currently a **claim-restricted bridge result**, not a novelty claim.

---

## 10. Decision for proceeding to a neural minimal benchmark

**Decision: PASS — CLAIM-RESTRICTED.**

Reason:

- Q1 is resolved sharply: exact sufficiency requires controlled projectability and is not implied by classical slaving alone.
- Q2 supplies the requested smallest analytically transparent slow/fast counterexample.
- Q3 supplies both exact model-specific bounds and a general finite-horizon bridge estimate.
- Q4 cleanly separates graph invariance, global quotient closure, and response sufficiency.

This is sufficient to justify a later, separately authorised minimal benchmark whose purpose would be to test the already-frozen mathematical criterion rather than to search for a stronger effect or invent a new representation.

This PASS does not authorise such a benchmark by itself. MASTER must open any subsequent branch and freeze its model, intervention family, response functional, horizon, and success criteria before execution.

---

## 11. Open mathematical gaps

1. **Theorem-to-theorem prior-art subsumption of the bridge bound remains unresolved.** The proof is standard; a later literature task would need to determine whether an essentially identical response-error statement already exists in singular perturbation, nonlinear model reduction, approximate simulation/bisimulation, or input-output realization language.
2. **Necessity of the quantitative conditions is open.** B1–B3 are sufficient assumptions, not claimed necessary.
3. **Sharper pairwise fibre bounds are open.** The general `2B_T(ρ)` diameter estimate is conservative because it compares both states through a common graph-restricted trajectory.
4. **Stochastic extensions are outside this gate.** Noise would require a frozen probability metric and response notion before any theorem is attempted.
5. **Discrete-time and Markov analogues are outside this gate.** Their relationship to known lumpability and bisimulation results must be handled directly rather than inferred from the ODE case.
6. **Alternative response functionals are not analysed here.** For terminal, integral, threshold, or distributional responses, sufficiency may be strictly weaker than full controlled closure.
7. **Controlled persistence of a normally hyperbolic slaving manifold is not developed here.** If interventions are small, persistence theorems may produce a deformed controlled manifold rather than preserve the original one. That would be a different, separately frozen question.
8. **No novelty conclusion follows from the absence of a canonical Haken-to-bisimulation theorem in the frozen literature audit.** A dedicated comparison would still be required before any manuscript-level novelty statement.

---

## 12. Final CORE boundary

The mathematical boundary established by this gate is:

> A pre-existing synergetic slaving reduction becomes intervention-response sufficient only when the admissible interventions are compatible with the reduction in a stronger sense than passive slaving alone. Exact global sufficiency for the full retained trajectory requires the already-known quotient condition of controlled fibre projectability. Approximate sufficiency can be certified, under explicit assumptions, by translating fast relaxation, slaving defect, and control leakage into a finite-horizon response-error bound. Interventions can otherwise expose nominally slaved directions even when the passive reduction is exact.

This is a theorem-level clarification and quantitative bridge. It is not a new generic equivalence framework and not a field-level novelty claim.

STOP — RETURN TO MASTER
