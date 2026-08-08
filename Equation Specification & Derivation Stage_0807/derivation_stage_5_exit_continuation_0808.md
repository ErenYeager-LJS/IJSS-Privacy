# Derivation Stage 5: Joint Exit-Continuation Audit (PO-11 / PO-16B)

> Task ID: task-004-joint-exit-continuation
> Branch: task-004-joint-exit-continuation
> Blueprint Freeze Version 2.0

## 1. Scope and verdict

This document uses the frozen PPC map, PO-16A local well-posedness, PO-07 local ES-102, and PO-13 symbolic feasibility. It adds no state, controller equation, barrier function, observer, or Lyapunov metric. It does not use PO-02B, PO-12, PO-14, PO-15, or a global asymptotic claim.

The correct proof object is one **Joint Exit-Continuation Lemma**. It treats funnel, physical, actuator, singularity, and loss-of-compactness exits in one first-exit problem. The lemma gives a conditional closure if a compact Lyapunov sublevel set with strict physical and actuator margins exists. That existence/margin condition is not proved by the current Assumption 1, PO-13, or PO-07. Consequently PO-11 and PO-16B remain `OPEN`; neither is relabeled `PROVED`.

## 2. Locality audit of ES-102

The constants entering ES-102 split as follows.

| Object | Role | Scope | Boundary behavior |
|---|---|---|---|
| `P_L^V,P_L^priv,p_zeta^V,p_chi^V,p_c^V,p_c^omega` | fixed metric weights | globally fixed by design; norm equivalence is evaluated on each chosen coordinate set | do not blow up |
| graph/pinning norms in `H_V,H_omega` | algebraic closure | fixed graph constants; the induced bounds are finite on every compact `K` compactly contained in `D_min` | may inherit state bounds through `K` |
| `h_bar_i^V,h_bar_i^omega` | PPC transformation bounds | finite on a compact set with `rho_i>0` and `|sigma_i|<=sigma_bar_i<1` | diverge as `rho_i(1-sigma_i^2)` approaches zero |
| `bar(R)_i^nu` | physical uncertainty | fixed/bounded on the declared operating region under Assumption 1 | not the present singularity |
| `bar r^nu`, `C_c^nu(K)` | residual and command-rate bounds | compact-dependent; finite on each `K` but not globally supplied | can fail when the trajectory leaves every compact subset |
| `d_R,d_priv^loc` | ES-102 disturbance constants | finite only after a compact set and its local bounds are selected | no uniform global value is established |
| actuator margins in PO-13 | input feasibility | verified only on the PO-13 bootstrap design region | not a global invariance result |
| gains and epsilons | design parameters | fixed once selected | no blow-up; must satisfy the local matrix certificate |

Thus the compact-subset extension statement is valid for local regularity, but it is not a continuation theorem: for each `K \Subset D_min` one obtains new finite constants, not one constant valid on all of `D_min`.

## 3. One admissible first-exit problem

Let `X_min(t)` be the independent state of PO-16A, with maximal interval `[0,t_max)`, and let `D_min` be its genuine open admissible domain. Define the candidate exit time

```text
tau_exit = inf { t in (0,t_max) : X_min(t) approaches the relative boundary of D_min,
                  or ||X_min(t)|| becomes unbounded on a finite interval }.
```

The relative boundary is partitioned into:

1. PPC/funnel exit: `|sigma_i^nu| -> 1` for some `i,nu`;
2. physical exit: the physical projection approaches `partial Delta`;
3. actuator exit: some `u_i` approaches `partial U_i`;
4. denominator/singularity exit: a retained denominator approaches zero;
5. loss of compactness: an independent coordinate becomes unbounded while no named boundary is reached.

This is one exit problem, not separate PO-11 and PO-16B exit arguments.

## 4. Joint Exit-Continuation Lemma (conditional form)

Define the explicit proof/design-domain condition `JECFC`:

```text
There exists c>V_cl(X_min(0)) and a set
Omega_c = { X_min in D_min : V_cl(X_min) <= c }
such that Omega_c is compactly contained in D_min,
the physical projection of Omega_c has positive distance from partial Delta,
the compact-subset instantiation satisfies Q_cl(Omega_c) >> 0,
and u_i(X_min,t) has positive distance from partial U_i on Omega_c
for the time interval under consideration.
```

Let `K=Omega_c`. Instantiate PO-03 and PO-07 on this `K`, producing finite `a_cl(K)>0`, `d_R(K)`, and `d_priv(K,t)`. If, on a finite interval `[0,T]`,

```text
bar d_K(T) = d_R(K) + esssup_{0<=t<=T} d_priv(K,t) < a_cl(K)c,
```

then ES-102 implies, on the boundary `V_cl=c`,

```text
dot(V_cl) <= -a_cl(K)c + bar d_K(T) < 0.
```

The first-exit argument therefore excludes crossing of the `V_cl=c` boundary before `T`. Since `Omega_c` is compactly contained in `D_min` and has strict physical/actuator margins, the funnel, physical, actuator, denominator, and loss-of-compactness exits are all excluded on `[0,T]`. PO-16A's Caratheodory continuation alternative then extends the solution beyond any finite `T` for which `JECFC` and the displayed margin condition hold.

This proves a conditional joint closure only. It does not prove that such a `c` and such margins exist under the current frozen assumptions.

## 5. Funnel boundary component

For every channel, the frozen transformation is `zeta_i^nu=atanh(sigma_i^nu)`. If a first funnel exit existed at `tau_exit`, continuity from the interior gives `sigma_i^nu(t)->+1` or `-1`, hence `|zeta_i^nu(t)|->infinity`. Under `JECFC`, the trajectory remains in `Omega_c` up to the candidate exit, while the frozen metric gives `V_cl<=c` there and `m_V||xi||^2<=V_cl`. The `zeta` component would force `V_cl->infinity`, contradicting `V_cl<=c`. Therefore the PPC boundary is excluded conditionally on `JECFC`.

## 6. Physical, actuator, and singularity components

The same argument excludes physical and actuator exits only because `JECFC` explicitly requires strict positive distance from `partial Delta` and `partial U_i` on `Omega_c`. PO-13 alone does not provide this property outside its bootstrap design region. Denominator exits are excluded by compact containment in `D_min`; loss of compactness is excluded by compactness of `Omega_c`.

Without `JECFC`, none of these conclusions follows from ES-102: a bounded transformed-error metric does not control an unpenalized physical coordinate such as an accumulated phase difference, and PO-13 is not a global actuator-invariance theorem.

## 7. Status and dependency consequence

The conditional lemma has the acyclic proof-level shape

```text
PO-07 + PO-13 + PO-16A + JECFC
                 |
                 v
Joint Exit-Continuation Lemma
              /                 \
           PO-11              PO-16B
```

`JECFC` is a required design-domain feasibility condition, not an existing completed proof obligation. Because its existence is not established by the frozen equations, PO-11 and PO-16B remain `OPEN`. PO-02B remains `OPEN` and downstream.

## 8. Audit conclusion

- Standalone PO-11 failed because ES-102 is local on a non-invariant `K_0`.
- Compact-subset re-instantiation is valid, but it does not by itself produce a common invariant compact set.
- Funnel exit is conditionally excluded by the existing `atanh` coordinate and metric coercivity.
- Physical and actuator exits require the explicit strict-margin part of `JECFC`.
- No ES equation, controller equation, privacy mechanism, PPC transformation, or Lyapunov metric was changed.
- Blueprint Reopen Required: **NO**.
