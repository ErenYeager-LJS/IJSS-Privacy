# Derivation Stage 4: Composite Gain Closure (PO-07)

> Task ID: task-003-po07-composite-gain
> Scope: assembly of ES-94, ES-98, and ES-101 on `K_0`
> Blueprint Freeze Version 2.0

This is an assembly of the already-proved local inequalities. It introduces no state, metric, controller, privacy mechanism, graph, or PPC equation. It does not prove PO-02B, PO-11, PO-16B, or Theorem 1.

## 1. Composite candidate

Use exactly ES-89:

```text
mathscr V_cl = mathscr V_V + mathscr V_omega + mathscr V_priv.
```

The three terms are the frozen weighted metrics from ES-83, ES-87, and ES-89. With

```text
xi = col(bold(zeta)^V, bold(chi)^V,
         bold(zeta)^omega, bold(z)^V, bold(z)^omega,
         bold(r)^V, bold(r)^omega),
```

positive metric weights give finite local constants `m_V,M_V>0` on `K_0` such that

```text
m_V ||xi||^2 <= mathscr V_cl <= M_V ||xi||^2.
```

Thus the candidate is positive definite and radially unbounded with respect to the analysis coordinates within the local admissible region. This is local coercivity, not a global or invariant-region claim. The candidate is differentiable along the absolutely continuous Caratheodory solution almost everywhere; the privacy product `g_i z_i` is locally Lipschitz.

## 2. Existing component inequalities

PO-08, PO-09, and PO-10 already provide, without recomputation,

```text
dot(mathscr V_V)
 <= -a_Vz ||bold(zeta)^V||^2
    -a_Vchi ||bold(chi)^V||^2
    + sum_i (p_chi^V)^2 [D_i^V]^2/(2 eps_V2),

a_Vz = p_zeta^V k_1^V - eps_V0/2,
a_Vchi = p_chi^V k_2^V - eps_V2/2
          - (Delta_p^V)^2(h_bar_i^V)^2/(2 eps_V0),
```

from ES-94,

```text
dot(mathscr V_omega)
 <= -a_omegaz ||bold(zeta)^omega||^2
    + sum_i h_bar_i^2 [D_i^omega]^2/(2 eps_omega),

a_omegaz = k_1^omega - eps_omega/2,
```

from ES-98, and

```text
dot(mathscr V_priv)
 <= -a_z ||bold(z)||^2 - a_r ||bold(r)||^2
    + d_c ||dot(bold(c))||^2
```

from ES-101. These are local inequalities on `K_0`; `a_Vz,a_Vchi,a_omegaz,a_z,a_r` are positive under PO-08, PO-09, and PO-10.

## 3. Graph and disturbance bookkeeping

PO-06 and ES-101a give finite induced-norm bounds on `e` and `c`. Therefore the ES-93 and ES-96 disturbance vectors admit the componentwise bounds

```text
bold(D)^V <= d_V^R + H_V |xi|,
bold(D)^omega <= d_omega^R + H_omega |xi|.
```

`H_V,H_omega` contain only existing constants: `k_c^V,k_c^omega`, `K_M^V,K_M^omega`, `||L_c||`, `h_bar`, the metric weights, the PPC gains, and the PO-06 graph/pinning bounds. Residual coordinates occur in `xi`, so graph and residual terms are not counted as external inputs twice. `d_V^R,d_omega^R` contain only the bounded physical uncertainty and fixed compact-region offsets.

PO-03 gives the finite local command-rate constants

```text
||dot(bold(c))^V|| <= C_c^V(K_0),
||dot(bold(c))^omega|| <= C_c^omega(K_0).
```

The privacy remainder contributed by ES-101 is therefore

```text
d_priv^loc = d_c[(C_c^V(K_0))^2+(C_c^omega(K_0))^2].
```

It is finite but not claimed to decay; ES-51 and PO-02B are not used.

## 4. Exact composite assembly

Set

```text
W_D = blkdiag((p_chi^V)^2/(2 eps_V2) I,
              1/(2 eps_omega) I),
H = col(H_V,H_omega),
d_R = col(d_V^R,d_omega^R),
Q_0 = diag(a_Vz I,a_Vchi I,a_omegaz I,
           a_z I,a_z I,a_r I,a_r I).
```

Adding ES-94, ES-98, and ES-101 exactly once gives

```text
dot(mathscr V_cl)
 <= -xi^T Q_0 xi
    + (d_R+H|xi|)^T W_D(d_R+H|xi|)
    + d_priv^loc.
```

The voltage, frequency, privacy, graph, physical-uncertainty, residual, and Young terms each occur once in this expression. There are no frozen cross-channel terms. The graph contribution enters only through `H`, as required by PO-06.

## 5. Minimal gain certificate

The minimal sufficient composite condition is

```text
Q_cl = Q_0 - H^T W_D H ≻ 0,
lambda_cl = lambda_min(Q_cl) > 0.
```

This is the non-redundant matrix certificate. The already-proved component conditions ES-95, ES-98, and the Privacy Gain Feasibility Condition make the diagonal blocks of `Q_0` positive; `Q_cl ≻ 0` is the remaining graph/gain compatibility test.

Dependencies are explicit: `k_1^V` enters `a_Vz`; `k_2^V` enters `a_Vchi`; `k_1^omega` enters `a_omegaz`; `k_c^V,k_c^omega,K_M^V,K_M^omega,L_c` enter `H`; metric weights and every epsilon enter `Q_0` or `W_D`; private tracking rates and weights enter `a_z,a_r`; and `h_bar` enters the PPC rows of `H`.

## 6. Derivation of ES-102

Expanding the quadratic cross term and applying Young's inequality once gives

```text
dot(mathscr V_cl)
 <= -(lambda_cl/2)||xi||^2
    + d_R^T W_D d_R
    + (2/lambda_cl)||H^T W_D d_R||^2
    + d_priv^loc.
```

Because `mathscr V_cl <= M_V||xi||^2`, define

```text
a_cl = lambda_cl/(2 M_V),
d_R^* = d_R^T W_D d_R
        + (2/lambda_cl)||H^T W_D d_R||^2,
d_priv(t) = d_priv^loc.
```

Then

```text
dot(mathscr V_cl)
 <= -a_cl mathscr V_cl + d_R^* + d_priv(t),
```

which is ES-102 obtained from ES-94, ES-98, ES-101, and PO-06 rather than cited. Every constant is traceable to an existing local inequality or a finite PO-03/PO-06 bound.

## 7. Interpretation and status

ES-102 proves a **local Lyapunov comparison inequality on `K_0`**. It does not prove global stability, forward invariance, practical prescribed-time recovery, or asymptotic privacy residual decay. Those remain assigned to PO-11, PO-16B, PO-12, and PO-02B.

**PO-07 verdict: PROVED.**

## 8. Verification

- Composite Lyapunov: ES-89 only; no new metric.
- Negative terms: `a_Vz,a_Vchi,a_omegaz,a_z,a_r`, reduced by `H^T W_D H`.
- Remaining disturbances: `d_R^*` and finite local `d_priv^loc`.
- Gain certificate: `Q_cl ≻ 0` plus the already-proved component feasibility conditions.
- Proof DAG: 18 nodes, 34 edges, 0 nontrivial SCCs.
- ES equations changed: **NO**.
- Blueprint Reopen Required: **NO**.
- Recommended next task: `task-004-po11-funnel-barrier`.
