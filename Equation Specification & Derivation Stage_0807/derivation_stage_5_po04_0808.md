# Derivation Stage 5: PO-04 Privacy Alternative Existence Audit (Major Revision)

> Task ID: `task-015-po04-privacy-alternative-existence-v2-2-domain`
> Active architecture: Blueprint Version 2.2, Privacy-Schedule Regularity Revision
> Theorem boundary: `LOCAL-BEFORE-EXIT`
> Scope: PO-04 only; PO-05 remains downstream

## 1. Final result

**Outcome A — PO-04 PROVED locally on the Version 2.2 schedule-regular domain.**

The previous reachability objection is withdrawn. It incorrectly treated an arbitrary preassigned `S_i+delta` as necessary and used an incomplete frequency derivative that omitted the `-tau_Pi alpha_i^omega` term. The correct construction starts with an admissible physical initial perturbation, evaluates the same frozen controller, and defines the induced protected value `S_i'`.

PO-04 is proved for a nonempty local family before the earliest finite-seed/regular-domain first exit. PO-05 remains `OPEN / NOT STARTED`; no denominator continuation beyond this local interval is claimed.

## 2. Weakest required quantifier

ES-55--ES-57 state an existential privacy target: at least one `S_i' != S_i` with an admissible private realization and identical observation history. The ledger additionally requires a positive local perturbation radius. The proof establishes the stronger, useful local statement: there is `epsilon_*>0` such that every nonzero physical perturbation `epsilon` in a punctured sufficiently small interval, excluding only the nominal zero, generates an admissible alternative family on a common local interval. No arbitrary global `delta` or universal initialization claim is made.

## 3. Exact frequency command map

At time zero, perturb only `omega_i(0)` to `omega_i'(0)=omega_i(0)+epsilon`, keep the voltage/phase states, schedules, references, powers at their instantaneous values, and all public `p(0)` values fixed. Since power flow does not depend on angular velocity instantaneously, `P_i(0)` is fixed in this partial derivative. From ES-8, ES-19, ES-21, ES-24, ES-25, ES-30, and ES-31,

```text
C_i(omega)
 = -[(omega-omega_ref)+k_Pi(P_i-P_i^d)]
   - tau_Pi alpha_i^omega(omega)
   + k_c^omega[b_i(omega-omega_ref)
       + sum_j a_ij(p_i^omega(0)-p_j^omega(0))].
```

Write `sigma=(omega-omega_ref)/rho` and `zeta=atanh(sigma)`. With rho and its time derivatives fixed at time zero,

```text
d alpha_i^omega/d omega
 = dot(rho_i^omega)/rho_i^omega
   - k_1^omega[1-2 sigma_i^omega zeta_i^omega].
```

Therefore

```text
d C_i/d omega
 = -1 - tau_Pi dot(rho_i^omega)/rho_i^omega
   + tau_Pi k_1^omega[1-2 sigma_i^omega zeta_i^omega]
   + k_c^omega b_i.
```

For the frozen quintic schedule, `dot(rho_i^omega)(0)=0` when the initial time is the schedule origin. At `sigma_i^omega(0)=0` and `k_c^omega b_i=1`, this becomes `tau_Pi k_1^omega != 0`. The earlier cancellation argument was therefore wrong because it omitted `-tau_Pi alpha_i^omega`.

The derivative can vanish at an isolated point for other admissible values of `sigma`, gains, or schedule slope. That does not make `C_i` locally constant: the analytic factor `1-2 sigma atanh(sigma)` is nonconstant on `(-1,1)`, and `k_1^omega>0`. Hence `C_i` is a nonconstant analytic function of omega on every admissible neighborhood. There are arbitrarily small `epsilon != 0` with `C_i(omega_i+epsilon) != C_i(omega_i)`. This proves the weakest needed non-nominality without requiring local surjectivity onto every prescribed delta.

## 4. Voltage channel audit

No independent voltage rank condition is needed. PO-04 protects the vector `S_i=[c_i^V(0),c_i^omega(0)]^T`; a change in one component is enough for `S_i' != S_i`. The frequency perturbation above already changes the omega component. ES-28 remains the same frozen command map and is evaluated along the resulting local alternative physical trajectory; no voltage perturbation is imposed.

## 5. ES-58 initial feasibility

Define the induced perturbation

```text
delta_i(epsilon)=C_i(omega_i(0)+epsilon)-C_i(omega_i(0)),
S_i'=S_i+[0,delta_i(epsilon)]^T.
```

Set

```text
p_i'(0)=p_i(0),
q_i'(0)=2S_i'-p_i(0),
z_i'(0)=z_i(0)-2[0,delta_i(epsilon)]^T.
```

Because `delta_i(epsilon)->0` and `|z_i^omega(0)|>=eta_{z,i}^omega`, choose `epsilon_*` so that the alternative initial split remains at least `eta_{z,i}^omega/2`. The unchanged voltage component has the nominal split. The initialization gives `r_i'(0)=0` in the perturbed channel and keeps all public initial messages unchanged.

## 6. Local physical trajectory and network coupling

Fix the nominal public trajectory `p(t)` as the public input to the alternative construction. Choose a `C^1` private path

```text
q_i'(t)=q_i(t)+2[0,delta_i(epsilon)]^T phi(t),
phi(0)=1,
```

with `phi` fixed and bounded on a sufficiently short interval; other agents/channels use the nominal path initially. The same frozen plant equations ES-1--ES-12 are then solved from the perturbed physical initial state, with `hat(c)'=(p+q')/2` as their only plant input. PO-16A local well-posedness and continuous dependence apply on a compact tube inside the open domain. The resulting `c'(t)` is the actual controller command, not an algebraic counterfactual.

The perturbation is not treated as isolated after time zero. Electrical coupling can change neighboring physical states and commands. All agents and channels are included in the construction; their private paths are kept nominal or perturbed by the same continuous extension as required. The public `p_j` values are fixed network-wide, so ES-20--ES-21 and all neighbor terms are evaluated consistently. No smaller affected subset is assumed closed.

## 7. ES-60 and ES-61 feasibility

At `epsilon=0`, the actual alternative trajectory, private paths, and weights equal the nominal ones. On a finite nominal local interval `[0,T_0]` before first exit, PO-01 and the nonzero initial split give a positive minimum `m_z` for each nominal `|z_j^nu|`. Version 2.2 gives `gamma_priv>=eta_gamma>0`, and the nominal weights have strict ES-46 margin `eta_w`.

The alternative physical solution, `q'`, `z'=p-q'`, `c'`, and `dot(q')` depend continuously on `epsilon` on a possibly smaller common interval. Therefore there is `epsilon_*>0` such that, for `|epsilon|<epsilon_*`,

```text
|z_j'^nu(t)| >= m_z/2,
|g_j'^nu z_j'^nu| >= min(m_z/2,eta_gamma,j^nu),
```

for all affected pairs and times in that interval. The ES-60 and ES-61 quotients are consequently continuous in `epsilon` at the nominal weights. Define `epsilon_*` as the minimum of the initial-domain radius, the first-exit continuity radius, and the radii at which either quotient reaches an ES-46 interior boundary. Strict nominal margins make this minimum positive.

## 8. Public-history equality

For every agent/channel, define `w_{j,21}'` by ES-60 and `w_{j,12}'` by ES-61 on the common local interval. ES-61 makes the chosen `q_j'` satisfy ES-45. ES-60 makes the right-hand side of ES-44 equal to the nominal `dot(p_j)`, while `p_j'(0)=p_j(0)`. Thus `p_j'(t)=p_j(t)` for the complete network and both channels on the local interval.

The remaining elements of ES-16 (`H_c`, graph, references, schedules, and public controller parameters) are unchanged. Physical sensor histories and private memory are not observed. Hence the complete passive public history, not merely one local message, is identical.

## 9. PO-04 / PO-05 separation

PO-04 is closed only on the constructed local interval: a genuine non-nominal induced `S'`, admissible ES-58 initialization, bounded ES-60/61 weights, identical public history, and a positive physical perturbation radius exist before first exit. PO-05 is not used to obtain this local result. Any continuation through later zeros of `z'`, isolated denominator extensions, or persistence beyond the local interval remains PO-05.

## 10. Final status and next task

- **Outcome:** **A — PO-04 PROVED locally.**
- **PO-04:** **PROVED** on the Version 2.2 schedule-regular local domain.
- **PO-05:** **OPEN / NOT STARTED**.
- **Architecture reopening:** **NO**. No Blueprint, controller, ES, Lyapunov, state, observation, or theorem-scope change is required.
- **Recommended next task:** `task-016-po05-alternative-denominator-validity`.
