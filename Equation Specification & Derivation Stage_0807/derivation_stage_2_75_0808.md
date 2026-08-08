# Derivation Stage 2.75 0808

> Task ID: `task-001-proof-dependency-decycle`
> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Scope: proof-dependency decycling before PO-07

## 1. Decision summary

The former proof ledger mixed three different mathematical statements:

1. local existence of a solution while the vector field is defined;
2. bounded estimates on a compact set selected for bootstrapping;
3. forward continuation and invariance of the operating region.

That conflation created the principal cycle

```text
PO-16 -> PO-03 -> PO-07 -> PO-13 -> PO-16.
```

The repair splits the former PO-16 into:

- `PO-16A`: local existence/uniqueness and selection of a compact bootstrap set;
- `PO-16B`: forward continuation and exclusion of all relevant exit boundaries.

`PO-13` is moved before `PO-07`. It is a design-domain feasibility check on the bootstrap set, not a theorem consequence and not a premise of local existence. `PO-07` may begin after `PO-16A`, `PO-03`, `PO-02A`, `PO-06`, `PO-08`, `PO-09`, `PO-10`, and `PO-13` have supplied their stated prerequisites; `PO-02B` is intentionally later.

No ES equation, controller, privacy mechanism, graph model, PPC transformation, or theorem number changes.

## 2. Mathematical domains

### 2.1 Admissible open domain

Let `D_open` denote the intersection of the open physical operating region, the strict funnel interior `|sigma_i|<1`, the regular privacy-state domain, and the domains on which the denominators and smooth load/power-flow terms in ES-1--ES-82 are defined. `D_open` is an open domain for the frozen vector field. It is not asserted to be invariant.

The regularity content needed for local existence is already part of Assumptions 1--2: positive plant coefficients, differentiable bounded loads on the declared region, fixed graph data, positive privacy rates/weights, and admissible initial funnel values. No actuator feasibility conclusion is inserted into this local statement.

### 2.2 Compact bootstrap set

Choose a compact set `K_0` such that the initial closed-loop state lies in its interior and `K_0` is compactly contained in `D_open`. This is a proof construction, not an invariant-set assumption. Its existence follows from the openness of `D_open` and the finite admissible initial state; its numerical size and input margin are checked by PO-13.

All bounds used before PO-07 are explicitly local bounds on `K_0`. In particular, a bound on `dot(c_i)` over `K_0` is not a global trajectory bound and does not imply that the trajectory remains in `K_0`.

### 2.3 Local maximal interval

PO-16A supplies a unique local solution on a maximal interval `[0,tau_max)`, with the solution remaining in `D_open` until the first exit time. The first exit can only be addressed later by PO-11 and PO-16B. This is the point that was missing when the former PO-16 was used simultaneously for local existence and global invariance.

## 3. Cycle audit before repair

The old ledger had these dependency edges, where an arrow points from a prerequisite to the obligation that uses it:

```text
PO-16 -> PO-03 -> PO-07 -> PO-13 -> PO-16
PO-16 -> PO-08 -> PO-07
PO-16 -> PO-09 -> PO-07
```

The nontrivial strongly connected component was `{PO-02, PO-03, PO-07, PO-08, PO-09, PO-10, PO-13, PO-16}`. The first cycle count is therefore **1 nontrivial SCC**. Its principal cycle is the four-node loop shown above; PO-02 and PO-08--PO-10 are in the same SCC because they provide alternate paths into PO-07.

The direct logical error was:

- PO-03 claimed a bound on an invariant operating set while PO-16 supplied that invariance only after PO-13;
- PO-13 required PO-07 through ES-102/composite closure;
- PO-07 required PO-03 and PO-08--PO-10;
- PO-16 required PO-13.

This was a proof-dependency error, not an equation or architecture contradiction.

## 4. Revised obligation semantics

### PO-16A: local well-posedness

PO-16A proves local existence and uniqueness of the frozen ES-1--ES-82 vector field on `D_open`, identifies the maximal local interval, and permits selection of `K_0`. It depends only on regularity and admissibility conditions. It does not require PO-03, PO-07, PO-11, PO-12, PO-13, or PO-16B.

### PO-03: provisional command-rate bound

PO-03 is evaluated on `K_0` before any invariance conclusion. Compactness of `K_0`, regularity from PO-16A, PO-06 graph bounds, and the declared uncertainty/privacy bounds provide finite local constants for `dot(c_i^V)` and `dot(c_i^omega)`. The result is a provisional estimate valid up to the first exit time.

### Residual-envelope dependency clarification

The former aggregate `PO-02` is split into two claims with different logical strength. `PO-02A` uses `PO-01` and the finite command-rate estimate from `PO-03` to derive the exact variation-of-constants representation and a finite residual/convolution bound on `K_0`. It is valid only up to the first exit time and does not imply `gamma_priv(t)->0`.

`PO-02B` is the later obligation that proves ES-51 and `gamma_priv(t)->0`. It must use a genuine command-rate decay result obtained after the composite closed-loop analysis and continuation chain (`PO-07`, `PO-11`, `PO-16B`); the uniform PO-03 bound is explicitly insufficient. No new assumption is introduced to replace this proof.

This split removes the hidden dependency because PO-07 consumes only the finite local estimate `PO-02A`, while the asymptotic envelope `PO-02B` is placed after `PO-16B`. Any post-deadline or sharing statement that requires ES-51 remains downstream of PO-02B. No controller equation, privacy target, Lyapunov metric, theorem number, or Blueprint item is changed; Blueprint Reopen Required remains **NO**.

### PO-10

PO-10 uses PO-01 and PO-03 to close the privacy Lyapunov inequality. It does not require global continuation or PO-07.

### PO-08 and PO-09

The voltage and frequency Lyapunov chains are pointwise estimates on `K_0`. Their dependency is changed from the aggregate PO-16 to PO-16A. Their status remains conditional because later continuation still needs PO-11 and PO-16B, but their local algebra does not depend on those later obligations.

### PO-13: pre-PO-07 design feasibility

PO-13 verifies that a nonempty design choice exists on `K_0` satisfying the initial funnel condition, voltage gain conditions, residual allocation, actuator set membership, and the local command/residual bounds. ES-102 and PO-07 are deliberately excluded from its prerequisites. The check may restrict the admissible gain/deadline region; it does not claim composite Lyapunov negativity.

### PO-07: composite gain closure

PO-07 starts only after PO-13 has shown that the design domain is nonempty and after PO-03, PO-08, PO-09, and PO-10 have supplied local coefficients. It then chooses the remaining Young/gain allocations so that `a_cl>0` on `K_0`. It is not used to prove the existence of `K_0` or to justify actuator feasibility.

### PO-11: barrier before exit

PO-11 uses the local solution from PO-16A, the local Lyapunov inequalities, PO-07, and PO-13 to exclude a finite-time prescribed-performance boundary hit before the local exit time. It proves a barrier statement only; it does not silently promote `K_0` to an invariant set.

### PO-16B: forward continuation

PO-16B uses PO-16A, PO-11, PO-07, and PO-13 to exclude exit through the remaining physical operating-region, denominator, privacy-admissibility, and actuator boundaries. It is the first obligation allowed to conclude forward continuation and persistence in `Delta`. It does not depend on PO-12, PO-14, or PO-15, so no theorem-level conclusion is used to establish well-posedness.

## 5. Acyclic proof DAG

The revised proof DAG is:

```text
PO-01 ----------------------> PO-02A ---------------------> PO-10 --+
                                  ^                         |          |
PO-16A -> PO-03 -----------------+                         |          |
    |                             |                         v          |
    +-------------------------> PO-08 -----------------> PO-07 ------+
    |                             |                         ^          |
    +-------------------------> PO-09 ---------------------+          |
    |                                                                |
    +-------------------------> PO-13 ------------------------------+
PO-06 -----------------------> PO-08, PO-09, PO-07

PO-07, PO-08, PO-09, PO-13, PO-16A -> PO-11 -> PO-16B
PO-16B -> PO-02B
PO-02A, PO-02B, PO-07, PO-11, PO-16B -> PO-12 -> PO-14
PO-04 -> PO-05 -> PO-15
PO-12, PO-14 -----------------> PO-15
```

The ordering is:

```text
PO-16A
  -> PO-03
  -> PO-02A, PO-08, PO-09, PO-10
  -> PO-13
  -> PO-07
  -> PO-11
  -> PO-16B
  -> PO-12 (after PO-02B)
  -> PO-14
  -> PO-15
```

PO-01 and PO-06 enter as independent prerequisites at the indicated points. PO-04 and PO-05 remain an independent privacy-existence branch feeding PO-15.

The second cycle count is **0 nontrivial SCCs**. The graph is acyclic because every edge points from local/bootstrap facts toward composite closure and then toward continuation and performance conclusions.

## 6. Why the split is mathematically necessary

Local existence is a theorem about the vector field in an open domain and is established before any trajectory-bound conclusion. Forward invariance is a theorem about excluding the maximal-solution exit set and therefore requires estimates generated by the controller design. Treating both as one PO-16 forces the local estimate PO-03 to depend on a result that it is itself needed to prove.

Similarly, actuator feasibility is existential design information. It can be checked on `K_0` before PO-07 by evaluating the frozen controller and its known local bounds. It cannot be defined through ES-102, because ES-102 is the output of the composite gain proof. Moving PO-13 before PO-07 is therefore a mathematical reclassification from a post-theorem consequence to a pre-theorem nonemptiness condition, not an administrative reorder.

No unsupported global invariant-set assumption has been introduced. `K_0` is compact but explicitly non-invariant until PO-11 and PO-16B are proved.

## 7. Equation impact

No ES equation changes are required. The only equation-specification edits are proof-level dependency clarifications in the equation-to-result map, the composite comparison paragraph, the freeze checklist, and revision log ER-07. ES numbering, controller equations, privacy equations, graph equations, PPC equations, and the Stage-2.5 metric repair are unchanged.

## 8. Acceptance audit

| Check | Result | Evidence |
|---|---|---|
| Directed dependency cycles | PASS | Old graph: 1 nontrivial SCC; revised graph: 0. |
| Local existence vs forward invariance | PASS | PO-16A and PO-16B have separate claims and outputs. |
| PO-03 circularity | PASS | PO-03 depends on PO-16A and `K_0`, never PO-07 or PO-13. |
| PO-13 circularity | PASS | PO-13 is checked on `K_0` and excludes ES-102/PO-07 from its prerequisites. |
| Residual-envelope split | PASS | PO-02A supplies only a finite local residual bound; PO-02B is the later ES-51 decay proof after PO-16B. |
| PO-07 start condition | PASS | PO-07 may begin after PO-16A, PO-03, PO-02A, PO-06, PO-08, PO-09, PO-10, and PO-13. |
| Unsupported assumption | PASS | `K_0` is a compact bootstrap construction, not an assumed invariant set. |
| ES equation changes | NO | Proof-level dependency statements only. |
| Blueprint Reopen Required | NO | No architecture contradiction found. |

## 9. Final status

1. Cycle count before: **1 nontrivial strongly connected component**, with principal cycle `PO-16 -> PO-03 -> PO-07 -> PO-13 -> PO-16`.
2. Cycle count after: **0 nontrivial strongly connected components**.
   For this PO-02 review specifically, the pre-repair graph had **0 explicit SCCs but 1 hidden semantic dependency**; after splitting, the explicit and semantic dependency audits both report **0 cycles**.
3. Files requiring revision: `proof_obligations_0807.md`, `equation_traceability_matrix_0807.md`, `equation_spec_0807.md`, and this Stage-2.75 report.
4. PO IDs changed: former `PO-02` split into `PO-02A` and `PO-02B`; former `PO-16` split into `PO-16A` and `PO-16B`; dependent entries PO-07, PO-08, PO-09, PO-12, PO-13, and PO-14 were redirected.
5. PO-07 may now begin: **YES, structurally and conditionally**, after `PO-02A` and its other revised prerequisites are closed; it is not yet proved.
6. Blueprint Reopen Required: **NO**.
7. Remaining hidden-dependency blocker: **PO-02B remains OPEN**; no fake ES-51 proof or strengthened assumption has been introduced.
