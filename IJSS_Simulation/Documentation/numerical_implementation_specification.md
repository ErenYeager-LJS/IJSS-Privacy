# Task-029-A Numerical Implementation Specification

## Material Passport

- Artifact ID: `IJSS-PRIVACY-TASK-029-A`
- Artifact type: numerical experiment plan and implementation contract
- Status: `PASS WITH ISSUES`
- Theory boundary: `LOCAL-BEFORE-EXIT`
- Upstream authority: Blueprint Version 2.2, frozen Equation Specification,
  current manuscript Sections II--VII, and Task-028 simulation architecture
- Downstream consumer: Task-029-B Simulation Execution
- Execution state: no simulation, figure, data, result, or parameter tuning performed

This document specifies how Task-029-B may implement the two experiments
approved in Task-028. It does not supply numerical values or authorize
execution. Simulation architecture serves the theorem; numerical output cannot
enlarge either theorem.

## 1. Repository Audit

### 1.1 Existing assets

| Path | Purpose | Reuse decision | Compatibility |
|---|---|---|---|
| `Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex` | Current IEEE manuscript and publication-facing frozen equations | Authoritative read-only implementation source | Compatible with `LOCAL-BEFORE-EXIT` |
| `Equation Specification & Derivation Stage_0807/equation_spec_0807.md` | Frozen ES equation ledger and source-level dependencies | Authoritative read-only equation source | Compatible when the final local claim layer overrides historical stronger result descriptions |
| `Equation Specification & Derivation Stage_0807/equation_traceability_matrix_0807.md` | Equation/proof traceability | Use for implementation audit only | Compatible with the closed local proof chain |
| `docs/handoff/task-028-simulation-architecture.md` | Two-run/four-figure experiment architecture | Direct upstream specification | Compatible |
| `Origin/IJSS.pdf`, `Origin/Privacy.pdf` | Source papers | Context only; not executable specifications | Do not infer numerical defaults |
| `Standard Tex Usage/IJSS_tex.tex` | Historical manuscript | Terminology/reference context only | `LEGACY / DO NOT REUSE` for equations, parameters, results, figures, or claims |
| `Standard Tex Usage/private.tex` | Pre-existing untracked user file | Read-only; excluded from Task-029-A and commits | Not an approved implementation source |

No tracked MATLAB, Simulink, Python, notebook, parameter manifest, numerical
data, or reusable figure source exists. Existing PNG files under `buffer/` are
LaTeX render checks, not simulation results.

### 1.2 Legacy exclusion ledger

The historical `IJSS_tex.tex` simulation and HIL sections use an earlier
prescribed-time/RBF/adaptive architecture and assert recovery and active-power
sharing. Its numerical gains, networks, loads, cases, OPAL-RT material, plots,
and conclusions are classified `LEGACY / DO NOT REUSE`. No historical number is
a default or candidate value unless the user later approves it after a
frozen-equation compatibility audit.

## 2. Paper-Equation-to-Code Mapping

The source hierarchy for every implemented expression is:

1. current manuscript equation and definition;
2. matching frozen ES equation for implementation detail;
3. derivation document only for diagnostic constants, never for a new state or
   controller term.

Conflicts stop implementation and require review; code must not silently choose
one version.

| Paper object and source | Numerical object | Python location | MATLAB/Simulink location |
|---|---|---|---|
| Independent state `X=col_i(V_i,dot V_i,omega_i,delta_i,p_i^V,q_i^V,p_i^omega,q_i^omega)` (`independent_coordinates`; ES-80 clarification) | Flat state vector with deterministic index map and shape `(8N,)` | `src/model/state_layout.py` | bus/vector definition in `parameters/state_layout.m`; signals across plant/privacy subsystems |
| Voltage/frequency plant (`physical_states`--`frequency_input_affine`; ES-1--ES-11) | ODE right-hand-side blocks | `src/model/plant.py` | `DG_Subsystem` |
| Lossless power flow (`active_power_flow`, `reactive_power_flow`; ES-6--ES-7) | Pure algebraic `P,Q` function | `src/model/power_flow.py` | `DG_Subsystem/Power_Flow` |
| Electrical graph `G_e` | Edge list/susceptance matrix | validated configuration | plant parameter structure |
| Cyber graph `G_c`, `A`, `L_c`, pins `b` (`cyber_graph`; ES-13) | Immutable graph matrices with symmetry/connectivity checks | `src/model/graphs.py` | `Communication_Subsystem` |
| Public message `m_i=[p_i^V,p_i^omega]^T` (`public_message`; ES-14) | Two-channel logged payload | `src/privacy/observation.py` | `Measurement_Subsystem/Public_History` |
| Complete observation `O_adv` (`adversary_history`; ES-16) | Public payload plus canonical metadata manifest/hash | `src/privacy/observation.py` | `Measurement_Subsystem/Observation_Map` |
| Physical/distributed errors (ES-17, ES-20--ES-21) | Reconstructed algebraic arrays | `src/controller/errors.py` | `Communication_Subsystem/Distributed_Error` |
| PPC schedule and maps (`ppc_envelope`--`ppc_coordinates`; ES-22--ES-27, ES-30, ES-33--ES-38) | Pure time/state functions returning `rho`, derivatives, `sigma`, `zeta`, `h`, `alpha`, and voltage `dot alpha` | `src/controller/ppc.py` | `Controller_Subsystem/PPC` |
| Frozen commands (`local_voltage_command`, `local_frequency_command`; ES-28, ES-31) | Pure algebraic controller outputs `c^V,c^omega` | `src/controller/secondary.py` | `Controller_Subsystem/Secondary_Control` |
| Wrapper dynamics (`local_z_dynamics`, `local_r_dynamics` as consequences of ES-44--ES-50) | Integrate only `p,q`; reconstruct `z=p-q`, `hat c=(p+q)/2`, `r=hat c-c` | `src/privacy/wrapper.py` | `Privacy_Subsystem` |
| Unique plant interface (`plant_interface`, `local_reconstructed_inputs`; ES-12, ES-47, ES-53) | `u=hat c=c+r` assertion at each logged sample | controller/privacy integration boundary | Controller-to-plant signal boundary |
| Uncertainty `R_i^V,R_i^omega` | User-confirmed deterministic measurable callback and declared bound | `src/model/uncertainty.py` | `DG_Subsystem/Uncertainty_Input` |
| `D_min`, `K_0`, actuator sets, strict margins | Named event functions and audit channels | `src/solver/events.py` | `Measurement_Subsystem/Event_Monitor` |
| Lyapunov components and local comparison (`frozen_lyapunov_components`--`local_comparison_bound`; ES-83--ES-103 local use) | Offline diagnostic values, not integrated states | `src/model/diagnostics.py` | `Measurement_Subsystem/Local_Diagnostics` |
| Alternative initialization (`alternative_initialization`; ES-58) | Paired nominal/alternative initial manifests | `src/privacy/witness.py` | `Privacy_Subsystem/Witness_Initialization` |
| Forced alternative weights (ES-59--ES-61) | User-confirmed admissible private path and evaluated weights with denominator events | `src/privacy/witness.py` | `Privacy_Subsystem/Witness_Construction` |

### 2.1 State rule

Only the `(8N,)` independent vector is integrated. `P`, `Q`, `e_0`, `e`,
`sigma`, `zeta`, `h`, `alpha`, `chi`, `c`, `hat c`, `z`, `r`, `u`, and all
Lyapunov quantities are reconstructed. Solver bookkeeping and event flags may
exist in software, but they are not model states and must never be described as
new theoretical states.

### 2.2 Units and shapes

Task-029-B must attach a unit and array shape to every manifest field before
execution. SI or per-unit representation is user-confirmed and must be applied
consistently to plant parameters, actuator sets, uncertainty bounds, and plot
labels. No automatic conversion is allowed without an explicit base-value
manifest.

## 3. Controller Implementation Specification

### 3.1 Inputs and outputs

For each DG and channel, the controller receives the current physical state,
local powers reconstructed from the electrical network, public neighbor values
`p_j`, public graph/pinning data, references, PPC schedule values, and the
frozen gains. It outputs only the nominal commands `c_i^V,c_i^omega`. The
privacy wrapper receives `c`, its own `p,q`, frozen private weights, tracking
rates, and privacy schedule; it outputs `dot p,dot q` and reconstructs `hat c`.
The plant input is exactly `u=hat c`.

### 3.2 Initialization

- P1: user-confirmed `X(0)` must be strictly inside `D_min` and `K_0`, satisfy
  both funnel inequalities, ES-41 wrapper initialization, private margins, and
  actuator-domain conditions.
- W1 nominal: the same checks apply to its nominal manifest.
- W1 alternative: preserve public `p'(0)=p(0)`, impose
  `q'(0)=2S'-p(0)` with `S' != S`, and check every strict nominal/alternative
  privacy, physical, funnel, input, and denominator margin before integration.
- No initial condition is inferred from historical simulation values.

### 3.3 Time semantics

The frozen equations are continuous-time. Python must use a continuous-time ODE
solver with terminal event localization. The Simulink model must use an
equivalent continuous solver configuration. Any sampled logging interval is an
output setting, not a discretization of the controller. A discrete controller,
zero-order-hold communication layer, delay, filter, observer, rate limiter,
saturation block, anti-windup block, soft start, or regularized denominator is a
theoretical mismatch and is prohibited without prior review.

### 3.4 Runtime identity assertions

Before accepting a run, Task-029-B must verify numerically at logged samples:

- `hat c=(p+q)/2`;
- `r=hat c-c`;
- `u=hat c=c+r` within the reported numerical tolerance;
- public error terms use `p`, not `c` or `hat c`;
- electrical and cyber neighbor structures remain distinct;
- `r` is never folded into `R`;
- no observer-visible log contains a channel excluded by Definition 2.

Failure is an implementation error, not a reason to tune or alter equations.

## 4. Event Function Specification

All strict conditions use signed interior margins: positive means admissible,
zero is the boundary, and decreasing through zero triggers a terminal event.
Each event returns `direction=-1` and `terminal=true`, except the finite seed
clock, whose event value increases to zero and uses `direction=+1`. Exact
numeric guard tolerances require user confirmation and must be reported as
solver settings, not substituted into the mathematical definitions.

### 4.1 Physical stopping time `tau_num`

| Event | Event value | Direction | Rule/source |
|---|---|---:|---|
| Voltage funnel | `1-abs(sigma_i^V)` | `-1` | Stop at first zero; strict PPC domain |
| Frequency funnel | `1-abs(sigma_i^omega)` | `-1` | Stop at first zero; strict PPC domain |
| Positive envelope | `rho_i^nu(t)` | `-1` | Stop at zero; regular PPC map |
| Physical/regular domain | one signed margin per user-confirmed inequality defining `D_min` | boundary-oriented | Stop at first boundary; do not collapse unknown domain conditions into an invented norm ball |
| Compact bootstrap region | user-confirmed signed membership margin for `K_0` | `-1` | Required whenever compact-dependent diagnostics are interpreted; `K_0` is not invariant |
| Actuator set | user-confirmed signed distance of `u_i^nu` to boundary of `U_i^nu` | `-1` | Stop at first input boundary; do not add saturation |
| Privacy denominator/regularity used by physical closed loop | signed margin for every frozen required denominator | boundary-oriented | Stop before a singular expression is evaluated |

`tau_num` is the earliest timestamp among applicable physical events. If
several localize within event tolerance, record all co-triggers. Manuscript data
use only `0 <= t < tau_num`; the boundary sample is retained only in the event
log. The event does not diagnose instability, theorem failure, or failure of
continuation.

### 4.2 Privacy stopping time `tau_priv`

For W1, monitor nominal and alternative realizations wherever Section V
requires common admissibility. The retained boundary is the earliest of:

| Event | Event value | Direction | Stopping rule |
|---|---|---:|---|
| Finite seed end | `t-T_s` | `+1` | Stop at `T_s`; no post-seed interpretation |
| Alternative `D_min` exit | each confirmed alternative-domain signed margin | boundary-oriented | Stop at first zero |
| Nonzero split | `abs(z_i'^nu)` | `-1` | Stop at zero for each denominator-affected pair |
| Schedule denominator | `gamma_priv,i^nu(t)` | `-1` | Stop at zero; also record margin to confirmed lower bound on the seed interval |
| Lower private-weight margin | `w_i'^nu-underline(w)_i^nu` | `-1` | Stop at zero |
| Upper private-weight margin | `bar(w)_i^nu-w_i'^nu` | `-1` | Stop at zero |
| Physical/funnel/input boundary | same signed margins as applicable to the alternative realization | boundary-oriented | Stop at first zero |
| ES-60 denominator | `abs(g_i'^nu z_i'^nu)` | `-1` | Stop at zero before division |
| ES-61 denominator | `abs(z_i'^nu)` | `-1` | Stop at zero before division |
| Other frozen regular-domain singularity | explicit signed margin from confirmed `D_min` definition | boundary-oriented | Stop at first boundary |

`tau_priv` is the earliest retained event, with all co-triggers logged. Public
history equality and private diagnostics use only `0 <= t < tau_priv`. No event
is evidence of privacy loss outside Definition 2, instability, or a failed
theorem.

### 4.3 Event logging contract

Each run writes an event table with: run ID, event ID, agent, channel,
realization, event time, raw signed margin, solver event tolerance, terminal
flag, and source equation/domain clause. The table must distinguish a solver
horizon ending before any event from an actual detected event.

## 5. Parameter Freeze Table

### 5.1 Frozen symbolic parameters and semantics

| Category | Frozen items | Implementation rule |
|---|---|---|
| Plant | state ordering, droop and lossless power-flow equations, signs, unique input path | Exact transcription; no unmodeled conductance or extra dynamics |
| Graph | separate electrical/cyber roles; fixed connected undirected cyber graph and pins | Validate numerically before run |
| Controller | PPC maps, `alpha`, `c`, `e`, gains as symbolic objects | No term, filter, observer, adaptive gain, or limiter added |
| Privacy wrapper | ES-41--ES-50 and nontransparent `hat c=c+r` architecture | Integrate `p,q`; reconstruct wrapper quantities |
| Observation | Definition 2 complete public history | Public logger exposes exactly declared channels/metadata |
| Domains | meanings of `D_min`, `K_0`, actuator sets, `tau_num`, `tau_priv` | User supplies numerical representations; code reports first exit only |
| Witness | ES-58--ES-61 construction and existence-based quantifier | One confirmed nonzero admissible witness; no universalization |
| Analysis | frozen Lyapunov quantities, certificate, local comparison | Offline diagnostics only on the applicable pre-exit interval |

### 5.2 Implementation parameters

These are not theorem parameters but must be frozen in a versioned run manifest:

- language/runtime and package versions;
- ODE solver name and continuous/adaptive settings;
- relative and absolute tolerances by state scale;
- maximum/internal step and output/logging interval;
- event localization and equality-diagnostic tolerances;
- simulation horizon and whether non-manuscript post-event diagnostics are
  disabled (preferred) or separately isolated;
- interpolation method for Python/Simulink comparison;
- floating-point precision, random seed if any deterministic input generation
  uses a PRNG, and machine/platform metadata;
- file formats, precision, delimiter, missing-value policy, and plot style
  version.

### 5.3 User confirmation required

No executable run may start until the user confirms all rows.

| Decision ID | Required decision |
|---|---|
| U01 | DG count, ratings, base values, units, and per-unit conversion if used |
| U02 | Electrical topology, susceptances, and voltage-dependent load functions/parameters |
| U03 | Cyber topology, `a_ij`, `b_i`, and channel pinning |
| U04 | `V_ref`, `omega_ref`, droop setpoints, time constants, droop coefficients, and voltage-loop coefficients |
| U05 | Deterministic uncertainty functions and valid local bounds `bar R_i^nu` |
| U06 | Every frozen-controller gain and every Young/composite-certificate parameter satisfying the Section IV inequalities and `Q_cl>0` |
| U07 | PPC radii/schedules `rho_i,0^nu`, `rho_i,infty^nu`, `T_nu` and strict initial funnel margins |
| U08 | Privacy tracking rates, weight intervals/margins, gains, `gamma_priv`, finite-seed schedule, and `T_s` |
| U09 | Actuator sets `U_i^nu` and their signed-distance implementation |
| U10 | Complete numerical inequality representation of `D_min` and `K_0` |
| U11 | Nominal independent initial state for P1 and W1 |
| U12 | Protected agent/channel, `S_i'`, perturbation, private path, and forced-weight construction for W1 |
| U13 | Solver, tolerances, maximum step, event localization, horizon, and logging interval |
| U14 | Python/Simulink comparison variables, interpolation grid, norm convention, zero-denominator rule, and acceptance threshold |
| U15 | Stop-at-event policy (preferred) or separately retained debug-only post-event data |
| U16 | Final decision to omit an algorithm baseline, as recommended by Task-028 |

Historical numerical values are not approved answers to these decisions.

## 6. Python Architecture

Task-029-B should create the following implementation only after U01--U16 are
resolved:

```text
IJSS_Simulation/
  Python_Simulation/
    README.md
    src/
      model/
        state_layout.py
        plant.py
        power_flow.py
        graphs.py
        uncertainty.py
        diagnostics.py
      controller/
        errors.py
        ppc.py
        secondary.py
      privacy/
        wrapper.py
        witness.py
        observation.py
      solver/
        rhs.py
        events.py
        run_physical.py
        run_privacy_witness.py
      plotting/
        figure_f1.py
        figure_f2.py
        figure_f3.py
        figure_f4.py
        export_origin.py
    config/
      schema.json
      confirmed_parameters.yaml
      run_p1.yaml
      run_w1.yaml
    output/
      figures/
        manuscript/
        origin/
        debug/
      tables/
        origin/
      events/
      manifests/
```

Implementation modules must be side-effect free except run entry points and
export functions. Configuration validation occurs before integration and
rejects missing user decisions, graph incompatibility, non-interior initial
conditions, nonpositive margins, failed gain certificates, or incomplete unit
metadata.

### 6.1 Output/data contract

Every manuscript figure must be generated from a saved real-output table:

| Figure | Required source tables (minimum) |
|---|---|
| F1 | `F1_physical_states.csv`, `F1_inputs.csv`, `P1_events.csv` |
| F2 | `F2_ppc_diagnostics.csv`, `F2_local_comparison.csv`, `P1_events.csv` |
| F3 | `F3_public_history.csv`, `F3_public_equality_residual.csv`, `W1_events.csv` |
| F4 | `F4_private_diagnostics.csv`, `F4_stopping_margins.csv`, `W1_events.csv` |

Tables use one time column and explicit unit-bearing column names or a paired
metadata dictionary. Each row carries run/config hashes. CSV precision must be
sufficient to regenerate the plotted curves. Figures are exported as PNG, PDF,
and SVG; Origin receives the same CSV tables, not hand-transcribed values.

Private/internal F4 tables are stored and labeled as analyst diagnostics. They
must never be merged into the eavesdropper-visible F3 observation table.

## 7. MATLAB/Simulink Architecture

```text
IJSS_Simulation/
  MATLAB/
    scripts/
      prepare_parameters.m
      run_main_model.m
      export_results.m
    functions/
      validate_configuration.m
      evaluate_events.m
      compute_diagnostics.m
    parameters/
      confirmed_parameters.m
  Simulink/
    main.slx
    subsystems/
      DG_Subsystem/
      Controller_Subsystem/
      Communication_Subsystem/
      Privacy_Subsystem/
      Measurement_Subsystem/
      Logging/
  Validation/
    python_vs_simulink/
  Documentation/
```

`main.slx` must be a complete, reproducible model, not a shell around an
untracked MATLAB script. The six named subsystems retain manuscript ownership:

- `DG_Subsystem`: physical states, lossless power flow, uncertainty, and plant
  input equations;
- `Controller_Subsystem`: PPC and frozen secondary commands only;
- `Communication_Subsystem`: fixed cyber graph, public neighbor exchange, and
  distributed errors;
- `Privacy_Subsystem`: `p/q` dynamics, reconstruction, and W1 alternative
  construction, with private signals not exported to the public bus;
- `Measurement_Subsystem`: event margins, local diagnostics, and exact
  Definition 2 observation-map selection;
- `Logging`: versioned tables and metadata without feedback into dynamics.

Signal buses must separate `PublicBus`, `PrivateInternalBus`, `PlantBus`, and
`DiagnosticsBus`. Only `PublicBus` and disclosed metadata feed the observation
logger. Saturation, transport delay, discrete communication, noise, observers,
and implementation filters remain absent.

## 8. Python--Simulink Consistency Plan

### 8.1 Shared contract

Both implementations must consume a generated, hash-identified parameter
manifest derived from the same confirmed source. They must use identical
equations, state ordering, units, electrical/cyber topology, initial conditions,
references, schedules, uncertainty inputs, witness construction, solver family
and settings, event definitions, horizon, and logging grid. Manual duplication
of parameter values is prohibited.

### 8.2 Comparison variables

Compare at minimum:

- all independent state components;
- reconstructed `P,Q,e_0,e,sigma,zeta,chi,c,hat c,z,r,u`;
- all physical and privacy event margins and detected stopping time;
- P1 Lyapunov/local-comparison diagnostics;
- W1 observer-visible public messages and public equality residual;
- W1 selected private diagnostics, kept outside the observation map.

### 8.3 Procedure

1. Validate both manifests and record tool/version metadata.
2. Run P1 and W1 independently in each environment only after authorization.
3. Truncate each comparison at the earliest stopping time reported by either
   implementation.
4. Interpolate only onto the user-confirmed common grid using the confirmed
   method; never extrapolate beyond either run.
5. For each vector `x`, report absolute error and the requested normalized
   diagnostic
   `||x_python-x_simulink||/||x_simulink||`.
6. Apply the user-confirmed zero-denominator convention and norm.
7. Report maximum, RMS, and time-localized error, stopping-time difference,
   event-ID agreement, and manifest hashes.
8. Preserve raw exports and the comparison script so the report is reproducible.

The acceptance threshold is `USER CONFIRMATION REQUIRED`; none is invented in
Task-029-A. Numerical agreement supports implementation consistency only, not a
new theorem or proof.

## 9. Experiment Folder Structure

The complete Task-029-B target is:

```text
IJSS_Simulation/
  README.md
  Python_Simulation/
    README.md
    src/
      model/
      controller/
      privacy/
      solver/
      plotting/
    config/
    output/
      figures/
        manuscript/
        origin/
        debug/
      tables/
        origin/
      events/
      manifests/
  MATLAB/
    scripts/
    functions/
    parameters/
  Simulink/
    main.slx
    subsystems/
      DG_Subsystem/
      Controller_Subsystem/
      Communication_Subsystem/
      Privacy_Subsystem/
      Measurement_Subsystem/
      Logging/
  Validation/
    python_vs_simulink/
  Documentation/
    numerical_implementation_specification.md
```

The root README must state the local theorem boundary, exact reproduction
commands, runtime versions, confirmed manifests, run-to-figure map, event
semantics, data provenance, and the distinction between public and internal
diagnostic exports.

## 10. Task-029-B Preparation Checklist

### Gate 1: user decisions

- [ ] U01--U16 are explicitly confirmed.
- [ ] P1 and W1 remain independent runs.
- [ ] Omission of an algorithm baseline is confirmed or a separate fairness
  audit has approved one.

### Gate 2: transcription and configuration

- [ ] Every implemented expression has a manuscript/ES source mapping.
- [ ] State index, unit, and shape dictionaries are frozen.
- [ ] Plant and cyber topologies pass structural checks.
- [ ] Controller and privacy wrapper pass equation-by-equation inspection.
- [ ] Initial conditions pass all strict interior checks.
- [ ] Gain/Young/composite certificate and actuator-demand checks pass before a
  run; parameters are not tuned from plot appearance.

### Gate 3: events and observation

- [ ] Each `D_min`, `K_0`, actuator, funnel, and denominator condition has a
  named event function.
- [ ] `tau_num` and `tau_priv` use earliest-event semantics.
- [ ] Definition 2 public channels and metadata are represented exactly.
- [ ] Private/internal channels are excluded from the public-history export.

### Gate 4: reproducibility

- [ ] Python architecture and complete Simulink architecture are ready.
- [ ] Solver/version/manifests and run hashes are logged.
- [ ] Figure naming and Origin table contracts are fixed.
- [ ] Each figure reads a persisted real-output table.
- [ ] Python--Simulink comparison procedure and threshold are confirmed.
- [ ] README reproduction instructions are prepared.

Task-029-B is blocked until every applicable checkbox is closed.

## 11. Reviewer Risk Audit

| Risk | Required control | Blocking condition |
|---|---|---|
| Controller drift | Equation-source map and runtime identities | Added filter, observer, limiter, saturation, compensation, or state |
| Theorem-scope leakage | Truncate figures at local boundary; use “illustrates”/“consistent with” | Global, invariant, convergence, deadline-recovery, or sharing language |
| Composite-theorem leakage | Separate P1/W1 configs, outputs, captions, and discussions | One run claimed to jointly prove physical and privacy results |
| Universal privacy leakage | Identify one selected existence witness | Claims over arbitrary initialization/perturbation or all time |
| Observation-model drift | Generate F3 only from Definition 2 public bus and metadata | Raw sensors or private/internal channels exposed to adversary |
| Denominator regularization | Terminal events before division | Epsilon replacement, clipping, or silent continuation |
| Simulation-as-proof | Describe numerical consistency, not theorem verification | Plot treated as proof or as closing an open PO |
| Parameter cherry-picking | Freeze user-approved manifest before execution | Curve-driven tuning without logged, theory-based reapproval |
| Legacy contamination | No historical values/code imported by default | Old adaptive/RBF/HIL or stronger-claim asset reused |
| Post-exit interpretation | Earliest event and strict pre-event export | Boundary/post-boundary sample used to support a claim |
| Floating-point overstatement | Report equality residual and tolerance separately from analytical equality | Numerical closeness described as exact theorem equality |
| Cross-platform mismatch | Shared manifest, state map, solver settings, event audit | Different equations, inputs, grids, or hidden defaults |
| Origin provenance loss | Persist source table and config hash per figure | Manual curve editing or values without real-output table |

## Task-029-A Status

**PASS WITH ISSUES**

The reproducible implementation contract is complete. The blocking issues are
the unresolved user decisions U01--U16; they are numerical-design inputs, not
defects to be filled by invention. No controller, observation model, theorem,
assumption, equation, state, or manuscript section was changed. No executable
simulation asset or result was created.

STOP: Awaiting user confirmation before Task-029-B Simulation Execution.
