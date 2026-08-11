# Derivation Stage 6: PO-05 Alternative Denominator Validity and Local Continuation

> Task ID: `task-016-po05-alternative-denominator-validity`
> Active architecture: Blueprint Version 2.2, Privacy-Schedule Regularity Revision
> Theorem boundary: `LOCAL-BEFORE-EXIT`
> Scope: PO-05 only; PO-04 is an input and is not re-proved

## 1. Final result

**Outcome A — PO-05 PROVED on the maximal local regular continuation interval.**

The alternative family supplied by PO-04 can be restarted and continued from every strict interior time. ES-60 and ES-61 remain legal and their forced weights remain strictly inside ES-46 throughout the continuation interval. The interval ends only at the first retained privacy/physical admissibility exit or at the finite-seed horizon `T_s`, whichever occurs first. No continuation beyond that boundary, no global `z'` separation, and no all-time ES-46 invariance are claimed.

## 2. Exact PO-05 statement and PO-04 input

The frozen PO-05 obligation is the downstream alternative-denominator validity problem for ES-60--ES-61. It starts after the initial/common local construction interval established by PO-04 and asks for any additional nonvanishing, continuation, or compatible extension needed before the retained privacy stopping boundary. It does not re-prove PO-04's initial interval.

At the PO-04 endpoint used as the continuation seed, the following are available on a common interval `[0,t_seed]`:

- a genuine induced `S' != S` and a positive physical perturbation radius;
- ES-58-compatible initial private states and nonzero alternative `z_j'^nu`;
- `gamma_priv,j^nu >= eta_{gamma,j}^nu > 0` on `I_s=[0,T_s]`;
- legal `g_j'^nu z_j'^nu` and `z_j'^nu` denominators;
- strict ES-46 interior margins for both forced alternative weights;
- the same complete passive public history `O_adv`.

These facts are data for PO-05, not conclusions to be reproved.

## 3. Regular alternative domain

Let `D_min` be the frozen open independent-coordinate domain used by PO-16A. For the alternative construction define the time-dependent regular set

```text
D_alt(t) = { X_alt in D_min :
             |sigma_j'^nu| < 1,
             X_alt physical projection in Delta,
             u_j'^nu in U_j^nu,
             z_j'^nu != 0,
             underline(w)_j^nu < w_{j,12}'^nu,w_{j,21}'^nu < bar(w)_j^nu,
             p_j'(t)=p_j(t) for all j,nu }.
```

The schedule condition `gamma_priv,j^nu(t)>=eta_{gamma,j}^nu>0` is imposed for `0<=t<=T_s`; it is not extended after `T_s`. Since `g'z'` is the saturation product from ES-43, `z'!=0` together with this schedule margin is equivalent to legality of the ES-60 denominator on the strict interior. The set is open in the state/weight coordinates because all state, funnel, split, input, and weight inequalities are strict. `p'=p` and the frozen metadata are equalities defining the constructed observation-equivalent section, not open-domain inequalities.

## 4. Exact retained stopping boundary

The repository's PO-16A notation defines

```text
tau_exit = inf{ t>0 : X_min(t) notin D_min }.
```

For the alternative continuation, use the same first-exit meaning for the alternative independent coordinates and add the privacy-specific exits already required by ES-58--ES-61. Starting at `t_seed`, define

```text
tau_priv = min{ T_s,
                tau_exit^alt,
                tau_z,
                tau_w,
                tau_U },
```

where `tau_exit^alt` is the first exit from the frozen `D_min`, `tau_z` is the first time any affected `z_j'^nu` reaches zero, `tau_w` is the first ES-46 boundary hit by either forced weight, and `tau_U` is the first actuator/input-boundary exit. Redundant members are harmless because `D_min`/the alternative admissibility section already contains the corresponding physical and funnel conditions. The privacy conclusion is only on `[t_seed,tau_priv)` and stops at `T_s` if that occurs first.

## 5. Maximal continuation interval

Let `J_alt=[t_seed,tau_max)` be the maximal connected interval containing the PO-04 seed on which:

1. the frozen alternative plant/controller ODE has an absolutely continuous solution;
2. the chosen private paths satisfy ES-45 and the forced weights satisfy ES-60--ES-61;
3. `X_alt(t) in D_alt(t)` and all complete public messages satisfy `p'(t)=p(t)`;
4. the Version 2.2 schedule margin is available, hence `t<T_s`.

By construction, `tau_max<=tau_priv`. PO-05 proves that no unexplained finite termination can occur while all these strict conditions hold.

## 6. Restart and local-extension argument

Fix any `t_0 in J_alt` with `t_0<tau_priv`. Strict interiority gives positive distances at `t_0` from every `z'=0`, ES-46, funnel, physical, and input boundary. The alternative independent differential equations are the frozen ES-3--ES-5 plant equations together with ES-44--ES-45 for `(p',q')`, after substituting the frozen algebraic maps ES-6--ES-12, ES-17, ES-20--ES-37, and ES-47. Along the constructed section, `p'=p` is fixed by the ES-60 identity, while the private paths are the selected `C^1` paths from PO-04 and their local continuation.

On a compact neighborhood strictly inside `D_alt(t_0)`, the PPC maps are locally Lipschitz because `rho>0` and `|sigma|<1`; power-flow/load maps are `C^1`; graph maps are affine; and the privacy vector-field products `g'z'` are the continuous 1-Lipschitz saturation products. The time schedules, uncertainty, and `gamma_priv` are measurable and locally essentially bounded, exactly as required by the frozen Caratheodory audit. The forced weights are measurable and locally bounded because their denominators have positive distance from zero and their numerators are locally bounded.

Therefore the same Caratheodory local existence/uniqueness theorem used by PO-16A supplies an extension on `[t_0,t_0+delta)` for some `delta>0`. ES-60 preserves the nominal `dot(p)` from the same public initial value at `t_0`; ES-61 preserves the selected `dot(q')`. Thus the complete public history continues to match, not merely one agent's message.

## 7. Denominator and weight audit

For every strict interior time in `J_alt`,

```text
|z_j'^nu(t)| > 0,
gamma_priv,j^nu(t) >= eta_{gamma,j}^nu > 0,
|g_j'^nu(t)z_j'^nu(t)|
  = min(|z_j'^nu(t)|,gamma_priv,j^nu(t)) > 0.
```

Consequently ES-60 is algebraically legal. ES-61 is legal because its denominator is `z_j'^nu(t)`. The quotient numerators are locally bounded on each compact interior neighborhood. Since PO-04 starts the continuation with strict weight margins and the weight functions are continuous in the local continuation parameter/time wherever the quotients are legal, the weights remain strictly inside ES-46 until `tau_w`; no permanent interiority is asserted.

## 8. Termination-mode classification

| Event | Classification under PO-05 |
|---|---|
| `z_j'^nu -> 0` | Legitimate first privacy-domain exit; validity is asserted only before it. |
| `gamma_priv -> 0` | Excluded on `[0,T_s]` by `gamma_priv>=eta_gamma`; `T_s` is the stopping boundary, and no post-`T_s` claim is made. |
| `w_12'` reaches an ES-46 endpoint | Legitimate first weight-domain exit; no all-time weight invariance is required. |
| `w_21'` reaches an ES-46 endpoint | Same legitimate first-exit event. |
| Physical/funnel/input boundary | Legitimate `tau_exit^alt`/`tau_U` event already retained by LOCAL-BEFORE-EXIT. |
| `T_s` reached | Legitimate finite-seed stopping event. The Version 2.2 lower margin is not extrapolated. |
| Loss of ODE existence while all strict margins remain | Not an admissible unresolved interior failure: the compact-interior Caratheodory extension contradicts maximality. |
| Other frozen singularity (`rho=0`, `|sigma|=1`, undefined power/load map) | Already a `D_min`/physical/PPC first-exit boundary, not a hidden continuation claim. |

## 9. Maximality conclusion

Assume `tau_max<tau_priv`. If the alternative trajectory remained in a compact subset of `D_alt` with positive distances from all listed boundaries, the local extension in Section 6 would continue it beyond `tau_max`, contradicting maximality. If no such compact interior subset exists, at least one strict defining margin tends to its boundary; by the definitions above this is exactly one of `tau_exit^alt`, `tau_z`, `tau_w`, `tau_U`, or `T_s`. Hence the only finite termination mechanisms are the retained stopping events.

This is a first-exit result, not a proof that the trajectory reaches `T_s`, avoids `z'=0`, remains inside ES-46 forever, or continues globally.

## 10. Network and observation consequences

The construction remains network-wide. At every restart, all neighboring public trajectories are the fixed nominal `p_j`; the perturbed physical states solve the same coupled ES-1--ES-12 dynamics; private paths and weights may differ but remain hidden; and `H_c`, graph/reference/schedule metadata, and public controller parameters remain unchanged. ES-59/ES-60 preserve every `p_j`, so ES-14--ES-16 give identical complete passive public history on `J_alt`.

## 11. Final status

- **Outcome:** **A — PO-05 PROVED locally up to the retained stopping boundary.**
- **PO-04:** **PROVED** and used as the seed input.
- **PO-05:** **PROVED** on `[t_seed,tau_priv)` in the strict regular alternative domain.
- **Blueprint / architecture change:** **NO**.
- **Controller, ES equations, Lyapunov, states, observation model, theorem scope:** unchanged.
- **Global continuation, all-time `z'` separation, post-`T_s` validity, and global privacy:** not claimed.

## 12. Recommended next task

`task-017-final-proof-chain-and-manuscript-readiness-audit`

This should audit the remaining OPEN proof obligations and the exact local theorem claim before any manuscript LaTeX work. It must not retroactively strengthen PO-05 into a global invariance result.
