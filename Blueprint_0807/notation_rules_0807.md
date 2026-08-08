# Notation Rules 0807: Immutable Minimal Symbol Contract

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07

## Status

This file is the authoritative notation contract before equation generation. It fixes symbol meaning, channel ownership, information ownership, graph labels, time labels, privacy semantics, and experiment metrics. Every manuscript symbol must also appear in `variables_0807.md`.

## 1. Channels and indices

- Superscript `V` denotes the voltage channel.
- Superscript `omega` denotes the frequency channel.
- The same base symbol has the same semantic role in both channels.
- `i` is the local DG index; `j,k` are other DG, neighbor, or line indices only when the surrounding subscript is explicit.
- `N` is the number of DGs; `mathcal V` is the vertex set.
- A local scalar carries an agent subscript. A stacked network vector uses bold lowercase notation, with DG index first in the stacking order.
- Matrices and operators use uppercase notation. Transpose is the superscript `T`; a prime is never a derivative.

## 2. Physical plant symbols

- `V_i` is physical voltage amplitude only.
- `omega_i` is physical angular frequency only. A frequency reported in hertz uses a separate experimental symbol and an explicit conversion.
- `delta_i` is the physical voltage phase angle only.
- `P_i` and `Q_i` are physical active and reactive power only.
- `P_i^m` and `Q_i^m` are filtered physical powers; superscript `m` does not mean public data.
- `P_i^L`, `Q_i^L`, and `S_i^L` are local load quantities and are not public merely because they occur in the plant model.
- `x_i^V` and `x_i^omega` are local channel state vectors and are not transmitted.
- `Y_ik`, `G_ik`, and `B_ik` denote electrical admittance, conductance, and susceptance. They must not be reused for cyber weights or controller gains.

## 3. References, errors, and funnels

- `V_ref` and `omega_ref` are the only regulated references.
- `e_i^V` and `e_i^omega` are physical tracking/coordination errors. They never denote residuals or transformed errors.
- `e_{i,0}^V` and `e_{i,0}^omega` are local physical errors relative to the references. `e_i^V` and `e_i^omega` are the distributed/pinning errors built from those local errors and public coordination differences.
- `sigma_i^V` and `sigma_i^omega` are normalized errors, equal to the corresponding local physical error divided by its positive funnel radius.
- `h_i^V` and `h_i^omega` are the corresponding positive transformation gains `1/[rho_i(1-sigma_i^2)]`.
- `rho_i^V(t)` and `rho_i^omega(t)` are prescribed-performance envelopes only.
- `zeta_i^V` and `zeta_i^omega` are transformed errors only. No second transformed-error family may be introduced.
- `epsilon_final^V` and `epsilon_final^omega` are final practical physical tolerances only.
- Funnel invariance means `e` remains in its envelope. Practical prescribed-time recovery means entry into `epsilon_final` by `T_V` or `T_omega`.

## 4. Nominal coordination and control inputs

- `c_i^V` and `c_i^omega` are ideal local virtual secondary coordination states.
- `hat c_i^V` and `hat c_i^omega` are locally reconstructed coordination states. The hat does not imply public disclosure.
- `u_i^V` and `u_i^omega` are the reconstructed secondary inputs applied locally to the physical plant.
- `alpha_i^V` and `alpha_i^omega` are reserved for channel-specific virtual controls if the final controller retains a backstepping step.
- `chi_i^V` is the voltage backstepping error between physical voltage velocity and `alpha_i^V`. No separate frequency backstepping error is introduced because the retained frequency model is first order.
- `F_i^V` and `F_i^omega` are known channel drifts after the physical equations are put into input-affine form; bounded unknown terms remain `R_i^V` and `R_i^omega`.
- `lambda_tr,i^V` and `lambda_tr,i^omega` are positive public command-tracking rates with units of inverse time.
- `k_V`, `k_omega`, `Pi_V`, and `Pi_omega` are public design gains/allocations only when they are explicitly declared.
- `U_i` denotes the feasible local actuator-input set.
- The controller order is: local measurement/reference processing; receipt of public states; direct distributed-error calculation; nominal coordination; public/private update; local reconstruction and residual evaluation; funnel/controller assembly; feasible plant input.
- Regular messages may contain only the declared public virtual states and disclosed protocol metadata. Raw `V_i`, `omega_i`, `P_i`, `Q_i`, `u_i^V`, and `u_i^omega` are excluded.

## 5. Public, private, and residual families

- `p_i^V` and `p_i^omega` are the only public virtual coordination states.
- `q_i^V` and `q_i^omega` are private virtual coordination states retained locally.
- `r_i^V` and `r_i^omega` are privacy/decomposition residuals with the fixed orientation “locally reconstructed coordination state minus ideal coordination state.”
- `bar r^V` and `bar r^omega` are declared residual upper bounds used in the funnel budget.
- `gamma_priv,i^V(t)` and `gamma_priv,i^omega(t)` are residual-decay schedules, never physical funnels.
- `theta_i^{priv,V}`, `theta_i^{priv,omega}`, `w_{i,12}^V`, `w_{i,21}^V`, `w_{i,12}^omega`, and `w_{i,21}^omega` are private decomposition parameters. They carry no hats because the controller does not estimate them.
- `z_i^V=p_i^V-q_i^V` and `z_i^omega=p_i^omega-q_i^omega` are private decomposition differences. They are not transformed physical errors.
- `g_i^V` and `g_i^omega` are bounded local correction factors used only in the decomposition dynamics.
- `mathbf m_i=[p_i^V,p_i^omega]^T` is the regular public message vector.
- Public/private ownership is semantic. A locally reconstructed quantity is not public unless the observation map explicitly includes it.
- `c_cm^omega` is a common steady-state frequency correction used only in the sharing derivation.

## 6. Uncertainty and proof objects

- `R_i^V` and `R_i^omega` denote bounded physical or unmodeled channel terms.
- `X_cl` is the stacked closed-loop state used in the physical proof.
- `mathscr V_cl` is the composite Lyapunov candidate. The bare `V` is never used for a Lyapunov function.
- `mathscr V_V`, `mathscr V_omega`, and `mathscr V_priv` are the voltage, frequency, and privacy components of `mathscr V_cl`.
- `P_L` is reserved for a positive-definite Lyapunov matrix, if one is required.
- `lambda_min` and `lambda_max` apply only to explicitly named symmetric matrices.
- The composite proof state contains plant/controller states, transformed errors, public/private states, and residuals only.

## 7. Electrical and cyber graph notation

- `G_e=(mathcal V,mathcal E_e)` and `L_e` refer only to electrical coupling.
- `G_c=(mathcal V,mathcal E_c)` and `L_c` refer only to the fixed connected undirected cyber graph.
- `mathcal N_i^e` and `mathcal N_i^c` are electrical and cyber neighbor sets. A bare `mathcal N_i` is forbidden when both graphs appear.
- `a_ij` is a cyber adjacency weight. It is time-independent in the core theory.
- Cyber connectivity does not imply electrical connectivity, and electrical connectivity does not imply information flow.

## 8. Time and deadlines

- `T_V` and `T_omega` are designed physical recovery deadlines.
- `T_{V,meas}` and `T_{omega,meas}` are measured tolerance-entry times and must never replace the design symbols.
- Core signals are continuous-time and use parentheses, such as `p_i^V(t)`.
- Square-bracket sample notation is reserved for HIL logs and does not create a core sampled-data model.
- A prime denotes an alternative admissible privacy realization, never a time derivative.

## 9. Adversary and public history

- `y_adv(t)` is the instantaneous aggregate public observation.
- `O_adv[0,t]` is the complete public history, including every transmitted public value and all disclosed metadata.
- `H_c[0,t]` is the public graph/timing/metadata component of that history.
- `S_i` is the protected initial local virtual-coordination quantity; `S_i'` is an alternative admissible value.
- `A_i(S_i)` is the set of private explanations compatible with a declared public history.
- `E_inv` is attacker reconstruction/inversion error; `A_priv` is compatible-initialization ambiguity. Neither is a controller residual.
- The privacy claim is deterministic public-history indistinguishability under a passive eavesdropper. It is not complete security, active security, cryptographic secrecy, or differential privacy.

## 10. Experiment metrics

- `E_env` is maximum funnel violation.
- `E_V` and `E_omega` are final physical voltage and frequency errors.
- `E_share` and `E_share,max` are sharing deviation and its acceptance limit.
- `R_priv` is measured residual magnitude.
- `U_peak` is peak secondary input, `M_payload` is public payload size, and `N_seed` is the number of private initialization seeds.
- Every metric must map to a theorem, assumption, implementation fact, or explicitly non-theorem sensitivity objective.

## 11. Identifier convention

- `A-E*` denotes retained IJSS-derived equation families.
- `B-E*` denotes retained privacy-layer equation families.
- `N-E*` denotes newly coupled equation families.
- These are planning labels, not final equation numbers. Final results use Definition 1-2, Assumption 1-2, Lemma 1, and Theorem 1-4.

## Forbidden reuse table

| Symbol/family | Fixed meaning | Forbidden reuse |
|---|---|---|
| `V_i`, `omega_i` | Physical voltage/frequency | Lyapunov, virtual, or graph symbols |
| `P_i`, `Q_i` | Physical active/reactive power | Matrices or privacy states |
| `e_i`, `rho_i`, `zeta_i` | Physical error, funnel, transformed error | Estimation or residual families |
| `sigma_i` | Normalized physical error | Graph switching or privacy parameter |
| `chi_i^V` | Voltage backstepping error | Privacy substate difference |
| `p_i`, `q_i`, `r_i` | Public state, private state, privacy residual | Power, probability, reference, or generic disturbance |
| `z_i` | Public-private substate difference | Prescribed-performance transformed error |
| `hat c_i` | Local reconstruction | Public message or ideal state |
| `L_e`, `L_c` | Electrical/cyber operators | Interchangeable graph or Lyapunov object |
| `T_V`, `T_omega` | Designed physical deadlines | Measured times or hidden deadlines |
| `E_inv` | Attacker inversion metric | Physical residual or proof-state vector |
| prime symbol | Alternative privacy realization | Derivative |

## Pre-equation notation gate

Specification-only channel-suppressed notation such as `rho`, `sigma`, `zeta`, `z`, `r`, `c`, `g`, `T`, and `h(s)` must be expanded into the voltage or frequency family before manuscript equations are numbered. Young-inequality constants and comparison coefficients are derived proof constants, not controller states or privacy parameters.

Before deriving any equation, confirm that every symbol is present in the variable dictionary, has one ownership class and one channel role, belongs to a retained equation family, and supports a named theorem or experiment metric. Any symbol failing one of these checks is removed before derivation.
