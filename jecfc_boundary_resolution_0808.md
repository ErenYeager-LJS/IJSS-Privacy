# JECFC Boundary Resolution 0808

> Task ID: `task-007-jecfc-boundary-resolution`
> Basis: Blueprint Freeze Version 2.0, frozen ES-1--ES-103, PO-16A, PO-07, PO-13, and the joint-exit audit

## Continuation-domain decision

The continuation domain required by the current frozen theory is:

> **a JECFC-admissible compact Lyapunov tube/sublevel domain in the full independent state space, compactly embedded in `D_min`, with strict PPC, physical-operating-region, denominator, compactness, and actuator margins.**

This is one domain concept. It is not the bootstrap ball `K_0`, not the whole open domain `D_min`, not the physical region `Delta` alone, and not the unqualified sublevel set of `mathscr V_cl`.

Among the listed candidates, this is **Candidate E: another already frozen domain**, namely the JECFC proof/design domain already specified by the joint-exit audit.

## Why the other candidates are insufficient

| Candidate | Decision | Mathematical reason |
|---|---|---|
| `K_0` only | Rejected | `K_0` is constructed for local well-posedness and finite local constants. It is explicitly not forward invariant. |
| Any compact subset of `D_min` | Rejected as the continuation domain | ES-102 can be instantiated on any such compact set, but each instantiation supplies new local constants. This describes local regularity, not one invariant domain. |
| `Delta` | Rejected as the sole domain | `Delta` is the compact physical operating region used for model regularity and bounded physical functions. The frozen theory does not prove its forward invariance, and it says nothing by itself about PPC singularities, privacy trackers, or actuator margins. |
| Unqualified `mathscr V_cl` sublevel set | Rejected | `mathscr V_cl` is coercive in the analysis vector `xi`, not in every independent coordinate. In particular, `delta_i` has no Lyapunov block, and tracker coordinates are only indirectly reconstructed through compact-dependent command bounds. A bare sublevel need not be compact in the full independent state space. |
| JECFC-admissible compact tube/sublevel domain | **Selected** | It is the only already-specified proof object that combines the ES-102 comparison region with strict distance from every named exit boundary and full-state compactness. |

## `Delta` interpretation

Under the frozen Blueprint, `Delta` is the **physical admissible operating region** and a **proof-domain ingredient**, but not the complete continuation domain.

It supplies the physical neighborhood on which the plant, load, and power-flow functions have the declared regularity and bounds. Membership in `Delta` is part of the open admissible domain `D_min`. Nothing in the current proof turns this declaration into forward invariance. Therefore saying that a trajectory is analyzed “on `Delta`” is a domain restriction, not a continuation result.

## State coverage required for continuation

Continuation must keep every independent coordinate finite and inside the relevant strict domain margins:

- physical coordinates: `V_i`, `dot(V_i)`, `omega_i`, and `delta_i`;
- privacy tracker coordinates: `p_i^V`, `q_i^V`, `p_i^omega`, and `q_i^omega`.

The transformed errors, backstepping error, public-private differences, residuals, commands, and graph errors are derived or analysis coordinates. They must remain finite because they preserve the domain and feed the controller, but they do not replace the independent-state continuation test.

`delta_i` must be bounded as a physical phase coordinate under the compact operating-domain contract. Bounding only the relative phase terms appearing in power flow is insufficient for the frozen reduced ODE because `delta_i` is an independent coordinate and no frozen identity reconstructs its absolute value from `xi`. The physical operating-domain margin must therefore cover the allowed phase-coordinate representation (or its already-frozen admissible phase chart); this is a continuation requirement, not a new Lyapunov term.

The privacy tracker coordinates need not receive new quadratic blocks in `mathscr V_cl`: the frozen reconstruction identities and compact-domain command bounds can bound them on the selected tube. That indirect argument is valid only after the full tube and its margins have been established.

## JECFC boundary meaning

JECFC is not a new controller assumption and not a proof of PO-11 or PO-16B. It is the boundary specification for the domain on which ES-102 is intended to be applied in a continuation argument. Its missing part is the existence of one compact tube satisfying all of the following simultaneously:

1. initial-state inclusion with positive Lyapunov-level slack;
2. compact containment in the strict open domain `D_min`;
3. a positive PPC interior margin, keeping every funnel transformation regular;
4. a positive physical margin from the boundary of `Delta`;
5. a positive margin from every retained denominator/singularity;
6. a positive actuator margin for every admissible control input;
7. finite, consistently instantiated ES-102 constants on the same tube.

The current frozen results establish local estimates that could be tested on a proposed tube. They do not establish the existence or forward invariance of such a tube. In particular, compactness of `Delta`, local feasibility on `K_0`, and coercivity in `xi` cannot be substituted for that existence statement.

## Architect recommendation

**Revise theorem wording.**

The current theorem boundary must remain local-before-exit until a JECFC-admissible compact tube is independently established. Do not resume PO-11 or PO-16B by treating JECFC as already available. No Blueprint review is required: the audit identifies a missing continuation-domain certificate and a theorem-boundary limitation, not a controller or architecture contradiction.
