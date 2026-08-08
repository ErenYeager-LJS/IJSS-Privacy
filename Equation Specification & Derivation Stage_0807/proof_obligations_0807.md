# Proof Obligations 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Equation Review Revision

## Purpose and completion rule

This ledger is the authoritative list of derivations intentionally deferred from `equation_spec_0807.md`. An item can be closed only by a derivation that states its constants, domains, and required gain/feasibility conditions. `OPEN` does not authorize a stronger manuscript claim.

| ID | Title | Mathematical claim | Depends on equations | Depends on assumptions | Required output | Used by | Status | Failure consequence |
|---|---|---|---|---|---|---|---|---|
| PO-01 | Public-private difference decay | For each channel, derive the exact solution/bound of `z_i` from ES-49 and show exponential decay with a rate bounded below by `lambda_tr,i + underline w_i`; quantify the effect of the bounded correction factor. | ES-41--ES-43, ES-46, ES-49 | Assumption 2: positive tracking rates, positive bounded private weights, admissible `gamma_priv` | Channel-wise decay formula and a uniform decay-rate constant. | Lemma 1; PO-02; PO-10 | PROVED | Equation revision if ES-49 cannot ensure decay under the admitted weights; Blueprint reopen only if the retained decomposition itself must change. |
| PO-02 | Residual convolution and envelope | Solve/bound ES-50 using PO-01 and the command-rate bound; prove ES-51 with a declared decaying `gamma_priv,i` that dominates the convolution. | ES-49--ES-51 | Assumption 2; PO-01; PO-03 | Explicit convolution inequality, sufficient schedule condition, and constants `bar r^V,bar r^omega`. | Lemma 1; Theorems 1--4; PO-13 | PROVED SUBJECT TO PO-03 | Assumption-level revision is required: the decaying command-rate envelope must be proved later or stated explicitly; no Blueprint reopen. |
| PO-03 | Admissible command-rate bound | Derive a finite, channel-specific bound on `dot(c_i^V)` and `dot(c_i^omega)` over the declared invariant operating set, including `dot(alpha_i^V)` and public coordination terms. | ES-6--ES-11, ES-20--ES-31, ES-33--ES-37, ES-62--ES-70, ES-80--ES-82 | Assumption 1: compact `Delta`, regular loads, initial funnel feasibility, bounded uncertainties; candidate invariant set | Explicit `doti_c` bounds with units and their dependence on gains, `h_bar`, residuals, and graph norms. | PO-02; PO-10; PO-13; Theorem 1 | PROVED SUBJECT TO PO-16 | PO-06 is now closed; final numerical constants await compact-tube closure. |
| PO-04 | Nonempty admissible alternative set | Establish that, for at least one `S_i' != S_i` in a local admissible neighborhood, an alternative private initialization/path/weight pair satisfies ES-58--ES-61 and all clauses defining `A_i(S_i)`. | ES-16, ES-41--ES-46, ES-54--ES-61 | Assumption 2: passive adversary, private weight margins, regular alternative path, plant/input compatibility | Existence theorem/constructive local neighborhood with at least two compatible realizations. | Lemma 1; Definition 2; Theorem 4 | OPEN | Equation revision if only the nominal realization exists; Blueprint reopen if no admissible privacy mechanism remains. |
| PO-05 | Alternative-denominator validity | Prove that the denominators `g_i'z_i'` and `z_i'` in ES-60--ES-61 are nonzero wherever division is used, or provide a bounded continuous compatible extension at isolated zeroes without changing the public history. | ES-43, ES-58--ES-61 | Assumption 2; PO-04 | Explicit nonvanishing interval/continuation conditions and weight-bound verification. | Lemma 1; Theorem 4 | OPEN | Equation revision if a required division is generically singular; Blueprint reopen only if the privacy target cannot be realized locally. |
| PO-06 | Graph and algebraic closure | Derive norm/coercivity bounds connecting `e`, `c`, `e_0`, `r`, and `z` from ES-20, ES-21, ES-21a, and ES-101a; resolve the algebraic command dependence without treating the graph term as an input. | ES-18--ES-21a, ES-28, ES-31, ES-48, ES-101a | Assumption 1: fixed connected graph, pinning, invertibility in ES-21a | Explicit graph-norm bounds and the inverse/operator constants used later. | PO-03; PO-07--PO-09; Theorem 1 | PROVED | Equation revision is unnecessary under the frozen common-scalar coordination-gain convention. |
| PO-07 | Composite gain conditions | Convert ES-94, ES-98, and ES-101 plus PO-06 into explicit sufficient inequalities guaranteeing `a_cl>0` in ES-102; state all Young constants and graph/gain restrictions. | ES-90--ES-102 | Assumptions 1--2; PO-02; PO-03; PO-06; PO-08--PO-10 | A complete set of verifiable gain inequalities and formulas for `a_cl,d_R,d_priv`. | Theorem 1; Theorem 2 | OPEN | Equation revision if no feasible positive-gain region exists; Blueprint reopen only if a missing stabilizing mechanism is necessary. |
| PO-08 | Voltage Lyapunov chain | Close ES-83--ES-95, including cancellation, graph/residual/uncertainty bounds, and compatibility of the voltage terms with the PPC transformation. | ES-26--ES-29, ES-36, ES-62--ES-67, ES-83--ES-95 | Assumption 1; Lemma 1/PO-02; PO-06 | Formal voltage derivative inequality with positive coefficients and specified constants. | Theorem 1; PO-07; PO-11 | PROVED SUBJECT TO PO-16 | Pointwise weighted chain is closed; full trajectory finiteness remains. |
| PO-09 | Frequency Lyapunov chain | Close ES-85--ES-98, including transformation-gain bounds and graph/residual/uncertainty terms. | ES-30--ES-32, ES-37, ES-68--ES-70, ES-85--ES-98 | Assumption 1; Lemma 1/PO-02; PO-06 | Formal frequency derivative inequality with positive coefficients and specified constants. | Theorem 1; PO-07; PO-11 | PROVED SUBJECT TO PO-16 | Pointwise chain is closed; full trajectory finiteness remains. |
| PO-10 | Privacy Lyapunov chain | Close ES-87--ES-101 by applying PO-01 and PO-03; give explicit positive `a_z,a_r` and finite `d_c`. | ES-43--ES-51, ES-87--ES-101 | Assumption 2; PO-01; PO-03 | Channel-combined privacy inequality, with conditions on `eps_r1,eps_r2` and private-weight margins. | Lemma 1; Theorem 1; PO-07 | PROVED SUBJECT TO PO-03 | Metric normalization is repaired; explicit private-weight feasibility remains. It does not use ES-51. |
| PO-11 | Funnel-domain forward invariance | Starting from ES-38, show that no finite-time boundary `|sigma_i|=1` can occur while the closed-loop solution exists; use the transformed-coordinate/barrier argument together with PO-08--PO-09. | ES-22--ES-40, ES-65--ES-70, ES-83--ES-103 | Assumption 1; Lemma 1; PO-07--PO-09; PO-16 | A continuation/barrier proof of ES-39 and bounded `h_i` on the declared invariant set. | Theorem 1; Theorem 2 | OPEN | Equation revision if the PPC coordinate becomes singular under its own feasible controls; Blueprint reopen only if prescribed-performance architecture must be changed. |
| PO-12 | Practical prescribed-time recovery | Combine forward invariance, the quintic schedule, and ES-35 to prove post-deadline entry into the declared nonzero tolerances and state precisely the residual/uncertainty ultimate bound. | ES-22--ES-40, ES-51, ES-102--ES-103 | Assumptions 1--2; PO-02; PO-07; PO-11 | Theorem-ready deadline statement for `T_V,T_omega`, with no exact-zero claim. | Theorem 2; Theorem 3; Theorem 4 | OPEN | Equation revision if the claimed tolerance is smaller than the proven post-deadline bound; no Blueprint reopen for a parameter-only change. |
| PO-13 | Actuator and funnel feasibility | Verify there exists a joint choice of funnel endpoints/deadlines/gains satisfying ES-38, ES-95, PO-07, residual allocation ES-67, and `u_i in U_i` for all admissible states. | ES-12, ES-22--ES-31, ES-51, ES-62, ES-67, ES-68, ES-95, ES-102 | Assumption 1; Assumption 2; PO-02; PO-03; PO-07 | Explicit feasibility test or design inequalities linking deadlines, inputs, and compact region. | Assumption 1; Theorems 1--2 | OPEN | Equation revision if a particular gain/deadline choice is infeasible; Blueprint reopen only if no feasible retained-controller design exists. |
| PO-14 | Exact and practical active-power sharing | Prove ideal sharing ES-75--ES-77 from the regulated equilibrium and derive/limit ES-79 with all residual, frequency, derivative, and uncertainty terms. | ES-4, ES-71--ES-79 | Assumptions 1--2; PO-02; PO-12; equilibrium existence | Theorem-ready exact-case conditions and practical residual bound, including convergence conditions for every right-hand term. | Theorem 3; Theorem 4 | OPEN | Equation revision if equilibrium algebra is inconsistent; Blueprint reopen only if the droop objective must be changed. |
| PO-15 | Theorem 4 composition | Compose the local/existence-based public-history equivalence result with the physical PPC and sharing guarantees without claiming transparency or universal/global ambiguity. | ES-16, ES-51--ES-61, ES-71--ES-79, ES-102--ES-103 | Definitions 1--2; Assumptions 1--2; Lemma 1; PO-04--PO-05; PO-12; PO-14 | A precise simultaneous guarantee and its quantifier order. | Theorem 4 | OPEN | Equation revision if the observation map includes a hidden private/physical signal; Blueprint reopen if the privacy target itself must change. |
| PO-16 | Closed-loop well-posedness and operating-region invariance | Establish local existence/uniqueness, bounded public/private states, persistence in `Delta`, and compatibility of the lossless power-flow functions with the proof domain. | ES-1--ES-16, ES-22--ES-23, ES-41--ES-53, ES-80--ES-82 | Assumption 1: regular loads/compact region; Assumption 2: bounded admissible privacy parameters; PO-13 | A well-posedness/continuation statement defining the domain on which all preceding inequalities apply. | Lemma 1; Theorems 1--4; PO-03; PO-11 | OPEN | Equation revision if the specified vector field is not locally well posed; Blueprint reopen if lossless operation cannot be maintained in the stated domain. |

## Dependency order

```text
PO-16 -> PO-03 -> PO-02 -> PO-10
PO-01 -----------^          |
PO-04 -> PO-05 -> PO-15     |
PO-06 -> PO-08/PO-09 -> PO-07 -> PO-11 -> PO-12 -> PO-14 -> PO-15
PO-13 ----------------------^          ^
```

The diagram is a proof order, not a controller signal path. It preserves the frozen theorem hierarchy: Lemma 1 packages PO-01--PO-05 and PO-10; Theorem 1 uses PO-06--PO-11 and PO-16; Theorem 2 uses PO-12; Theorem 3 uses PO-14; Theorem 4 uses PO-15.

## Closure gate

Equation Freeze may be upgraded from conditional to final only when every `OPEN` item is either proved or explicitly moved into an assumption that is technically defensible and accepted by the theorem design. Moving PO-04, PO-05, PO-07, PO-11, PO-13, or PO-16 into an unsupported assumption is not acceptable.

## Derivation-stage status record

| ID | Status | Completion date | Proof location | Revision needed? |
|---|---|---|---|---|
| PO-01 | PROVED | 2026-08-07 | `derivation_stage_1_0807.md`, PO-01 | NO |
| PO-02 | PROVED SUBJECT TO PO-03 | 2026-08-07 (conditional) | `derivation_stage_1_0807.md`, PO-02 | YES |
| PO-03 | PROVED SUBJECT TO PO-16 | 2026-08-07 (conditional) | `derivation_stage_1_0807.md`, PO-03 | NO |
| PO-04 | OPEN | -- | Not yet derived | NO |
| PO-05 | OPEN | -- | Not yet derived | NO |
| PO-06 | PROVED | 2026-08-07 | `derivation_stage_1_0807.md`, PO-06 | NO |
| PO-07 | OPEN | -- | Not yet derived | NO |
| PO-08 | PROVED SUBJECT TO PO-16 | 2026-08-07 (conditional) | `derivation_stage_2_5_0807.md`, PO-08 | NO |
| PO-09 | PROVED SUBJECT TO PO-16 | 2026-08-07 (conditional) | `derivation_stage_2_5_0807.md`, PO-09 | NO |
| PO-10 | PROVED SUBJECT TO PO-03 | 2026-08-07 (conditional) | `derivation_stage_2_5_0807.md`, PO-10 | NO |
| PO-11 | OPEN | -- | Not yet derived | NO |
| PO-12 | OPEN | -- | Not yet derived | NO |
| PO-13 | OPEN | -- | Not yet derived | NO |
| PO-14 | OPEN | -- | Not yet derived | NO |
| PO-15 | OPEN | -- | Not yet derived | NO |
| PO-16 | OPEN | -- | Not yet derived | NO |

### Stage-2.5 normalization completion record

The Stage-2.5 repair has been incorporated into the authoritative ledger. `PO-08` and `PO-09` remain conditionally closed only on the already-declared operating-region/well-posedness obligation `PO-16`; `PO-10` remains conditionally closed on the command-rate bound `PO-03`. No status is upgraded to `PROVED`, `PO-07` is not started, and the Equation Freeze gate remains conditional.

### Stage-1 correction record

The PO-02 derivation shows that a uniform `dot(c)` bound yields only an ultimate residual bound and cannot prove the decaying ES-51 envelope. Before theorem derivation, the project must either prove a compatible decaying command-rate envelope from the later closed-loop analysis or state it as an explicit technical assumption. This is an assumption-level correction, not a new controller module and not a Blueprint-reopen event.
