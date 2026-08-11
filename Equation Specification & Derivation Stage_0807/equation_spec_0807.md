# Equation Specification 0807

> Blueprint Version 2.2
> Privacy-Schedule Regularity Revision: 2026-08-11
> Predecessor: Blueprint Version 2.1, Privacy-Domain Revision
> Historical baseline: Blueprint Freeze Version 2.0, frozen 2026-08-07

## Status and authority

This document is the equation-level specification for the frozen architecture. It is not manuscript prose and does not contain final theorem proofs. Equation identifiers `ES-*` are specification identifiers only.

The retained architecture is continuous-time, uses a fixed connected undirected cyber graph, directly receives public neighbor states, and contains no observer, neighbor-state estimator, online function approximator, switching graph, residual floor, projection block, sampled-data theorem, or anti-windup state.

## NEW SYMBOL REQUIRING FREEZE UPDATE

The following symbols are unavoidable equation-level auxiliaries and have been added to `variables_0807.md` and `notation_rules_0807.md` without changing the architecture:

- plant parameters `tau_Pi`, `tau_Qi`, `k_Pi`, `k_Qi`, `k_Vi`, `P_i^d`, `Q_i^d`;
- local physical errors `e_{i,0}^V`, `e_{i,0}^omega`;
- normalized errors `sigma_i^V`, `sigma_i^omega`;
- funnel endpoints `rho_{i,0}^V`, `rho_{i,infty}^V`, `rho_{i,0}^omega`, `rho_{i,infty}^omega`;
- input-affine drifts `F_i^V`, `F_i^omega` and voltage backstepping error `chi_i^V`;
- decomposition differences `z_i^V`, `z_i^omega` and correction factors `g_i^V`, `g_i^omega`;
- public message vector `mathbf m_i`, command-tracking rates, uncertainty bounds, controller gains, and private-weight bounds.
- channel-consistent privacy-domain margins `eta_{z,i}^V`, `eta_{z,i}^omega`, `eta_{w,i}^V`, `eta_{w,i}^omega`, `eta_{gamma,i}^V`, and `eta_{gamma,i}^omega`, together with the common finite privacy seed interval `I_s=[0,T_s]`.

Channel-suppressed notation in Parts 4-8 and 13-14 is specification shorthand only. Every such equation represents two equations obtained by restoring superscript `V` or `omega`; the shorthand is not a third channel or a manuscript symbol family.

These are notation completions, not module additions. Derived proof constants introduced later are defined locally and are not independent controller parameters.

### Notation Freeze Delta

Equation review rechecked every item in the preceding list against `variables_0807.md` and `notation_rules_0807.md`.

| Symbol family | Dictionary/notation status | Equation-level role | Decision |
|---|---|---|---|
| `tau_Pi,tau_Qi,k_Pi,k_Qi,k_Vi,P_i^d,Q_i^d` | Defined physical/droop parameters | ES-4--ES-11, ES-74--ES-79 | Retained; no delta. |
| `e_{i,0}^{V,omega},sigma_i^{V,omega},rho_{i,0}^{V,omega},rho_{i,infty}^{V,omega}` | Defined physical-error and PPC families | ES-17, ES-22--ES-40 | Retained; no delta. |
| `F_i^{V,omega},alpha_i^{V,omega},chi_i^V,h_i^{V,omega}` | Defined input-affine/backstepping/derived-gain families | ES-8--ES-11, ES-26--ES-37, ES-62--ES-70 | Retained; no delta. |
| `p_i,q_i,r_i,z_i,g_i,lambda_{tr,i},w_{i,12},w_{i,21},bar r,gamma_priv` | Defined public/private/residual families | ES-41--ES-61, ES-80--ES-103 | Retained; no delta. |
| `D_i,eps_*,w_delta_bar_i,a_z,a_r,d_c,a_cl,d_R,d_priv,h_bar_i` | Defined as derived proof constants only | ES-90--ES-103 | Retained; no delta. |
| `P_L^V,P_L^priv,p_zeta^V,p_chi^V,p_c^V,p_c^omega,eps_V0` | Constant proof-metric blocks/entries and a Young constant | ES-83--ES-101 | Derived proof objects; no controller or communication role. |
| `S_i,S_i',A_i(S_i),O_adv,H_c` | Defined privacy-observation family | ES-16, ES-54--ES-61 | Retained; no delta. |

No controller-level symbol is missing from the frozen dictionaries, and no observer, estimator, approximator, projection, switching, sampled-data, residual-floor, or anti-windup symbol appears. The only notation delta is the proof-only block entries of the already reserved `P_L`; **Notation Freeze Delta: PROOF-METRIC ENTRIES ONLY.**

## Equation provenance and purpose ledger

| Equation group | Source status | Mathematical purpose |
|---|---|---|
| ES-1 to ES-11 | Adapted from IJSS | Fix the reduced droop plant, electrical coupling, state order, uncertainty location, and input signs. |
| ES-12 | Newly introduced interface | Make reconstruction the unique privacy-to-plant connection. |
| ES-13 | Simplified from both source graph models | Freeze a fixed connected undirected cyber graph. |
| ES-14 to ES-16 | Newly introduced | Define the exact public payload and adversary-visible history. |
| ES-17 to ES-21 | Adapted from IJSS distributed secondary errors | Separate physical regulation error from cyber coordination disagreement. |
| ES-21a | Newly introduced consistency condition | Make the plaintext algebraic coordinator well posed. |
| ES-22 to ES-40 | Corrected IJSS prescribed-performance construction | Replace the inconsistent source transformation with a nonsingular logarithmic transform and derive its inverse and deadline implication. |
| ES-41 to ES-43 | Adapted from Privacy | Define initial state splitting and a bounded public-private correction. |
| ES-44 to ES-53 | Newly adapted privacy wrapper | Track time-varying secondary commands, derive reconstruction residuals, and distinguish transparent from nontransparent operation. |
| ES-54 to ES-61 | Privacy principle plus new construction | Define exact observation equivalence and the alternative private realization. |
| ES-62 to ES-70 | Newly introduced coupling | Insert privacy residuals explicitly into voltage and frequency closed loops. |
| ES-71 to ES-79 | Adapted IJSS droop relation plus new privacy analysis | Derive exact and practical active-power sharing. |
| ES-80 to ES-103 | Newly introduced analysis specification | Define the augmented state, Lyapunov candidates, cross-term bounds, and comparison inequality. |

## 1. Physical microgrid model

### 1.1 States and reduced droop dynamics

For DG `i`, define the retained channel states by

```text
x_i^V = [x_{i,1}^V, x_{i,2}^V]^T = [V_i, dot(V_i)]^T              (ES-1)
x_i^omega = omega_i                                                (ES-2)
dot(delta_i) = omega_i                                             (ES-3)
```

The final reduced droop dynamics are

```text
tau_Pi dot(omega_i)
  = -(omega_i - omega_ref)
    - k_Pi (P_i - P_i^d)
    - u_i^omega
    + tau_Pi R_i^omega.                                            (ES-4)

tau_Qi k_Vi ddot(V_i)
  = -(tau_Qi + k_Vi) dot(V_i)
    - (V_i - V_ref)
    - k_Qi (Q_i - Q_i^d)
    - u_i^V
    + tau_Qi k_Vi R_i^V.                                           (ES-5)
```

`R_i^omega` has angular-acceleration units and `R_i^V` has voltage-acceleration units. They collect only bounded physical/model uncertainty. They do not contain privacy residuals.

Source status:

| Object | Status | Adaptation |
|---|---|---|
| Reduced frequency droop dynamics | Adapted from IJSS equation (3) | Uses `omega_ref`, separates `R_i^omega`, and fixes the secondary-input sign. |
| Reduced voltage droop dynamics | Adapted from IJSS equation (3) | Uses `V_ref`, separates `R_i^V`, and fixes the channel state order. |
| Phase equation | Standard physical closure | Makes phase differences in power flow well defined. |

Filtered powers `P_i^m` and `Q_i^m` are implementation measurements that motivate `tau_Pi` and `tau_Qi`; they are not additional core closed-loop states after the reduced model (ES-4)-(ES-5) is adopted.

### 1.2 Electrical power flow

The core uses the lossless inductive network specialization retained by IJSS. For `delta_ik = delta_i - delta_k`,

```text
P_i = P_i^L(V_i)
      + sum_{k in N_i^e} V_i V_k |B_ik| sin(delta_ik),              (ES-6)

Q_i = Q_i^L(V_i)
      + V_i^2 sum_{k in N_i^e} |B_ik|
      - sum_{k in N_i^e} V_i V_k |B_ik| cos(delta_ik).              (ES-7)
```

The load functions `P_i^L(V_i)` and `Q_i^L(V_i)` are continuously differentiable and bounded on `Delta`. Conductance `G_ik` is set to zero in the core model. A lossy-network extension would change (ES-6)-(ES-7) and is not silently included in `R_i`.

`N_i^e` is the electrical neighbor set. It is unrelated to `N_i^c` unless a particular experiment happens to choose identical edge sets.

### 1.3 Input-affine form and unique plant interface

Define the known channel drifts

```text
F_i^omega
  = -[(omega_i - omega_ref) + k_Pi(P_i - P_i^d)] / tau_Pi,         (ES-8)

F_i^V
  = -[(tau_Qi + k_Vi) x_{i,2}^V
      + (x_{i,1}^V - V_ref)
      + k_Qi(Q_i - Q_i^d)] / (tau_Qi k_Vi).                        (ES-9)
```

Then

```text
dot(x_{i,1}^V) = x_{i,2}^V,
dot(x_{i,2}^V) = F_i^V - u_i^V/(tau_Qi k_Vi) + R_i^V,              (ES-10)

dot(omega_i) = F_i^omega - u_i^omega/tau_Pi + R_i^omega.           (ES-11)
```

The privacy-aware controller reaches the plant only through

```text
u_i^V = hat(c)_i^V,
u_i^omega = hat(c)_i^omega.                                        (ES-12)
```

No public/private state enters (ES-10)-(ES-11) through any other path.

## 2. Cyber communication model

### 2.1 Fixed graph

```text
G_c = (mathcal V, mathcal E_c),
a_ij = a_ji > 0 when (i,j) is in mathcal E_c,
a_ij = 0 otherwise,
L_c = diag(sum_j a_ij) - [a_ij].                                   (ES-13)
```

`G_c` is fixed, connected, and undirected. Reference access is encoded by `b_i >= 0`, with at least one `b_i > 0` in each regulated channel. The pinned matrix `L_c + diag(b_i)` must be positive definite.

### 2.2 Public payload

The regular message sent by DG `i` is exactly

```text
mathbf m_i(t) = [p_i^V(t), p_i^omega(t)]^T.                         (ES-14)
```

No regular message contains `V_i`, `omega_i`, `P_i`, `Q_i`, `c_i`, `hat(c)_i`, `q_i`, `r_i`, private weights, physical uncertainty, or controller memory.

### 2.3 Public and adversary histories

The message history available at DG `i` is

```text
{mathbf m_j(s): j in N_i^c, 0 <= s <= t}.                          (ES-15)
```

The complete passive-eavesdropper history is

```text
O_adv[0,t]
 = {mathbf m_j(s): j in mathcal V, 0 <= s <= t}
   union H_c[0,t]
   union {G_c, a_ij, b_i, V_ref, omega_ref,
          rho_i^V(.), rho_i^omega(.), T_V, T_omega,
          all controller parameters declared public}.              (ES-16)
```

Physical sensor histories and private local memory are not elements of (ES-16).

## 3. Nominal plaintext secondary controller

### 3.1 Physical and distributed errors

The local physical errors are

```text
e_{i,0}^V = V_i - V_ref,
e_{i,0}^omega = omega_i - omega_ref.                                (ES-17)
```

In the plaintext baseline, `p_i^V = c_i^V` and `p_i^omega = c_i^omega`. Its distributed/pinning errors are

```text
e_i^V
 = b_i e_{i,0}^V
   + sum_{j in N_i^c} a_ij(c_i^V - c_j^V),                         (ES-18)

e_i^omega
 = b_i e_{i,0}^omega
   + sum_{j in N_i^c} a_ij(c_i^omega - c_j^omega).                 (ES-19)
```

After privacy is enabled, only the coordination-difference terms change:

```text
e_i^V
 = b_i e_{i,0}^V
   + sum_{j in N_i^c} a_ij(p_i^V - p_j^V),                         (ES-20)

e_i^omega
 = b_i e_{i,0}^omega
   + sum_{j in N_i^c} a_ij(p_i^omega - p_j^omega).                 (ES-21)
```

Equations (ES-18)-(ES-19) define the counterfactual plaintext baseline. Equations (ES-20)-(ES-21) define the implementable privacy-aware coordination errors.

Because the plaintext error contains `c_i-c_j`, the algebraic command solve is part of the nominal baseline. The scalar coordination gains must satisfy

```text
det(I_N - k_c^V L_c) != 0,
det(I_N - k_c^omega L_c) != 0.                                     (ES-21a)
```

For the privacy-enabled controller, `p` is a dynamic state and (ES-20)-(ES-21) are evaluated directly from received public values.

### 3.2 Funnel schedules

For channel deadline `T` and endpoints `rho_0 > rho_infty > 0`, define

```text
rho(t) = rho_infty + (rho_0 - rho_infty) h(t/T),                    (ES-22)

h(s) = 1 - 10s^3 + 15s^4 - 6s^5,  0 <= s <= 1,
h(s) = 0,                      s > 1.                               (ES-23)
```

Use `(rho_{i,0}^V, rho_{i,infty}^V, T_V)` for voltage and `(rho_{i,0}^omega, rho_{i,infty}^omega, T_omega)` for frequency. This quintic schedule is positive, nonincreasing, twice continuously differentiable at the deadline, and constant afterward.

### 3.3 Normalization and transformation

```text
sigma_i^V = e_{i,0}^V / rho_i^V(t),
sigma_i^omega = e_{i,0}^omega / rho_i^omega(t),                    (ES-24)

zeta_i^V = 0.5 ln[(1 + sigma_i^V)/(1 - sigma_i^V)],
zeta_i^omega = 0.5 ln[(1 + sigma_i^omega)/(1 - sigma_i^omega)].    (ES-25)
```

This corrected logarithmic transformation replaces the internally inconsistent IJSS scalar transformation. Its complete verification is in Part 4.

### 3.4 Nominal voltage command

From (ES-24)-(ES-25), define the local funnel feedforward velocity. This corrected one-step realization avoids differentiating a neighbor's private decomposition state.

```text
alpha_i^V
 = sigma_i^V dot(rho_i^V)
   - k_1^V rho_i^V[1-(sigma_i^V)^2]zeta_i^V,
h_i^V
 = 1/[rho_i^V(1-(sigma_i^V)^2)],                                  (ES-26)

chi_i^V = x_{i,2}^V - alpha_i^V,
dot(alpha_i^V)
 = dot(sigma_i^V)dot(rho_i^V) + sigma_i^V ddot(rho_i^V)
   - k_1^V{dot(rho_i^V)[1-(sigma_i^V)^2]zeta_i^V
            -2rho_i^V sigma_i^V dot(sigma_i^V)zeta_i^V
            +rho_i^V[1-(sigma_i^V)^2]dot(zeta_i^V)},
dot(sigma_i^V) = [chi_i^V-k_1^V rho_i^V(1-(sigma_i^V)^2)zeta_i^V]
                 /rho_i^V.                                        (ES-27)
```

The ideal nominal voltage coordination command is

```text
c_i^V
 = tau_Qi k_Vi [F_i^V - dot(alpha_i^V) + k_2^V chi_i^V
                 + h_i^V zeta_i^V]
   + k_c^V e_i^V.                                                   (ES-28)
```

With plaintext input `u_i^V = c_i^V`, substitution into (ES-10) gives

```text
dot(chi_i^V)
 = -k_2^V chi_i^V
   - h_i^V zeta_i^V
   - k_c^V e_i^V/(tau_Qi k_Vi)
   + R_i^V.                                                         (ES-29)
```

### 3.5 Nominal frequency command

Define the desired frequency-error derivative

```text
alpha_i^omega
 = sigma_i^omega dot(rho_i^omega)
   - k_1^omega rho_i^omega [1 - (sigma_i^omega)^2] zeta_i^omega.   (ES-30)
```

The ideal nominal frequency coordination command is

```text
c_i^omega
 = tau_Pi [F_i^omega - alpha_i^omega]
   + k_c^omega e_i^omega.                                          (ES-31)
```

With plaintext input `u_i^omega = c_i^omega`,

```text
dot(e_{i,0}^omega)
 = alpha_i^omega
   - k_c^omega e_i^omega/tau_Pi
   + R_i^omega.                                                     (ES-32)
```

The commands (ES-28) and (ES-31) are the protected ideal virtual coordination signals. “Ideal” means before privacy reconstruction; it does not mean that their privacy-enabled trajectories equal the counterfactual plaintext trajectories.

## 4. Prescribed-performance transformation verification

For either channel, omit only the channel superscript in this subsection.

### 4.1 Complete derivative

From `sigma=e_0/rho`,

```text
dot(sigma) = [rho dot(e_0) - e_0 dot(rho)]/rho^2
           = [dot(e_0) - sigma dot(rho)]/rho.                       (ES-33)
```

From `zeta=atanh(sigma)`,

```text
dot(zeta)
 = dot(sigma)/(1 - sigma^2)
 = [dot(e_0) - sigma dot(rho)]/[rho(1 - sigma^2)].                  (ES-34)
```

The inverse is

```text
sigma = tanh(zeta),
e_0 = rho tanh(zeta).                                               (ES-35)
```

For voltage, using (ES-26)-(ES-27),

```text
dot(zeta_i^V)
 = -k_1^V zeta_i^V
   + chi_i^V/[rho_i^V(1 - (sigma_i^V)^2)].                         (ES-36)
```

For nominal frequency, using (ES-30)-(ES-32),

```text
dot(zeta_i^omega)
 = -k_1^omega zeta_i^omega
   + [-k_c^omega e_i^omega/tau_Pi + R_i^omega]
     /[rho_i^omega(1 - (sigma_i^omega)^2)].                        (ES-37)
```

### 4.2 Nonsingularity and performance implication

Required initial feasibility is

```text
|e_{i,0}^V(0)| < rho_{i,0}^V,
|e_{i,0}^omega(0)| < rho_{i,0}^omega.                              (ES-38)
```

If `zeta_i` is bounded on every finite interval, then `|tanh(zeta_i)|<1`; therefore

```text
|e_{i,0}^V(t)| < rho_i^V(t),
|e_{i,0}^omega(t)| < rho_i^omega(t),    for all t >= 0.            (ES-39)
```

At and after the deadlines,

```text
|e_{i,0}^V(t)| < rho_{i,infty}^V,          t >= T_V,
|e_{i,0}^omega(t)| < rho_{i,infty}^omega,  t >= T_omega.           (ES-40)
```

Thus the claim is practical prescribed-time recovery, with final tolerances selected no smaller than the corresponding post-deadline funnel radii.

### Transformation Verification

| Check | Result |
|---|---|
| Dimensions | `sigma` and `zeta` are dimensionless; `rho` has the same unit as `e_0`. |
| Sign | `atanh` is odd, so transformed and physical errors have the same sign. |
| Denominator | Positive whenever `rho>0` and `|sigma|<1`. |
| Initial feasibility | Explicitly required by (ES-38). |
| Deadline behavior | `dot(rho)=ddot(rho)=0` at and after the deadline. |
| Interpretation | Bounded `zeta` implies funnel invariance and post-deadline practical tolerance, not exact zero convergence. |

## 5. Privacy-preserving virtual-state mechanism

### 5.0 Blueprint Version 2.2 schedule-regular privacy domain

The ES formulas in this section are unchanged from Blueprint Versions 2.0 and 2.1. Version 2.2 adds only the finite-seed schedule regularity needed for the alternative-realization proof.

For every agent/channel pair affected through the frozen physical/electrical coupling by a candidate alternative construction, Assumption 2 requires

```text
|z_j^nu(0)| >= eta_{z,j}^nu > 0,

underline(w)_j^nu + eta_{w,j}^nu
 <= w_{j,12}^nu(t), w_{j,21}^nu(t)
 <= bar(w)_j^nu - eta_{w,j}^nu,

gamma_priv,j^nu(t) >= eta_{gamma,j}^nu > 0,
                         t in I_s=[0,T_s]
```

with `nu in {V,omega}`, `T_s>0`, and `2eta_{w,j}^nu < bar(w)_j^nu-underline(w)_j^nu`. The margins carry the units of their corresponding channel quantities. Unless PO-04 proves that a smaller affected subset is closed, the condition is applied network-wide along the coupled model. The new schedule condition is equivalent to bounded `1/gamma_priv,j^nu` on `I_s`; pointwise positivity without a uniform local lower bound is insufficient.

For affected pairs, the privacy singular set relevant to ES-60--ES-61 is the union of `z_j^nu=0` and `gamma_priv,j^nu=0`. Version 2.2 separates the prescribed schedule from the second stratum on `I_s`. The exact ES-49 nominal solution and the Version 2.1 initial split margin provide nominal finite-interval separation from the first stratum; PO-04 must still establish the alternative separation needed by its construction.

These inequalities are nominal design-domain data. They do not posit `S_i'`, `q_i'`, `w_i'`, `p_i'=p_i`, a compatible alternative trajectory, or a positive perturbation radius. The local privacy claim stops at the earliest of `T_s` and the first exit from the regular privacy/physical domain. This is a stopping boundary, not a claim that the domain is invariant. PO-04 must construct the alternative and prove that some nonzero perturbation remains admissible before that stop. PO-05 remains downstream and must validate the divisions used by ES-60--ES-61.

### 5.1 Initialization and ownership

For both channels, initialize

```text
p_i^V(0) + q_i^V(0) = 2 c_i^V(0),
p_i^omega(0) + q_i^omega(0) = 2 c_i^omega(0).                      (ES-41)
```

Only `p_i^V` and `p_i^omega` are transmitted. The `q` states and all `w` parameters remain private.

Define the private substate differences

```text
z_i^V = p_i^V - q_i^V,
z_i^omega = p_i^omega - q_i^omega.                                 (ES-42)
```

### 5.2 Bounded correction factors

For each channel,

```text
g_i(t) = 1,                                      |z_i(t)| <= gamma_priv,i(t),
g_i(t) = gamma_priv,i(t)/|z_i(t)|,               otherwise.        (ES-43)
```

Hence `|g_i z_i| <= gamma_priv,i(t)`. The channel superscript on `g_i`, `z_i`, and `gamma_priv,i` is restored in all channel equations.

### 5.3 Final decomposition dynamics

The command-tracking adaptation of the Privacy mechanism is

```text
dot(p_i^V)
 = lambda_tr,i^V(c_i^V - p_i^V) - w_{i,21}^V g_i^V z_i^V,

dot(q_i^V)
 = lambda_tr,i^V(c_i^V - q_i^V) + w_{i,12}^V z_i^V,               (ES-44)

dot(p_i^omega)
 = lambda_tr,i^omega(c_i^omega - p_i^omega)
   - w_{i,21}^omega g_i^omega z_i^omega,

dot(q_i^omega)
 = lambda_tr,i^omega(c_i^omega - q_i^omega)
   + w_{i,12}^omega z_i^omega.                                    (ES-45)
```

The new terms `c_i-p_i` and `c_i-q_i` are necessary because the protected object is a time-varying secondary command rather than the source paper's plant state. They make (ES-44)-(ES-45) explicit command trackers.

The private weights obey

```text
underline(w)_i^V <= w_{i,12}^V(t), w_{i,21}^V(t) <= bar(w)_i^V,
underline(w)_i^omega <= w_{i,12}^omega(t), w_{i,21}^omega(t)
                      <= bar(w)_i^omega.                            (ES-46)
```

### 5.4 Reconstruction and exact residual

```text
hat(c)_i^V = [p_i^V + q_i^V]/2,
hat(c)_i^omega = [p_i^omega + q_i^omega]/2,                        (ES-47)

r_i^V = hat(c)_i^V - c_i^V,
r_i^omega = hat(c)_i^omega - c_i^omega,

p_i = c_i + r_i + 0.5 z_i,
q_i = c_i + r_i - 0.5 z_i.                                        (ES-48)
```

From (ES-44)-(ES-45),

```text
dot(z_i)
 = -[lambda_tr,i + w_{i,12} + w_{i,21} g_i] z_i,                  (ES-49)

dot(r_i)
 = -lambda_tr,i r_i
   + 0.5 [w_{i,12} - w_{i,21} g_i] z_i
   - dot(c_i).                                                      (ES-50)
```

Because (ES-41) gives `r_i(0)=0`, the positive-weight decay claim for `z_i` is assigned to **PO-01**. **PO-02A** uses the finite command-rate bound from **PO-03** to obtain only a local residual convolution bound. **PO-02B**, after the forward closed-loop results, determines when (ES-50) implies `r_i -> 0`. The residual is therefore a consequence of command tracking and unequal internal coupling; it is not mathematically required for privacy.

The frozen physical analysis requires the verified envelopes

```text
|r_i^V(t)| <= bar(r)^V gamma_priv,i^V(t),
|r_i^omega(t)| <= bar(r)^omega gamma_priv,i^omega(t),
gamma_priv,i^V(t) -> 0,
gamma_priv,i^omega(t) -> 0.                                       (ES-51)
```

**Proof Obligation PO-02A**, using the explicit command-rate bound from **PO-03**, establishes the finite local convolution estimate from (ES-49)--(ES-50). **PO-02B** is the separate proof target for the decaying envelope (ES-51); until it is discharged, (ES-51) is not available as a theorem consequence and must not be inferred from bounded `dot(c)` alone.

**Derivation-stage condition (2026-08-07):** a merely uniform bound on `dot(c_i)` yields only an ultimate bound for `r_i`; ES-51 additionally requires a known decaying envelope for `dot(c_i)`, either established by later closed-loop analysis or stated as an explicit technical assumption. This condition does not add a controller module or permit a residual floor.

## 6. Transparent-wrapper condition

### Case A: transparent wrapper

Transparency requires `hat(c)_i(t)=c_i(t)`, equivalently `r_i(t)=0`, for all time. With `r_i(0)=0`, (ES-50) shows that this occurs if and only if

```text
[w_{i,12}(t) - w_{i,21}(t) g_i(t)] z_i(t)
  = 2 dot(c_i(t)),    for every t.                                 (ES-52)
```

This is an exact algebraic condition; the tracking rate cancels because `r_i=0`. The simpler equality `w_{i,12}=w_{i,21}g_i` is sufficient only when `dot(c_i)=0`; it does not make a changing command transparent.

Condition (ES-52) couples private weights to the derivative of the nominal command. It can violate the fixed admissible weight bounds when `z_i` is small or crosses zero. It also removes part of the free private-parameter set used in the indistinguishability construction.

### Case B: nontransparent wrapper

Under the frozen architecture, the private weights are independently admissible and (ES-52) is not imposed. Therefore

```text
hat(c)_i^V = c_i^V + r_i^V,
hat(c)_i^omega = c_i^omega + r_i^omega,                             (ES-53)
```

with residual dynamics (ES-50) and envelope (ES-51).

### Equation-level decision

Blueprint Versions 2.0--2.2 all implement Case B. Versions 2.1--2.2 change only the privacy-admissible design domain. Case A is algebraically possible only under the extra constraint (ES-52), which is not part of the private-parameter contract and cannot be assumed globally under bounded weights. This conclusion is based on (ES-50), not on intuition.

## 7. Privacy observation map and target

The protected quantity is

```text
S_i = [c_i^V(0), c_i^omega(0)]^T.                                  (ES-54)
```

An alternative admissible value is

```text
S_i' != S_i.                                                        (ES-55)
```

Two complete private realizations are observation-equivalent on `[0,t]` when

```text
O_adv[0,t; S_i, q_i(0), w_i(.)]
 = O_adv[0,t; S_i', q_i'(0), w_i'(.)].                             (ES-56)
```

The exact privacy target is

```text
there exist S_i' != S_i and admissible q_i'(0), w_i'(.)
such that (ES-56) holds for every t >= 0.                           (ES-57)
```

This is deterministic observation equivalence. It contains no probability or differential-privacy parameter.

## 8. Algebraic indistinguishability construction

Fix one admissible realization. Choose a different protected initialization `S_i'` sufficiently close to `S_i` so that the private bounds below remain feasible. Set

```text
p_i'(0) = p_i(0),
q_i'(0) = 2 S_i' - p_i(0).                                        (ES-58)
```

This gives the same initial public message and preserves `r_i'(0)=0`.

To maintain `p_i'(t)=p_i(t)`, comparison of the two public equations in (ES-44)-(ES-45) requires

```text
w_{i,21}'(t) g_i'(t) z_i'(t)
 = lambda_tr,i [c_i'(t) - c_i(t)]
   + w_{i,21}(t) g_i(t) z_i(t).                                   (ES-59)
```

Whenever `g_i'(t) z_i'(t) != 0`, choose

```text
w_{i,21}'(t)
 = [lambda_tr,i(c_i'(t) - c_i(t))
    + w_{i,21}(t)g_i(t)z_i(t)]
   /[g_i'(t)z_i'(t)].                                              (ES-60)
```

Choose an admissible differentiable private path `q_i'(t)` satisfying (ES-58). Its second private weight is then forced by

```text
w_{i,12}'(t)
 = [dot(q_i'(t))
    - lambda_tr,i(c_i'(t)-q_i'(t))]/z_i'(t),                      (ES-61)
```

whenever `z_i'(t) != 0`.

The admissible alternative set `A_i(S_i)` consists only of alternatives constructed from a nominal realization in the Version 2.2 schedule-regular privacy domain and for which:

1. the denominators in (ES-60)-(ES-61) do not vanish before their numerators;
2. the resulting weights satisfy (ES-46);
3. `p_i'=p_i` is compatible with the same public neighbor histories;
4. the alternative plant/controller trajectory remains in `Delta` and its input remains in `U_i`;
5. private states remain bounded;
6. the complete public metadata in (ES-16) is unchanged.

This construction adapts the Privacy paper's “same public state, adjusted private weights” idea. Equations (ES-59)-(ES-61), command-tracking terms, plant compatibility, and the admissible-set restrictions are new.

The construction targets local/existence-based ambiguity before the Version 2.2 stopping boundary, not ambiguity for every arbitrary `S_i'`, every initialization in the historical Version 2.0 bounded class, or after the seed interval/domain exit. **PO-04** must establish nonemptiness of `A_i(S_i)` beyond the nominal realization and quantify a nonzero perturbation radius from the declared margins; **PO-05** remains downstream and establishes the denominator conditions used by (ES-60)--(ES-61).

## 9. Voltage closed-loop equations

### 9.1 Privacy-aware command insertion

From (ES-12), (ES-28), and (ES-53),

```text
u_i^V
 = c_i^V + r_i^V
 = tau_Qi k_Vi [F_i^V - dot(alpha_i^V) + k_2^V chi_i^V
                 + h_i^V zeta_i^V]
   + k_c^V e_i^V
   + r_i^V.                                                         (ES-62)
```

Substituting (ES-62) into the plant gives

```text
dot(x_{i,2}^V)
 = dot(alpha_i^V)
   - k_2^V chi_i^V
   - h_i^V zeta_i^V
   - k_c^V e_i^V/(tau_Qi k_Vi)
   - r_i^V/(tau_Qi k_Vi)
   + R_i^V.                                                         (ES-63)
```

Therefore

```text
dot(chi_i^V)
 = -k_2^V chi_i^V
   - h_i^V zeta_i^V
   - k_c^V e_i^V/(tau_Qi k_Vi)
   - r_i^V/(tau_Qi k_Vi)
   + R_i^V.                                                         (ES-64)
```

The complete voltage transformed-error subsystem is

```text
dot(zeta_i^V)
 = -k_1^V zeta_i^V
   + chi_i^V/[rho_i^V(1 - (sigma_i^V)^2)],                         (ES-65)

dot(chi_i^V)
 = -k_2^V chi_i^V
   - h_i^V zeta_i^V
   - k_c^V e_i^V/(tau_Qi k_Vi)
   - r_i^V/(tau_Qi k_Vi)
   + R_i^V,                                                         (ES-66)
```

coupled to (ES-20), (ES-44), (ES-49), and (ES-50). The privacy term is explicit; it is not folded into `R_i^V`.

### 9.2 Voltage residual bound entering the plant

Using (ES-51),

```text
|r_i^V/(tau_Qi k_Vi)|
 <= bar(r)^V gamma_priv,i^V(t)/(tau_Qi k_Vi).                      (ES-67)
```

This is the exact residual allocation that must fit the voltage Lyapunov/funnel budget.

## 10. Frequency closed-loop equations

### 10.1 Privacy-aware command insertion

From (ES-12), (ES-31), and (ES-53),

```text
u_i^omega
 = c_i^omega + r_i^omega
 = tau_Pi [F_i^omega - alpha_i^omega]
   + k_c^omega e_i^omega
   + r_i^omega.                                                     (ES-68)
```

Substitution into (ES-11) gives

```text
dot(e_{i,0}^omega)
 = alpha_i^omega
   - k_c^omega e_i^omega/tau_Pi
   - r_i^omega/tau_Pi
   + R_i^omega.                                                     (ES-69)
```

Hence the complete transformed frequency dynamics are

```text
dot(zeta_i^omega)
 = -k_1^omega zeta_i^omega
   + [-k_c^omega e_i^omega/tau_Pi
      - r_i^omega/tau_Pi
      + R_i^omega]
     /[rho_i^omega(1 - (sigma_i^omega)^2)].                        (ES-70)
```

The frequency privacy term is again explicit.

### 10.2 Equilibrium compatibility

At a synchronized regulated equilibrium, require

```text
omega_i^* = omega_ref,
dot(omega_i^*) = 0,
z_i^omega* = 0,
r_i^omega* = 0,
p_i^omega* = q_i^omega* = c_i^omega*.                              (ES-71)
```

If the pinned coordination condition yields

```text
L_c p^omega* = 0,                                                   (ES-72)
```

connectedness of `G_c` gives

```text
p_1^omega* = ... = p_N^omega* = c_common^omega.                    (ES-73)
```

Because of (ES-71), (ES-73) implies common steady-state secondary frequency correction without a projection operator.

## 11. Active-power sharing derivation

At equilibrium, (ES-4) becomes

```text
0
 = -(omega_i^* - omega_ref)
   - k_Pi(P_i^* - P_i^d)
   - u_i^omega*
   + tau_Pi R_i^omega*.                                            (ES-74)
```

### 11.1 Ideal case

Under `omega_i^*=omega_ref`, `R_i^omega*=0`, and `u_i^omega*=c_common^omega`,

```text
k_Pi(P_i^* - P_i^d) = -c_common^omega.                             (ES-75)
```

For any DGs `i,j`,

```text
k_Pi(P_i^* - P_i^d) = k_Pj(P_j^* - P_j^d),                        (ES-76)

(P_i^* - P_i^d)/(P_j^* - P_j^d) = k_Pj/k_Pi.                      (ES-77)
```

Thus the active-power increments share inversely with the droop coefficients. If droop coefficients are chosen inversely proportional to DG ratings, normalized active powers are equal.

### 11.2 Practical case

Rearranging (ES-4) at any time gives

```text
k_Pi(P_i - P_i^d)
 = -u_i^omega
   - (omega_i - omega_ref)
   - tau_Pi dot(omega_i)
   + tau_Pi R_i^omega.                                             (ES-78)
```

Subtracting the expressions for `i` and `j`, using `u=c+r`, and applying the triangle inequality yields

```text
|k_Pi(P_i-P_i^d) - k_Pj(P_j-P_j^d)|
 <= |c_i^omega-c_j^omega|
    + |r_i^omega| + |r_j^omega|
    + |omega_i-omega_ref| + |omega_j-omega_ref|
    + tau_Pi|dot(omega_i)| + tau_Pj|dot(omega_j)|
    + tau_Pi bar(R)_i^omega + tau_Pj bar(R)_j^omega.               (ES-79)
```

Exact sharing follows only when every term on the right tends to zero. Otherwise (ES-79) is the required residual-dependent sharing bound.

## 12. Augmented closed-loop system

Define the network stacks by DG order:

```text
bold(zeta)^V = col_i(zeta_i^V),       bold(chi)^V = col_i(chi_i^V),
bold(zeta)^omega = col_i(zeta_i^omega),
bold(p)^V = col_i(p_i^V),             bold(q)^V = col_i(q_i^V),
bold(p)^omega = col_i(p_i^omega),     bold(q)^omega = col_i(q_i^omega),
bold(r)^V = col_i(r_i^V),             bold(r)^omega = col_i(r_i^omega).  (ES-80)
```

The augmented state is

```text
X_cl
 = col_i(e_{i,0}^V, zeta_i^V, chi_i^V,
         e_{i,0}^omega, zeta_i^omega,
         p_i^V, q_i^V, p_i^omega, q_i^omega,
         r_i^V, r_i^omega).                                        (ES-81)
```

Its dynamics are not written as one undefined disturbance map. They are the ordered column of the already defined component equations:

```text
dot(X_cl)
 = col_i(
     ES-35/ES-65 voltage error relation,
     ES-65,
     ES-66,
     ES-35/ES-70 frequency error relation,
     ES-70,
     ES-44 voltage public/private equations,
     ES-45 frequency public/private equations,
     ES-50 voltage residual equation,
     ES-50 frequency residual equation
   ),                                                              (ES-82)
```

with `P_i,Q_i` supplied by (ES-6)-(ES-7), distributed errors by (ES-20)-(ES-21), and commands by (ES-28),(ES-31). Each term in (ES-82) therefore has a unique source equation.

**Proof-level coordinate clarification:** ES-81 is an augmented analysis/bookkeeping vector. The independent ODE coordinates are the physical coordinates `(V_i,dot(V_i),omega_i,delta_i)` and privacy tracker states `(p_i^V,q_i^V,p_i^omega,q_i^omega)`. The entries `e_{i,0}`, `zeta_i`, `chi_i`, and `r_i` in ES-81 are reconstructed algebraically from those coordinates and time. ES-82 is therefore interpreted as the consistency derivative of the augmented image, not as an unconstrained Euclidean ODE with all ES-81 entries independent. This clarification changes no equation or identifier.

## 13. Lyapunov structure

### Lyapunov Metric Convention

The physical/controller variables retain their original units. The Lyapunov proof uses constant positive-definite diagonal metric blocks, represented as instances of the reserved proof matrix `P_L`:

```text
P_L^V = diag(p_zeta^V I_N, p_chi^V I_N),
P_L^priv = diag(p_c^V I_{2N}, p_c^omega I_{2N}),
```

where every diagonal entry is constant and strictly positive, and its unit is selected so each quadratic block is dimensionless in the proof metric. These are proof weights, not controller gains, adaptive parameters, states, or communication variables. `mathscr V_omega` is already a quadratic form in dimensionless transformed errors and uses unit weight. The metric weights are chosen once on the declared operating region and are not time-varying.

Equivalently, `p_zeta^V` has the common proof-energy unit for a dimensionless transformed error, `p_chi^V` has that unit divided by the squared voltage-rate unit, `p_c^V` has that unit divided by the squared voltage-command unit, and `p_c^omega` has that unit divided by the squared frequency-command unit. The metric is therefore a unit-bearing proof object, while all controller equations retain their original physical units.

### 13.1 Voltage candidate

```text
mathscr V_V
 = 0.5 sum_i [p_zeta^V (zeta_i^V)^2 + p_chi^V (chi_i^V)^2].         (ES-83)
```

It is positive definite in the voltage transformed and backstepping errors. Its derivative, before bounding, is

```text
dot(mathscr V_V)
 = sum_i {
     -p_zeta^V k_1^V (zeta_i^V)^2
     -p_chi^V k_2^V (chi_i^V)^2
     +(p_zeta^V-p_chi^V)h_i^V zeta_i^V chi_i^V
     -p_chi^V k_c^V chi_i^V e_i^V/(tau_Qi k_Vi)
     -p_chi^V chi_i^V r_i^V/(tau_Qi k_Vi)
     +p_chi^V chi_i^V R_i^V
   }.                                                              (ES-84)
```

### 13.2 Frequency candidate

```text
mathscr V_omega
 = 0.5 sum_i (zeta_i^omega)^2.                                     (ES-85)
```

Its exact derivative is

```text
dot(mathscr V_omega)
 = sum_i {
     -k_1^omega (zeta_i^omega)^2
     + zeta_i^omega[-k_c^omega e_i^omega/tau_Pi
                    -r_i^omega/tau_Pi
                    +R_i^omega]
       /[rho_i^omega(1-(sigma_i^omega)^2)]
   }.                                                              (ES-86)
```

### 13.3 Privacy candidate

```text
mathscr V_priv
 = 0.5 sum_i [p_c^V (z_i^V)^2 + p_c^V (r_i^V)^2
              + p_c^omega (z_i^omega)^2 + p_c^omega (r_i^omega)^2]. (ES-87)
```

For either channel, its component derivative is

```text
 0.5 d/dt[p_c^nu z_i^2+p_c^nu r_i^2]
 = -p_c^nu[lambda_tr,i+w_{i,12}+w_{i,21}g_i]z_i^2
   -p_c^nu lambda_tr,i r_i^2
   + 0.5 p_c^nu r_i[w_{i,12}-w_{i,21}g_i]z_i
   -p_c^nu r_i dot(c_i).                                            (ES-88)
```

The `z` term is strictly dissipative. The residual term requires a bound on `dot(c_i)` derived from the nominal controller and the compact operating region.

### 13.4 Composite candidate

```text
mathscr V_cl = mathscr V_V + mathscr V_omega + mathscr V_priv.      (ES-89)
```

No deleted module contributes a Lyapunov term.

## 14. Intended inequality chains

### 14.1 Transformation-gain bounds

On any invariant sublevel set with `|sigma_i| <= sigma_bar_i < 1`, define the derived constant

```text
h_i = 1/[rho_i(t)(1-sigma_i(t)^2)],
0 < h_i(t) <= h_bar_i.                                             (ES-90)
```

Then

```text
1/[rho_i(t)(1-sigma_i(t)^2)] <= h_bar_i.                           (ES-91)
```

`h_bar_i` is a proof constant, not a controller state.

### 14.2 Voltage chain

Under the repaired positive diagonal metric, the transformed-error/control terms produce the explicit metric cross term in (ES-84). It cancels only in the special unit-weight case `p_zeta^V=p_chi^V`; the general bound uses `eps_V0` below in addition to the disturbance Young constant `eps_V2`.

```text
p_chi^V |chi_i^V| D_i^V(t)
 <= 0.5 eps_V2 (chi_i^V)^2
    + (p_chi^V)^2 [D_i^V(t)]^2/(2eps_V2),                          (ES-92)

D_i^V(t)
 = k_c^V |e_i^V|/(tau_Qi k_Vi)
   + |r_i^V|/(tau_Qi k_Vi)
   + bar(R)_i^V.                                                    (ES-93)
```

With the repaired metric, let `Delta_p^V=p_zeta^V-p_chi^V` and use a positive proof constant `eps_V0` for the metric cross term. Young's inequality gives

```text
|Delta_p^V h_i^V zeta_i^V chi_i^V|
 <= 0.5 eps_V0 (zeta_i^V)^2
    +0.5 (Delta_p^V)^2 (h_bar_i^V)^2 (chi_i^V)^2/eps_V0.
```

For the aggregate disturbance `D_i^V(t)` in (ES-93),

```text
p_chi^V |chi_i^V|D_i^V(t)
 <= 0.5 eps_V2 (chi_i^V)^2
    +(p_chi^V)^2[D_i^V(t)]^2/(2eps_V2).
```

Substitution into the repaired (ES-84) yields

```text
dot(mathscr V_V)
 <= -sum_i [p_zeta^V k_1^V-0.5 eps_V0](zeta_i^V)^2
    -sum_i [p_chi^V k_2^V-0.5 eps_V2
            -0.5(Delta_p^V)^2(h_bar_i^V)^2/eps_V0](chi_i^V)^2
    +sum_i (p_chi^V)^2[D_i^V(t)]^2/(2 eps_V2).                     (ES-94)
```

The displayed voltage coefficients are design constraints. **PO-08** verifies their compatibility with the graph-dependent terms and the declared operating set.

```text
k_1^V > eps_V0/(2p_zeta^V),
k_2^V > [eps_V2+(Delta_p^V)^2(h_bar_i^V)^2/eps_V0]/(2p_chi^V),
for every i.                                                       (ES-95)
```

### 14.3 Frequency chain

Define

```text
D_i^omega(t)
 = k_c^omega |e_i^omega|/tau_Pi
   + |r_i^omega|/tau_Pi
   + bar(R)_i^omega.                                                (ES-96)
```

With positive `eps_omega`,

```text
h_bar_i |zeta_i^omega| D_i^omega
 <= 0.5 eps_omega (zeta_i^omega)^2
    + 0.5 h_bar_i^2 [D_i^omega(t)]^2/eps_omega.                    (ES-97)
```

Therefore

```text
dot(mathscr V_omega)
 <= -sum_i[k_1^omega-0.5 eps_omega](zeta_i^omega)^2
    +sum_i h_bar_i^2[D_i^omega(t)]^2/(2 eps_omega).                (ES-98)
```

### 14.4 Privacy chain

Let `w_delta_bar_i` be the maximum admissible value of `|w_{i,12}-w_{i,21}g_i|`. With positive `eps_r1,eps_r2`,

```text
0.5 p_c^nu |r_i| w_delta_bar_i |z_i|
 <= 0.25 p_c^nu eps_r1 r_i^2
    + 0.25 p_c^nu w_delta_bar_i^2 z_i^2/eps_r1,                    (ES-99)

 p_c^nu |r_i dot(c_i)|
 <= 0.5 p_c^nu eps_r2 r_i^2
    + p_c^nu |dot(c_i)|^2/(2eps_r2).                               (ES-100)
```

Using (ES-46), (ES-88) becomes

```text
dot(mathscr V_priv)
 <= -a_z ||bold(z)||^2
    -a_r ||bold(r)||^2
    + d_c ||dot(bold(c))||^2,                                     (ES-101)
```

where, for `nu in {V,omega}`,

```text
a_z=min_{i,nu} p_c^nu[lambda_tr,i^nu+underline(w)_i^nu
                       -w_delta_bar_i^nu^2/(4eps_r1)],
a_r=min_{i,nu} p_c^nu[lambda_tr,i^nu-eps_r1/4-eps_r2/2],
d_c=max_{i,nu} p_c^nu/(2eps_r2).
```

The positive metric weights multiply both the nominal dissipation and the Young terms, so the private-weight feasibility condition is unchanged after cancellation of the common positive factor `p_c^nu`. **PO-10** records these constants and verifies their positivity; they are not controller gains.

### 14.5 Composite comparison inequality

The graph term is not treated as an unnamed input. From (ES-20)-(ES-21) and (ES-48), for either channel,

```text
bold(e)
 = diag(b_i) bold(e_0)
   + L_c bold(c)
   + L_c bold(r)
   + 0.5 L_c bold(z).                                               (ES-101a)
```

**PO-06** uses the algebraic controller equations (ES-28),(ES-31) and condition (ES-21a) to bound `bold(c)` and `bold(e)` by the physical, residual, and decomposition states.

Subject to **PO-06--PO-10** and the pre-checked design-domain feasibility **PO-13**, combining (ES-94),(ES-98),(ES-101), using the finite PO-02A residual bound, and bounding the graph errors through `L_c+diag(b_i)` gives the form

```text
dot(mathscr V_cl)
 <= -a_cl mathscr V_cl
    + d_R
    + d_priv(t),                                                    (ES-102)
```

where:

- `a_cl>0` is the minimum remaining negative coefficient after all Young bounds;
- `d_R` depends only on `bar(R)_i^V`, `bar(R)_i^omega` and declared compact-region bounds;
- `d_priv(t)` depends only on `gamma_priv,i^V(t)`, `gamma_priv,i^omega(t)` and `dot(c_i)` terms established by the privacy lemma.

The comparison solution is

```text
mathscr V_cl(t)
 <= exp(-a_cl t) mathscr V_cl(0)
    + integral_0^t exp[-a_cl(t-s)] [d_R+d_priv(s)] ds.             (ES-103)
```

After **PO-07** is closed, (ES-103) gives a comparison estimate on whichever compact subset of `D_min` has been selected. Funnel and operating-region admissibility are handled together by the proof-only Joint Exit-Continuation Lemma under the explicit JECFC sublevel/margin condition; no result is attributed to **PO-11** before that joint argument is complete. Local existence/uniqueness needed to start the argument is **PO-16A**, which is proved on the admissible open domain before any invariant-region claim.

### 14.6 Bootstrap/continuation separation

The proof uses a compact bootstrap set `K_0` selected inside the admissible open domain `D_min` of the independent coordinates. `K_0` is not assumed invariant. **PO-16A** supplies Caratheodory local existence and uniqueness up to the first exit time from `D_min`; **PO-03**, **PO-08**, **PO-09**, and **PO-10** are pointwise estimates on any selected compact subset, with constants re-instantiated for that subset. Algebraically dependent quantities in ES-81 are reconstructed from the independent state and are not treated as independent Euclidean coordinates. **PO-13** checks actuator and funnel feasibility on its bootstrap design region before composite gain closure. **PO-07** then closes the composite negative coefficient locally. The Joint Exit-Continuation Lemma handles the single exit time and yields the PO-11 and PO-16B branches only under JECFC; no equation in ES-1--ES-103 is changed by this separation.

## 15. Equation-to-result dependency map

| Final result | Required equations | Required assumptions | Proof method | Output |
|---|---|---|---|---|
| Definition 1 | ES-1 to ES-16, ES-41 to ES-53 | Plant/interface ownership | Closed-loop specification | Admissible physical/cyber/private system |
| Definition 2 | ES-16, ES-54 to ES-57 | Passive observation boundary | Exact history equivalence | Public-history indistinguishability target |
| Assumption 1 | ES-4 to ES-13, ES-22 to ES-23, ES-38, ES-46 | Compact/open operating domain, fixed graph, measurable locally essentially bounded uncertainty, and initial funnel feasibility; actuator feasibility is checked on `K_0` by PO-13 rather than assumed globally | Regularity ledger | Admissible physical/controller model |
| Assumption 2 | ES-41 to ES-51, ES-57 to ES-61 | Nominal nonzero-split margin, nominal private-weight interior margin, finite-seed positive lower margin for `gamma_priv`, Privacy Gain Feasibility Condition for PO-10, residual regularity/decay target, and passive adversary; existence of a non-nominal admissible alternative is a PO-04 conclusion, not an Assumption 2 premise | Decomposition admissibility | Valid privacy layer |
| Lemma 1 | ES-41 to ES-61 | Assumption 2 | Linear decay of `z`, finite residual filter estimate, alternative-weight construction; the decaying ES-51 envelope remains PO-02B | Bounded substates, residual envelope when PO-02B is closed, indistinguishable alternatives |
| Theorem 1 | ES-62 to ES-73, ES-80 to ES-103 | Assumptions 1-2, Lemma 1, PO-02A, PO-07, PO-11, PO-13, PO-16A, PO-16B, gain inequalities; any asymptotic ES-51 claim additionally requires PO-02B | Composite Lyapunov plus barrier/continuation argument | Boundedness and funnel invariance |
| Theorem 2 | ES-22 to ES-40, ES-95, ES-98, ES-103 | Theorem 1 | Inverse transformation and deadline schedule | Practical recovery by `T_V`,`T_omega` |
| Theorem 3 | ES-71 to ES-79 | Assumptions 1-2, Theorem 2 | Equilibrium droop algebra | Exact or bounded sharing |
| Theorem 4 | ES-54 to ES-61 plus Theorems 1-3 equations | Definitions 1-2, Assumptions 1-2, Lemma 1 | Observation-equivalence construction plus theorem composition | Simultaneous privacy/performance/sharing guarantee |

## 16. Equation consistency audit

### Focused algebra and sign audit

| Equations audited | Result | Basis / remaining proof task |
|---|---|---|
| ES-4, ES-5, ES-10, ES-11 | PASS | Dividing the retained droop dynamics by their positive channel coefficients yields the displayed input-affine signs; `R` retains the positive additive orientation. |
| ES-28, ES-31, ES-62, ES-68 | PASS | Each command has the compensating positive drift term and enters the plant with its specified negative input coefficient; substituting `u=c+r` gives ES-63 and ES-69. |
| ES-49, ES-50, ES-52 | PASS | Subtracting/averaging ES-44--ES-45 gives the displayed `z` and `r` dynamics; setting `r=0` gives exactly the factor `2 dot(c)` in ES-52. PO-01--PO-03 prove the resulting bounds. |
| ES-58--ES-61 | PASS WITH OPEN PROOF OBLIGATION | Comparison of the public `p` dynamics gives ES-59 with the displayed sign. PO-04--PO-05 prove local alternative existence, denominator validity, and weight feasibility. |
| ES-63--ES-70 | PASS | Direct plant substitution produces the negative residual and distributed-error terms; ES-65 and ES-70 follow from ES-34. PO-08--PO-09 close their inequalities. |
| ES-71--ES-79 | PASS WITH OPEN PROOF OBLIGATION | Equilibrium substitution and pairwise subtraction give the displayed droop relation and triangle bound. PO-14 establishes the limiting conditions. |
| ES-84, ES-86, ES-88 | PASS WITH PROOF-METRIC UPDATE | ES-84 now contains `(p_zeta^V-p_chi^V)h zeta chi`; exact cancellation remains only for equal metric entries. ES-88 is scaled by the channel proof weight. PO-08--PO-10 close the weighted bounds. |
| ES-90--ES-98 | PASS WITH OPEN PROOF OBLIGATION | The gain upper bound and Young inequalities have the stated directions. PO-08--PO-09 verify invariant-set and coefficient conditions. |
| ES-101a, ES-102 | PASS | Substitution `p=c+r+0.5z` into ES-20--ES-21 gives ES-101a exactly. PO-06 and the `Q_cl` certificate in PO-07 supply the graph and gain closure locally on `K_0`; continuation remains downstream. |
| ES-83, ES-87 | PASS WITH PROOF-METRIC UPDATE | Constant positive diagonal blocks of the reserved `P_L` supply reciprocal-unit weights; no controller equation changes. |

### Symbol audit

- All architecture symbols are defined in the frozen dictionary.
- Equation-level additions are listed under `NEW SYMBOL REQUIRING FREEZE UPDATE` and have been inserted into the dictionary/notation contract.
- `zeta` is used only for transformed physical error; `z` is used only for public-private substate difference; `r` is used only for reconstruction residual.
- No deleted state or operator appears.

### Dimension audit

The original unweighted ES-83 and ES-87 were not dimensionally homogeneous under the frozen physical-unit notation. The proof-metric entries in the Lyapunov Metric Convention repair this without changing plant/controller dimensions.

| Equation | Check |
|---|---|
| ES-4 | Every term has angular-frequency units; division by `tau_Pi` gives angular acceleration. |
| ES-5 | Every term has voltage units after multiplication by the declared coefficients; division gives voltage acceleration. |
| ES-6/ES-7 | Voltage-squared times susceptance has power units. |
| ES-24/ES-25 | `sigma` and `zeta` are dimensionless. |
| ES-26 | Every term has voltage-per-time units. |
| ES-28 | Every term has voltage-channel secondary-input units. |
| ES-30 | Every term has angular-acceleration units. |
| ES-31 | Every term has frequency-channel secondary-input units. |
| ES-44/ES-45 | `lambda_tr,i(c_i-p_i)` and the private coupling terms have command-per-time units; `lambda_tr,i` has unit 1/s. |

### Graph audit

- `N_i^e` appears only in (ES-6)-(ES-7).
- `N_i^c`, `a_ij`, and `L_c` appear only in cyber coordination and public-message equations.
- No equality between `G_e` and `G_c` is assumed.

### Privacy audit

- The public payload is exactly (ES-14).
- Private states and weights do not appear in the payload.
- The adversary history includes all public messages, topology, timing, references, funnels, deadlines, and public gains.
- Privacy is exact history equality (ES-56), not trajectory similarity.
- Alternative admissibility includes plant and actuator compatibility.

### Control audit

- The plant input is uniquely defined by (ES-12), (ES-47), and (ES-53).
- The transformation is nonsingular under (ES-38)-(ES-39).
- Physical deadlines appear only in the funnel schedules and performance conclusions.
- Privacy residuals are never absorbed into physical uncertainty.

### Sharing audit

- Exact sharing follows only through (ES-71)-(ES-77).
- Practical sharing uses the explicit bound (ES-79).
- No common-mode property is assumed without (ES-71)-(ES-73).

### Dead-code audit

Every retained dynamic equation supports Lemma 1 or Theorems 1-3. Observation equations support Definition 2 and Theorem 4. HIL-only filtered measurements and experiment metrics do not enter the core proof. No equation is reserved for a future robustness theorem.

## 17. Critical contradiction report

The Stage-2 dimension audit found a genuine proof-metric inconsistency in the unweighted ES-83 and ES-87 expressions. It is repaired by constant positive diagonal proof metrics; no plant, controller, privacy, or graph equation is redesigned. The remaining open items are proof-closure conditions recorded in `proof_obligations_0807.md`.

## Equation Freeze Candidate

### Equations ready to freeze

- reduced physical plant and lossless electrical power flow, ES-1 to ES-12;
- fixed cyber graph, payload, and observation history, ES-13 to ES-16;
- corrected prescribed-performance transformation, ES-22 to ES-40;
- reconstruction and exact residual definitions, ES-41 to ES-50;
- transparent-wrapper condition and nontransparent decision, ES-52 to ES-53;
- voltage/frequency privacy insertion, ES-62 to ES-70;
- power-sharing algebra and practical bound, ES-71 to ES-79;
- equation/result dependency map.

### Open proof obligations

- **PO-01--PO-03:** substate decay, bootstrap command-rate bound, finite residual estimate (PO-02A), and the later decaying residual envelope (PO-02B) for (ES-49)--(ES-51).
- **PO-04--PO-05:** nonempty admissible alternative realization and denominator/weight validity for (ES-58)--(ES-61).
- **PO-06:** graph/algebraic closure; **PO-07:** composite-gain certificate and local derivation of (ES-102).
- **PO-08--PO-12:** voltage, frequency, privacy, barrier-invariance, and practical prescribed-time proof chains.
- **PO-13:** bootstrap actuator/funnel feasibility before PO-07; **PO-14--PO-15:** sharing and theorem composition; **PO-16A--PO-16B:** local well-posedness and forward operating-region continuation.

The core plant remains lossless. A lossy-network claim would require reopening (ES-6)--(ES-9), not hiding conductance inside `R_i`.

### Architecture contradictions

No contradiction forces removal of a frozen essential module. However, two claim restrictions are now explicit:

- global transparent reconstruction is not supplied by the frozen architecture because it requires (ES-52);
- global ambiguity for every arbitrary protected alternative is not established; the defensible target is non-uniqueness over the admissible set defined by (ES-58)-(ES-61).

These restrictions narrow claims but do not redesign the architecture.

### Required Blueprint Reopen

`NO`

The command-tracking rates and proof constants are notation/equation completions that can be accepted during equation review without reopening the module architecture.

### Formal Equation Freeze Checklist

| Item | Status | Review basis |
|---|---|---|
| A. Architecture consistency | PASS | Retained modules only; forbidden modules do not appear. |
| B. Symbol completeness | PASS WITH PROOF-METRIC UPDATE | Constant entries of reserved `P_L` are defined in the Lyapunov Metric Convention and have no controller role. |
| C. Dimension consistency | PASS WITH OPEN PROOF OBLIGATION | ES-83/ES-87 are repaired by the constant diagonal metric; PO-13 still verifies actuator units. |
| D. Equation dependency consistency | PASS | ES dependencies are mapped; PO-06 and PO-07 close graph/comparison dependencies locally, with PO-11/PO-16B still downstream. |
| E. Proof-obligation completeness | PASS | All unresolved derivations are assigned in `proof_obligations_0807.md`. |
| F. Privacy observation consistency | PASS WITH OPEN PROOF OBLIGATION | Public history/payload are explicit; PO-04--PO-05 and PO-15 prove existence-based equivalence. |
| G. Plant-interface uniqueness | PASS | ES-12, ES-47, and ES-53 are the sole privacy-to-plant path. |
| H. Graph consistency | PASS WITH OPEN PROOF OBLIGATION | Electrical/cyber graphs are separated; PO-06 derives the required algebraic bounds. |
| I. Funnel-domain feasibility | PASS WITH OPEN PROOF OBLIGATION | ES-38--ES-40 are structurally correct; PO-11 proves forward invariance. |
| J. Actuator feasibility | PASS WITH OPEN PROOF OBLIGATION | PO-13 checks funnels, gains, and `U_i` on `K_0`; it is not used as a premise for local existence. |
| K. Theorem dependency coverage | PASS WITH OPEN PROOF OBLIGATION | Traceability matrix and PO-15 connect privacy, performance, and sharing results. |

### Revision Log

| Revision ID | Change | Affected equations/results | Reason and downstream effect |
|---|---|---|---|
| ER-01 | Added Notation Freeze Delta audit; no dictionary files changed. | All ES families | Confirms every listed auxiliary is already frozen and no deleted module symbol remains. |
| ER-02 | Replaced unsupported imperative claims by PO-02--PO-05, PO-06, PO-08, and PO-10 references. | ES-51; ES-58--ES-61; ES-94--ES-102 | Makes the unproved envelope, admissible-alternative construction, graph closure, and Lyapunov coefficients explicit proof targets. |
| ER-03 | Completed formal PASS/PASS WITH OPEN PROOF OBLIGATION checklist and verdict. | Equation-freeze decision | Prevents an Equation Freeze declaration before the required derivations exist. |
| ER-04 | Algebra/sign audit completed with no equation-text correction. | ES-4, ES-5, ES-10, ES-11, ES-28, ES-31, ES-49, ES-50, ES-52, ES-62--ES-79, ES-84--ES-102 | Direct substitution confirms the specified signs and reconstruction orientation. Remaining gaps are proof closure, not algebraic contradiction. |
| ER-05 | Added the Stage-1 condition for the decaying residual envelope; no ES formula was changed. | ES-51; Lemma 1; Theorems 1--4 | `derivation_stage_1_0807.md` shows that uniform `dot(c)` boundedness is insufficient. Final theorem use needs a proved or explicitly assumed decaying command-rate envelope. |
| ER-06 | Repaired Lyapunov metric homogeneity with constant positive diagonal blocks of reserved `P_L`. | ES-83--ES-84, ES-87--ES-88, ES-92, ES-94--ES-95, ES-99--ES-101; ES-89/ES-102 proof constants | The unweighted quadratic sums mixed physical units. The repair changes only proof metrics and derived inequalities; controller, privacy, graph, and ES numbering remain unchanged. |
| ER-07 | Split the aggregate PO-16 dependency into local well-posedness PO-16A and forward continuation PO-16B; moved PO-13 to a pre-PO-07 bootstrap feasibility check. | Proof dependency map, ES-38--ES-40, ES-80--ES-103 dependency statements | The former PO-16/PO-03/PO-07/PO-13 loop mixed local existence, design feasibility, and global invariance. The split changes proof order only; no ES equation or theorem numbering changes. |

## Equation Review Verdict

**B. CONDITIONALLY READY FOR EQUATION FREEZE**

The equation architecture is internally consistent under the frozen lossless model, fixed connected undirected cyber graph, nontransparent wrapper, and existence-based passive-eavesdropper privacy claim. The proof dependency structure now separates local well-posedness from forward continuation; ES numbering and controller architecture remain unchanged. Equation Freeze is conditional on discharging the open proof obligations in `proof_obligations_0807.md`; no item in the formal checklist is FAIL.

**Blueprint Reopen Required: NO**
