# Local Theorem Claim-Scope Alignment 0808

> Task ID: `task-009-local-theorem-wording-alignment`
> Branch: `task-009-local-theorem-wording-alignment`
> Governing decision: Task-008 Recommendation A, FREEZE LOCAL THEOREM

## 1. Authority boundary

Blueprint Freeze Version 2.0 remains the historical baseline and records the original stronger design target. Task-012 activated Version 2.1 for the split/weight privacy-domain contract. The controlled Task-014 revision activates Blueprint Version 2.2 only for finite-seed privacy-schedule regularity and its local stopping boundary; the controller, ES formulas, Lyapunov design, theorem strategy, and local-before-exit physical boundary remain unchanged.

The final manuscript theorem scope is a separate, non-frozen claim layer:

> **LOCAL-BEFORE-EXIT.** Conclusions hold only on the maximal local solution interval while the independent trajectory remains in the strict admissible domain and, for compact-dependent estimates, within the selected compact bootstrap/design region before the first admissibility exit.

The frozen Blueprint target theorem is historical design intent. It is not evidence that its stronger continuation, invariance, deadline, sharing, residual-decay, or simultaneous-composite conclusions have been proved.

## 2. Final manuscript-facing theorem template

### Theorem 1: local-before-exit closed-loop result

Under the frozen Definitions 1-2, Assumptions 1-2, gain/regularity conditions, and an admissible initial condition in `D_min`, consider the unique maximal local solution supplied by PO-16A and the already-defined first admissibility-exit time. On every compact time interval before that exit for which the independent trajectory remains in the selected compact bootstrap/design region:

1. the retained plant, PPC, controller, reconstruction, and privacy-wrapper maps are well defined;
2. the independent and algebraically reconstructed coordinates remain finite on that compact interval;
3. the voltage, frequency, and privacy component inequalities and the ES-102 comparison inequality hold with constants instantiated on that same compact region;
4. the privacy reconstruction residual satisfies the finite local PO-02A bound, without any ES-51 decay conclusion;
5. actuator feasibility is asserted only on the PO-13 verified design region and only while the trajectory remains in that region.

No conclusion is made at or after the first admissibility exit. The theorem does not assert global continuation, all-time existence, forward invariance of `K_0`, forward invariance of `Delta`, all-time funnel invariance, unconditional denominator avoidance, all-time actuator feasibility, global state boundedness, prescribed-time deadline recovery, ES-51 residual decay, or active-power sharing.

### Privacy clause pending required proof closure

The final local manuscript must retain a local public-history indistinguishability result because privacy is a core paper claim. That clause may be appended to the local theorem or stated under the already-frozen theorem number assigned to the privacy result only after PO-04 and PO-05 are proved. Its legal scope is existence-based public-history non-uniqueness for nominal realizations in the Blueprint Version 2.2 schedule-regular privacy design domain, before the earliest of the finite seed horizon and first regular-domain exit, under the passive-eavesdropper observation model. It must not claim the historical unrestricted Version 2.0 class, the Version 2.1 schedule class without a local lower margin, global ambiguity, universal alternative realizations, transparent reconstruction, cryptographic secrecy, or protection against physical-sensor/private-memory access.

PO-04 and PO-05 are now closed for the retained local-before-exit privacy domain. The privacy observation-equivalence clause is available only on that domain: PO-04 supplies the initial/common construction interval, and PO-05 supplies continuation or compatible extension after that interval up to the retained stopping boundary. No global, post-`T_s`, or all-time denominator claim is available.

## 3. Downstream OPEN-PO classification

| PO | Current ledger status | Classification | Claim supported | Does the claim survive Route L? | Must finish before Proof Freeze? | Exact reason |
|---|---|---|---|---|---|---|
| PO-04 | PROVED | **A. REQUIRED FOR FINAL LOCAL MAIN THEOREM** | Nonempty admissible alternative private realization and public-history non-uniqueness | **YES, locally on the Version 2.2 schedule-regular privacy design domain.** The completed PO-04 construction uses an admissible physical frequency perturbation and proves a coupled family with positive local radius. | **YES** | The proof is local-before-exit and supplies the initial/common denominator-valid construction interval; PO-05 handles only continuation beyond that interval. |
| PO-05 | PROVED | **A. REQUIRED FOR FINAL LOCAL MAIN THEOREM** | Additional validity of the alternative-realization denominators or compatible extension beyond the PO-04 construction interval | **YES, after PO-04, for the retained stopping-domain portion beyond the initial/common local interval.** PO-05 does not re-prove the denominator legality already established by PO-04 on that initial interval. | **YES** | The maximal strict regular continuation argument closes the downstream interval up to first retained exit or `T_s`; no global continuation is asserted. |
| PO-12 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Practical recovery by the prescribed deadlines | **NO.** Its frozen dependency chain uses PO-11, PO-16B, and PO-02B, which Route L does not pursue. | **NO** | A local-before-exit theorem cannot guarantee existence/admissibility through the deadlines or use ES-51 decay. |
| PO-14 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Exact or practical active-power sharing | **NO.** The theorem-ready sharing claim requires PO-12, PO-02B, equilibrium closure, and residual limits. | **NO** | The required upstream performance/residual chain is outside Route L. Frozen sharing algebra remains design intent, not a final theorem. |
| PO-15 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Simultaneous privacy, persistent PPC, deadline recovery, and sharing composition | **NO.** Its frozen claim composes unavailable physical and sharing results. | **NO** | Narrowing PO-15 silently would change its frozen ledger claim. Route L retains separate local physical and, after PO-04/05, local privacy results without the stronger simultaneous guarantee. |

PO-04 and PO-05 are discharged on their stated local domains by the completed Task-015 and Task-016 derivations. The remaining classifications do not discharge any other OPEN obligation.

## 4. Manuscript claim alignment

| Claim family | Route-L classification | Allowed manuscript wording | Unavailable wording |
|---|---|---|---|
| Local closed-loop existence | **FINAL LOCAL THEOREM CLAIM** | Unique maximal local solution from an admissible initial condition, up to the first admissibility exit | Solution exists for all time; global continuation |
| Local boundedness and ES-102 | **FINAL LOCAL THEOREM CLAIM** | Finite compact-interval bounds and compact-dependent comparison while the trajectory remains in the selected region | Global boundedness; globally proper Lyapunov certificate |
| Prescribed-performance machinery | **FINAL LOCAL THEOREM CLAIM** | PPC coordinates and local inequalities are regular before exit | Forward invariance of the complete funnel; no funnel crossing for all time |
| Actuator feasibility | **FINAL LOCAL THEOREM CLAIM** | Symbolic feasibility on the PO-13 design region while the trajectory remains there | All-time actuator feasibility or saturation avoidance |
| Finite privacy residual | **FINAL LOCAL THEOREM CLAIM** | Finite PO-02A local residual/convolution bound | Residual converges to zero; ES-51 decay |
| Public-history indistinguishability | **FINAL LOCAL CLAIM** | Local existence-based non-unique reconstruction for the Version 2.2 schedule-regular privacy domain before its stopping boundary, under the frozen passive observation model, using PO-04 for initial construction and PO-05 for post-seed continuation | Historical Version 2.0 class, Version 2.1 schedules without a local lower margin, global/universal ambiguity, perfect secrecy, transparent reconstruction |
| Deadline recovery | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | May be described only as an original frozen target or unproved limitation | Recovery by `T_V` or `T_omega`; continued post-deadline boundedness |
| Active-power sharing | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Frozen equilibrium algebra may be identified as original design intent or future work | Exact sharing or a proved residual-dependent sharing bound |
| Simultaneous composite guarantee | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Separate local physical and privacy results may be reported after their own closures | One theorem simultaneously guaranteeing privacy, persistent PPC, deadlines, and sharing |
| Global continuation and domain invariance | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Explicit local-before-exit limitation | `K_0` invariant, `Delta` invariant, denominator/actuator margins persist for all time |

The public-history claim is final only within the retained local-before-exit domain. PO-04 supplies the local alternative construction and positive radius, while PO-05 supplies the post-seed regular continuation; Blueprint Version 2.2 still supplies only designer-selectable local domain margins and a stopping boundary, not invariance or global ambiguity.

## 5. Blocked stronger-theorem chain

### OPEN - BLOCKED STRONGER-THEOREM CONTINUATION CHAIN

- `PO-11`: remains OPEN; not pursued under Route L; not a prerequisite for the final local theorem.
- `PO-16B`: remains OPEN; not pursued under Route L; not a prerequisite for the final local theorem.
- `PO-02B`: remains OPEN; not pursued under Route L; ES-51 decay is excluded from the final local theorem.

These statuses are intentionally retained. They can re-enter the proof pipeline only after a future Architecture Review changes the Task-008 route decision.

## 6. Proof-pipeline consequence

| PO | Current status | Route-L relevance | Must finish before Proof Freeze? | Reason |
|---|---|---|---|---|
| PO-04 | PROVED | Local privacy construction on the Version 2.2 schedule-regular domain | **YES** | Completed by Task-015; supplies the initial/common denominator-valid construction interval |
| PO-05 | PROVED | Additional denominator validity/continuation after the PO-04 construction interval | **YES, after PO-04** | Does not re-prove PO-04's initial/common local denominator legality; closes the remaining retained stopping-domain interval by local restart/extension, up to first retained exit or `T_s` |
| PO-11 | OPEN | Stronger-theorem funnel continuation only | **NO** | Route L stops before exit |
| PO-12 | OPEN | Deadline theorem only | **NO** | Deadline claim is outside final scope |
| PO-14 | OPEN | Sharing theorem only | **NO** | Sharing claim is outside final scope |
| PO-15 | OPEN | Strong simultaneous composition only | **NO** | Composite claim is outside final scope |
| PO-16B | OPEN | Global/forward continuation only | **NO** | Route L uses PO-16A local existence |
| PO-02B | OPEN | Asymptotic residual-decay chain only | **NO** | Route L uses the finite PO-02A bound |

PO-05's downstream continuation/extension audit is complete for the retained local-before-exit domain. PO-04's initial/common local denominator legality is already proved and is not repeated by PO-05.

## 7. Manuscript-facing dependency presentation

The non-frozen final claim presentation must use the following separation:

1. PO-16A and the proved local component/composite obligations support Theorem 1 only before exit.
2. PO-04 then PO-05 support the retained local privacy observation-equivalence claim.
3. PO-11, PO-16B, and PO-02B are displayed as an intentionally inactive stronger-theorem branch.
4. PO-12, PO-14, and PO-15 remain OPEN historical/downstream targets outside the final manuscript theorem scope.

The frozen Blueprint dependency graph remains untouched and must be labeled, when referenced, as the **Frozen Blueprint target theorem** rather than the final proof-status graph.

## 8. Architecture classification

- The stopped continuation chain remains a **Proof Boundary** and **Claim Issue**, already resolved by Route L scope restriction. PO-05 closes only the privacy alternative's local regular continuation; it does not reopen the stronger continuation branch.
- The Task-010 zero-split blocker is resolved by Version 2.1, and the Task-013 schedule-reciprocal blocker is resolved at architecture level by the Version 2.2 finite-seed schedule margin. PO-04 and PO-05 are proved locally on their stated domains; neither is a premise embedded in Assumption 2.
- Architecture Review Required: **NO** for the present classification and the completed PO-04/PO-05 local proof chain.

If a later audit shows that the frozen construction is generically singular and cannot be extended without equation or assumption changes, that task must stop and report `ARCHITECTURE REVIEW REQUIRED`.

## 9. Exact next task

Recommend exactly:

`task-017-final-proof-chain-and-manuscript-readiness-audit`

Scope: audit the remaining open proof obligations and exact local theorem claim before manuscript LaTeX work. Preserve the completed PO-04 construction and PO-05 post-seed continuation result. Any future audit must stay within the retained Version 2.2 finite-seed/first-exit boundary. If extension requires another assumption, an equation change, a new state, or a privacy-mechanism change, stop and report `ARCHITECTURE REVIEW REQUIRED`.

## 10. Modification declaration

- Blueprint changed by Tasks 012 and 014: **YES, only the approved Version 2.1 split/weight domain and Version 2.2 finite-seed schedule regularity; Version 2.0 remains the historical baseline**.
- Controller changed: **NO**.
- ES equations changed: **NO**.
- Lyapunov design changed: **NO**.
- State definitions changed: **NO**.
- Assumptions changed by Tasks 012 and 014: **YES, only Assumption 2's approved regular privacy-domain margins, affected-pair scope, and finite-seed schedule lower margin**.
- Theorem numbering changed: **NO**.
- Proof-obligation statuses changed: **NO**.
- Simulation/HIL files changed: **NO**.
