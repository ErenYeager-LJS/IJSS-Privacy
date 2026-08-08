# Theory Boundary Review 0808

> Task ID: task-005-theory-boundary-resolution
> Scope: architecture-level proof audit only
> Baseline: latest `origin/main` after task-004

## Single conclusion

**Category B: the current frozen theory proves a weaker theorem than the intended Theorem 1.**

The strongest result currently supported is a **local-before-exit closed-loop result**: for an admissible initial condition in `D_min`, the reduced closed loop has a unique Caratheodory solution on a nontrivial maximal local interval; while that solution remains in a selected compact bootstrap subset, the frozen PPC coordinates and controller are regular, the component Lyapunov inequalities and ES-102 comparison inequality hold with compact-dependent constants, the privacy difference/residual quantities have the proved local bounds, and the actuator inequalities are symbolically feasible on the PO-13 bootstrap design region.

The current theory does not prove that the solution remains in that compact region, remains in the physical operating region, preserves actuator feasibility for all future time, keeps every PPC error strictly inside its funnel for the whole maximal trajectory, or admits global-in-time continuation.

## Audit findings

### 1. Independent state coverage

`X_min` contains the physical coordinates `(V_i,dot(V_i),omega_i,delta_i)` and the four privacy tracker coordinates. `mathscr V_cl` is a metric on transformed voltage/frequency errors, the voltage backstepping error, privacy difference states, and residual states. The remaining independent coordinates are handled only through algebraic reconstruction, local compact-domain bounds, or the declared physical operating domain. The current proof does not establish one invariant compact set covering all independent coordinates.

### 2. Composite Lyapunov coverage

PO-07 proves ES-102 locally on a selected compact subset such as `K_0`. Its metric coercivity and disturbance constants are compact-dependent. ES-102 therefore supplies a valid local comparison inequality, but not a global properness or continuation certificate for the full independent state.

### 3. Operating-region assumptions

`Delta` is declared as a compact admissible operating region and supplies bounded model functions and a domain for local analysis. The frozen documents do not prove that the closed-loop trajectory remains in `Delta`. Declaring the region is not equivalent to proving its forward invariance.

### 4. Physical-state assumptions

Physical regularity, bounded uncertainty, and admissible initial operation are sufficient for PO-16A local well-posedness. They do not exclude a later exit through the boundary of `Delta` or loss of compactness. In particular, the existing local result must stop at the first admissible-domain exit.

### 5. Actuator assumptions

PO-13 establishes symbolic actuator feasibility on its bootstrap design region. It does not prove that the trajectory remains in that region or that actuator margins persist along an extended trajectory. Consequently actuator feasibility is available only within the local design-domain statement.

### 6. Continuation assumptions

PO-16A supplies the local Caratheodory solution and the continuation alternative. PO-16B remains open. The Joint Exit-Continuation Lemma from task-004 is conditional on JECFC, whose required invariant compact sublevel/tube has not been established. No unconditional forward continuation result is currently available.

### 7. Residual assumptions

PO-02A proves a finite local residual convolution bound. PO-02B remains open, so ES-51 residual decay and any asymptotic consequence depending on it are unavailable. Theorem 1 cannot use a decaying privacy residual as an established fact.

## Minimal theorem boundary

The current mathematical boundary is:

> Local existence, uniqueness, controller/PPC regularity, compact-dependent Lyapunov comparison, finite local privacy residual bounds, and symbolic actuator feasibility hold only up to the first exit from the selected admissible bootstrap domain.

Anything beyond this boundary requires an unproved result: funnel-boundary exclusion, physical/actuator-domain persistence, global continuation, or residual decay.

This is a boundary statement, not a rewritten theorem.

## Missing ingredient

The missing ingredient is a valid, noncircular exit/continuation closure establishing a forward-invariant admissible compact set or equivalent persistence result with physical, PPC, actuator, denominator, and disturbance margins. The current theory names this requirement through JECFC but does not prove it. PO-02B is a separate downstream missing ingredient for residual-decay claims.

## Required decisions

- Blueprint must change: **NO**. No architectural contradiction has been established.
- Controller must change: **NO**. The audit identifies a proof boundary, not a control-law defect.
- Theorem wording must change: **YES**, if a theorem is stated before the missing continuation and residual obligations are closed. It must remain within the local-before-exit boundary above.
- Equations must change: **NO**.
- Proof obligations must change: **NO**.

## Recommended next engineering task

Align the theorem/claim ledger with the local-before-exit boundary and identify every downstream result that currently consumes PO-11, PO-16B, or PO-02B. This should be a claim-traceability audit, not a proof extension or controller redesign.
