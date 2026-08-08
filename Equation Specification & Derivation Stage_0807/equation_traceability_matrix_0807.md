# Equation Traceability Matrix 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Equation Review Revision

## Status key

- `Frozen candidate`: equation text is structurally retained and may enter the derived manuscript after proof closure.
- `Open derivation`: equation is a valid specification target whose stated bound/claim depends on an open proof obligation.
- `Proof-only auxiliary`: equation or inequality is an analysis device, not a controller or communication module.

| Equation ID | Category | Blueprint section/module | Variables | Assumptions | Proof obligation | Dependent lemma/theorem | Intended manuscript section | Status |
|---|---|---|---|---|---|---|---|---|
| ES-1--ES-3 | PHY | Physical model: DG states and phase closure | `x_i^V,x_i^omega,V_i,omega_i,delta_i` | A1 operating region | PO-16A; PO-16B | Def. 1; Thm. 1 | System model | Frozen candidate |
| ES-4--ES-5 | PHY | Reduced droop plant | `tau_P,tau_Q,k_P,k_Q,k_V,u,R` | A1 lossless compact operation, bounded `R` | PO-13, PO-14, PO-16A, PO-16B | Def. 1; Thm. 1; Thm. 3 | System model | Frozen candidate |
| ES-6--ES-7 | PHY | Lossless electrical power flow | `P,Q,V,delta,B,P^L,Q^L,N_i^e` | A1 differentiability and `Delta`; `G_ik=0` | PO-03, PO-16A, PO-16B | Def. 1; Thm. 1 | Electrical network model | Frozen candidate |
| ES-8--ES-11 | PHY | Input-affine plant representation | `F_i^V,F_i^omega,u_i,R_i,x_i^V` | A1 plant parameter positivity; measurable locally essentially bounded uncertainty | PO-03, PO-08, PO-09, PO-16A | Def. 1; Thm. 1 | Controller preparation | Frozen candidate |
| ES-12 | CTL | Unique privacy-to-plant interface | `u_i^V,u_i^omega,hat c_i` | A1 local regularity; PO-13 bootstrap input feasibility | PO-13, PO-16A, PO-16B | Def. 1; Thm. 1; Thm. 4 | Control architecture | Frozen candidate |
| ES-13 | CYB | Fixed cyber graph and pinning | `G_c,L_c,a_ij,b_i` | A1 fixed connected undirected graph; positive pinned matrix | PO-06, PO-16A | Assump. 1; Thm. 1 | Communication graph | Frozen candidate |
| ES-14 | PRI | Regular public payload | `m_i,p_i^V,p_i^omega` | A2 public/private ownership | PO-15 | Def. 2; Thm. 4 | Privacy model | Frozen candidate |
| ES-15--ES-16 | PRI | Local message and adversary observation histories | `O_adv,H_c,m_i` | A2 passive eavesdropper/public metadata | PO-04, PO-15 | Def. 2; Thm. 4 | Threat model | Frozen candidate |
| ES-17 | PPC | Local physical regulation errors | `e_{i,0}^V,e_{i,0}^omega,V_ref,omega_ref` | A1 references defined | PO-11, PO-12 | Thm. 1; Thm. 2 | Performance specification | Frozen candidate |
| ES-18--ES-19 | CTL | Counterfactual plaintext distributed error | `e_i,c_i,e_{i,0},b_i,a_ij` | A1 baseline graph | PO-06 | Provenance baseline only | Nominal-controller comparison | Proof-only auxiliary |
| ES-20--ES-21 | CTL/CYB | Implementable privacy-aware distributed error | `e_i,p_i,e_{i,0},L_c,b_i` | A1 fixed graph; A2 public payload | PO-03, PO-06--PO-09 | Def. 1; Thm. 1 | Distributed secondary controller | Frozen candidate |
| ES-21a | CTL | Plaintext algebraic well-posedness condition | `I_N,k_c^V,k_c^omega,L_c` | A1 graph spectrum and gain selection | PO-06 | Thm. 1 | Controller solvability note | Frozen candidate |
| ES-22--ES-23 | PPC | Quintic prescribed-performance funnel schedule | `rho,rho_0,rho_infty,T,h` | A1 positive endpoints/deadlines | PO-11, PO-12, PO-13 | Assump. 1; Thm. 2 | Prescribed-performance design | Frozen candidate |
| ES-24--ES-25 | PPC | Normalized error and `atanh` transformation | `sigma,zeta,e_0,rho` | A1 initial funnel feasibility | PO-11 | Thm. 1; Thm. 2 | Prescribed-performance transformation | Frozen candidate |
| ES-26--ES-29 | CTL/PPC | Nominal voltage virtual control and backstepping state | `alpha^V,chi^V,h^V,c^V,e^V` | A1 smooth funnel/plant; ES-21a where baseline solve is invoked | PO-03, PO-06, PO-08, PO-13 | Def. 1; Thm. 1 | Voltage controller | Frozen candidate |
| ES-30--ES-32 | CTL/PPC | Nominal frequency virtual control | `alpha^omega,c^omega,e^omega` | A1 smooth funnel/plant; ES-21a where baseline solve is invoked | PO-03, PO-06, PO-09, PO-13 | Def. 1; Thm. 1 | Frequency controller | Frozen candidate |
| ES-33--ES-37 | PPC | Transformation derivative and channel dynamics | `dot sigma,dot zeta,tanh,alpha,chi,h` | A1 `rho>0`, `|sigma|<1` | PO-08, PO-09, PO-11 | Thm. 1; Thm. 2 | Performance analysis | Frozen candidate |
| ES-38--ES-40 | PPC | Initial feasibility and deadline implication | `e_0,rho,T` | A1 initial feasible state and selected tolerances | PO-11, PO-12, PO-13 | Assump. 1; Thm. 2 | Performance guarantee | Open derivation |
| ES-41--ES-42 | PRI | Public/private initialization and difference | `p_i,q_i,c_i,z_i` | A2 admissible private initialization | PO-01, PO-02A, PO-02B, PO-04 | Def. 1; Lemma 1; Thm. 4 | Privacy wrapper | Frozen candidate |
| ES-43 | PRI | Bounded correction factor | `g_i,z_i,gamma_priv,i` | A2 positive decay schedule | PO-01, PO-05, PO-10 | Lemma 1 | Privacy wrapper | Frozen candidate |
| ES-44--ES-45 | PRI | Command-tracking decomposition dynamics | `p,q,c,z,lambda_tr,w_12,w_21,g` | A2 positive bounded weights and tracking rates | PO-01--PO-05, PO-10, PO-16A | Def. 1; Lemma 1; Thm. 4 | Privacy wrapper dynamics | Frozen candidate |
| ES-46 | PRI | Private-weight admissibility interval | `underline w,bar w,w_12,w_21` | A2 strict positive margins | PO-01, PO-04, PO-05, PO-10 | Assump. 2; Lemma 1 | Privacy admissibility | Frozen candidate |
| ES-47--ES-48 | PRI/CTL | Reconstruction, residual orientation, state identities | `hat c,r,p,q,c,z` | A2 initialization/ownership | PO-02A, PO-02B, PO-06, PO-13 | Def. 1; Lemma 1; Thm. 1 | Privacy-to-control interface | Frozen candidate |
| ES-49--ES-50 | PRI | Difference and residual dynamics | `z,r,c,lambda_tr,w_12,w_21,g` | A2 positive weights/rates | PO-01, PO-02A, PO-02B, PO-03, PO-10 | Lemma 1; Thm. 1 | Privacy stability analysis | Frozen candidate |
| ES-51 | PRI | Decaying residual envelope | `bar r,gamma_priv,r` | A2 admissible schedule; PO-02B post-continuation command-rate decay | PO-02B | Lemma 1; Thm. 1--Thm. 4 | Privacy performance bound | Open derivation |
| ES-52 | PRI | Exact transparent-wrapper condition | `r,z,w_12,w_21,g,dot c` | A2 | PO-03 (for feasibility interpretation) | Claim restriction; Thm. 4 boundary | Transparency exclusion | Frozen candidate |
| ES-53 | PRI/CTL | Nontransparent Case-B reconstruction | `hat c,c,r` | A2; ES-52 not imposed | PO-02A, PO-13 | Def. 1; Thm. 1--Thm. 4 | Integrated architecture | Frozen candidate |
| ES-54--ES-57 | PRI | Protected datum and observation-equivalence target | `S_i,S_i',O_adv,q_i,w_i,A_i` | A2 passive adversary and local admissibility | PO-04, PO-15 | Def. 2; Thm. 4 | Privacy definition | Frozen candidate |
| ES-58--ES-61 | PRI | Alternative private-realization construction | `p_i',q_i',c_i',z_i',g_i',w_i'` | A2 private-weight margins and compatible alternative path | PO-04, PO-05, PO-15 | Lemma 1; Thm. 4 | Privacy proof construction | Open derivation |
| ES-62--ES-67 | CL/PPC | Voltage closed loop with explicit residual injection | `u^V,c^V,r^V,chi^V,zeta^V,e^V,R^V` | A1; A2 residual envelope | PO-02A, PO-06, PO-08, PO-13, PO-16A | Thm. 1; Thm. 2 | Closed-loop voltage dynamics | Frozen candidate |
| ES-68--ES-70 | CL/PPC | Frequency closed loop with explicit residual injection | `u^omega,c^omega,r^omega,zeta^omega,e^omega,R^omega` | A1; A2 residual envelope | PO-02A, PO-06, PO-09, PO-13, PO-16A | Thm. 1; Thm. 2 | Closed-loop frequency dynamics | Frozen candidate |
| ES-71--ES-73 | SHR | Regulated synchronized equilibrium compatibility | `omega^*,z^*,r^*,p^*,q^*,c_common^omega,L_c` | A1 graph connectedness; equilibrium existence; A2 residual decay | PO-02B, PO-14 | Thm. 3; Thm. 4 | Steady-state characterization | Open derivation |
| ES-74--ES-77 | SHR | Ideal droop sharing algebra | `k_P,P,P^d,u^omega,R^omega,c_common^omega` | Ideal regulated equilibrium and vanishing uncertainty | PO-14 | Thm. 3 | Active-power sharing | Frozen candidate |
| ES-78--ES-79 | SHR | Practical sharing residual bound | `P,u^omega,c^omega,r^omega,omega,dot omega,R^omega` | A1 bounded trajectories; A2 residual envelope | PO-12, PO-14 | Thm. 3; Thm. 4 | Practical sharing guarantee | Open derivation |
| ES-80--ES-82 | CL | Augmented analysis coordinates and consistency dynamics reconstructed from the minimal independent state | `X_cl,zeta,chi,p,q,r` | A1--A2 Caratheodory regularity; `X_cl` is not an unconstrained independent Euclidean state | PO-03, PO-16A, PO-16B | Def. 1; Thm. 1 | Closed-loop system | Frozen candidate |
| ES-83--ES-84 | LYA | Voltage Lyapunov candidate/derivative | `mathscr V_V,P_L^V,p_zeta^V,p_chi^V,zeta^V,chi^V,e^V,r^V,R^V` | A1; A2 residual bound; constant positive diagonal proof metric | PO-08 | Thm. 1 | Voltage stability proof | Proof-only auxiliary |
| ES-85--ES-86 | LYA | Frequency Lyapunov candidate/derivative | `mathscr V_omega,zeta^omega,e^omega,r^omega,R^omega,h` | A1; A2 residual bound | PO-09 | Thm. 1 | Frequency stability proof | Proof-only auxiliary |
| ES-87--ES-89 | LYA | Privacy and composite Lyapunov candidates | `mathscr V_priv,P_L^priv,p_c^V,p_c^omega,mathscr V_cl,z,r` | A2 bounded private weights; constant positive diagonal proof metric | PO-10 | Lemma 1; Thm. 1 | Composite stability proof | Proof-only auxiliary |
| ES-90--ES-91 | LYA/PPC | Transformation-gain upper bound | `h_i,h_bar_i,rho_i,sigma_i` | A1 candidate bootstrap sublevel set | PO-11 | Thm. 1; Thm. 2 | PPC proof estimates | Open derivation |
| ES-92--ES-95 | LYA | Voltage Young bounds and design coefficient | `D_i^V,p_chi^V,Delta_p^V,eps_V0,eps_V2,k_1^V,k_2^V` | A1 bounded `R`; PO-06 graph bounds; repaired `P_L^V` | PO-08, PO-07 | Thm. 1 | Voltage proof estimates | Proof-only auxiliary |
| ES-96--ES-98 | LYA | Frequency Young bounds | `D_i^omega,eps_omega,h_bar_i,k_1^omega` | A1 bounded `R`; PO-06 graph bounds | PO-09, PO-07 | Thm. 1 | Frequency proof estimates | Proof-only auxiliary |
| ES-99--ES-101 | LYA/PRI | Privacy Young bounds and aggregate derivative | `w_delta_bar,eps_r1,eps_r2,p_c^V,p_c^omega,a_z,a_r,d_c,dot c` | A2 Privacy Gain Feasibility Condition; PO-03 command-rate bound; repaired `P_L^priv` | PO-10, PO-07, PO-13 | Lemma 1; Thm. 1 | Privacy proof estimates | Proof-only auxiliary |
| ES-101a | LYA/CYB | Exact graph relation under reconstruction | `e,e_0,c,r,z,L_c,b_i` | A1 fixed graph; A2 reconstruction identity | PO-06 | Thm. 1 | Cross-layer proof closure | Frozen candidate |
| ES-102 | LYA | Composite comparison inequality from the assembled local quadratic certificate | `mathscr V_cl,Q_cl,a_cl,d_R,d_priv` | A1--A2; PO-02A, PO-03, PO-06, PO-08--PO-10, PO-13; `Q_cl` positive definite | PO-07 | Thm. 1; Thm. 2 | Main stability comparison | Proof-derived local inequality |
| ES-103 | LYA | Comparison solution and practical bound | `mathscr V_cl,a_cl,d_R,d_priv` | Positive `a_cl`; locally integrable disturbances | PO-07, PO-12 | Thm. 1; Thm. 2 | Stability/performance conclusion | Open derivation |

## Coverage check

All required identifier ranges are covered without renumbering: ES-1--ES-16, ES-17--ES-21a, ES-22--ES-40, ES-41--ES-61, ES-62--ES-79, and ES-80--ES-103. The Stage-2.5 metric delta is represented in the variable and assumption fields for ES-83--ES-84, ES-87--ES-88, ES-92--ES-95, and ES-99--ES-101. The proof dependency split is represented by `PO-02A`/`PO-02B` (local finite residual bound versus later decaying envelope) and `PO-16A`/`PO-16B` (local well-posedness versus forward continuation); the former aggregate labels are no longer used in current dependencies. The only `Open derivation` entries are equations whose asserted bounds, feasibility statements, or theorem-level closure are explicitly assigned to `proof_obligations_0807.md`; they are not untracked gaps.
