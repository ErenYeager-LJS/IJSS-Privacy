# Variables 0807: Minimal Variable Dictionary

> Blueprint Version 2.1
> Privacy-Domain Revision: 2026-08-11
> Historical baseline: Blueprint Freeze Version 2.0, frozen 2026-08-07

## Scope and ownership

This is the authoritative inventory before equation generation. `Public` means included in the declared cyber observation history; `Private` means retained locally and excluded from regular messages; `Local` means measured or computed at one DG and not public by default. A symbol may not be introduced only because it appears in either source paper.

All dimensions marked `TBD after equation freeze` must be fixed before the symbol enters a theorem. The dictionary contains no observer, neighbor-estimation, online-approximation, switching-topology, sampled-data, or anti-windup state families.

## 1. Indices and sets

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `i` | Local DG index | Integer | Public index | All local signals |
| `j,k` | Other DG, neighbor, or line index | Integer | Public index | Graph and coupling terms |
| `N` | Number of DGs | Positive integer | Public | Network stacking |
| `mathcal V` | DG vertex set | Finite set | Public | Both graphs |
| `mathcal E_e` | Electrical edge set | Set of pairs | Public | Power-flow model |
| `mathcal E_c` | Cyber edge set | Set of pairs | Public | Communication model |
| `mathcal N_i^e` | Electrical neighbors of DG `i` | Set | Public model data | Electrical coupling |
| `mathcal N_i^c` | Cyber neighbors of DG `i` | Set | Public model data | Direct public-state receipt |
| `Delta` | Compact admissible operating region | Set | Public assumption | Boundedness domain |

## 2. Electrical and cyber graphs

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `G_e=(mathcal V,mathcal E_e)` | Electrical power-flow graph | Graph | Public model data | Plant coupling |
| `L_e` | Electrical Laplacian/coupling operator, if used | Matrix | Public | Power-flow analysis |
| `G_c=(mathcal V,mathcal E_c)` | Fixed connected undirected cyber graph | Graph | Public protocol data | Distributed coordination |
| `L_c` | Cyber Laplacian | Symmetric matrix | Public | Consensus/pinning analysis |
| `a_ij` | Cyber adjacency weight | Nonnegative scalar | Public | Message coupling |
| `b_i` | Reference-pinning weight | Nonnegative scalar | Public | Voltage/frequency reference access |
| `Y_ik` | Electrical line admittance | Complex scalar | Public plant data | Power-flow relation |
| `G_ik`, `B_ik` | Line conductance and susceptance | Scalars | Public plant data | Real/reactive power terms |

Electrical and cyber graphs are distinct objects. Connectivity of one graph never implies connectivity of the other.

## 3. Physical plant and measurements

| Symbol | Meaning | Type or dimension | Units | Ownership | Use |
|---|---|---|---|---|---|
| `V_i` | Physical voltage amplitude | Scalar | V | Local | Voltage regulation |
| `omega_i` | Physical angular frequency | Scalar | rad/s | Local | Frequency regulation |
| `delta_i` | Voltage phase angle | Scalar | rad | Local | Power flow |
| `P_i` | Physical active power | Scalar | W | Local | Droop sharing |
| `Q_i` | Physical reactive power | Scalar | var | Local | Droop/voltage model |
| `P_i^m` | Filtered active power | Scalar | W | Local | Droop implementation |
| `Q_i^m` | Filtered reactive power | Scalar | var | Local | Droop implementation |
| `P_i^L` | Local active load | Scalar | W | Local | Plant uncertainty/model |
| `Q_i^L` | Local reactive load | Scalar | var | Local | Plant uncertainty/model |
| `S_i^L` | Local apparent-load quantity, if required | Scalar | VA | Local | Power-flow notation |
| `x_i^V` | Local voltage-channel state vector | Vector, dimension TBD | Channel-dependent | Local | Voltage controller |
| `x_i^omega` | Local frequency-channel state vector | Vector, dimension TBD | Channel-dependent | Local | Frequency controller |

### Equation-stage plant parameters

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `tau_Pi` | Active-power/frequency filter time constant | Positive scalar | Public plant data | Frequency drift |
| `tau_Qi` | Reactive-power/voltage filter time constant | Positive scalar | Public plant data | Voltage drift |
| `k_Pi` | Active-power droop coefficient | Positive scalar | Public plant data | Frequency droop |
| `k_Qi` | Reactive-power droop coefficient | Positive scalar | Public plant data | Voltage droop |
| `k_Vi` | Voltage-loop coefficient | Positive scalar | Public plant data | Voltage dynamics |
| `P_i^d` | Active-power droop setpoint | Scalar | Public plant data | Frequency equilibrium |
| `Q_i^d` | Reactive-power droop setpoint | Scalar | Public plant data | Voltage equilibrium |

Raw physical states and inputs are excluded from the regular cyber payload.

## 4. References, errors, funnels, and deadlines

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `V_ref` | Voltage reference | Scalar | Public design data | Voltage objective |
| `omega_ref` | Angular-frequency reference | Scalar | Public design data | Frequency objective |
| `e_i^V` | Voltage tracking/coordination error | Scalar or local vector, TBD | Local | Voltage funnel |
| `e_i^omega` | Frequency tracking/coordination error | Scalar or local vector, TBD | Local | Frequency funnel |
| `rho_i^V(t)` | Voltage prescribed-performance envelope | Positive scalar | Public design data | Funnel boundary |
| `rho_i^omega(t)` | Frequency prescribed-performance envelope | Positive scalar | Public design data | Funnel boundary |
| `zeta_i^V` | Transformed voltage error | Scalar/vector | Local analysis state | Voltage proof |
| `zeta_i^omega` | Transformed frequency error | Scalar/vector | Local analysis state | Frequency proof |
| `e_{i,0}^V` | Local physical voltage error | Scalar | Local | Voltage transformation |
| `e_{i,0}^omega` | Local physical frequency error | Scalar | Local | Frequency transformation |
| `sigma_i^V` | Normalized voltage error | Scalar | Local analysis state | Transformation |
| `sigma_i^omega` | Normalized frequency error | Scalar | Local analysis state | Transformation |
| `rho_{i,0}^V`, `rho_{i,0}^omega` | Initial funnel radii | Positive scalars | Public design data | Transformation initialization |
| `rho_{i,infty}^V`, `rho_{i,infty}^omega` | Post-deadline funnel radii | Positive scalars | Public design data | Practical tolerance |
| `epsilon_final^V` | Final practical voltage tolerance | Positive scalar | Public design data | Deadline metric |
| `epsilon_final^omega` | Final practical frequency tolerance | Positive scalar | Public design data | Deadline metric |
| `T_V` | Designed voltage recovery deadline | Positive scalar | Public design data | Theorem 2 |
| `T_omega` | Designed frequency recovery deadline | Positive scalar | Public design data | Theorem 2 |

Funnel invariance and tolerance entry are separate claims. `T_V` and `T_omega` are design deadlines, not measured times.

## 5. Nominal coordination and physical inputs

| Symbol | Meaning | Type or dimension | Ownership | Use |
|---|---|---|---|---|
| `c_i^V` | Ideal voltage virtual coordination state | Scalar/vector, TBD | Local | Nominal controller output |
| `c_i^omega` | Ideal frequency virtual coordination state | Scalar/vector, TBD | Local | Nominal controller output |
| `hat c_i^V` | Locally reconstructed voltage coordination state | Scalar/vector | Local | Applied control interface |
| `hat c_i^omega` | Locally reconstructed frequency coordination state | Scalar/vector | Local | Applied control interface |
| `u_i^V` | Reconstructed voltage secondary input | Scalar/vector | Local | Plant input |
| `u_i^omega` | Reconstructed frequency secondary input | Scalar/vector | Local | Plant input |
| `alpha_i^V` | Voltage backstepping virtual control, if retained | Scalar/vector | Local | Controller design |
| `alpha_i^omega` | Frequency virtual control, if retained | Scalar/vector | Local | Controller design |
| `k_V`, `k_omega` | Channel controller gains | Positive scalars/matrices | Public design data | Stability tuning |
| `Pi_V`, `Pi_omega` | Channel funnel allocations, if used | Positive scalars | Public design data | Residual budgeting |
| `U_i` | Feasible local secondary-input set | Set | Public assumption | Actuator regularity |
| `F_i^V` | Known voltage-channel drift excluding secondary input and bounded uncertainty | Scalar | Local analysis quantity | State form |
| `F_i^omega` | Known frequency-channel drift excluding secondary input and bounded uncertainty | Scalar | Local analysis quantity | State form |
| `chi_i^V` | Voltage backstepping error | Scalar | Local analysis state | Voltage controller |
| `k_1^V`, `k_2^V` | Voltage funnel/backstepping gains | Positive scalars | Public design data | Voltage stability |
| `k_1^omega`, `k_c^V`, `k_c^omega` | Frequency/frequency-coordination gains | Positive scalars | Public design data | Controller tuning |
| `lambda_tr,i^V`, `lambda_tr,i^omega` | Public/private command-tracking rates | Positive scalars with unit 1/s | Public design data | Privacy dynamics |
| `bar R_i^V`, `bar R_i^omega` | Declared bounds on physical uncertainty | Positive scalars | Public design data | Practical bounds |

The exact order and dimensions of `x`, `c`, `hat c`, `u`, and `alpha` are equation-stage decisions.

## 6. Public/private privacy layer

| Symbol | Meaning | Type or dimension | Ownership | Use |
|---|---|---|---|---|
| `p_i^V` | Public voltage virtual coordination substate | Scalar/vector | Public | Neighbor message |
| `p_i^omega` | Public frequency virtual coordination substate | Scalar/vector | Public | Neighbor message |
| `q_i^V` | Private voltage virtual coordination substate | Scalar/vector | Private | Local decomposition |
| `q_i^omega` | Private frequency virtual coordination substate | Scalar/vector | Private | Local decomposition |
| `r_i^V` | Voltage reconstruction residual, reconstructed minus ideal | Scalar/vector | Local | Funnel and residual bound |
| `r_i^omega` | Frequency reconstruction residual, reconstructed minus ideal | Scalar/vector | Local | Funnel and sharing bound |
| `bar r^V` | Declared voltage residual upper bound | Positive scalar/vector bound | Public design data | Assumption 2 |
| `bar r^omega` | Declared frequency residual upper bound | Positive scalar/vector bound | Public design data | Assumption 2 |
| `gamma_priv,i^V(t)` | Voltage residual-decay schedule | Nonnegative function | Public design data | Lemma 1 |
| `gamma_priv,i^omega(t)` | Frequency residual-decay schedule | Nonnegative function | Public design data | Lemma 1 |
| `theta_i^{priv,V}` | Private voltage decomposition parameter | Scalar/vector | Private | Alternative realizations |
| `theta_i^{priv,omega}` | Private frequency decomposition parameter | Scalar/vector | Private | Alternative realizations |
| `w_{i,12}^V`, `w_{i,21}^V` | Private voltage coupling weights | Scalars/matrices | Private | Decomposition dynamics |
| `w_{i,12}^omega`, `w_{i,21}^omega` | Private frequency coupling weights | Scalars/matrices | Private | Decomposition dynamics |
| `z_i^V`, `z_i^omega` | Public-private substate differences | Scalar/vector | Private analysis state | Residual dynamics |
| `g_i^V`, `g_i^omega` | Bounded decomposition correction factors | Nonnegative scalars | Local/private | Residual dynamics |
| `underline w_i^V`, `bar w_i^V` | Voltage private-weight lower/upper bounds | Positive scalars | Public bounds | Admissibility |
| `underline w_i^omega`, `bar w_i^omega` | Frequency private-weight lower/upper bounds | Positive scalars | Public bounds | Admissibility |
| `eta_{z,i}^V`, `eta_{z,i}^omega` | Declared nonzero initial private-split margins | Positive scalars with the corresponding channel-command unit | Public design data | Assumption 2 regular privacy domain |
| `eta_{w,i}^V`, `eta_{w,i}^omega` | Declared private-weight interior margins | Positive scalars with the corresponding private-weight unit | Public design data | Assumption 2 regular privacy domain |
| `mathbf m_i` | Regular public message vector | Vector `[p_i^V,p_i^omega]^T` | Public | Cyber payload |

Only `p_i^V` and `p_i^omega` are regular coordination payloads.

## 7. Physical uncertainty and proof objects

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `R_i^V` | Bounded voltage-channel physical/unmodeled term | Scalar/vector | Local analysis quantity | Assumption 1; Theorems 1-2 |
| `R_i^omega` | Bounded frequency-channel physical/unmodeled term | Scalar/vector | Local analysis quantity | Assumption 1; Theorems 1-3 |
| `X_cl` | Stacked closed-loop state used in the proof | Vector, dimension TBD | Local analysis object | Theorem 1 |
| `mathscr V_cl` | Composite Lyapunov candidate | Scalar | Analysis object | Theorems 1-2 |
| `mathscr V_V`, `mathscr V_omega`, `mathscr V_priv` | Voltage, frequency, and privacy Lyapunov components | Scalars | Analysis objects | Theorem 1 |
| `P_L` | Positive-definite Lyapunov matrix, if needed | Matrix | Analysis object | Theorem 1 |
| `lambda_min`, `lambda_max` | Extremal eigenvalue notation | Scalars | Analysis notation | Symmetric matrices only |
| `Delta` | Compact operating region | Set | Public assumption | Boundedness |

The composite proof state contains only plant/controller states, transformed errors, public/private states, and residuals. It contains no auxiliary estimation or approximation state.

## 8. Adversary and privacy metrics

| Symbol | Meaning | Type | Ownership | Use |
|---|---|---|---|---|
| `y_adv(t)` | Instantaneous aggregate public observation | Vector | Public | Definition 2 |
| `O_adv[0,t]` | Complete public observation history | History object | Public | Definition 2; Theorem 4 |
| `H_c[0,t]` | Public topology, timing, and metadata history | History object | Public | Observation map |
| `S_i` | Protected initial local virtual-coordination quantity | Scalar/vector | Private target | Privacy claim |
| `S_i'` | Alternative admissible protected quantity | Scalar/vector | Private construction | Privacy claim |
| `A_i(S_i)` | Private explanations compatible with a public history | Set | Analysis object | Indistinguishability |
| `E_inv` | Attacker reconstruction/inversion error | Scalar/vector metric | Experiment output | Privacy evidence |
| `A_priv` | Compatible-initialization ambiguity metric | Scalar/set metric | Experiment output | Privacy evidence |
| `c_cm^omega` | Common steady-state frequency correction | Scalar | Public equilibrium quantity | Theorem 3 |

Privacy is deterministic public-history indistinguishability, not a probabilistic or cryptographic metric.

## 9. Experiment and HIL metrics

| Symbol | Meaning | Type | Use |
|---|---|---|---|
| `T_{V,meas}` | Worst-DG measured voltage tolerance-entry time | Scalar | Compare with `T_V` |
| `T_{omega,meas}` | Worst-DG measured frequency tolerance-entry time | Scalar | Compare with `T_omega` |
| `E_env` | Maximum funnel violation | Scalar | Theorem 1 evidence |
| `E_V` | Final voltage error | Scalar | Theorem 2 evidence |
| `E_omega` | Final frequency error | Scalar | Theorem 2 evidence |
| `E_share` | Active-power sharing deviation | Scalar | Theorem 3 evidence |
| `E_share,max` | Declared sharing acceptance limit | Scalar | Experiment criterion |
| `R_priv` | Simulated/HIL residual magnitude | Scalar | Lemma 1 evidence |
| `U_peak` | Peak secondary input | Scalar | Engineering report |
| `M_payload` | Public message payload size | Integer/bytes | Communication cost |
| `N_seed` | Number of private initialization seeds | Integer | Reproducibility |

## 10.1 Derived proof symbols

The following are derived constants or channel-suppressed proof notation, not additional controller modules:

| Symbol | Meaning | Status |
|---|---|---|
| `h_i^V`, `h_i^omega` | Instantaneous channel transformation gains `1/[rho_i(1-sigma_i^2)]` | Derived signals |
| `h_bar_i` | Upper bound on the channel transformation gain | Derived from the invariant set |
| `D_i^V`, `D_i^omega` | Aggregated channel disturbance bounds used in Young inequalities | Derived bound |
| `eps_V2`, `eps_omega`, `eps_r1`, `eps_r2` | Positive Young-inequality constants | Proof constants |
| `w_delta_bar_i` | Bound on `|w_{i,12}-w_{i,21}g_i|` | Derived private-weight bound |
| `a_z`, `a_r`, `d_c`, `a_cl`, `d_R`, `d_priv` | Composite comparison coefficients | Derived proof constants |
| `h(s)`, `s`, `T` | Specification-only funnel schedule notation | Meta-notation; expand by channel before manuscript use |
| `delta_ik` | Phase difference `delta_i-delta_k` | Derived shorthand |
| `I_N` | Identity matrix of size `N` | Standard matrix notation |
| `c_i'`, `q_i'`, `w_i'` | Alternative private realization variables | Privacy-construction notation |

## 10.2 Source and identifier contract

`A-E*` labels identify retained IJSS-derived equation families; `B-E*` labels identify retained privacy-layer families; `N-E*` labels identify newly coupled families. They are planning labels, not final equation numbers. Final results use Definition 1-2, Assumption 1-2, Lemma 1, and Theorem 1-4.

## 10.3 Notation-level freeze update

The symbols added in Sections 3-6 are equation-stage auxiliaries required to make the frozen modules explicit. Blueprint Version 2.1 adds only `eta_{z,i}^nu` and `eta_{w,i}^nu` as privacy-domain design margins; they are not states, controller gains, masking signals, or existence certificates. No observer, estimator, approximator, graph-switching, sampling, or controller subsystem is added.

## 11. Ownership and forbidden reuse rules

- `V_i`, `omega_i`, `P_i`, and `Q_i` are physical quantities only.
- `p` means public virtual state; `q` means private virtual state; `r` means privacy residual.
- `e` means physical tracking/coordination error; `zeta` means transformed error; `R` means bounded physical uncertainty.
- A hat means local reconstruction, not public disclosure.
- `L_e` and `L_c` are graph-qualified and never interchangeable.
- A prime denotes an alternative privacy realization, never a derivative.
- No Nash/game variables, cryptographic variables, stochastic privacy parameters, or active-attack symbols are admissible.

## Pre-equation gate

Before equation generation, verify that every symbol used appears here, has one ownership class, has a fixed channel role, and is connected to one retained equation family and one theorem or declared experiment metric. Any symbol without that mapping is dead code and must be removed or explicitly justified.
