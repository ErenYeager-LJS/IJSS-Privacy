# Derivation Stage 6: JECFC Feasibility Audit

> Task ID: task-005-jecfc-feasibility
> Branch: task-005-jecfc-feasibility
> Blueprint Freeze Version 2.0

## Decision

**Case B: the current frozen theory cannot prove JECFC.**

This is a feasibility audit, not a controller or equation redesign. No equation, state, metric, PPC transformation, graph, privacy mechanism, or Blueprint item is changed. PO-11 and PO-16B remain `OPEN`.

## 1. JECFC requirements

JECFC asks for a level `c` such that

```text
Omega_c = {X_min in D_min : mathscr V_cl(X_min) <= c}
```

is compactly contained in `D_min`, has strict physical and actuator margins, and supports finite local constants with a practical boundary condition such as

```text
bar d_K(T) < a_cl(K)c.
```

The five requirements are logically distinct:

| Requirement | Current result | Audit conclusion |
|---|---|---|
| PPC funnel interior | `zeta=atanh(sigma)` is regular only for `|sigma|<1`; `h_bar` is finite on a compact interior subset | Local regularity is proved, but a compact sublevel with a uniform funnel margin is not established |
| Physical operating region | `Delta` is declared compact and `D_min` uses its interior | Compactness of `Delta` does not imply trajectory invariance or sublevel containment |
| Actuator feasibility | PO-13 verifies `u_i in U_i` on its bootstrap design region `K_0` | No forward feasibility outside `K_0` is proved |
| Regularity | PO-16A gives local Caratheodory well-posedness on `D_min` | This supports local continuation only, not a global compact tube |
| Disturbance admissibility | `R`, private weights, and `gamma_priv` are locally essentially bounded | Bounds are compact/time-window dependent; no uniform all-domain certificate is available |

## 2. Independent-state coverage

The independent state from PO-16A is

```text
X_min = col_i(V_i,dot(V_i),omega_i,delta_i,
             p_i^V,q_i^V,p_i^omega,q_i^omega).
```

| Independent variable | Controlled by `mathscr V_cl`? | Indirect information | Remaining requirement |
|---|---|---|---|
| `V_i` | Partly | `zeta^V` bounds `V_i-V_ref` only while funnel constants are valid | Funnel and physical-domain margin |
| `dot(V_i)` | Partly | `chi^V=dot(V_i)-alpha^V`; `alpha^V` is a derived quantity | Compact regularity of the controller map |
| `omega_i` | Partly | `zeta^omega` bounds `omega_i-omega_ref` only inside the funnel | Funnel and physical-domain margin |
| `delta_i` | No direct quadratic term | Appears in electrical power flow and may accumulate through `dot(delta_i)` | Independent operating-region/phase margin |
| `p_i^V,q_i^V` | No direct quadratic block | `p^V=c^V+r^V+0.5z^V` and `q^V=c^V+r^V-0.5z^V`, so they are indirectly bounded if the PO-06 command bound is valid | Compact physical/PPC bounds needed by the command estimate |
| `p_i^omega,q_i^omega` | No direct quadratic block | The same reconstruction from `c^omega,r^omega,z^omega` applies | Compact physical/PPC bounds needed by the command estimate |

Thus `mathscr V_cl` is coercive in the analysis vector `xi`, not in all coordinates of `X_min`. The uncontrolled `delta` direction alone prevents a conclusion that every `mathscr V_cl` sublevel is compact in `X_min`; the tracker coordinates additionally require compact-dependent command bounds rather than direct metric coercivity.

## 3. Sublevel-set compactness

The frozen metric relation is only

```text
m_V ||xi||^2 <= mathscr V_cl <= M_V ||xi||^2
```

on a selected compact subset. It does not provide a proper, radially unbounded function of `X_min`. The map from `X_min` to `xi` has an uncontrolled `delta` direction, while the tracker coordinates are only indirectly bounded through compact-dependent command estimates. Therefore a set defined only by `mathscr V_cl<=c` can be noncompact in `X_min` or can approach `partial D_min` through those directions.

The compact bootstrap set `K_0` supplied by PO-16A avoids this problem by construction, but PO-16A explicitly does not make `K_0` invariant. The existence of a larger compact `Omega_c` with all required margins is exactly the missing JECFC statement, not a consequence of the current Lyapunov inequality.

## 4. Operating-region audit

`Delta` is declared as a compact admissible operating region in the frozen variable contract, and `D_min` uses its interior. This gives bounded model functions and local regularity when a trajectory is already known to remain in `Delta`. It does not prove that the physical trajectory remains in `Delta`. The phase coordinate `delta` is not controlled by `mathscr V_cl`, so compactness of `Delta` cannot be converted into a Lyapunov sublevel inclusion or forward invariance result.

Restricting a theorem by saying “for trajectories evolving inside `Delta`” would be a claim restriction, not a proof of the required continuation. It would not establish JECFC and would not discharge PO-16B.

## 5. Actuator audit

PO-13 verifies simultaneous strict inequalities and `u_i in U_i` for all states in the selected bootstrap design region `K_0`. It is explicitly not a consequence of ES-102 and does not assert global actuator invariance. Since the current `mathscr V_cl` does not control every independent state direction, no implication

```text
mathscr V_cl <= c  =>  u_i in U_i
```

is available for a new sublevel set. A forward actuator margin must therefore be supplied by an additional, currently unproved design-domain result.

## 6. Decision and status

The current frozen theory proves the local ingredients needed to test JECFC on a proposed compact set, but it does not prove existence of a compact set satisfying all JECFC requirements. The exact missing hypothesis is a compact admissible tube/sublevel condition that controls the unpenalized independent coordinates and preserves actuator margins, together with the corresponding `Q_cl` and disturbance inequality.

Therefore:

- JECFC decision: **B — current theory cannot prove JECFC**.
- PO-11: **OPEN**.
- PO-16B: **OPEN**.
- PO-02B: **OPEN**.
- Need theorem restriction: **NO**; a restriction to trajectories already in `Delta` would not prove continuation.
- Blueprint Reopen Required: **NO**.
- Controller redesign: **NO**.
- Equation redesign: **NO**.

The next mathematically meaningful task is to establish a defensible compact admissible tube that also bounds `delta`, the compact-dependent tracker/command terms, and actuator margins, or to narrow the theorem claim explicitly to a local-before-exit statement. That decision requires a separate task; it is not silently assumed here.
