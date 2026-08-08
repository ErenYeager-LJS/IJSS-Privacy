# Mathematical Roadmap 0807: Minimal Architecture

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07

## Scope

This roadmap specifies why each surviving equation family is needed and how the families connect. It does not derive equations, write proofs, or generate LaTeX.

The core mathematical choice is a continuous-time model with:

- the IJSS physical inverter/droop and power-flow backbone;
- a fixed connected undirected cyber graph with direct public-state receipt;
- a public/private virtual coordination wrapper;
- a computable, bounded, decaying privacy residual;
- bounded physical uncertainty handled directly in the prescribed-performance controller;
- no PTESO, neighbor estimator, RBFNN, adaptive projection, explicit common-mode projection, or sampled-data theorem.

## 1. Mathematical Architecture at a Glance

The equation order is:

1. physical plant and droop dynamics;
2. electrical power-flow coupling;
3. fixed cyber graph and direct public-state information flow;
4. practical prescribed-time and funnel objectives;
5. voltage/frequency distributed errors;
6. virtual coordination interface;
7. public/private decomposition and residual;
8. nominal prescribed-performance controllers under bounded uncertainty;
9. composite residual-to-physical performance bound;
10. sharing compatibility and public-history indistinguishability.

The privacy layer acts on virtual coordination states and never replaces physical voltage, frequency, current, or power states in the plant model.

## 2. Equation-Block Ledger

### 2.1 Physical and controller blocks

| ID | Equation family | Why needed | Provenance | Primary proof / analysis tool |
|---|---|---|---|---|
| A-E1 | DG inverter/droop dynamics | Defines the physical states and the location of secondary inputs | IJSS | State-space modeling and local well-posedness |
| A-E2 | Electrical power-flow relations | Couples voltage, phase, active/reactive power, loads, and electrical neighbors | IJSS | Network modeling and bounded nonlinear-term analysis |
| A-E3 | Secondary-input insertion | Connects reconstructed virtual coordination to the plant | IJSS adapted | Input-affine interface and actuator-feasibility argument |
| A-E4 | Practical prescribed-time definition | Fixes tolerance-entry rather than unjustified exact convergence | IJSS rewritten | Comparison principle and tolerance-entry definition |
| A-E6 | Control objectives and funnel parameters | Defines references, envelopes, deadlines, tolerances, and sharing target | IJSS rewritten | Performance specification and residual budgeting |
| A-E7 | Voltage neighborhood/pinning error | Forms the distributed voltage objective from local states and received public states | IJSS adapted | Symmetric graph/Laplacian and pinning analysis |
| A-E8 | Frequency consensus/pinning error | Forms the distributed frequency objective and sharing-compatible equilibrium condition | IJSS adapted | Symmetric graph/Laplacian and equilibrium decomposition |
| A-E9 | Error-dependent funnel transformation | Converts physical transient constraints into bounded transformed errors | IJSS | Prescribed-performance transformation and invariance |
| A-E10 | Voltage state-space and bounded nonlinear decomposition | Exposes the voltage channel and collects unknown network/load terms | IJSS simplified | Backstepping and bounded-input propagation |
| A-E11 | Frequency state-space and bounded nonlinear decomposition | Exposes frequency coupling and active-power terms | IJSS simplified | Prescribed-performance Lyapunov analysis and bounded-input propagation |
| A-E13 | Voltage controller | Stabilizes the transformed voltage channel under declared bounds | IJSS structurally adapted | Backstepping and Lyapunov analysis |
| A-E14 | Frequency controller | Restores frequency under direct public-state coordination | IJSS structurally adapted | Prescribed-performance Lyapunov analysis |
| A-E15 | Channel/composite Lyapunov inequalities | Closes boundedness and funnel claims without NN or observer states | IJSS structurally simplified | Lyapunov analysis and comparison principle |
| A-E17 | Droop-sharing steady-state relation | Connects equal nominal frequency compensation to active-power sharing | IJSS principle, rewritten | Steady-state droop relation |

### 2.2 Privacy blocks

| ID | Equation family | Why needed | Provenance | Primary proof / analysis tool |
|---|---|---|---|---|
| B-E1 | Fixed connected undirected cyber graph | Supplies the minimum public information flow for direct neighbor receipt | Simplified Privacy/IJSS abstraction | Symmetric Laplacian and pinning property |
| B-E2 | Public/private state decomposition | Creates the hidden internal degrees of freedom | Privacy adapted | State-space decomposition and boundedness |
| B-E3 | Private internal coupling dynamics | Gives the hidden state a controlled evolution and residual decay | Privacy adapted | Invariance and residual-system analysis |
| B-E4 | Public-state update law | Defines the trajectory seen by neighbors and the eavesdropper | Privacy adapted | Distributed-state evolution and observation-map construction |
| B-E5 | Privacy residual definition | Names the transient mismatch instead of hiding it in uncertainty | New adaptation | Direct residual bound and propagation |
| B-E9 | Public observation map | Defines every quantity available to the passive eavesdropper | New formalization | Observation-map specification |
| B-E10 | Observation-equivalence relation | Formalizes identical public histories from different private initializations | Privacy principle, rewritten | Indistinguishability construction |
| B-E11 | Alternative private-parameter construction | Proves public-history non-uniqueness | Privacy principle, adapted | Admissible-parameter argument |
| B-E12 | Decaying residual envelope | Converts the decomposition schedule into a usable physical bound | New adaptation | Residual bounding and comparison principle |

### 2.3 New coupling blocks

| ID | Equation family | Why it is new | Primary proof / analysis tool |
|---|---|---|---|
| N-E1 | Electrical/cyber graph separation | Prevents physical and information coupling from being conflated | Two-graph state-space modeling |
| N-E2 | Virtual coordination interface | Attaches privacy to a secondary signal rather than a raw physical state | Interface consistency |
| N-E3 | Channel-specific decomposition | Respects different voltage/frequency dynamic orders | Channel-wise state decomposition |
| N-E4 | Bounded uncertainty plus privacy residual interface | Places physical uncertainty and the named residual in one explicit bound | Input-to-state/residual propagation |
| N-E5 | Privacy-aware funnel bound | Allocates a bounded decaying residual inside the physical performance analysis | Invariance and comparison principle |
| N-E7 | Minimal composite error state | Stacks plant, transformed tracking, and privacy residual states only | Augmented-state construction |
| N-E8 | Minimal composite Lyapunov candidate | Provides one proof object without deleted observer/NN components | Lyapunov analysis |
| N-E9 | Residual-to-physical-performance propagation | Converts the residual bound into voltage/frequency and sharing bounds | Comparison principle and residual propagation |
| N-E10 | Frequency equilibrium compatibility | Makes the differential privacy correction vanish without projection | Equilibrium decomposition and droop relation |
| N-E12 | Metric-to-theorem correspondence | Maps experiments to theorem quantities | Claim-to-evidence mapping, not proof |

## 3. Equation Connections

### 3.1 Physical chain

`A-E1/A-E2 -> A-E3 -> A-E7/A-E8 -> A-E9 -> A-E10/A-E11 -> A-E13/A-E14 -> A-E15`

This chain is the simplified IJSS backbone. Unknown network/load terms are bounded on the declared operating region; they are not approximated online by RBFNNs.

### 3.2 Privacy chain

`B-E1 -> B-E2/B-E3/B-E4 -> B-E5/B-E12 -> B-E9/B-E10 -> B-E11`

The public state is directly received by neighbors. There is no `hat p_ij` estimator layer. The residual is locally computable and decays under Assumption 2; it is not estimated by PTESO.

### 3.3 Coupling chain

`A-E13/A-E14 + B-E5/B-E12 -> N-E4/N-E5 -> N-E7/N-E8 -> Theorem 1 -> Theorem 2`

`A-E14 + N-E10 + A-E17 -> Theorem 3`

`B-E9/B-E10/B-E11 + Definitions 1-2 -> Theorem 4`

The privacy proof and physical Lyapunov proof remain separate until Theorem 4 composes their conclusions.

## 4. Assumption Ledger

### Assumption 1: Plant, reference, graph, and uncertainty regularity

The plant is locally well posed on a compact admissible operating region; references and required derivatives are bounded; electrical parameters and loads are bounded; physical network/load nonlinearities and disturbances have known bounds; the cyber graph is fixed, connected, undirected, and properly pinned; initial errors lie inside the initial funnels; and secondary inputs remain actuator-feasible.

This assumption supports A-E1-A-E4, A-E6-A-E15, B-E1, and Theorems 1-3.

### Assumption 2: Privacy decomposition and adversary compatibility

Private weights and substates remain admissible and bounded; the public/private decomposition is locally computable; the channel-specific residual has a declared nonnegative bound that decays as required by the sharing claim; the frequency residual has zero differential steady-state component; and the eavesdropper observes all public messages and disclosed metadata but cannot access private memory or local physical sensors.

This assumption supports B-E2-B-E12, Lemma 1, Theorem 3, and Theorem 4.

No observer derivative bound, graph switching condition, packet-loss condition, or NN approximation-region assumption is part of the core model.

## 5. Lemma and Theorem Dependencies

### Lemma 1: Public/private decomposition regularity and residual property

Under Definitions 1 and 2 and Assumption 2, the public/private substates and private parameters are well posed and bounded; the local reconstruction residual is computable and bounded; the residual follows the declared decay schedule; and for every admissible alternative protected initial state there exists an admissible private realization with the same public observation history.

### Theorem 1: Closed-loop boundedness and funnel invariance

Under Definition 1, Assumptions 1-2, and Lemma 1, all physical, public/private, transformed-error, and input signals remain bounded, and voltage/frequency errors stay inside their prescribed funnels.

### Theorem 2: Practical prescribed-time voltage and frequency recovery

Under Theorem 1 and the residual propagation bound, all DG voltage and frequency errors enter their declared practical tolerances by `T_V` and `T_omega`. The result is practical prescribed-time recovery, not automatic exact-zero convergence.

### Theorem 3: Droop-consistent active-power sharing

Under Assumptions 1-2 and Theorem 2, the differential steady-state frequency privacy correction vanishes. The remaining nominal equal frequency compensation preserves the IJSS droop-based active-power relation. If residual decay is not strong enough for exact asymptotic equality, the theorem must state the resulting residual-dependent sharing bound.

### Theorem 4: Privacy-preserving composite guarantee

Under Definitions 1-2, Assumptions 1-2, Lemma 1, and Theorems 1-3, the same closed loop simultaneously satisfies public-history indistinguishability, boundedness, funnel invariance, practical prescribed-time recovery, and droop-consistent sharing under the declared passive-eavesdropper model.

## 6. Proof Method Consistency Check

1. Theorem 1 uses bounded-input Lyapunov analysis, funnel invariance, and a comparison principle.
2. Theorem 2 uses the transformed-error Lyapunov inequality and residual propagation; it does not use observer convergence.
3. Theorem 3 uses the equilibrium compatibility condition and the steady-state droop relation; it does not infer sharing from voltage/frequency recovery alone.
4. Theorem 4 uses an observation-equivalence construction separately from the physical Lyapunov proof.
5. Every residual in the composite claim is bounded by Lemma 1 or Assumption 1.
6. No theorem depends only on simulation.

## 7. Source and Non-Goal Ledger

### Retained from IJSS

- physical plant and power-flow model;
- voltage/frequency channel separation;
- distributed pinning/consensus errors;
- prescribed-performance transformation;
- bounded-uncertainty/backstepping structure;
- practical prescribed-time definition;
- droop-sharing steady-state relation.

### Retained from Privacy

- public/private decomposition;
- private internal parameters;
- passive public-history observation model;
- indistinguishability construction.

### Deleted source baggage

- PTESO and all observer equations;
- neighbor public-state estimator;
- RBFNN and adaptive projection;
- directed/time-varying graph core;
- positive residual floor;
- explicit common-mode projection;
- sampled-data theorem map and Optional T7.

## 8. Equation-Generation Gate

Before writing equations, resolve only:

- exact decomposition/reconstruction map;
- residual decay law and channel-specific bounds;
- robust/backstepping controller form under bounded physical uncertainty;
- fixed-graph pinning convention;
- frequency equilibrium compatibility condition;
- whether the residual enters the input explicitly or only its bound enters the proof.

No deleted module may re-enter as an unspoken helper variable.
