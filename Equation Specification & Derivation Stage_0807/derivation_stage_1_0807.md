# Derivation Stage 1 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Scope: foundational derivation of PO-01, PO-03, PO-02, and PO-06

## Status convention and regularity domain

This is a derivation record, not manuscript prose. It does not redesign the controller, alter the privacy target, or renumber ES equations. A conditional result is not promoted to a theorem claim until its named dependency is closed.

The derivations use the frozen assumptions together with the following explicit interpretations:

1. `lambda_tr,i^nu >= underline(lambda)_i^nu > 0`, `underline(w)_i^nu > 0`, and ES-43 gives `0 <= g_i^nu(t) <= 1`. Strict positivity of `g_i^nu` is not needed.
2. The PPC domain has `rho_i^nu >= underline(rho)_i^nu > 0` and `|sigma_i^nu| <= bar(sigma)_i^nu < 1`. The ES-23 quintic is globally `C^2`; its one-sided third derivative at `T_nu` is bounded, so the voltage command rate below is an almost-everywhere bound at that isolated time.
3. Intermediate command-rate constants are stated on a candidate compact tube `K` for physical and privacy states. This is a bootstrap domain, not a replacement for PO-16; PO-16 must later prove persistence in `K`.
4. `k_c^V` and `k_c^omega` are common scalar channel gains, exactly as written in ES-28 and ES-31.

## PO-01: public-private difference decay

For `nu in {V,omega}`, define the derived scalar rate

```text
kappa_i^nu(t) = lambda_tr,i^nu + w_{i,12}^nu(t) + w_{i,21}^nu(t) g_i^nu(t).
```

ES-49 is `dot(z_i^nu)=-kappa_i^nu(t)z_i^nu`; its exact solution is

```text
z_i^nu(t) = z_i^nu(0) exp(- integral_0^t kappa_i^nu(s) ds).
```

By ES-43 and ES-46,

```text
kappa_i^nu(t) >= lambda_tr,i^nu + underline(w)_i^nu
              =: a_{z,i}^nu > 0,

|z_i^nu(t)| <= |z_i^nu(0)| exp(-a_{z,i}^nu t).
```

The strongest uniform rate available from the frozen assumptions is `a_{z,i}^nu=lambda_tr,i^nu+underline(w)_i^nu`, not `lambda_tr,i^nu+2underline(w)_i^nu`. The second weight is multiplied by `g_i^nu`, which may be below one outside the ES-43 inner region. It is only additional nonnegative damping. `lambda_tr`, the weights, and `a_z` have units `s^-1`; `g` is dimensionless and `z` retains command units.

**PO-01 verdict: PROVED.**

## PO-03: admissible command-rate bounds

### Physical derivative constants

Differentiating the lossless ES-6--ES-7 gives the exact identities

```text
dot(P_i) = P_i^{L\prime}(V_i)dot(V_i)
 + sum_k |B_ik|[(dot(V_i)V_k+V_i dot(V_k))sin(delta_ik)
 + V_iV_k cos(delta_ik)(omega_i-omega_k)],

dot(Q_i) = Q_i^{L\prime}(V_i)dot(V_i)
 + 2V_i dot(V_i)sum_k|B_ik|
 - sum_k |B_ik|[(dot(V_i)V_k+V_i dot(V_k))cos(delta_ik)
 - V_iV_k sin(delta_ik)(omega_i-omega_k)].
```

On `K`, replace each magnitude in these identities by its stated supremum: `bar V_i`, `bar Vdot_i`, `bar omega_i`, `bar B_ik`, `bar L_i^P=sup|P_i^{L\prime}|`, and `bar L_i^Q=sup|Q_i^{L\prime}|`. This explicitly defines finite `bar Pdot_i` and `bar Qdot_i`; no conductance term is used.

From ES-10--ES-12 and ES-53,

```text
bar Vddot_i = bar F_i^V + (bar c_i^V+bar r_i^V)/(tau_Qi k_Vi)+bar R_i^V,
bar omegadot_i = bar F_i^omega+(bar c_i^omega+bar r_i^omega)/tau_Pi+bar R_i^omega,

bar Fdot_i^V = [(tau_Qi+k_Vi)bar Vddot_i+bar Vdot_i+k_Qi bar Qdot_i]/(tau_Qi k_Vi),
bar Fdot_i^omega = [bar omegadot_i+k_Pi bar Pdot_i]/tau_Pi.
```

Thus `dot(F)` is bounded using only physical derivatives, bounded `R`, and the command/residual magnitude bounds supplied later by PO-06 and PO-16; no `dot(R)` is required.

### PPC derivative constants

For either channel,

```text
dot(h) = -dot(rho)/[rho^2(1-sigma^2)]
         +2sigma dot(sigma)/[rho(1-sigma^2)^2].
```

Consequently `bar h=1/[underline(rho)(1-bar(sigma)^2)]` and `bar hdot` follows by replacing `rho,sigma,dot(sigma),dot(rho)` in this identity by their bounds.

For voltage, the needed exact derivative chain is

```text
dot(sigma^V)=[dot(e_0^V)-sigma^V dot(rho^V)]/rho^V,
ddot(sigma^V)=[ddot(e_0^V)-2dot(sigma^V)dot(rho^V)-sigma^V ddot(rho^V)]/rho^V,
dot(zeta^V)=-k_1^V zeta^V+h^V chi^V,
ddot(zeta^V)=-k_1^V dot(zeta^V)+dot(h^V)chi^V+h^V dot(chi^V),
dot(chi^V)=-k_2^Vchi^V-h^Vzeta^V-k_c^Ve^V/(tau_Qik_Vi)
            -r_i^V/(tau_Qik_Vi)+R_i^V.
```

Here `dot(e_0^V)=dot(V_i)` and `ddot(e_0^V)=ddot(V_i)`. Differentiating the explicit ES-27 expression for `dot(alpha_i^V)` uses only the listed quantities, the schedule derivatives through `dddot(rho_i^V)`, and `dot(A)=-2sigma dot(sigma)`, `ddot(A)=-2[(dot(sigma))^2+sigma ddot(sigma)]` for `A=1-sigma^2`. These identities define the finite symbolic constant `bar alphaddot_i^V` on `K`.

For frequency, differentiating ES-30 yields

```text
dot(alpha^omega)=dot(sigma^omega)dot(rho^omega)+sigma^omega ddot(rho^omega)
 -k_1^omega[dot(rho^omega)A^omega zeta^omega
 +rho^omega dot(A^omega)zeta^omega+rho^omega A^omega dot(zeta^omega)].
```

Together with ES-11 and ES-37, this defines `bar alphadot_i^omega` on `K`.

### No hidden command-rate loop in `dot(e)`

Differentiating `p=c+r+0.5z` and using ES-44--ES-45 gives directly

```text
dot(p_i^nu)=lambda_tr,i^nu(c_i^nu-p_i^nu)-w_{i,21}^nu g_i^nu z_i^nu.
```

Using ES-48, this is equivalently

```text
dot(p_i^nu)=-lambda_tr,i^nu r_i^nu
             -0.5lambda_tr,i^nu z_i^nu
             -w_{i,21}^nu g_i^nu z_i^nu,
```

so a fully explicit provisional bound is

```text
bar pdot_i^nu=lambda_tr,i^nu bar r_i^nu
 +[0.5lambda_tr,i^nu+bar(w)_i^nu]bar z_i^nu.
```

Hence `dot(e)^nu=B dot(e_0)^nu+L_c dot(p)^nu`, where `B=diag(b_i)`. The apparently circular `L_c dot(c)+L_c dot(r)` terms cancel through ES-50. Therefore

```text
bar edot_i^nu <= b_i bar e0dot_i^nu+||L_c||_infty max_j bar pdot_j^nu.
```

Finally, differentiating ES-28 and ES-31 gives the required explicit symbolic bounds

```text
bar cdot_i^V=tau_Qik_Vi[bar Fdot_i^V+bar alphaddot_i^V+k_2^Vbar chidot_i^V
 +bar hdot_i^Vbar zeta_i^V+bar h_i^Vbar zetadot_i^V]+|k_c^V|bar edot_i^V,

bar cdot_i^omega=tau_Pi[bar Fdot_i^omega+bar alphadot_i^omega]
 +|k_c^omega|bar edot_i^omega.
```

All constants state their dependencies above: compact physical bounds, PPC bounds, gains, `||L_c||`, and provisional `bar c,bar r,bar z`. The latter three are supplied only after PO-06 and PO-16; no desired residual-decay conclusion was assumed.

**PO-03 verdict: PROVED SUBJECT TO PO-16.** PO-06 is closed below; final numerical constants still require the compact-tube result.

## PO-02: residual convolution and envelope

With `r_i^nu(0)=0`, variation of constants in ES-50 gives exactly

```text
r_i^nu(t)=integral_0^t exp[-lambda_tr,i^nu(t-s)]
 {0.5[w_{i,12}^nu(s)-w_{i,21}^nu(s)g_i^nu(s)]z_i^nu(s)-dot(c_i^nu(s))}ds.
```

Set `bar d_i^nu=bar(w)_i^nu+bar(w)_i^nu`. Using PO-01 and `a_{z,i}^nu-lambda_tr,i^nu=underline(w)_i^nu`,

```text
|r_i^nu(t)| <= A_{r0,i}^nu exp(-lambda_tr,i^nu t)
 + integral_0^t exp[-lambda_tr,i^nu(t-s)]|dot(c_i^nu(s))|ds,

A_{r0,i}^nu=bar d_i^nu|z_i^nu(0)|/[2underline(w)_i^nu].
```

| Command-rate condition | Residual conclusion | Validity of ES-51 |
|---|---|---|
| `|dot(c)|<=C_c` only | `limsup|r|<=C_c/lambda_tr`; generally nonzero | Invalid with decaying `gamma_priv`. |
| bounded and `dot(c)->0` | stable-filter convergence gives `r->0` | A specified envelope is still required. |
| `dot(c) in L1` | `r->0` | An explicit `L1` tail envelope is still required. |
| `|dot(c)|<=C_c exp(-beta t)` | explicit exponential decay | Valid using the schedule below. |

For the exponential case, let

```text
psi_{lambda,beta}(t)=(exp(-beta t)-exp(-lambda t))/(lambda-beta)
```

when `lambda!=beta`, and `psi_{lambda,lambda}(t)=t exp(-lambda t)`. Then

```text
|r_i^nu(t)|<=Gamma_i^nu(t)
=A_{r0,i}^nu exp(-lambda_tr,i^nu t)+C_{c,i}^nu psi_{lambda_tr,i^nu,beta_i^nu}(t).
```

ES-51 holds precisely when a public design schedule and positive `bar(r)^nu` are chosen so that

```text
gamma_priv,i^nu(t)>=Gamma_i^nu(t)/bar(r)^nu,
gamma_priv,i^nu(t)->0.
```

Thus ES-50 does not imply ES-51 from a uniform command-rate bound. The smallest correction is an explicit decaying command-rate envelope, either proved later from the closed loop or stated as a technical regularity assumption. It requires no new module and no Blueprint reopen.

**PO-02 verdict: PROVED SUBJECT TO PO-03 and an explicit decaying command-rate condition.**

## PO-06: graph and algebraic closure

Let `B=diag(b_i)`, `A_V=diag_i(tau_Qi k_Vi)`, and `A_omega=diag_i(tau_Pi)`. The following are proof-only diagonal scales; they do not add controller states. Define

```text
M_c^V=I_N-k_c^V L_c,
M_c^omega=I_N-k_c^omega L_c.
```

### Voltage channel

Substituting ES-101a into ES-28 gives

```text
bold(c)^V=A_V[bold(F)^V-dot(bold(alpha))^V+k_2^Vbold(chi)^V
 +diag(h^V)bold(zeta)^V]
 +k_c^V[Bbold(e_0)^V+L_cbold(c)^V+L_cbold(r)^V+0.5L_cbold(z)^V].
```

Moving only the command-dependent graph term left gives the exact relation

```text
M_c^Vbold(c)^V=A_V[bold(F)^V-dot(bold(alpha))^V+k_2^Vbold(chi)^V
 +diag(h^V)bold(zeta)^V]
 +k_c^V[Bbold(e_0)^V+L_cbold(r)^V+0.5L_cbold(z)^V].
```

### Frequency channel

The same substitution in ES-31 gives

```text
bold(c)^omega=A_omega[bold(F)^omega-bold(alpha)^omega]
 +k_c^omega[Bbold(e_0)^omega+L_cbold(c)^omega
 +L_cbold(r)^omega+0.5L_cbold(z)^omega],

M_c^omegabold(c)^omega=A_omega[bold(F)^omega-bold(alpha)^omega]
 +k_c^omega[Bbold(e_0)^omega+L_cbold(r)^omega+0.5L_cbold(z)^omega].
```

The matrix to invert is therefore `I_N-k_c^nu L_c`, not `I_N+k_c^nu L_c`. The heterogeneous quantities `tau_Pi`, `tau_Qi`, and `k_Vi` occur only in `A_omega` and `A_V` on the right-hand sides. They do not multiply `L_cbold(c)` and do not create a channel-scaled graph matrix.

### Induced-norm bounds

Under ES-21a, define the finite proof constants

```text
K_M^V=||(M_c^V)^(-1)||,
K_M^omega=||(M_c^omega)^(-1)||.
```

For any declared induced norm,

```text
||bold(c)^V||<=K_M^V{||A_V||[||bold(F)^V||+||dot(bold(alpha))^V||
 +k_2^V||bold(chi)^V||+||diag(h^V)bold(zeta)^V||]
 +|k_c^V|[||Bbold(e_0)^V||+||L_cbold(r)^V||+0.5||L_cbold(z)^V||]},

||bold(c)^omega||<=K_M^omega{||A_omega||[||bold(F)^omega||+||bold(alpha)^omega||]
 +|k_c^omega|[||Bbold(e_0)^omega||+||L_cbold(r)^omega||
 +0.5||L_cbold(z)^omega||]}.
```

Finally ES-101a itself gives, for either channel,

```text
||bold(e)^nu||<=||B||||bold(e_0)^nu||
 +||L_c||[||bold(c)^nu||+||bold(r)^nu||+0.5||bold(z)^nu||].
```

Thus ES-21a is sufficient as written under the frozen common-scalar `k_c` convention. If a future version makes `k_c` agent-dependent, the condition must become `det(I_N-K_c^nu L_c)!=0`; that is not the current architecture.

**PO-06 verdict: PROVED.**

## Dependent-equation consistency check

| Object | Stage-1 finding | Impact |
|---|---|---|
| ES-21a | Correct for scalar `k_c^V,k_c^omega`; neither a plus sign nor a physical time-scale factor appears. | No equation change. |
| ES-49--ES-51 | ES-49 and ES-50 are exact. ES-51 requires the additional known decay envelope for `dot(c)`. | Assumption-level closure is still required before final Equation Freeze. |
| ES-62--ES-70 | `r` retains the explicit negative plant contribution after `u=c+r` substitution. | No change. |
| ES-88, ES-101, ES-101a | Their stated algebra and graph identity remain consistent with the stage-1 bounds. | PO-07--PO-10 remain downstream. |
| ES-102 | Cannot be claimed yet because the composite gain and invariant-tube arguments are not closed. | PO-07 remains OPEN. |

## Circularity audit and minimal resolution

There is no algebraic `dot(c)` loop in `dot(e)`: the public-state identity derived from ES-44--ES-45 removes it exactly. The remaining logical loop is different: ES-51 is used by later Lyapunov bounds, while a decaying `dot(c)` envelope may itself be obtained only after a later closed-loop convergence proof. A uniform rate bound from PO-03 cannot break this loop.

Two technically valid resolutions remain within the frozen architecture:

1. Add a technical assumption giving a channel-wise decaying envelope for `dot(c_i^nu)` and choose `gamma_priv` to dominate the convolution derived above.
2. In a later stage, retain the exact ES-50 residual state in the composite analysis and derive the command-rate decay without first invoking ES-51; only then instantiate ES-51.

This document does not select the second path because PO-07 and later are out of scope. The smallest immediate closure is the first, assumption-level condition. It requires no Blueprint reopen, but it must be made explicit before Lemma 1 or Theorem 1 relies on a decaying residual schedule.

## Stage-1 status

- PO-01: **PROVED**.
- PO-03: **PROVED SUBJECT TO PO-16**.
- PO-02: **PROVED SUBJECT TO PO-03 and an explicit decaying command-rate condition**.
- PO-06: **PROVED**.

No ES equation has been changed. The Stage-1 finding is an assumption-level gap in the decaying ES-51 claim, not an algebraic contradiction or an architecture defect. Blueprint Reopen Required: **NO**.
