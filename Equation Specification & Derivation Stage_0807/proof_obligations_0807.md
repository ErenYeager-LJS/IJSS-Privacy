# Proof Obligations 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Equation Review Revision

## Purpose and completion rule

This ledger is the authoritative list of derivations intentionally deferred from `equation_spec_0807.md`. An item can be closed only by a derivation that states its constants, domains, and required gain/feasibility conditions. `OPEN` does not authorize a stronger manuscript claim.

| ID | Title | Mathematical claim | Depends on equations | Depends on assumptions | Required output | Used by | Status | Failure consequence |
|---|---|---|---|---|---|---|---|---|
| PO-01 | Public-private difference decay | For each channel, derive the exact solution/bound of `z_i` from ES-49 and show exponential decay with a rate bounded below by `lambda_tr,i + underline w_i`; quantify the effect of the bounded correction factor. | ES-41--ES-43, ES-46, ES-49 | Assumption 2: positive tracking rates, positive bounded private weights, admissible `gamma_priv` | Channel-wise decay formula and a uniform decay-rate constant. | PO-02A; PO-02B; PO-10 | PROVED | Equation revision if ES-49 cannot ensure decay under the admitted weights; Blueprint reopen only if the retained decomposition itself must change. |
| PO-02A | Local residual convolution and boundedness | Using PO-01 and PO-03, derive the exact variation-of-constants formula and a finite residual/convolution bound on the compact bootstrap set `K_0`. This obligation does not assert `gamma_priv(t)->0` or any asymptotic closed-loop property. | ES-49--ES-50 | Assumption 2; PO-01; PO-03 | Finite local residual constants `bar r^V,bar r^omega` and a convolution estimate valid up to the first exit time. | PO-07; PO-08; PO-09; PO-10; PO-13; PO-11; PO-16B | PROVED | Proved locally on `K_0`; no ES-51 decay claim is available and PO-02A is not an asymptotic result. |
| PO-02B | Decaying residual envelope | Prove ES-51 with `gamma_priv,i(t)->0` using the forward closed-loop results available after PO-07, PO-11, and PO-16B. The required command-rate decay must be derived from those later results; it is not supplied by the uniform PO-03 bound. | ES-49--ES-51 | Assumption 2; PO-01; PO-02A; PO-07; PO-11; PO-16B | A genuine decaying command-rate/residual envelope and explicit schedule condition for `gamma_priv,i`; no new assumption may replace this proof. | PO-12; PO-14; PO-15; Theorems 1--4 | OPEN | ES-51 remains an unproved target; any theorem claim requiring residual decay is blocked until PO-02B is discharged. |
| PO-03 | Admissible command-rate bound on bootstrap set | Derive a finite, channel-specific bound on `dot(c_i^V)` and `dot(c_i^omega)` over a selected compact bootstrap set `K_0` contained in the admissible open domain. The bound includes `dot(alpha_i^V)` and public coordination terms, but makes no forward-invariance claim. | ES-6--ES-11, ES-20--ES-31, ES-33--ES-37, ES-62--ES-70, ES-80--ES-82 | Assumption 1 regularity; PO-16A; `K_0` compactly embedded in the open domain; bounded uncertainties | Explicit `dot(c_i)` bounds with units and their dependence on gains, `h_bar`, residuals, and graph norms on `K_0`. | PO-02A; PO-10; PO-13; PO-07 | PROVED | Proved locally on `K_0`; global boundedness is deferred to PO-16B. |
| PO-04 | Nonempty admissible alternative set | Establish that, for at least one `S_i' != S_i` in a local admissible neighborhood, an alternative private initialization/path/weight pair satisfies ES-58--ES-61 and all clauses defining `A_i(S_i)`. | ES-16, ES-41--ES-46, ES-54--ES-61 | Assumption 2: passive adversary, private weight margins, regular alternative path, plant/input compatibility | Existence theorem/constructive local neighborhood with at least two compatible realizations. | Lemma 1; Definition 2; Theorem 4 | OPEN | Equation revision if only the nominal realization exists; Blueprint reopen if no admissible privacy mechanism remains. |
| PO-05 | Alternative-denominator validity | Prove that the denominators `g_i'z_i'` and `z_i'` in ES-60--ES-61 are nonzero wherever division is used, or provide a bounded continuous compatible extension at isolated zeroes without changing the public history. | ES-43, ES-58--ES-61 | Assumption 2; PO-04 | Explicit nonvanishing interval/continuation conditions and weight-bound verification. | Lemma 1; Theorem 4 | OPEN | Equation revision if a required division is generically singular; Blueprint reopen only if the privacy target cannot be realized locally. |
| PO-06 | Graph and algebraic closure | Derive norm/coercivity bounds connecting `e`, `c`, `e_0`, `r`, and `z` from ES-20, ES-21, ES-21a, and ES-101a; resolve the algebraic command dependence without treating the graph term as an input. | ES-18--ES-21a, ES-28, ES-31, ES-48, ES-101a | Assumption 1: fixed connected graph, pinning, invertibility in ES-21a | Explicit graph-norm bounds and the inverse/operator constants used later. | PO-03; PO-07--PO-09; Theorem 1 | PROVED | Equation revision is unnecessary under the frozen common-scalar coordination-gain convention. |
| PO-07 | Composite gain conditions | Convert ES-94, ES-98, and ES-101 plus PO-06 into the minimal matrix certificate `Q_cl ≻ 0`, guaranteeing `a_cl>0` in ES-102 on `K_0`; state all Young constants, graph/gain restrictions, and compatibility with the pre-checked actuator/funnel design domain. | ES-90--ES-102 | Assumptions 1--2; PO-02A; PO-03; PO-06; PO-08--PO-10; PO-13 | A complete verifiable composite gain certificate and explicit formulas for `a_cl,d_R,d_priv`. | PO-11; Theorem 1; Theorem 2 | PROVED | ES-102 is derived as a local Lyapunov comparison inequality on `K_0`; no global continuation or asymptotic claim is made. |
| PO-08 | Voltage Lyapunov chain on bootstrap set | Close ES-83--ES-95, including cancellation, graph/residual/uncertainty bounds, and compatibility of the voltage terms with the PPC transformation on `K_0`. | ES-26--ES-29, ES-36, ES-62--ES-67, ES-83--ES-95 | Assumption 1; Lemma 1/PO-02A; PO-06; PO-16A | Formal voltage derivative inequality with positive coefficients and specified constants on the local domain. | PO-07; PO-11; Theorem 1 | PROVED | Proved as a pointwise local inequality on `K_0`; full trajectory continuation remains in PO-11 and PO-16B. |
| PO-09 | Frequency Lyapunov chain on bootstrap set | Close ES-85--ES-98, including transformation-gain bounds and graph/residual/uncertainty terms on `K_0`. | ES-30--ES-32, ES-37, ES-68--ES-70, ES-85--ES-98 | Assumption 1; Lemma 1/PO-02A; PO-06; PO-16A | Formal frequency derivative inequality with positive coefficients and specified constants on the local domain. | PO-07; PO-11; Theorem 1 | PROVED | Proved as a pointwise local inequality on `K_0`; full trajectory continuation remains in PO-11 and PO-16B. |
| PO-10 | Privacy Lyapunov chain | Close ES-87--ES-101 by applying PO-01 and the local command-rate estimate PO-03; give explicit positive `a_z,a_r` and finite `d_c`. | ES-43--ES-51, ES-87--ES-101 | Assumption 2; PO-01; PO-03; Privacy Gain Feasibility Condition | Channel-combined privacy inequality, with explicit nonempty ranges for `eps_r1,eps_r2` and private-weight margins. | PO-07; Theorem 1 | PROVED | Proved locally on `K_0` under the formal admissible-design clause; it does not use ES-51 or PO-02B. |
| PO-11 | Funnel-domain barrier before exit | Starting from ES-38, show that no finite-time boundary `|sigma_i|=1` can occur before the maximal local solution exits the open domain; use the transformed-coordinate/barrier argument together with PO-07--PO-10 and the actuator design check PO-13. This obligation does not assert global continuation. | ES-22--ES-40, ES-65--ES-70, ES-83--ES-103 | Assumption 1; Lemma 1; PO-07--PO-10; PO-13; PO-16A | A barrier/continuation-to-exit statement proving funnel admissibility up to the local exit time and bounded `h_i` on `K_0`. | PO-16B; Theorem 1; Theorem 2 | OPEN | Equation revision if the PPC coordinate becomes singular before the local exit time; Blueprint reopen only if prescribed-performance architecture must be changed. |
| PO-12 | Practical prescribed-time recovery | Combine the forward continuation result, the quintic schedule, and ES-35 to prove post-deadline entry into the declared nonzero tolerances and state precisely the residual/uncertainty ultimate bound. | ES-22--ES-40, ES-51, ES-102--ES-103 | Assumptions 1--2; PO-02A; PO-02B; PO-07; PO-11; PO-16B | Theorem-ready deadline statement for `T_V,T_omega`, with no exact-zero claim. | Theorem 2; Theorem 3; Theorem 4 | OPEN | Equation revision if the claimed tolerance is smaller than the proven post-deadline bound; no Blueprint reopen for a parameter-only change. |
| PO-13 | Bootstrap actuator and funnel feasibility | Verify, before composite gain closure, that there exists a joint choice of funnel endpoints, deadlines, preliminary gains, residual allocation, and compact bootstrap set `K_0` satisfying ES-38, ES-67, ES-68, ES-95 and `u_i in U_i` for all states in `K_0`. This is a design-domain feasibility check, not a consequence of Theorem 1 or ES-102. | ES-12, ES-22--ES-31, ES-62, ES-67, ES-68, ES-95 | Assumption 1; Assumption 2; PO-02A; PO-03; PO-10; PO-16A | Explicit symbolic feasibility test and strict actuator/gain/deadline margin inequalities; no use of ES-51, ES-102, PO-07, PO-16B, or PO-02B. | PO-07; PO-11; PO-16B; Theorems 1--2 | PROVED | Symbolic design feasibility is proved under the displayed simultaneous strict inequalities; verification of a particular numerical/HIL tuple remains an experiment item, not a theoretical blocker. |
| PO-14 | Exact and practical active-power sharing | Prove ideal sharing ES-75--ES-77 from the regulated equilibrium and derive/limit ES-79 with all residual, frequency, derivative, and uncertainty terms. | ES-4, ES-71--ES-79 | Assumptions 1--2; PO-02A; PO-02B; PO-12; equilibrium existence | Theorem-ready exact-case conditions and practical residual bound, including convergence conditions for every right-hand term. | Theorem 3; Theorem 4 | OPEN | Equation revision if equilibrium algebra is inconsistent; Blueprint reopen only if the droop objective must be changed. |
| PO-15 | Theorem 4 composition | Compose the local/existence-based public-history equivalence result with the physical PPC and sharing guarantees without claiming transparency or universal/global ambiguity. | ES-16, ES-51--ES-61, ES-71--ES-79, ES-102--ES-103 | Definitions 1--2; Assumptions 1--2; Lemma 1; PO-04--PO-05; PO-12; PO-14 | A precise simultaneous guarantee and its quantifier order. | Theorem 4 | OPEN | Equation revision if the observation map includes a hidden private/physical signal; Blueprint reopen if the privacy target itself must change. |
| PO-16A | Local closed-loop well-posedness and bootstrap-domain existence | Establish local existence and uniqueness of the reduced ES-1--ES-82 vector field on the genuine open domain `D_min` of independent coordinates, reconstruct the algebraically dependent ES-81 coordinates consistently, and select a compact bootstrap set `K_0` with the initial state in its interior. No forward invariance, actuator feasibility, or global boundedness is claimed here. | ES-1--ES-16, ES-22--ES-23, ES-41--ES-53, ES-80--ES-82 | Assumption 1 regularity, measurable locally essentially bounded `R_i^nu`, and initial funnel feasibility; Assumption 2 bounded admissible privacy parameters | Caratheodory local existence/uniqueness, maximal interval, first-exit definition, derived-coordinate consistency, and compact `K_0` embedded in `D_min`. | PO-03; PO-08; PO-09; PO-13; PO-11; PO-16B | PROVED | Local existence/uniqueness and compact bootstrap construction are proved on independent coordinates; no forward invariance, actuator feasibility, or global boundedness is claimed. |
| PO-16B | Forward continuation and operating-region invariance | Starting from PO-16A, PO-07, PO-11, and PO-13, prove that the maximal local solution cannot exit through the admissible operating-region, funnel, or actuator boundary, so the solution continues in the declared domain and all bootstrap bounds can be extended along the trajectory. This is the global/forward closure obligation formerly conflated with PO-16. | ES-1--ES-16, ES-22--ES-40, ES-41--ES-53, ES-62--ES-103 | Assumptions 1--2; PO-02A; PO-07; PO-11; PO-13; PO-16A | A continuation theorem with explicit exit-set exclusion and persistence in `Delta`; no use of PO-02B, PO-12, PO-14, or PO-15. | PO-02B; PO-12; PO-14; PO-15; Theorems 1--4 | OPEN | Equation revision if boundedness cannot exclude an exit; Blueprint reopen only if an additional stabilizing module would be required. |

## Dependency order

```text
PO-16A -> PO-03 -> PO-02A -----------+
PO-01 -------------------------------|
PO-06 -> PO-08/PO-09 ---------------|-> PO-07
PO-02A -> PO-10 ---------------------+
PO-16A,PO-10 -> PO-13 ---------------+
PO-07,PO-08,PO-09,PO-13,PO-16A -> PO-11 -> PO-16B
PO-16B -> PO-02B
PO-02A,PO-02B,PO-07,PO-11,PO-16B -> PO-12 -> PO-14
PO-04 -> PO-05 ---------------------------> PO-15
PO-12,PO-14 ------------------------------> PO-15
```

The diagram is a proof order, not a controller signal path. `PO-02A` is finite local residual boundedness; `PO-02B` is the later asymptotic ES-51 envelope. `PO-16A` is local existence only; `PO-16B` is forward/global continuation. PO-07 may begin after PO-02A and its other listed prerequisites are closed; PO-02B is deliberately downstream of PO-16B. The former aggregate `PO-02` and `PO-16` labels are retired as active dependency labels and must not be used without the appropriate suffix.

## Closure gate

Equation Freeze may be upgraded from conditional to final only when every `OPEN` item is either proved or explicitly moved into an assumption that is technically defensible and accepted by the theorem design. Moving PO-04, PO-05, PO-07, PO-11, PO-13, PO-16A, or PO-16B into an unsupported assumption is not acceptable.

## Derivation-stage status record

| ID | Status | Completion date | Proof location | Revision needed? |
|---|---|---|---|---|
| PO-01 | PROVED | 2026-08-07 | `derivation_stage_1_0807.md`, PO-01 | NO |
| PO-02A | PROVED | 2026-08-08 (local on `K_0`) | `derivation_stage_3_bootstrap_0808.md`, PO-02A | YES |
| PO-02B | OPEN | -- | Not yet derived; requires post-PO-16B asymptotic command-rate analysis | NO |
| PO-03 | PROVED | 2026-08-08 (local on `K_0`) | `derivation_stage_3_bootstrap_0808.md`, PO-03 | YES |
| PO-04 | OPEN | -- | Not yet derived | NO |
| PO-05 | OPEN | -- | Not yet derived | NO |
| PO-06 | PROVED | 2026-08-07 | `derivation_stage_1_0807.md`, PO-06 | NO |
| PO-07 | PROVED | 2026-08-08 (local on `K_0`) | `derivation_stage_4_composite_0808.md`, PO-07 | YES |
| PO-08 | PROVED | 2026-08-08 (pointwise local on `K_0`) | `derivation_stage_3_bootstrap_0808.md`, PO-08 | YES |
| PO-09 | PROVED | 2026-08-08 (pointwise local on `K_0`) | `derivation_stage_3_bootstrap_0808.md`, PO-09 | YES |
| PO-10 | PROVED | 2026-08-08 (local on `K_0`) | `derivation_stage_3_bootstrap_0808.md`, PO-10 | YES |
| PO-11 | OPEN | -- | Not yet derived | NO |
| PO-12 | OPEN | -- | Not yet derived | NO |
| PO-13 | PROVED | 2026-08-08 (symbolic design feasibility) | `derivation_stage_3_bootstrap_0808.md`, PO-13 | YES |
| PO-14 | OPEN | -- | Not yet derived | NO |
| PO-15 | OPEN | -- | Not yet derived | NO |
| PO-16A | PROVED | 2026-08-08 | `derivation_stage_3_bootstrap_0808.md`, PO-16A | NO |
| PO-16B | OPEN | -- | Not yet derived | NO |

### Stage-2.5 normalization completion record

The Stage-2.5 repair has been incorporated into the authoritative ledger. Its former aggregate `PO-16` dependency is split here into local well-posedness `PO-16A` and forward continuation `PO-16B`. The former aggregate `PO-02` is split into local finite residual boundedness `PO-02A` and the later decaying envelope `PO-02B`. `PO-08` and `PO-09` are proved only as pointwise local inequalities on `K_0`; PO-10 is proved under the formal Privacy Gain Feasibility Condition; and PO-13 is proved as symbolic design feasibility. Numerical/HIL parameter verification remains separate. The Equation Freeze gate remains conditional because downstream obligations remain open.

### Stage-1 correction record

The PO-02 derivation shows that a uniform `dot(c)` bound yields only an ultimate residual bound and cannot prove the decaying ES-51 envelope. Before theorem derivation, the project must either prove a compatible decaying command-rate envelope from the later closed-loop analysis or state it as an explicit technical assumption. This is an assumption-level correction, not a new controller module and not a Blueprint-reopen event.

### Stage-4 composite closure record

PO-07 is closed by the minimal local matrix certificate `Q_cl=Q_0-H^T W_D H ≻ 0`. ES-102 is thereby established as a local Lyapunov comparison inequality on `K_0`. This closure does not prove PO-02B, PO-11, PO-16B, or any global stability statement.
