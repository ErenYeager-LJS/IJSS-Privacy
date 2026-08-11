# Derivation Stage 5: PO-04 Privacy Alternative Existence Audit

> Task ID: `task-015-po04-privacy-alternative-existence-v2-2-domain`
> Active architecture: Blueprint Version 2.2, Privacy-Schedule Regularity Revision
> Theorem boundary: `LOCAL-BEFORE-EXIT`
> Scope: PO-04 only; PO-05 is not started

## 1. PO-04 statement and verdict

PO-04 asks whether, for a nominal admissible realization, there is a coupled local family containing a genuinely non-nominal protected initialization `S' != S`, with identical complete passive public history and admissible private weights before the earliest finite-seed or regular-domain exit.

**Outcome B — PO-04 remains blocked; architecture review required.** The Version 2.2 schedule margin repairs the Task-013 reciprocal-schedule obstruction, but the frozen assumptions do not establish a nonzero reachable perturbation of the protected command initialization for the same plant/controller. No alternative realization or positive perturbation radius is therefore proved, and the proof-obligation ledger remains unchanged.

## 2. Exact assumptions used

The audit uses only the existing Version 2.2 contracts:

- nominal `|z_j^nu(0)| >= eta_{z,j}^nu > 0` on affected pairs;
- nominal private weights have strict ES-46 interior margin `eta_{w,j}^nu`;
- `gamma_priv,j^nu(t) >= eta_{gamma,j}^nu > 0` on `I_s=[0,T_s]`;
- the residual regularity/decay target and passive-eavesdropper observation model;
- Assumption 1 plant regularity, initial funnel feasibility, fixed graph, and local operating-domain regularity.

These are nominal/domain conditions. None asserts an alternative initial plant state, a command-map rank condition, a nonzero perturbation radius, or invariance of the alternative trajectory.

## 3. Perturbation parameterization

For affected channels, write

```text
S_i' = S_i + delta_i,
delta_i = [delta_i^V, delta_i^omega]^T.
```

ES-58 and ES-41 then force

```text
p_i'(0) = p_i(0),
q_i'(0) = 2S_i' - p_i(0) = q_i(0) + 2delta_i,
z_i'(0) = p_i'(0)-q_i'(0) = z_i(0)-2delta_i,
c_i'(0) = c_i(0)+delta_i.
```

Consequently `r_i'(0)=0` whenever the alternative physical/controller initial state actually realizes `c_i'(0)=S_i'`. This last realization condition is the unresolved step; it is not implied by ES-58.

For `|delta_i^nu| < eta_{z,i}^nu/2`, the algebraic candidate satisfies `|z_i'^nu(0)| >= eta_{z,i}^nu/2`. This is only zero-time candidate feasibility.

## 4. Zero-time ES-60 audit

At `delta=0`, the candidate is nominal and ES-60 returns `w_{i,21}'(0)=w_{i,21}(0)` whenever the nominal denominator is legal. If a genuine alternative physical initial state depended continuously on `delta`, then the Version 2.2 lower margin and the split margin would give, on a sufficiently short candidate interval,

```text
|g_i' z_i'| >= min(eta_{z,i}^nu/4, eta_{gamma,i}^nu) > 0.
```

The strict nominal ES-46 interior margin would then make the quotient continuous at `delta=0`, provided `c_i'`, `z_i'`, and the selected private path are continuous in `delta`. Version 2.2 supplies the denominator schedule margin, but it does not supply the required physical initial-state-to-command map or its continuity/rank property.

## 5. Zero-time ES-61 audit

ES-61 gives

```text
w_{i,12}'(0)
 = [dot(q_i'(0))-lambda_tr,i(c_i'(0)-q_i'(0))]/z_i'(0).
```

At the nominal point this equals `w_{i,12}(0)` if `dot(q_i'(0))=dot(q_i(0))`. A continuous choice of `dot(q_i')` with this nominal value would preserve the strict ES-46 interior margin for sufficiently small `delta`. However, the frozen equations do not prescribe a free private path independently of the actual alternative command trajectory; the path and its derivative must coexist with the same coupled plant/controller. Thus this is a conditional local quotient argument, not an existence proof.

There is no unavoidable jump caused by the Version 2.2 schedule margin. The remaining issue is existence of a compatible alternative trajectory, not the pointwise value of `gamma_priv`.

## 6. Conditional continuity and radius calculation

Suppose, in addition to the frozen documents, that a coupled initial-state selection map `X_0(delta)` existed with

```text
c(X_0(delta),p(0)) = c(0)+delta,
```

and that the resulting reduced vector field and private-path construction were continuous in `(delta,t)` on a common local nonsingular tube. Then the maps `delta -> c'(t;delta)`, `delta -> z'(t;delta)`, `delta -> w_21'(t;delta)`, and `delta -> w_12'(t;delta)` would be continuous at `delta=0`.

Let `m_z=eta_z/2`, `m_gamma=eta_gamma`, and `m_w=eta_w` denote the available strict margins after selecting a compact candidate tube. A positive radius could then be defined by the first `delta` for which any of `|z'|-m_z`, `|g'z'|-min(m_z/2,m_gamma)`, `w_12'-underline(w)-m_w`, or `bar(w)-m_w-w_21'` reaches zero. This would be a legitimate `delta_* > 0` only after the missing initial-state selection and coupled trajectory maps had been constructed. The current theory supplies none of these maps, so this conditional radius cannot be reported as a proved constant.

## 7. Missing command-initialization reachability

The protected datum is the value of the controller command itself, but ES-28 and ES-31 define that command from physical states, funnel variables, distributed errors, and public messages. The frozen assumptions require regularity and admissibility of those states; they do not require that the map from admissible physical initial states to `c(0)` have a nonzero local image in every protected channel.

This is a genuine logical gap. For example, in an admissible frequency specialization with constant power terms and `k_c^omega b_i=1`, the coefficient of `(omega_i(0)-omega_ref)` in ES-31 cancels between `tau_Pi F_i^omega` and the pinned error term. With public `p` fixed, the command can therefore be locally insensitive to the physical frequency initial state. The frozen assumptions do not exclude this rank-degenerate case. Hence they cannot imply the existence of any `delta_i^omega != 0` satisfying `c_i'(0)=c_i(0)+delta_i^omega`.

The same issue is not repaired by choosing `q_i'(0)` in ES-58: that changes the private decomposition but does not change the physical/controller command generated by ES-28/ES-31.

## 8. Coupled network and public-history audit

Changing one protected command generally changes physical trajectories and therefore commands at electrically and cyber-coupled agents. Complete public-history equality requires `p_j'=p_j` for every agent and channel, because ES-14--ES-16 expose the network-wide message history. The required family is therefore a coupled network construction unless a smaller affected set is proved closed.

The current assumptions retain network-wide affected scope but provide neither a joint command-map surjectivity/rank condition nor a proof that the algebraic/dynamic constraints induced by all neighboring agents have a nonzero solution. Treating one agent as isolated would contradict ES-20--ES-21 and the explicit Version 2.2 affected-scope rule.

The actual observation map also includes `H_c`, graph/reference/schedule metadata, and public controller parameters. Physical sensor histories and private memory are excluded. Matching one `p_i` is insufficient, and no metadata change may hide a failure of ES-59.

## 9. Plant/controller compatibility and PO-05 boundary

PO-16A supplies local existence for a selected admissible initial state of the frozen system. It does not prove that an admissible initial state with a prescribed nonzero command displacement exists, nor does it solve the coupled initial-value reachability problem above. Algebraically selecting `p'`, `q'`, and quotient weights without such a state would not be an alternative realization of ES-1--ES-12.

If a reachable initial state and coupled local solution were supplied, the nonzero `z'(0)` margin plus local continuity could define a short first-exit interval on which ES-60--ES-61 are legal. That local construction is the PO-04 boundary. General denominator continuation, isolated-zero extensions, or persistence beyond that interval remain PO-05 and are not used here.

## 10. Quantifier result

The current theory establishes neither a nonzero radius `delta_*` for every `0<|delta|<delta_*` nor even one non-nominal admissible `delta` for the frozen coupled plant/controller. The nominal point `delta=0` is not sufficient because it is not a privacy alternative.

## 11. Architecture and proof status

- **Outcome:** **B — PO-04 STILL BLOCKED, ARCHITECTURE REVIEW REQUIRED**.
- **Architecture changed in Task-015:** **NO**.
- **Controller, ES equations, Lyapunov design, state definitions, observation model:** unchanged.
- **PO-04:** **OPEN / NOT PROVED**.
- **PO-05:** **OPEN / NOT STARTED**, downstream of PO-04.
- **Blueprint Reopen Required:** **YES**, but only for a future review of a defensible command-initialization reachability/domain condition. No such condition is introduced here.

## 12. Recommended next task

`task-016-privacy-command-reachability-architecture-review`

That task should decide whether a mathematically legitimate local reachability/domain condition can be added without changing ES-58--ES-61, or whether the privacy target must be narrowed. It must not begin PO-05.
