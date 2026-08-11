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

Until PO-04 and PO-05 close, the privacy observation-equivalence clause is a required but unavailable final claim, not a proved conclusion.

## 3. Downstream OPEN-PO classification

| PO | Current ledger status | Classification | Claim supported | Does the claim survive Route L? | Must finish before Proof Freeze? | Exact reason |
|---|---|---|---|---|---|---|
| PO-04 | OPEN | **A. REQUIRED FOR FINAL LOCAL MAIN THEOREM** | Nonempty admissible alternative private realization and public-history non-uniqueness | **YES, locally on the Version 2.2 schedule-regular privacy design domain.** PO-04 may be re-attempted and must construct the coupled family and positive perturbation radius; neither is assumed by the schedule margin. | **YES** | A privacy-preserving paper cannot treat observation ambiguity as proved without at least one non-nominal admissible realization. |
| PO-05 | OPEN | **A. REQUIRED FOR FINAL LOCAL MAIN THEOREM** | Validity of the alternative-realization denominators or compatible extension | **YES, locally, after revised-domain PO-04 closes.** | **YES** | The PO-04 construction cannot support a legal privacy theorem while its frozen alternative-weight formulas may be singular. |
| PO-12 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Practical recovery by the prescribed deadlines | **NO.** Its frozen dependency chain uses PO-11, PO-16B, and PO-02B, which Route L does not pursue. | **NO** | A local-before-exit theorem cannot guarantee existence/admissibility through the deadlines or use ES-51 decay. |
| PO-14 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Exact or practical active-power sharing | **NO.** The theorem-ready sharing claim requires PO-12, PO-02B, equilibrium closure, and residual limits. | **NO** | The required upstream performance/residual chain is outside Route L. Frozen sharing algebra remains design intent, not a final theorem. |
| PO-15 | OPEN | **C. OUTSIDE FINAL MANUSCRIPT THEOREM SCOPE** | Simultaneous privacy, persistent PPC, deadline recovery, and sharing composition | **NO.** Its frozen claim composes unavailable physical and sharing results. | **NO** | Narrowing PO-15 silently would change its frozen ledger claim. Route L retains separate local physical and, after PO-04/05, local privacy results without the stronger simultaneous guarantee. |

No listed PO is discharged or moved to another ledger status by this classification.

## 4. Manuscript claim alignment

| Claim family | Route-L classification | Allowed manuscript wording | Unavailable wording |
|---|---|---|---|
| Local closed-loop existence | **FINAL LOCAL THEOREM CLAIM** | Unique maximal local solution from an admissible initial condition, up to the first admissibility exit | Solution exists for all time; global continuation |
| Local boundedness and ES-102 | **FINAL LOCAL THEOREM CLAIM** | Finite compact-interval bounds and compact-dependent comparison while the trajectory remains in the selected region | Global boundedness; globally proper Lyapunov certificate |
| Prescribed-performance machinery | **FINAL LOCAL THEOREM CLAIM** | PPC coordinates and local inequalities are regular before exit | Forward invariance of the complete funnel; no funnel crossing for all time |
| Actuator feasibility | **FINAL LOCAL THEOREM CLAIM** | Symbolic feasibility on the PO-13 design region while the trajectory remains there | All-time actuator feasibility or saturation avoidance |
| Finite privacy residual | **FINAL LOCAL THEOREM CLAIM** | Finite PO-02A local residual/convolution bound | Residual converges to zero; ES-51 decay |
| Public-history indistinguishability | **CONDITIONAL CLAIM pending PO-04/PO-05** | Local existence-based non-unique reconstruction for the Version 2.2 schedule-regular privacy domain before its stopping boundary, under the frozen passive observation model after both POs close | Historical Version 2.0 class, Version 2.1 schedules without a local lower margin, global/universal ambiguity, perfect secrecy, transparent reconstruction |
| Deadline recovery | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | May be described only as an original frozen target or unproved limitation | Recovery by `T_V` or `T_omega`; continued post-deadline boundedness |
| Active-power sharing | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Frozen equilibrium algebra may be identified as original design intent or future work | Exact sharing or a proved residual-dependent sharing bound |
| Simultaneous composite guarantee | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Separate local physical and privacy results may be reported after their own closures | One theorem simultaneously guaranteeing privacy, persistent PPC, deadlines, and sharing |
| Global continuation and domain invariance | **NOT AVAILABLE UNDER CURRENT FINAL THEORY** | Explicit local-before-exit limitation | `K_0` invariant, `Delta` invariant, denominator/actuator margins persist for all time |

The public-history claim remains conditional because PO-04 and PO-05 are open. Blueprint Version 2.2 supplies only designer-selectable local domain margins and a stopping boundary; it does not assume alternative construction, identical public history, a positive perturbation radius, or invariance. Task-015 must re-attempt the first proof step.

## 5. Blocked stronger-theorem chain

### OPEN - BLOCKED STRONGER-THEOREM CONTINUATION CHAIN

- `PO-11`: remains OPEN; not pursued under Route L; not a prerequisite for the final local theorem.
- `PO-16B`: remains OPEN; not pursued under Route L; not a prerequisite for the final local theorem.
- `PO-02B`: remains OPEN; not pursued under Route L; ES-51 decay is excluded from the final local theorem.

These statuses are intentionally retained. They can re-enter the proof pipeline only after a future Architecture Review changes the Task-008 route decision.

## 6. Proof-pipeline consequence

| PO | Current status | Route-L relevance | Must finish before Proof Freeze? | Reason |
|---|---|---|---|---|
| PO-04 | OPEN | Required local privacy construction on the Version 2.2 schedule-regular domain; eligible to re-attempt | **YES** | Immediate prerequisite for the retained privacy claim |
| PO-05 | OPEN | Required local privacy-construction validity; inactive until PO-04 closes | **YES, after PO-04** | Removes singularity gap in the frozen construction |
| PO-11 | OPEN | Stronger-theorem funnel continuation only | **NO** | Route L stops before exit |
| PO-12 | OPEN | Deadline theorem only | **NO** | Deadline claim is outside final scope |
| PO-14 | OPEN | Sharing theorem only | **NO** | Sharing claim is outside final scope |
| PO-15 | OPEN | Strong simultaneous composition only | **NO** | Composite claim is outside final scope |
| PO-16B | OPEN | Global/forward continuation only | **NO** | Route L uses PO-16A local existence |
| PO-02B | OPEN | Asymptotic residual-decay chain only | **NO** | Route L uses the finite PO-02A bound |

The remaining mathematical work before Proof Freeze is therefore PO-04 followed by PO-05. This ordering does not authorize both in one task: PO-05 depends on the construction established by PO-04.

## 7. Manuscript-facing dependency presentation

The non-frozen final claim presentation must use the following separation:

1. PO-16A and the proved local component/composite obligations support Theorem 1 only before exit.
2. PO-04 then PO-05 support the retained local privacy observation-equivalence claim.
3. PO-11, PO-16B, and PO-02B are displayed as an intentionally inactive stronger-theorem branch.
4. PO-12, PO-14, and PO-15 remain OPEN historical/downstream targets outside the final manuscript theorem scope.

The frozen Blueprint dependency graph remains untouched and must be labeled, when referenced, as the **Frozen Blueprint target theorem** rather than the final proof-status graph.

## 8. Architecture classification

- The stopped continuation chain remains a **Proof Boundary** and **Claim Issue**, already resolved by Route L scope restriction.
- The Task-010 zero-split blocker is resolved by Version 2.1, and the Task-013 schedule-reciprocal blocker is resolved at architecture level by the Version 2.2 finite-seed schedule margin. PO-04 and PO-05 remain **open proof obligations**, not conclusions embedded in Assumption 2.
- Architecture Review Required: **NO** for the present classification and the immediate PO-04 proof task.

If PO-04 later shows that no non-nominal admissible alternative exists, or PO-05 shows that the frozen construction is generically singular and cannot be extended without equation or assumption changes, that later task must stop and report `ARCHITECTURE REVIEW REQUIRED`.

## 9. Exact next task

Recommend exactly:

`task-015-po04-privacy-alternative-existence-v2-2-domain`

Scope: re-attempt only PO-04's coupled nonempty alternative-set claim and positive perturbation radius on the Version 2.2 schedule-regular privacy design domain before the finite-seed/first-exit boundary. Do not begin PO-05. If the construction requires another assumption, an equation change, a new state, or a privacy-mechanism change, stop and report `ARCHITECTURE REVIEW REQUIRED`.

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
