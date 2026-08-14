# Manuscript Main-Body Draft

> Task-029-D working draft. This document excludes Discussion and Conclusion.
> It does not replace or modify the tracked IEEE LaTeX manuscript.

## I. Introduction

Islanded AC microgrids use hierarchical control to coordinate inverter-based
distributed generators (DGs). Primary droop control provides decentralized
load response, but it generally leaves voltage and frequency offsets that must
be corrected by a secondary layer \cite{Guerrero2011,Bidram2012}. Distributed
secondary control reduces dependence on a central coordinator by exchanging
coordination variables over a cyber graph. This architecture supports voltage
restoration and frequency regulation, while the underlying droop
characteristics remain responsible for power allocation among heterogeneous
DGs \cite{Lantao2019,Xiaokang2023,Rosini2024,Bu2025}.

The communication channel needed for distributed regulation also creates an
information-exposure surface. An observer that records the exchanged
coordination signals may attempt to reconstruct local controller states or
protected initialization data. Existing privacy-preserving consensus methods
include weighted interactions and state-decomposition mechanisms that admit
different internal realizations for a declared public trajectory
\cite{WangLiuLiHuang2021,SD,SD-MSR,YeCaoChowCai2024}. These mechanisms address
observation ambiguity rather than message encryption, differential privacy,
or resilience to an adversary that modifies the communication process. Active
attacks and communication failures therefore remain outside the passive
observation model considered here \cite{Huang2026}.

Physical regulation and public-history indistinguishability must be analyzed
separately. A privacy wrapper that hides internal variables does not by itself
establish local well-posedness of the coupled plant and controller. Similarly,
a physically regular secondary controller does not prevent a public observer
from identifying a unique private realization. Prescribed Performance Control
(PPC) provides a structured way to impose a time-varying admissible envelope on
tracking errors \cite{Bechlioulis2008}, but prescribed-performance coordinates
must not be confused with a prescribed-time recovery theorem. The latter is
not established by the present proof chain.

This work studies whether a distributed secondary controller can retain a
rigorous local physical analysis while preventing unique reconstruction of
protected virtual coordination data from the complete passive public history.
The proposed architecture combines the fixed droop-controlled microgrid, a
distributed secondary controller, PPC coordinates, and a public/private
virtual-state decomposition. The physical analysis is restricted to the open
admissible domain and, for compact-dependent estimates, to the selected compact
bootstrap region $\mathcal K_0$ before the first admissibility exit. The
privacy construction is existence-based and stops at the earliest finite-seed
or regular-domain boundary.

The contributions are two bounded results. First, the specified closed loop is
shown to admit a unique local solution together with finite component bounds,
a finite privacy-residual estimate, compact-region actuator feasibility, and a
composite local comparison inequality before the applicable exit. Second, an
admissible non-nominal private initialization is constructed and locally
continued so that it produces the same complete passive public history as the
nominal realization. These results are intentionally separate. Global
continuation, forward invariance, all-time funnel or actuator feasibility,
prescribed-time recovery, asymptotic residual convergence, an active-power
sharing theorem, and a simultaneous physical/privacy theorem are not claimed.

## II. Proposed Methodology and Control Framework

### A. Droop-Controlled Microgrid

Consider an islanded microgrid with $N$ inverter-based DGs. For DG $i$, let
$V_i$, $\omega_i$, and $\delta_i$ denote voltage amplitude, angular frequency,
and phase angle. The reduced voltage and frequency dynamics are

$$
\tau_{P_i}\dot\omega_i
=-(\omega_i-\omega_{\mathrm{ref}})
-k_{P_i}(P_i-P_i^d)-u_i^\omega+\tau_{P_i}R_i^\omega,
$$

$$
\tau_{Q_i}k_{V_i}\ddot V_i
=-(\tau_{Q_i}+k_{V_i})\dot V_i-(V_i-V_{\mathrm{ref}})
-k_{Q_i}(Q_i-Q_i^d)-u_i^V+\tau_{Q_i}k_{V_i}R_i^V.
$$

The electrical graph determines the active- and reactive-power couplings. A
separate fixed, connected, undirected cyber graph determines which public
coordination variables are exchanged. At least one DG is pinned to the
reference in each regulated channel. Keeping the electrical and cyber graphs
distinct prevents communication adjacency from being confused with physical
line coupling.

### B. Secondary-Control Architecture and Operating Sequence

For each channel $\nu\in\{V,\omega\}$, the secondary controller forms a
nominal coordination command $c_i^\nu$. A privacy wrapper decomposes this
command into a transmitted public substate $p_i^\nu$ and a private substate
$q_i^\nu$, and the locally reconstructed command is

$$
\widehat c_i^\nu=c_i^\nu+r_i^\nu,
$$

where $r_i^\nu$ is the finite local reconstruction residual retained explicitly
in the analysis. The plant interface is unique:

$$
u_i^V=\widehat c_i^V,\qquad
u_i^\omega=\widehat c_i^\omega.
$$

The numerical case uses a three-stage timeline. During Stage 1,
$0\leq t<5.00$ s, only primary droop control operates. At Stage 2,
$t=5.00$ s, the frozen secondary-control path is activated. During Stage 3,
the secondary controller reduces voltage and frequency tracking errors while
the PPC coordinates remain within their admissible numerical boundaries in the
selected run. The marker at $6.30$ s is used to evaluate the requested settling
behavior; it is a numerical marker, not a theorem-level deadline.

The selected simulation also records active-power allocation. Its role is to
check whether secondary voltage/frequency restoration destroys the displayed
droop-based proportional relationship. This is a numerical preservation
diagnostic, not an exact-sharing result and not an active-power sharing theorem.

### C. Prescribed Performance Control

For channel $\nu\in\{V,\omega\}$, PPC assigns the tracking error
$e_{i,0}^\nu$ a positive time-varying envelope

$$
\rho_i^\nu(t)=\rho_{i,\infty}^\nu+
(\rho_{i,0}^\nu-\rho_{i,\infty}^\nu)h(t/T_\nu),
$$

where

$$
h(s)=
\begin{cases}
1-10s^3+15s^4-6s^5,&0\leq s\leq 1,\\
0,&s>1.
\end{cases}
$$

The normalized and transformed errors are

$$
\sigma_i^\nu=\frac{e_{i,0}^\nu}{\rho_i^\nu},\qquad
\zeta_i^\nu=\operatorname{atanh}(\sigma_i^\nu),\qquad
h_i^\nu=\frac{1}{\rho_i^\nu[1-(\sigma_i^\nu)^2]}.
$$

These coordinates are defined only for $|\sigma_i^\nu|<1$. Thus, remaining
inside the predefined performance boundary on a stated interval enforces the
corresponding transient envelope on that interval. It does not prove that the
boundary is forward invariant for all time. The voltage channel additionally
uses a backstepping error $\chi_i^V=\dot V_i-\alpha_i^V$, while the frequency
channel is first order. The specified commands retain the physical uncertainty
and privacy residual as separate terms rather than absorbing one into the
other.

## III. Privacy-Preserving Mechanism

### A. Passive Observation Model

Each DG transmits only

$$
\bm m_i(t)=\begin{bmatrix}p_i^V(t)&p_i^\omega(t)\end{bmatrix}^{T}.
$$

The passive eavesdropper observes the complete history of these public
messages together with the disclosed cyber graph, timing and protocol
metadata, public references, schedules, and declared public controller
parameters. The observation channel does not include the private substates
$q_i^\nu$, private weights, residual variables, local controller memory,
locally reconstructed commands, or raw physical-sensor histories. The model
therefore addresses inference from the declared communication record only.

### B. Alternative Private Initialization

Let the protected initial virtual command of DG $i$ be

$$
S_i=\begin{bmatrix}c_i^V(0)&c_i^\omega(0)\end{bmatrix}^{T}.
$$

An alternative realization keeps the initial public message unchanged and
moves the private component:

$$
p_i'(0)=p_i(0),\qquad
q_i'(0)=2S_i'-p_i(0),\qquad S_i'\neq S_i.
$$

For a sufficiently small nonzero perturbation inside the declared strict
privacy-domain margins, the alternative split is nonzero, the forced private
weights remain inside their admissible intervals, and the coupled plant and
wrapper variables remain locally regular. Alternative existence is a
construction result, not an assumption.

### C. Public-History Equivalence and Stopping Boundary

The local privacy objective is

$$
\mathcal O_{\mathrm{adv}}[0,t]
=\mathcal O'_{\mathrm{adv}}[0,t],
\qquad 0\leq t<\tau_{\mathrm{priv}}.
$$

Because the public metadata are fixed, this equality reduces to equality of
all transmitted public message histories. Compatible private paths and forced
private weights provide the internal degrees of freedom needed to maintain the
same public trajectory. The construction remains legal only while the required
denominators are nonzero, private weights remain strictly interior, and the
alternative physical, funnel, and input variables remain in the declared
regular domain.

The stopping time $\tau_{\mathrm{priv}}$ is the earliest finite-seed or
regular-domain stopping event. No privacy conclusion is made at or after that
time. The statement is existence-based public-history indistinguishability. It
does not imply cryptographic secrecy, differential privacy, information-
theoretic privacy, universal ambiguity for every protected value, or protection
against unmodeled physical sensing.

## IV. Stability and Performance Analysis

### A. Local Well-Posedness

Let $\mathcal D_{\min}$ be the open domain on which the plant, PPC,
controller, reconstruction, and privacy maps are defined, and let
$\mathcal K_0\Subset\mathcal D_{\min}$ be the selected compact bootstrap
region used to instantiate finite constants. Local regularity of the reduced
independent vector field gives a unique maximal local solution from each
admissible initial condition. All subsequent estimates are restricted to
compact time intervals before the first admissibility exit, while the
trajectory remains in $\mathcal D_{\min}$ and, where compact-dependent bounds
are used, in $\mathcal K_0$.

### B. Component Bounds

On the selected local region, differentiation of the fixed command maps gives
finite command-rate bounds

$$
\|\dot{\bm c}^V\|\leq C_c^V(\mathcal K_0),\qquad
\|\dot{\bm c}^\omega\|\leq C_c^\omega(\mathcal K_0).
$$

The privacy residual consequently admits a finite convolution estimate; no
asymptotic residual-decay premise is used. The voltage, frequency, and privacy
Lyapunov components satisfy local inequalities of the form

$$
\dot{\mathscr V}_{V}
\leq-a_{Vz}\|\bm\zeta^V\|^2-a_{V\chi}\|\bm\chi^V\|^2+d_V,
$$

$$
\dot{\mathscr V}_{\omega}
\leq-a_{\omega z}\|\bm\zeta^\omega\|^2+d_\omega,
$$

$$
\dot{\mathscr V}_{\mathrm{priv}}
\leq-a_z\|\bm z\|^2-a_r\|\bm r\|^2+d_c\|\dot{\bm c}\|^2,
$$

with positive dissipative coefficients under the frozen gain and Young-
parameter conditions. Compact-region command bounds also provide an actuator
and funnel feasibility test on $\mathcal K_0$. That test does not establish
persistence after an exit.

### C. Composite Local Comparison

After closing the graph-dependent terms, the sufficient composite certificate
is

$$
Q_{\mathrm{cl}}=Q_0-H^TW_DH\succ0.
$$

It yields, only on the stated local interval,

$$
\dot{\mathscr V}_{\mathrm{cl}}
\leq-a_{\mathrm{cl}}\mathscr V_{\mathrm{cl}}
+d_R+d_{\mathrm{priv}}(t),
$$

and hence

$$
\mathscr V_{\mathrm{cl}}(t)
\leq e^{-a_{\mathrm{cl}}t}\mathscr V_{\mathrm{cl}}(0)
+\int_0^t e^{-a_{\mathrm{cl}}(t-s)}
[d_R+d_{\mathrm{priv}}(s)]\,ds.
$$

This comparison result supplies local boundedness information before exit. It
does not exclude a later funnel, actuator, physical-domain, or
loss-of-compactness exit. Accordingly, the physical result remains a
local-before-exit theorem and is kept separate from the local privacy theorem.

## V. Simulation Setup

### A. System Configuration

The numerical study uses four DGs (DG1--DG4) connected by distinct electrical
and cyber chain graphs. The engineering bases are $310$ V, $50$ Hz,
$1000$ W, and $500$ var. The voltage and frequency references are
$V_{\mathrm{ref}}=310$ V and $f_{\mathrm{ref}}=50$ Hz. The complete parameter
set is listed in `parameter_table.md`; all values are taken from the frozen
manifest `f27c2278f5bdb77b`.

The simulation horizon is $15$ s. Primary droop control operates alone until
the secondary controller is activated at $5.00$ s. A prescribed settling-time
marker is displayed at $6.30$ s for numerical evaluation. Restoration is
defined by enter-and-remain thresholds of $\pm0.05$ V for voltage and
$\pm0.005$ Hz for frequency. The privacy witness is evaluated only on
$0\leq t\leq0.50$ s.

The Python implementation uses an RK45 solver with relative tolerance
$10^{-9}$, absolute tolerance $10^{-11}$, maximum step $0.005$ s, and output
step $0.005$ s. The frozen Simulink and Python implementations agree over the
physical run with a maximum absolute state difference of $5.8557\times10^{-10}$,
below the predefined $10^{-5}$ implementation threshold.

### B. Evaluation Quantities

F1 and F2 report physical trajectories, reference errors, PPC utilization,
the secondary-activation marker, and the $6.30$ s evaluation marker. PPC
utilization below one indicates that the normalized error remains in the
admissible funnel for the recorded samples. F3 reports active power, normalized
power allocation, and a final nonzero sharing-error metric. F4 contains only
observer-visible public information for the finite privacy window. F5 contains
private/internal differences and is not part of the eavesdropper's observation.

No admissibility exit was detected before $15$ s in the selected physical run.
This is reported as a numerical observation, $t_{\mathrm{exit}}>15$ s for that
run, and not as evidence of forward invariance or global continuation.

## VI. Simulation Results and Analysis

### A. Voltage Restoration (F1)

During the droop-only interval, the four voltage trajectories exhibit small
steady offsets from the $310$ V reference. After secondary activation at
$5.00$ s, all voltage trajectories enter and remain within the declared
$\pm0.05$ V restoration band at $5.19$ s. The maximum voltage deviation over
the full record is $0.3720$ V. The maximum voltage PPC utilization is $0.0150$,
which remains below the unit admissible boundary for all recorded samples.
Thus, F1 demonstrates voltage restoration and PPC-envelope compliance for the
selected pre-exit numerical trajectory. It does not establish an all-time
funnel-invariance or prescribed-time recovery theorem.

### B. Frequency Restoration (F2)

The droop-only stage produces a visible frequency deviation from the $50$ Hz
reference. Following secondary activation, the four frequency trajectories
enter and remain within the declared $\pm0.005$ Hz band at $5.32$ s. The
maximum frequency deviation over the full record is $0.0350$ Hz, and the
maximum frequency PPC utilization is $0.15335$. The response therefore remains
inside the displayed PPC boundary in the selected run and satisfies the
numerical restoration criterion before the $6.30$ s marker. This observation
does not upgrade the local theorem to a deadline-recovery result.

### C. Active Power Sharing Preservation (F3)

F3 compares the four active-power trajectories, their normalized allocations,
and the sharing-error metric. Secondary voltage and frequency regulation does
not destroy the displayed droop-based proportional allocation in this selected
case. The final sharing error is $0.0225442$, which is intentionally nonzero.
The evidence therefore supports the wording "active power sharing
preservation" for this numerical case, not perfect sharing, exact zero-error
allocation, or a general active-power sharing theorem.

### D. Observer-Visible Public-History Indistinguishability (F4)

F4 compares the nominal and non-nominal observer-visible public signals only on
$0\leq t\leq0.50$ s. The two histories overlap, and the maximum archived
public-history difference norm is zero. For the selected witness pair and the
declared passive observation map, the observer therefore cannot distinguish
the two internal realizations from the public record on this finite interval.
No conclusion is made outside the displayed window or for observation channels
that include private memory or raw physical sensing.

### E. Distinct Internal Realizations (F5)

F5 complements the public comparison by showing that the hidden realizations
are not identical. The maximum private $q^V$ difference is
$9.6180\times10^{-9}$, and the maximum private $q^\omega$ difference is
$6.8892\times10^{-12}$. The frequency-side difference is displayed as
$10^{12}\Delta q^\omega$ for readability while the raw values remain in the
archived CSV. The protected-agent command difference reaches
$4.8090\times10^{-9}$, the protected-agent state difference reaches
$1.0000\times10^{-10}$, and the private-weight difference norm reaches
$0.39419$.

The different magnitudes are not compared as measures of privacy strength.
Their role is to establish that different voltage-side, frequency-side,
protected-agent, and private-weight realizations coexist with the identical
observer-visible history shown in F4. Together, F4 and F5 provide numerical
evidence for the selected existence-based witness within the finite evaluation
window.

## Draft Validation Notes

### Completed Sections

- Introduction.
- Proposed methodology and control framework.
- PPC definition and local interpretation.
- Privacy-preserving mechanism.
- Local stability and performance analysis.
- Simulation setup.
- Simulation results and analysis in F1--F5 order.

### Assumptions or Missing Information

- The draft uses the current manuscript's verified citation keys; final
  bibliography placement remains a LaTeX-integration task.
- The canonical manifest uses internal per-unit plant variables and declared
  engineering bases. The draft reports figure-facing voltage and frequency in
  volts and hertz and lists the internal values separately in the parameter
  table.
- The notation `$T_s$` is overloaded across project artifacts: the theory uses
  it for the finite privacy-seed horizon (`privacy.T_s=0.80 s`), whereas F1--F3
  use it for the `6.30 s` settling-time/evaluation marker. These quantities must
  receive distinct manuscript symbols before TeX integration. This draft does
  not silently identify them.
- No baseline-comparison or ablation result is available in the frozen evidence
  package. None is claimed in this draft.
- RT-LAB target execution and hardware validation have not been performed.

### Claim-Evidence Map

| Claim | Evidence | Status |
|---|---|---|
| Local physical regularity and comparison before exit | Frozen local proof chain and current Theorem 1 | Supported within stated domain |
| Local public-history indistinguishability | PO-04/PO-05 closure and current Theorem 2 | Supported before privacy stopping boundary |
| Voltage restoration in selected run | F1 and frozen CSV | Supported numerically |
| Frequency restoration in selected run | F2 and frozen CSV | Supported numerically |
| Sharing relationship preserved in selected run | F3 and final nonzero error | Supported as diagnostic only |
| Identical public history for selected witness | F4 on `0--0.50 s` | Supported numerically |
| Distinct hidden realizations | F5 private-state/weight differences | Supported numerically |
| Global continuation, exact sharing, or all-time privacy | No closed proof/evidence | Not claimed |
