# Task-028: Simulation Architecture

## Task-028 Status

**PASS WITH ISSUES**

The architecture is theorem-aligned and manuscript-ready, but simulation
execution is blocked until the user confirms all numerical plant, controller,
domain, witness, and solver data listed below. No simulation was run.

## 1. Repository Audit

### Current resources

- Current manuscript: `Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex`.
- Historical physical-control source: `Standard Tex Usage/IJSS_tex.tex`.
- Historical privacy-reference source: the pre-existing untracked
  `Standard Tex Usage/private.tex`, inspected read-only.
- Source papers: `Origin/IJSS.pdf` and `Origin/Privacy.pdf`.
- Bibliography: no tracked `.bib`; the current manuscript has 12 inline,
  DOI-verified `\bibitem` entries.
- Simulation assets: no tracked MATLAB, Python, Simulink, parameter, numerical
  data, or reusable plot files were found.

The current manuscript defines the plant, controller, independent coordinates,
public/private interface, observation map, local domains, stopping boundaries,
Lyapunov quantities, and two theorem statements symbolically. It does not fix a
complete executable numerical instance.

### Legacy / scope-incompatible material

The historical `IJSS_tex.tex` contains an `Illustrative Simulation` section
beginning at line 718 and HIL material beginning around line 808. It is not an
implementation source for the frozen controller.

| Location | Legacy content | Conflict | Disposition |
|---|---|---|---|
| `IJSS_tex.tex:39` and `:48`--`:51` | Prescribed-time recovery and active-power-sharing title/abstract claims | Exceeds `LOCAL-BEFORE-EXIT` and the two frozen theorem families | `LEGACY / SCOPE-INCOMPATIBLE`; do not reuse |
| `IJSS_tex.tex:718`--`:754` | Old two-stage simulation, numerical gains, loads, and topology | Uses the prior prescribed-time/RBF/adaptive architecture rather than the frozen controller | Do not import values; user confirmation required for every numerical parameter |
| `IJSS_tex.tex:793`--`:808` | Claims that simulations verify prescribed-time recovery and power allocation | Simulation-as-proof and theorem-scope leakage | Do not reuse wording or figures |
| `IJSS_tex.tex:906`--`:1006` | OPAL-RT/HIL platform and recovery/power-sharing cases | No current HIL asset or approved experiment scope; claims stronger results | Isolate as legacy; HIL is outside Task-028/029 unless separately authorized |
| `IJSS_tex.tex:1014` onward | Prescribed-time recovery conclusion | Not supported by the frozen proof chain | Do not migrate |

## 2. Scope Audit

All planned interpretation is subordinate to the frozen theorem scope.

- Physical interval: `0 <= t < tau_num`, where `tau_num` is the first
  numerically detected loss of any domain/compact condition required by the
  plotted local estimate. It cannot exceed the relevant first-exit boundary.
- Privacy interval: `0 <= t < tau_priv`, with `tau_priv` defined exactly by
  Section V. No sample at or after the stopping event supports a privacy claim.
- `K_0` is an estimation/design region, not a numerically inferred invariant
  set. A run that remains inside it is an illustration, not an invariance proof.
- The physical and privacy runs remain independent. Their shared use of the
  frozen closed loop does not create a composite theorem.
- No result may be described as global, asymptotic, all-time, prescribed-time
  recovery, active-power sharing, or universal privacy.

## 3. Theorem-to-Experiment Mapping

| Theorem | Experiment | Figure | Recorded evidence | Allowed claim |
|---|---|---|---|---|
| Theorem 1, local physical result | P1: one admissible local physical run | F1 and F2 | Physical trajectories, PPC coordinates, actuator/funnel/domain margins, residual, and local comparison quantity before `tau_num` | The run illustrates behavior consistent with the local physical estimates on the displayed pre-exit interval |
| Theorem 2, local public-history indistinguishability | W1: one nominal realization and one constructed admissible non-nominal witness | F3 and F4 | Equality of all observer-visible public message histories; a nonzero protected/private difference; stopping margins before `tau_priv` | The selected pair is an existence witness for local public-history indistinguishability under Definition 2 |

F1/F2 must not be used to infer stability or continuation. F3/F4 must not be
used to infer privacy for arbitrary initializations or perturbations.

## 4. Minimal Experiment Set

Only two simulation runs are required. Multiple figures are derived from the
same recorded trajectories rather than from duplicate cases.

### P1: Local physical trajectory and margin run

- **Purpose:** Numerically examine the frozen closed-loop trajectories and
  local comparison quantities while all applicable local conditions hold.
- **Related theorem:** Theorem 1 only.
- **Inputs:** Frozen plant/controller equations, confirmed graph and plant
  parameters, one admissible initial independent state, declared uncertainty
  signals, and confirmed performance/privacy schedules.
- **Initial conditions:** Must satisfy the strict funnels and lie in the
  interior of `D_min` and the selected `K_0`; numerical values are not yet set.
- **Parameters:** All plant, controller, schedule, actuator, graph, and domain
  values listed in Section 6.
- **Recorded variables:** `V_i`, `omega_i`, `delta_i`, `sigma_i^nu`,
  `zeta_i^nu`, `chi_i^V`, `e_i^nu`, `r_i^nu`, `u_i^nu`, actuator/funnel/domain
  margins, `V_cl`, and the right-hand side of the local comparison bound.
- **Valid interval:** `0 <= t < tau_num`; separately record which condition
  defines `tau_num`.
- **Expected figures:** F1 and F2.
- **Allowed claim:** Local numerical behavior is consistent with the displayed
  pre-exit physical estimates for this confirmed case.
- **Forbidden claim:** Global stability, forward invariance, guaranteed
  convergence, prescribed-time recovery, active-power sharing, or post-exit
  validity.

### W1: One public-history indistinguishability witness

- **Purpose:** Instantiate the existence construction using one nominal and
  one admissible non-nominal realization.
- **Related theorem:** Theorem 2 only.
- **Inputs:** The same disclosed graph, references, schedules, timing metadata,
  and public controller parameters; one nominal initialization; one constructed
  nonzero witness perturbation and its compatible private paths/weights.
- **Initial conditions:** `p_i'(0)=p_i(0)`, `q_i'(0)=2S_i'-p_i(0)`, and
  `S_i' != S_i`, with every nominal/alternative strict margin checked.
- **Parameters:** Confirmed finite-seed schedule, weight bounds, private gains,
  protected agent/channel, and witness magnitude.
- **Recorded variables:** Every `p_j^V`, `p_j^omega`, disclosed metadata hash or
  equality check, `O_adv` equality residual, protected `S_i'-S_i`, selected
  `q`, `w`, `r`, reconstructed-command differences, and all privacy stopping
  margins. Raw physical trajectories are internal diagnostics, not observer
  inputs.
- **Valid interval:** `0 <= t < tau_priv` only.
- **Expected figures:** F3 and F4.
- **Allowed claim:** This explicitly selected pair supplies one local existence
  witness under the passive observation model.
- **Forbidden claim:** Privacy for every initialization, arbitrary perturbation,
  all-time privacy, information-theoretic secrecy, differential privacy, or
  robustness to active/extra-sensor adversaries.

## 5. Figure Plan

| Figure | Title and layout | Axes and plotted quantities | Local marker | Risk-controlled caption intent |
|---|---|---|---|---|
| F1 | Local physical trajectories; 2x2 panels | time vs `V_i`; time vs `omega_i`; time vs `u_i^V`; time vs `u_i^omega` | Vertical `tau_num`; shade/omit `t >= tau_num` | “Trajectories for the selected admissible case on the displayed pre-exit interval” |
| F2 | Prescribed-performance and local comparison diagnostics; 2x2 panels | time vs `sigma_i^V` with `+/-1`; time vs `sigma_i^omega` with `+/-1`; time vs selected transformed/residual coordinates; time vs `V_cl` and its comparison envelope | Vertical `tau_num`; label the triggering margin | “Local diagnostic quantities while the applicable `D_min/K_0` conditions hold”; never “funnel invariance” |
| F3 | Public-history overlap for one witness; 2 panels | time vs all nominal/alternative `p_j^V`; time vs all nominal/alternative `p_j^omega`, using matched color and distinct line style | Vertical `tau_priv`; truncate thereafter | “Coincident public messages for the selected nominal/non-nominal existence witness under Definition 2” |
| F4 | Private/internal separation and witness margins; 2x2 panels | time vs selected `q-q'`; time vs selected private-weight/residual differences; time vs `S_i'-S_i` or protected diagnostic; time vs minimum denominator/weight/domain margin | Vertical `tau_priv`; no post-boundary interpretation | “Internal differences and strict margins for the same selected witness”; explicitly state these are not eavesdropper-visible channels |

If a computed trajectory continues after an exit for diagnostic reasons, that
segment must be excluded from manuscript plots or visually greyed and labeled
“outside theorem interpretation.” The preferred publication output truncates at
the first applicable stopping marker.

## 6. Parameter Confirmation Table

### Frozen symbolic items

| Item | Frozen source | Rule |
|---|---|---|
| Plant and power-flow equations | Section II | Implement without structural change |
| Independent state `X` and reconstructed coordinates | Section III | Add no simulation-only state to the theory |
| Electrical/cyber graph roles and public message `m_i` | Section II | Numerical topology may be chosen, but semantics are fixed |
| Controller, PPC maps, residual dynamics, gains as symbolic design objects | Section IV | Numerical values must satisfy the frozen conditions; controller terms cannot change |
| `D_min`, `K_0`, `tau_ex`, and `tau_priv` semantics | Sections III and V | Numerical detection must implement these stopping rules |
| Definition 2 observation map | Section II/III | Observer sees only the declared public history |
| Nominal/alternative initialization relation | Section V | Witness must use the frozen construction |
| Theorem 1/2 claim boundaries | Section VI | Simulation language remains subordinate |

### Recommended implementation choices

| Item | Recommendation | Status |
|---|---|---|
| Run organization | One P1 run and one W1 paired run | Recommended, not a theorem premise |
| Event handling | Solver event functions for every strict domain/margin boundary; record first trigger | Recommended |
| Logging | Log all independent states and reconstruct diagnostics offline from frozen maps | Recommended |
| Public-history equality diagnostic | Plot public pairs and a numerical equality residual with stated solver tolerance | Recommended; tolerance must be reported as numerical, not theoretical equality |
| Plot treatment | Truncate at stopping boundary; matched colors/line styles for witness pair | Recommended |
| Reproducibility | Save confirmed parameter manifest, solver/version, event log, and plotting script | Recommended |

### User confirmation required

| Item | Required decision |
|---|---|
| DG count, ratings, base values, and units | Confirm executable physical scale |
| Electrical topology, line susceptances, and load functions | Confirm values consistent with Section II specialization |
| Cyber topology, weights `a_ij`, and pins `b_i` | Confirm fixed connected undirected graph and regulated-channel pinning |
| `V_ref`, `omega_ref`, droop setpoints, time constants, and droop/voltage-loop coefficients | Confirm numerical plant values |
| Uncertainty scenario and local bounds `bar R_i^nu` | Confirm deterministic signals/bounds; do not introduce unmodeled stochastic assumptions |
| Frozen-controller gains and every Young/composite-certificate parameter | Confirm values satisfying all Section IV inequalities and `Q_cl > 0` |
| PPC radii and schedules `rho_i,0^nu`, `rho_i,infty^nu`, `T_nu` | Confirm strict initial funnel feasibility; `T_nu` is not a recovery guarantee |
| Privacy rates, private-weight intervals/margins, finite-seed schedule, and `T_s` | Confirm Assumption 2 domain data |
| Actuator sets `U_i^nu` and numerical margin test | Confirm physical/input limits |
| Numerical representation of `D_min` and `K_0` | Confirm every event inequality and compact-region boundary/radius |
| Nominal independent initial state | Confirm interior point of `K_0` and `D_min` |
| Protected agent/channel, `S_i'`, perturbation magnitude, private path, and forced weights | Confirm one admissible Theorem 2 witness after margin checks |
| Solver, fixed/adaptive step rule, tolerances, event localization, horizon, and sampling rate | Confirm numerical method |
| Plotting interval and treatment of a detected exit | Confirm truncation at the first applicable boundary |

The numerical values in the historical simulation are not defaults. They come
from a different controller and remain unapproved.

## 7. Baseline Strategy

No algorithm baseline is required for the minimal theorem-aligned study.

- P1 evaluates quantities already named by Theorem 1; another controller would
  change the question and does not help establish the local claim boundary.
- W1 compares the nominal realization with its admissible non-nominal witness.
  This is the theorem's essential comparison, not a baseline algorithm.
- No method has been confirmed to share the same plant, frozen controller,
  Definition 2 observation map, existence-based privacy definition, and
  local-before-exit regime.

**No directly comparable baseline has yet been confirmed.** Any later baseline
candidate requires literature verification and a fairness audit before
inclusion.

## 8. Reviewer Risk Audit

| Risk | Exposure | Mitigation wording/action |
|---|---|---|
| Scope leakage | F1/F2 may look like stability validation | Use “illustrates local behavior for the selected case before the detected exit”; display `tau_num` |
| All-time privacy leakage | F3 overlap may be read beyond the seed/domain boundary | Truncate at `tau_priv`; caption says “on the displayed local witness interval” |
| Universalization | One W1 pair may be generalized to arbitrary perturbations | Use singular “one selected existence witness”; do not use Monte Carlo privacy-success rates |
| Simulation-as-proof | Agreement with bounds may be called verification | Use “numerically examines” or “is consistent with”; Theorems are supported by Sections IV/V, not the plots |
| Observation-model drift | F4 shows information unavailable to the eavesdropper | Label F4 “internal diagnostics, not observer-visible”; compute F3 solely from Definition 2 channels |
| Controller drift | Tuning may add filters, saturation logic, observers, or soft start | Implement frozen equations exactly; any implementation regularization is a blocker requiring architecture review |
| Assumption drift | Noise or load changes may introduce a new stochastic premise | Use only confirmed locally bounded uncertainty consistent with Assumption 1; document its bound |
| Baseline fairness | A literature method may use another information pattern/objective | Omit baseline unless same-model fairness is demonstrated and verified |
| Post-exit interpretation | Solver may continue past an event | Stop integration or exclude/grey post-exit samples with “outside theorem interpretation” |
| Numerical equality overstatement | Floating-point public histories cannot be literally identical | Report solver tolerance and equality residual as numerical diagnostics; retain theorem equality as the analytical statement |
| Composite-theorem leakage | P1 and W1 may be presented as one success case | Keep separate experiment IDs, figures, captions, and claim paragraphs |

## 9. Files Modified

- `Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex`: added only
  the Section VII simulation-architecture skeleton and revised the preceding
  transition from “reserved” to “specifies architecture.”
- `docs/handoff/task-028-simulation-architecture.md`: complete design report.
- `docs/handoff/latest.md`: Task-028 status and next gate.

No simulation code, data, results, figure curves, numerical parameters, or
baseline was created. Sections I--V and the mathematical content of Section VI
were not modified. The controller, equations, observation model, assumptions,
proofs, and theorem statements are unchanged.

## 10. User Decisions Required

Before Task-029, the user must approve:

1. the two-run/four-figure minimal architecture;
2. every numerical item in the User Confirmation Required table;
3. the exact event-function representation of `D_min`, `K_0`, and
   `tau_priv`;
4. one admissible privacy witness and its protected agent/channel;
5. the decision to omit an algorithm baseline;
6. whether post-exit solver samples are stopped entirely or retained only in
   non-manuscript diagnostics.

## Verification

- IEEEtran/pdfLaTeX compilation: PASS
- `git diff --check`: PASS
- Citation/reference closure: PASS
- Section VII contains architecture only: PASS
- Numerical simulation execution: NOT STARTED
- Theorem-scope audit: PASS; `LOCAL-BEFORE-EXIT` unchanged
- Unresolved issue: all executable numerical values require user confirmation

STOP: Awaiting user confirmation before Task-029.
