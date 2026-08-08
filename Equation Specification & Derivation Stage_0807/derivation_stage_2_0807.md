# Derivation Stage 2 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Scope: PO-08, PO-09, PO-10 only

## Scope boundary

This document derives consequences of the frozen ES equations. It does not derive PO-07, Theorem 1, or any new controller state. The composite inequality ledger at the end is preparatory only.

The calculations use the exact channel equations and the Stage-1 results PO-01, PO-03, and PO-06. No step below assumes the stronger ES-51 decay claim unless explicitly stated.

## PO-08: voltage Lyapunov chain

### Exact derivative from ES-83, ES-65, and ES-66

For

```text
mathscr V_V = 0.5 sum_i[(zeta_i^V)^2+(chi_i^V)^2],
```

the product rule gives

```text
dot(mathscr V_V)
 = sum_i[zeta_i^V dot(zeta_i^V)+chi_i^V dot(chi_i^V)].
```

Substitute ES-65 and ES-66 term by term:

```text
zeta_i^V dot(zeta_i^V)
 = -k_1^V(zeta_i^V)^2
   + h_i^V zeta_i^V chi_i^V,

chi_i^V dot(chi_i^V)
 = -k_2^V(chi_i^V)^2
   - h_i^V chi_i^V zeta_i^V
   - [k_c^V/(tau_Qi k_Vi)]chi_i^V e_i^V
   - [1/(tau_Qi k_Vi)]chi_i^V r_i^V
   + chi_i^V R_i^V.
```

The two transformation terms are exactly equal and opposite:

```text
+h_i^V zeta_i^V chi_i^V - h_i^V chi_i^V zeta_i^V = 0.
```

Therefore the exact derivative is

```text
dot(mathscr V_V)
 = sum_i[-k_1^V(zeta_i^V)^2-k_2^V(chi_i^V)^2
   - beta_{e,i}^V chi_i^V e_i^V
   - beta_{r,i}^V chi_i^V r_i^V
   + chi_i^V R_i^V],
```

where the proof-only coefficients are

```text
beta_{e,i}^V = k_c^V/(tau_Qi k_Vi),
beta_{r,i}^V = 1/(tau_Qi k_Vi).
```

This is ES-84 obtained directly from ES-83 and ES-65--ES-66. ES-62--ES-64 are consistent with the same sign: `r_i^V` enters `dot(chi_i^V)` as `-r_i^V/(tau_Qi k_Vi)`.

### Separate disturbance bounds

For fixed positive Young parameters `eps_V1`, `eps_V2`, and `eps_V3`, apply the scalar inequality
`ab <= 0.5 eps a^2 + b^2/(2 eps)` separately to the three nonnegative magnitudes:

```text
|beta_{e,i}^V chi_i^V e_i^V|
 <= 0.5 eps_V1(chi_i^V)^2
    + (beta_{e,i}^V)^2(e_i^V)^2/(2 eps_V1),

|beta_{r,i}^V chi_i^V r_i^V|
 <= 0.5 eps_V2(chi_i^V)^2
    + (beta_{r,i}^V)^2(r_i^V)^2/(2 eps_V2),

|chi_i^V R_i^V|
 <= 0.5 eps_V3(chi_i^V)^2
    + (R_i^V)^2/(2 eps_V3).
```

The three positive terms are not combined before their origin is recorded. Summing gives

```text
dot(mathscr V_V)
 <= -sum_i k_1^V(zeta_i^V)^2
    -sum_i[k_2^V-0.5(eps_V1+eps_V2+eps_V3)](chi_i^V)^2
    +sum_i[(beta_{e,i}^V)^2(e_i^V)^2/(2 eps_V1)
          +(beta_{r,i}^V)^2(r_i^V)^2/(2 eps_V2)
          +(R_i^V)^2/(2 eps_V3)].
```

For the selected three-parameter allocation, the smallest direct sufficient condition on the retained `chi` coefficient is

```text
k_1^V > 0,
k_2^V > 0.5(eps_V1+eps_V2+eps_V3).
```

There is no numerical minimum until the epsilons are selected: decreasing an epsilon reduces the dissipative penalty but increases its corresponding disturbance coefficient. The condition is therefore the exact Young-allocation condition, not an assertion that `k_2^V` has a universal lower bound.

### Recovery of ES-94

Define the aggregate disturbance magnitude from ES-93,

```text
D_i^V(t)=|beta_{e,i}^V||e_i^V|+|beta_{r,i}^V||r_i^V|+bar(R)_i^V.
```

The triangle inequality gives

```text
|chi_i^V|D_i^V(t)
 >= |chi_i^V|(|beta_{e,i}^V e_i^V|+|beta_{r,i}^V r_i^V|+|R_i^V|)
```

as an upper-bound device, and one Young inequality with `eps_V2>0` gives

```text
|chi_i^V|D_i^V(t)
 <= 0.5 eps_V2(chi_i^V)^2+[D_i^V(t)]^2/(2 eps_V2).
```

Substitution into the exact derivative yields

```text
dot(mathscr V_V)
 <= -sum_i k_1^V(zeta_i^V)^2
    -sum_i[k_2^V-0.5 eps_V2](chi_i^V)^2
    +sum_i[D_i^V(t)]^2/(2 eps_V2),
```

which is ES-94. In this aggregate form the corresponding condition is ES-95:
`k_1^V>0` and `k_2^V>0.5 eps_V2`. The separated three-epsilon condition above is sharper for source attribution; ES-94 is the compact single-epsilon form retained by the specification.

### PO-08 status and constants

The algebraic chain through ES-94 is complete. `D_i^V` is finite on a compact tube only after the graph bound PO-06 and the state-domain continuation PO-16; ES-51 is not needed to establish the pointwise inequality, but it is needed later if `D_i^V` is required to decay.

| Constant | Units in the normalized proof metric | Depends on |
|---|---|---|
| `beta_{e,i}^V` | inverse time after channel scaling | `k_c^V,tau_Qi,k_Vi` |
| `beta_{r,i}^V` | inverse time after channel scaling | `tau_Qi,k_Vi` |
| `eps_V1,eps_V2,eps_V3,eps_V2` | squared `chi`-coefficient units | Young allocation only |
| `D_i^V` | `chi`-derivative magnitude | graph error, residual, `bar R` |
| `k_2^V-0.5 eps_V2` | dissipation coefficient | `k_2^V,eps_V2` |
| `[D_i^V]^2/(2eps_V2)` | Lyapunov-derivative units | `D_i^V,eps_V2` |

**PO-08 verdict: PROVED SUBJECT TO PO-16 and a declared per-unit/normalization convention for ES-83.** If ES-83 is interpreted in raw physical units, `zeta_i^V` is dimensionless while `chi_i^V` has voltage-per-time units, so their squares cannot be added without a positive metric weight. This is a dimension-audit gap, not an algebraic sign error; ES-83 was not modified under the no-redesign rule.

## PO-09: frequency Lyapunov chain

### Exact derivative from ES-85 and ES-70

From ES-85,

```text
mathscr V_omega=0.5 sum_i(zeta_i^omega)^2,
dot(mathscr V_omega)=sum_i zeta_i^omega dot(zeta_i^omega).
```

ES-70 gives

```text
dot(zeta_i^omega)
 = -k_1^omega zeta_i^omega
   + h_i^omega[-beta_{e,i}^omega e_i^omega
               -beta_{r,i}^omega r_i^omega+R_i^omega],

beta_{e,i}^omega=k_c^omega/tau_Pi,
beta_{r,i}^omega=1/tau_Pi,
h_i^omega=1/[rho_i^omega(1-(sigma_i^omega)^2)].
```

Therefore the exact product expansion is

```text
dot(mathscr V_omega)
 = sum_i[-k_1^omega(zeta_i^omega)^2
   -h_i^omega beta_{e,i}^omega zeta_i^omega e_i^omega
   -h_i^omega beta_{r,i}^omega zeta_i^omega r_i^omega
   +h_i^omega zeta_i^omega R_i^omega],
```

which is ES-86. The factor `h_i^omega` multiplies every nonnominal term because ES-34 divides the physical-error derivative by `rho_i^omega(1-(sigma_i^omega)^2)`; it cannot be omitted from the graph, residual, or uncertainty terms.

### Separate graph, privacy, and uncertainty bounds

On the invariant PPC domain, `0<h_i^omega<=h_bar_i^omega`. Define

```text
D_{e,i}^omega=|beta_{e,i}^omega||e_i^omega|,
D_{r,i}^omega=|beta_{r,i}^omega||r_i^omega|,
D_{R,i}^omega=bar(R)_i^omega.
```

Before aggregation, the three terms obey

```text
|h_i^omega zeta_i^omega beta_{e,i}^omega e_i^omega|
 <= h_bar_i^omega|zeta_i^omega|D_{e,i}^omega,

|h_i^omega zeta_i^omega beta_{r,i}^omega r_i^omega|
 <= h_bar_i^omega|zeta_i^omega|D_{r,i}^omega,

|h_i^omega zeta_i^omega R_i^omega|
 <= h_bar_i^omega|zeta_i^omega|D_{R,i}^omega.
```

For `eps_{omega,e},eps_{omega,r},eps_{omega,R}>0`, applying Young separately gives

```text
h_bar_i^omega|zeta_i^omega|D_{e,i}^omega
 <= 0.5 eps_{omega,e}(zeta_i^omega)^2
    +(h_bar_i^omega)^2[D_{e,i}^omega]^2/(2eps_{omega,e}),

h_bar_i^omega|zeta_i^omega|D_{r,i}^omega
 <= 0.5 eps_{omega,r}(zeta_i^omega)^2
    +(h_bar_i^omega)^2[D_{r,i}^omega]^2/(2eps_{omega,r}),

h_bar_i^omega|zeta_i^omega|D_{R,i}^omega
 <= 0.5 eps_{omega,R}(zeta_i^omega)^2
    +(h_bar_i^omega)^2[D_{R,i}^omega]^2/(2eps_{omega,R}).
```

Hence a separated bound is

```text
dot(mathscr V_omega)
 <= -sum_i[k_1^omega-0.5(eps_{omega,e}+eps_{omega,r}+eps_{omega,R})]
       (zeta_i^omega)^2
    +sum_i(h_bar_i^omega)^2{[D_{e,i}^omega]^2/(2eps_{omega,e})
                            +[D_{r,i}^omega]^2/(2eps_{omega,r})
                            +[D_{R,i}^omega]^2/(2eps_{omega,R})}.
```

To recover the single-parameter ES-98 form, define

```text
D_i^omega(t)=D_{e,i}^omega+D_{r,i}^omega+D_{R,i}^omega,
eps_omega>0.
```

Then

```text
h_bar_i^omega|zeta_i^omega|D_i^omega
 <= 0.5 eps_omega(zeta_i^omega)^2
    +(h_bar_i^omega)^2[D_i^omega(t)]^2/(2eps_omega),
```

and substitution gives exactly ES-98:

```text
dot(mathscr V_omega)
 <= -sum_i[k_1^omega-0.5eps_omega](zeta_i^omega)^2
    +sum_i(h_bar_i^omega)^2[D_i^omega(t)]^2/(2eps_omega).
```

The single-parameter sufficient gain condition is

```text
k_1^omega>0.5eps_omega,
```

while the separated allocation requires `k_1^omega>0.5(eps_{omega,e}+eps_{omega,r}+eps_{omega,R})`. The aggregate ES-98 condition is the retained specification form.

### PO-09 status and constants

| Constant | Units in the normalized proof metric | Depends on |
|---|---|---|
| `beta_{e,i}^omega` | inverse time after frequency scaling | `k_c^omega,tau_Pi` |
| `beta_{r,i}^omega` | inverse time | `tau_Pi` |
| `h_bar_i^omega` | reciprocal frequency-error unit | `rho_i^omega,bar(sigma_i^omega)` |
| `eps_omega,eps_{omega,e},eps_{omega,r},eps_{omega,R}` | squared transformed-error coefficient units | Young allocation |
| `D_i^omega` | physical frequency-error derivative magnitude | `e_i^omega,r_i^omega,R_i^omega` and droop gains |

The frequency chain is algebraically closed as a pointwise inequality. Finiteness of the state-dependent `D_i^omega` on the full trajectory still belongs to PO-16, and decay of its residual component is not assumed here.

**PO-09 verdict: PROVED SUBJECT TO PO-16.**

## PO-10: privacy Lyapunov chain

### Exact derivative

For one channel, ES-88 is the derivative of `0.5[(z_i)^2+(r_i)^2]`. Using the exact ES-49--ES-50 dynamics,

```text
0.5 d/dt[(z_i)^2+(r_i)^2]
 = z_i[-kappa_i z_i]
   +r_i[-lambda_tr,i r_i+0.5 Delta_w,i z_i-dot(c_i)],

kappa_i=lambda_tr,i+w_{i,12}+w_{i,21}g_i,
Delta_w,i=w_{i,12}-w_{i,21}g_i.
```

Expanding gives

```text
 = -kappa_i z_i^2-lambda_tr,i r_i^2
   +0.5 r_i Delta_w,i z_i-r_i dot(c_i),
```

which is ES-88, with no ES-51 substitution.

### Bounds and positivity conditions

By PO-01, `kappa_i>=a_{z0,i}`, where

```text
a_{z0,i}^nu=lambda_tr,i^nu+underline(w)_i^nu.
```

By ES-46 and `0<=g_i<=1`, define

```text
bar(w_delta)_i^nu=bar(w)_{i,12}^nu+bar(w)_{i,21}^nu,
|Delta_w,i^nu|<=bar(w_delta)_i^nu.
```

For `eps_{r1,i}^nu>0` and `eps_{r2,i}^nu>0`,

```text
0.5|r_i^nu Delta_w,i^nu z_i^nu|
 <= 0.25 eps_{r1,i}^nu(r_i^nu)^2
    +[bar(w_delta)_i^nu]^2(z_i^nu)^2/(4eps_{r1,i}^nu),

|r_i^nu dot(c_i^nu)|
 <= 0.5 eps_{r2,i}^nu(r_i^nu)^2
    +|dot(c_i^nu)|^2/(2eps_{r2,i}^nu).
```

Therefore

```text
0.5 d/dt[(z_i^nu)^2+(r_i^nu)^2]
 <= -[a_{z0,i}^nu-[bar(w_delta)_i^nu]^2/(4eps_{r1,i}^nu)](z_i^nu)^2
    -[lambda_tr,i^nu-eps_{r1,i}^nu/4-eps_{r2,i}^nu/2](r_i^nu)^2
    +|dot(c_i^nu)|^2/(2eps_{r2,i}^nu).
```

Define

```text
a_z=min_{i,nu}{a_{z0,i}^nu-[bar(w_delta)_i^nu]^2/(4eps_{r1,i}^nu)},
a_r=min_{i,nu}{lambda_tr,i^nu-eps_{r1,i}^nu/4-eps_{r2,i}^nu/2},
d_c=max_{i,nu}1/(2eps_{r2,i}^nu).
```

Then

```text
dot(mathscr V_priv)
 <= -a_z||bold(z)||^2-a_r||bold(r)||^2
    +d_c||dot(bold(c))||^2.
```

The positive coefficients require

```text
eps_{r1,i}^nu > [bar(w_delta)_i^nu]^2/(4a_{z0,i}^nu),
eps_{r1,i}^nu/4+eps_{r2,i}^nu/2 < lambda_tr,i^nu.
```

There exist positive epsilons satisfying both inequalities only if

```text
[bar(w_delta)_i^nu]^2 < 16 lambda_tr,i^nu a_{z0,i}^nu
```

for every agent and channel, or the corresponding common-epsilon worst-case condition if epsilons are shared. Thus `a_z>0` is not guaranteed by ES-46 alone; it requires this private-weight/tracking-rate feasibility condition.

### Units and status

`eps_{r1}` and `eps_{r2}` have the squared units required by the selected Lyapunov metric; `a_z` and `a_r` have inverse-time units; `d_c` has the reciprocal units required to multiply `||dot(bold(c))||^2`. ES-87 adds voltage- and frequency-command residual squares, so its raw-unit interpretation also requires an explicit per-unit/common proof normalization.

PO-03 supplies a provisional finite command-rate bound on its compact tube. No ES-51 decay is used here, so this chain is not dependent on PO-02.

**PO-10 verdict: PROVED SUBJECT TO PO-03, PO-16, the private-weight feasibility inequality above, and the ES-87 normalization convention.**

## Local consistency audit

| Equation | Result | Discrepancy or dependency |
|---|---|---|
| ES-84 | PASS algebraically | Exact `+h zeta chi` and `-h chi zeta` cancel; the remaining signs match ES-66. |
| ES-86 | PASS algebraically | `h=1/[rho(1-sigma^2)]` multiplies graph, residual, and uncertainty terms. |
| ES-88 | PASS algebraically | The factor `0.5` appears only in the `r Delta_w z` cross term. |
| ES-94 | PASS as aggregate bound | It follows from one Young parameter applied to `D_i^V`; the separated three-epsilon version gives source-specific margins. |
| ES-98 | PASS as aggregate bound | It follows from `h_bar|zeta|D_i^omega` and one `eps_omega`; separated epsilons are equivalent. |
| ES-101 | PASS conditionally | Algebra is correct, but `a_z>0` and `a_r>0` require the explicit private-weight feasibility inequalities. |
| ES-83 and ES-87 | DIMENSION GAP | Raw notation mixes dimensionless transformed errors with voltage-rate or command-unit coordinates. No equation was changed; PO-08/PO-10 remain conditional on per-unit or an accepted proof-metric normalization. |

No sign, graph coefficient, residual scaling, or Young-factor discrepancy requires ES-number revision. The dimension gap is recorded as an unresolved proof/notation condition rather than silently ignored.

## PO-07 preparation ledger (no PO-07 proof)

| Input to future ES-102 closure | Current derived form | Required future use | Unknown constants still open |
|---|---|---|---|
| Voltage contribution | `-k_1^V||zeta^V||^2-[k_2^V-0.5eps_V2]||chi^V||^2 + sum_i[D_i^V]^2/(2eps_V2)` | Substitute PO-06 bounds for `e^V` and separate state terms | `bar e^V`, graph-induced Young allocations |
| Frequency contribution | `-sum_i[k_1^omega-0.5eps_omega](zeta_i^omega)^2 + sum_i(h_bar_i^omega)^2[D_i^omega]^2/(2eps_omega)` | Expand `D_i^omega` and use graph norms | `bar e^omega`, feasible `eps_omega` |
| Privacy contribution | `-a_z||bold(z)||^2-a_r||bold(r)||^2+d_c||dot(bold(c))||^2` | Insert command-rate bounds and compare against physical terms | Positive `a_z,a_r`, finite `d_c` under PO-16 |
| Remaining graph terms | ES-101a and PO-06: `||e||<=||B||||e_0||+||L_c||(||c||+||r||+0.5||z||)` | Distribute graph terms into physical, residual, and decomposition quadratic terms | `K_M^V,K_M^omega` and Young parameters |
| Residual terms | `D^V,D^omega` contain `|r|`; ES-51 is not assumed in Stage 2 | Decide later whether to use a proven decay envelope or exact residual state | PO-02 decay condition; PO-16 tube |
| Composite negative coefficients | Voltage: `k_1^V`, `k_2^V-0.5eps_V2`; frequency: `k_1^omega-0.5eps_omega`; privacy: `a_z,a_r` | Keep all margins positive after graph absorption | `a_cl` and graph-absorbed margins |
| Unknown disturbance constants | `bar R`, load-flow derivative bounds, funnel derivative bounds, actuator margins | Establish finite `d_R` and feasibility simultaneously | PO-07, PO-11, PO-13, PO-16 |

This table is a dependency inventory only. It does not assert ES-102 or begin PO-07.

## Stage-2 verdict

- PO-08: **PROVED SUBJECT TO PO-16 and Lyapunov-metric normalization**.
- PO-09: **PROVED SUBJECT TO PO-16**.
- PO-10: **PROVED SUBJECT TO PO-03, PO-16, explicit private-weight feasibility, and ES-87 normalization**.
- PO-07: **NOT STARTED; preparation ledger only**.
- Blueprint Reopen Required: **NO**.
