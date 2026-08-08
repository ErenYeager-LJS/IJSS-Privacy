# Claim-Scope Alignment Review 0808

> Task ID: `task-006-claim-scope-alignment`  
> Branch: `task-006-claim-scope-alignment`  
> Basis: Blueprint Freeze Version 2.0, frozen equations, current proof ledger, and `theory_boundary_review_0808.md`

## 1. Audit conclusion

The frozen architecture is not internally contradictory, but its blueprint-level theorem descriptions are stronger than the currently discharged proof obligations. The strongest result supported today is a local-before-exit closed-loop result on a selected compact bootstrap set. The correct final path is **PATH B**: one or more open proof obligations must be closed before manuscript integration of the intended theorem set.

No new proof is performed here. No equation, controller, privacy target, PPC construction, Lyapunov function, theorem number, or Blueprint item is changed.

## 2. Proof-status basis

| Status | Current meaning |
|---|---|
| `PROVED` | The cited obligation is discharged at the stated scope without an open downstream condition. |
| `PROVED LOCALLY / BEFORE EXIT` | The derivation is valid on `K_0` or a compact subset while the trajectory remains in the admissible domain; it is not a continuation result. |
| `CONDITIONAL ON OPEN PO` | The claim follows only if named open obligations are later discharged. |
| `NOT YET PROVED` | The claim is a stated target, but the current proof record supplies no completed derivation for it. |
| `OUT OF SCOPE` | The claim is excluded by the frozen threat model or architecture. |

Authoritative open obligations are `PO-11` (funnel forward invariance), `PO-16B` (forward operating-region/actuator continuation), `PO-02B` (decaying residual envelope), `PO-04`/`PO-05` (privacy alternative construction and denominator validity), `PO-12` (deadline recovery), `PO-14` (sharing), and `PO-15` (composition).

## 3. Claim inventory and traceability

| Claim ID | Claim description | Equation basis | Proof obligation(s) | Current status | Allowed wording | Forbidden wording | Final theorem/lemma | Manuscript section |
|---|---|---|---|---|---|---|---|---|
| C-01 | Reduced closed loop has a unique local Caratheodory solution from an admissible initial state. | ES-1--ES-16, ES-22--ES-23, ES-41--ES-53, ES-80--ES-82 | PO-16A | `PROVED` | local existence and uniqueness on a nontrivial maximal interval before the first admissible-domain exit | global existence; solution for every `t >= 0` | Theorem 1 support | Closed-loop well-posedness |
| C-02 | Controller, PPC maps, reconstructed dependent coordinates, and virtual privacy states remain regular on the local proof interval. | ES-22--ES-53, ES-80--ES-82 | PO-16A, PO-03 | `PROVED LOCALLY / BEFORE EXIT` | regular and finite on `K_0` up to first exit | globally bounded augmented state | Theorem 1 support | Closed-loop regularity |
| C-03 | Voltage, frequency, and privacy component inequalities hold with finite constants on the selected compact bootstrap set. | ES-83--ES-101 | PO-02A, PO-03, PO-06, PO-08, PO-09, PO-10 | `PROVED LOCALLY / BEFORE EXIT` | pointwise local inequalities on `K_0` | global Lyapunov inequality on the full state space | Theorem 1 support | Lyapunov analysis |
| C-04 | The assembled composite comparison inequality ES-102/ES-103 holds locally. | ES-89--ES-103 | PO-07 plus local component POs | `PROVED LOCALLY / BEFORE EXIT` | compact-dependent comparison while the trajectory stays in the selected domain | global stability, global properness, or unconditional continuation | Theorem 1 support | Composite comparison |
| C-05 | Physical states and transformed coordinates are bounded before the first exit. | ES-62--ES-70, ES-80--ES-103 | PO-07, PO-16A | `PROVED LOCALLY / BEFORE EXIT` | bounded on the local bootstrap interval | bounded for all future time; global asymptotic stability | Theorem 1 support | Local boundedness |
| C-06 | Voltage/frequency errors remain inside their PPC funnels for all future time. | ES-22--ES-40, ES-90--ES-103 | PO-11, PO-16B | `CONDITIONAL ON OPEN PO` | conditional funnel exclusion under JECFC and the joint exit-continuation lemma | unconditional funnel invariance; `for all t >= 0` | Theorem 1 intended scope | Prescribed-performance analysis |
| C-07 | Voltage and frequency enter the final practical tolerances by `T_V` and `T_omega`. | ES-22--ES-40, ES-95, ES-98, ES-102--ES-103 | PO-02B, PO-07, PO-11, PO-12, PO-16B | `CONDITIONAL ON OPEN PO` | conditional practical deadline result with the explicitly derived residual/uncertainty bound | unconditional deadline recovery; exact-zero or finite-time convergence | Theorem 2 | Practical prescribed-time recovery |
| C-08 | The differential steady-state privacy correction vanishes and the nominal droop sharing relation is preserved. | ES-71--ES-77 | PO-02B, PO-12, PO-14 | `NOT YET PROVED` | only a future conditional exact-sharing result, or a residual-dependent bound once derived | exact asymptotic sharing now; sharing inferred from recovery alone | Theorem 3 | Active-power sharing |
| C-09 | A finite residual/convolution bound is available locally. | ES-49--ES-50 | PO-01, PO-02A, PO-03 | `PROVED LOCALLY / BEFORE EXIT` | finite residual bound on `K_0` up to first exit | residual converges to zero; ES-51 as a current theorem consequence | Lemma 1 / Theorem 1 support | Privacy residual interface |
| C-10 | The residual envelope ES-51 decays asymptotically. | ES-49--ES-51 | PO-02B, downstream PO-11/PO-16B | `NOT YET PROVED` | none beyond marking it as an open target or future conditional result | `r(t) -> 0`; asymptotic privacy-performance consequence | Lemma 1 / Theorems 1--4 only after PO-02B | Residual analysis |
| C-11 | Alternative private initializations generate the same complete public history. | ES-54--ES-61 | PO-04, PO-05, PO-15 | `CONDITIONAL ON OPEN PO` | local/existence-based public-history indistinguishability under the passive-eavesdropper model | global privacy ambiguity; cryptographic secrecy; exact transparent reconstruction | Definition 2 / Theorem 4 | Privacy guarantee |
| C-12 | Funnel, physical operating-region, denominator, actuator, and compactness exits are excluded and the solution continues. | ES-1--ES-103 | PO-11, PO-16B, JECFC | `CONDITIONAL ON OPEN PO` | conditional continuation if a valid compact sublevel/tube with strict margins is established | global continuation under current results; all-time actuator feasibility | Theorem 1 intended scope | Exit and continuation |
| C-13 | Exact or practical active-power sharing bound is established. | ES-71--ES-79 | PO-12, PO-14, PO-02B | `NOT YET PROVED` | residual-dependent sharing only after the relevant bound is derived | exact sharing without residual/equilibrium closure | Theorem 3 | Sharing analysis |
| C-14 | Privacy, prescribed performance, boundedness, and sharing hold simultaneously. | ES-54--ES-61, ES-71--ES-79, ES-102--ES-103 | PO-04, PO-05, PO-11, PO-12, PO-14, PO-15, PO-16B, and where needed PO-02B | `NOT YET PROVED` | future composite theorem after component closures; privacy and local physical claims may be reported separately | unconditional simultaneous guarantee; universal/global ambiguity | Theorem 4 | Composite guarantee |

## 4. Theorem 1 boundary

### Theorem 1 — current provable scope

The current theory supports only this boundary: local existence and uniqueness, local controller/PPC/privacy regularity, finite compact-dependent component inequalities, ES-102/ES-103 comparison, finite local residual bounds, and symbolic actuator/funnel feasibility, all up to the first exit from the selected admissible bootstrap domain.

### Allowed claims

- local well-posedness from `PO-16A`;
- boundedness and comparison estimates on `K_0` before exit;
- local finite residual bounds from `PO-02A`;
- symbolic feasibility on the `PO-13` design region.

### Not yet allowed

- all-time funnel forward invariance;
- forward invariance of the physical operating region `Delta`;
- all-time actuator feasibility;
- global-in-time continuation or global boundedness;
- global asymptotic stability;
- any use of ES-51 decay as an established consequence.

### Required open obligations for a stronger boundary

`PO-11` and `PO-16B` must close the joint exit/continuation argument under a defensible JECFC-type margin result. `PO-02B` is additionally required for residual-decay or asymptotic consequences.

## 5. Theorem 2 boundary

Theorem 2 can be stated only conditionally at present. ES-102/ES-103 and the PPC inverse provide the local ingredients, but a deadline guarantee requires the trajectory to remain in the funnel/operating domain (`PO-11`, `PO-16B`) and requires the post-continuation residual envelope and tolerance calculation (`PO-02B`, `PO-12`). No stronger quantifier or exact-zero claim is currently defensible.

## 6. Theorem 3 boundary

Theorem 3 is not currently closed. The equilibrium droop algebra is a frozen target, but exact sharing requires the differential frequency correction and residual terms to vanish or a derived practical bound. That requires `PO-02B`, `PO-12`, and `PO-14`, including equilibrium existence. Recovery alone cannot prove sharing.

## 7. Theorem 4 boundary

Privacy observation equivalence is logically separate from the physical Lyapunov chain and is itself conditional on `PO-04`, `PO-05`, and `PO-15`. A simultaneous privacy/performance/sharing theorem is therefore not yet available because Theorems 1--3 are not closed. The frozen Case-B wrapper supports only a passive, public-history, existence-based ambiguity claim; it does not support transparency, cryptographic secrecy, or protection against physical-sensor access.

## 8. Stale-overclaim audit

The following source documents contain intended theorem descriptions that exceed the current proof status:

1. `Blueprint_0807/theorem dependencies design_0807.md` describes Theorem 1 as full boundedness and funnel invariance, and describes Theorems 2--4 as if the preceding theorems were already closed.
2. `Blueprint_0807/roadmap_0807.md` presents the intended theorem chain without the current local-before-exit and open-PO qualifiers.
3. `Equation Specification & Derivation Stage_0807/equation_spec_0807.md` retains the theorem dependency map in which Theorem 1 consumes `PO-11`/`PO-16B`; its later bootstrap/continuation notes correctly identify the local boundary, but the headline output remains a target rather than a current result.
4. `Equation Specification & Derivation Stage_0807/equation_traceability_matrix_0807.md` correctly maps the open obligations, but labels the theorem outputs as intended manuscript results; those rows must be read as conditional/open until the listed POs close.
5. `theory_boundary_review_0808.md` is consistent with the conclusion here: Category B and local-before-exit scope.

These are recorded as claim-status discrepancies only. No frozen document is edited because the task forbids architecture/equation rewrites and the authoritative proof ledger already records the open obligations correctly.

## 9. Audit totals and decision

- Claims audited: **14** (including the ten required claim families plus supporting privacy/residual and composition claims).
- Fully proved: **1** (`C-01`, local well-posedness; the only fully closed claim at its stated scope).
- Proved locally / before exit: **5** (`C-02`, `C-03`, `C-04`, `C-05`, `C-09`).
- Conditional on open POs: **4** (`C-06`, `C-07`, `C-11`, `C-12`).
- Not yet proved: **4** (`C-08`, `C-10`, `C-13`, `C-14`).
- Locally proved or conditional: **9** (the preceding five local rows plus four conditional rows).
- Claims still requiring at least one open PO: **8** (four conditional rows plus four not-yet-proved rows).
- Out of scope: no core claim row; excluded security claims remain outside the frozen architecture.
- Stale overclaim locations: **4** source documents (theory boundary review is not stale).
- Equations changed: **NO**.
- Blueprint changed: **NO**.
- Blueprint Reopen Required: **NO**.
- Final path: **PATH B**.

## 10. Recommended next engineering task

Close or formally resolve the joint exit/continuation prerequisite for `PO-11` and `PO-16B` without introducing an unsupported assumption. After that, address `PO-02B`, then derive `PO-12` and `PO-14`, and finally close the privacy alternative/composition obligations `PO-04`, `PO-05`, and `PO-15`. Manuscript integration should wait until the intended theorem quantifiers match those closures.
