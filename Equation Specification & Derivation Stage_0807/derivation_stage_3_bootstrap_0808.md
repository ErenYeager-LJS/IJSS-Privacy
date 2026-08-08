# Derivation Stage 3: Bootstrap Prerequisites

> Task ID: task-002-bootstrap-prerequisites
> Scope: PO-16A, local bootstrap consequences, and PO-13 feasibility before PO-07
> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07

This document derives only local well-posedness, finite bootstrap estimates, and the pre-PO-07 feasibility conditions. It does not prove PO-07, ES-102, Theorem 1, PO-11, PO-16B, or PO-02B. The compact set `K_0` below is a proof construction and is never treated as invariant.

## 1. Admissible open domain

Let `X_cl` denote the frozen ES-1--ES-82 closed-loop state. Define `D_open` as the set of states and public design data satisfying all conditions needed to evaluate the retained vector field:

1. Every physical time constant, droop coefficient, filter coefficient, and input-affine coefficient appearing in ES-4--ES-11 is strictly positive where positivity is required, and every physical state is in the interior of the declared operating region `Delta`.
2. For each channel `nu in {V,omega}`, `rho_i^nu(t)>0` and `|sigma_i^nu|<1` for every state in the domain. Consequently `atanh(sigma_i^nu)`, `h_i^nu`, and the denominators in ES-33--ES-37 are finite.
3. Each load and power-flow function in ES-6--ES-7 is defined and continuously differentiable on a neighborhood of the physical projection of `D_open`; the phase differences and all trigonometric terms are therefore regular there.
4. Every denominator explicitly used by the retained controller is nonzero, including `tau_Pi`, `tau_Qi k_Vi`, `rho_i^nu`, `1-(sigma_i^nu)^2`, and the plaintext algebraic inverse condition in ES-21a.
5. Privacy variables satisfy the admissible ownership and initialization conditions in ES-41--ES-53. The private weights have strict margins `0<underline(w)_i^nu <= w_{i,12}^nu,w_{i,21}^nu <= bar(w)_i^nu`, and `gamma_priv,i^nu(t)>0` on every finite time interval considered locally.
6. The time-dependent funnel schedule and all derivatives required by ES-26--ES-37 are finite. The quintic schedule in ES-22--ES-23 is `C^2` at `T_nu` and constant after the deadline.

`D_open` is open in the state variables because all inequalities are strict. Actuator membership is deliberately not part of local well-posedness; it is checked later by PO-13.

## 2. PO-16A: local well-posedness

### 2.1 Time regularity

On any finite interval, the quintic schedule is polynomial on `[0,T_nu]` and constant on `(T_nu,infinity)`. Its value, first derivative, and second derivative agree at `T_nu`, so `rho`, `dot(rho)`, and `ddot(rho)` are continuous. The frozen controller uses no derivative of order higher than the stated local formulas require. The time-dependent coefficients are therefore continuous and locally bounded.

### 2.2 PPC regularity

On `|sigma|<1`, the map `sigma -> atanh(sigma)` is analytic. The map
`(rho,e_0) -> atanh(e_0/rho)` is consequently `C^1` wherever `rho>0` and `|e_0/rho|<1`. The factors `1/[rho(1-sigma^2)]` and all products in ES-26--ES-37 are locally Lipschitz on every compact subset strictly inside this domain. No claim is made at `|sigma|=1`; that boundary belongs to a later exit analysis.

### 2.3 Privacy correction regularity

For fixed positive `gamma`, define

```text
phi_gamma(z) = g(z) z = z,                    |z| <= gamma,
                 gamma sign(z),              |z| > gamma.
```

This is continuous and globally 1-Lipschitz in the scalar `z`: its slope is 1 in the inner interval and 0 on each outer interval, with matching values at `z=+-gamma`. Thus the vector-field products `g_i z_i` in ES-44--ES-50 are locally Lipschitz even though the separate quotient representation of `g_i` must be treated piecewise. On `D_open`, `gamma_priv,i^nu(t)>0`; the switching surfaces `|z_i|=gamma_priv,i^nu(t)` are therefore not singular. The separate factor `g_i` is bounded by 1 and is continuous across the switching surface, but its derivative need not exist there. The ODE needs local Lipschitzness of the vector-field product, not differentiability of `g_i` itself.

### 2.4 Componentwise local Lipschitz audit

The physical drift terms ES-6--ES-11 are compositions of `C^1` load/power-flow functions, polynomial/trigonometric functions, and affine uncertainty inputs, hence are continuous in time and locally Lipschitz in `X_cl`. ES-20--ES-21 are affine graph maps. ES-24--ES-25 and ES-33--ES-37 are locally Lipschitz on the strict PPC interior. ES-26--ES-32 are finite sums and products of those maps and their declared schedule derivatives. ES-41--ES-50 are affine tracking equations plus the locally Lipschitz products `phi_gamma(z)`. ES-53 and ES-62--ES-70 are algebraic compositions through the unique interface ES-12. ES-80--ES-82 stack these component fields and introduce no new operation. Therefore the complete frozen vector field `f(t,X_cl)` is continuous in `t` and locally Lipschitz in `X_cl` on `D_open`.

The condition `det(I_N-k_c^nu L_c)!=0` from ES-21a is a fixed design condition, not a state denominator. Once it holds, it contributes a finite constant to the local field and does not create a state singularity.

### 2.5 Local theorem and maximal interval

Apply the nonautonomous Picard-Lindelof theorem for a vector field continuous in time and locally Lipschitz in the state on an open domain. For every finite `X_cl(0) in D_open`, there is a `tau_0>0` and a unique solution on `[0,tau_0]`. Let `[0,tau_max)` be the maximal interval obtained by continuation. By the continuation alternative, if `tau_max` is finite then the solution leaves every compact subset of `D_open`; equivalently, it approaches the boundary of `D_open` or becomes unbounded. Until the first exit time, uniqueness and the defining inequalities of `D_open` hold. This proves local existence/uniqueness only and does not exclude a later exit.

### 2.6 Construction of `K_0`

Because `D_open` is open and `X_cl(0)` is finite and belongs to it, there exists `epsilon_0>0` such that the closed Euclidean ball

```text
K_0 = { X : ||X-X_cl(0)|| <= epsilon_0 }
```

is compact, contains `X_cl(0)` in its interior, and satisfies `K_0` compactly contained in `D_open`. Every continuous coefficient and every locally Lipschitz modulus of the frozen vector field has a finite supremum on `K_0`. `K_0` is not asserted to be forward invariant. Actuator feasibility is not part of this construction.

**PO-16A verdict: PROVED.**

## 3. Local obligations discharged by PO-16A

| Obligation | Classification after PO-16A | Remaining condition | Scope restriction |
|---|---|---|---|
| PO-03 | Mathematical derivation complete; status `PROVED` in the local sense | None beyond the frozen regularity and finite `K_0` constants | Finite `dot(c)` bounds only on `K_0` up to first exit |
| PO-02A | Mathematical derivation complete; status `PROVED` | PO-01 and PO-03 | Finite residual/convolution bound; no decay claim |
| PO-08 | Mathematical derivation complete; status `PROVED` in the local sense | Positive coefficients from the recorded Stage-2.5 inequalities | Pointwise voltage inequality on `K_0`; no global stability |
| PO-09 | Mathematical derivation complete; status `PROVED` in the local sense | Positive frequency gain coefficient from ES-98 | Pointwise frequency inequality on `K_0`; no global stability |
| PO-10 | Partial | Private-weight condition and epsilon feasibility must be part of the admissible design region | Local privacy inequality; no ES-51 use |

For PO-10, the required channel-wise private-weight condition is

```text
bar(w_delta)_i^nu^2
  < 16 lambda_tr,i^nu (lambda_tr,i^nu + underline(w)_i^nu).
```

The Young parameters must additionally satisfy

```text
0 < eps_r1 < 4 lambda_tr,i^nu,
0 < eps_r2 < 2[lambda_tr,i^nu - eps_r1/4],
```

for every channel and agent, with the resulting `a_z>0`, `a_r>0`, and finite `d_c`. Since the frozen documents do not yet declare these inequalities as a concrete admissible design-region clause, PO-10 is not upgraded to unconditional `PROVED`.

## 4. PO-13: symbolic bootstrap feasibility

PO-13 uses only finite quantities on `K_0`. It has no dependency on PO-07, ES-102, PO-11, PO-16B, PO-02B, or ES-51 decay.

For each channel `nu`, sufficient funnel conditions are

```text
|e_i,0^nu(0)| < rho_i,0^nu,
rho_i,0^nu > rho_i,infty^nu > 0,
0 < T_nu < infinity.
```

Let `bar zeta_i^nu`, `bar chi_i^V`, `bar e_i^nu`, `bar r_i^nu`, and `bar R_i^nu` denote the finite suprema on `K_0` supplied by PO-16A, PO-02A, PO-06, and the uncertainty bounds. Define the local actuator-demand bounds

```text
Ubar_i^V(K_0) = sup_{X in K_0}|hat(c)_i^V(X)|,
Ubar_i^omega(K_0) = sup_{X in K_0}|hat(c)_i^omega(X)|.
```

Using ES-28, ES-31, and `hat(c)=c+r`, these suprema are bounded by the explicit symbolic margins

```text
Ubar_i^V <= tau_Qi k_Vi[bar F_i^V + bar alphadot_i^V
              + k_2^V bar chi_i^V + bar h_i^V bar zeta_i^V]
              + |k_c^V| bar e_i^V + bar r_i^V,

Ubar_i^omega <= tau_Pi[bar F_i^omega + bar alpha_i^omega]
                  + |k_c^omega| bar e_i^omega + bar r_i^omega.
```

The funnel and gain design is feasible on `K_0` only if the declared actuator sets contain strict margins around these bounds. For symmetric sets this is

```text
Ubar_i^V(K_0) < U_i,max^V,
Ubar_i^omega(K_0) < U_i,max^omega.
```

For general sets, the required condition is `[-Ubar_i^nu,Ubar_i^nu]` compactly contained in `U_i^nu`. The quantities `bar alphadot`, `bar h`, and `bar zeta` increase with funnel aggressiveness (`T_nu` decreasing or endpoint gap increasing); `k_1^V,k_2^V,k_1^omega,k_c^V,k_c^omega` enter the displayed bounds directly; `P_L^V` and the graph constant `K_M` affect the admissible Lyapunov/gain margins and hence the allowed `K_0`; `bar r` enters additively; and `bar R` enters through `bar F` and the derivative bounds. No numerical actuator limit is invented.

The Stage-2.5 gain conditions must also hold:

```text
k_2^V > k_{2,min}^V(P_L^V,K_M,bar R,bar r,eps_V0,eps_V2),
k_1^omega > k_{1,min}^omega(K_M,bar R,bar r,eps_omega),
```

with the recorded positive epsilon choices and the PO-10 private-weight condition above. These are sufficient symbolic inequalities, but the repository contains no numerical actuator sets or selected gain/deadline tuple with which to prove that their intersection is nonempty for a particular experiment.

**PO-13 verdict: PARTIAL.** The symbolic feasibility test is complete. Concrete nonemptiness remains a design-parameter/HIL validation item, not a theorem consequence and not a reason to alter the Blueprint.

## 5. PO-07 readiness gate

| Prerequisite | Required status | Actual status | Ready? |
|---|---|---|---|
| PO-02A | PROVED on `K_0` | PROVED | YES |
| PO-03 | PROVED on `K_0` | PROVED | YES |
| PO-06 | PROVED | PROVED | YES |
| PO-08 | PROVED pointwise on `K_0` | PROVED | YES |
| PO-09 | PROVED pointwise on `K_0` | PROVED | YES |
| PO-10 | Private-weight and epsilon feasibility closed | PARTIAL | NO |
| PO-13 | Nonempty actuator/funnel design region | PARTIAL | NO |

**PO-07 UNLOCKED: NO.** The blockers are exactly the unclosed PO-10 private-weight/epsilon admissible-design clause and the absence of a declared numerical actuator/gain/deadline tuple or equivalent strict symbolic margin certificate for PO-13. PO-02B is not a PO-07 prerequisite and remains OPEN downstream of PO-16B.

## 6. Verification audit

- Proof DAG: 18 nodes, 32 directed edges, 0 nontrivial SCCs, topological order exists and follows `PO-16A -> PO-03 -> PO-02A -> PO-13 -> PO-07` with PO-06/PO-08/PO-09/PO-10 side prerequisites.
- Active bare aggregate references: no active bare `PO-02` or `PO-16` dependency remains; historical revision notes are classified as historical.
- PO-13 dependencies: no PO-07, ES-102, PO-16B, PO-02B, or ES-51-decay prerequisite.
- ES equations changed: **NO**. Only proof-level status and dependency prose changed.
- `docs/handoff/latest.md`: points to `task-002-bootstrap-prerequisites.md` after handoff update.

## 7. Final status

1. PO-16A: **PROVED**.
2. PO-03: **PROVED locally on `K_0`**.
3. PO-02A: **PROVED locally on `K_0`**.
4. PO-08: **PROVED pointwise locally on `K_0`**.
5. PO-09: **PROVED pointwise locally on `K_0`**.
6. PO-10: **PARTIAL**, pending explicit admissible private-weight/epsilon design clause.
7. PO-13: **PARTIAL**, pending strict actuator/gain/deadline margin certificate.
8. PO-07 UNLOCKED: **NO**.
9. Remaining blockers: PO-10 design feasibility and PO-13 concrete nonempty feasibility certificate; PO-02B, PO-07, PO-11, and PO-16B remain intentionally downstream/open.
10. Blueprint Reopen Required: **NO**.
11. Recommended next Task ID: `task-002-bootstrap-prerequisites` continuation for parameter-feasibility closure, then `task-002-po07-composite-gain` only after the gate passes.
