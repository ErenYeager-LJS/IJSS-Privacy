# Task-029-B Simulation Execution Report

## Task-029-B Status

**PASS WITH ISSUES**

Python P1/W1 execution, real-data exports, four figure groups, an executable
Simulink P1 model, and Python--Simulink consistency validation are complete.
The remaining issue is that the alternative W1 witness has not been implemented
as a separate Simulink mode; it is reproduced in the transparent Python
reference implementation only. The Simulink equation core is concentrated in
a Level-2 MATLAB S-function, while named subsystems document ownership groups.

## 1. Simulation Parameter Setup

The single source of truth is `canonical_parameter.yaml`, manifest
`9e81ce3e9621f78a`. It defines a three-DG, lossless, per-unit illustrative
numerical instance. Every value is a simulation parameter, not measured
hardware data. The parameter choices and units/reasons are recorded in the
manifest.

An initial choice `k_c^V=0.35`, `k_c^omega=0.30` was superseded after the
ES-41-consistent initialization exposed proximity to the ES-21a singular
surface. The accepted values are both `0.10`. The complete non-aesthetic reason
and invalidated manifest IDs are in `parameter_change_log.md`.

## 2. Python Implementation

The Python reference integrates only the 24 independent coordinates for three
DGs. Plant, lossless power flow, graph errors, PPC maps, frozen commands,
privacy wrapper, local events, diagnostics, witness construction, raw-data
retention, Origin export, and plotting are implemented as separate modules.

Identity audit:

- maximum `hat(c)-(p+q)/2`, `r-hat(c)+c`, and `u-hat(c)` residual:
  `4.440892098500626e-16`;
- electrical and cyber graph objects remain distinct;
- public logger fields are `time,pV,pomega,declared_metadata`;
- private leakage flag: `false`.

## 3. P1 Simulation Result

- Run ID: `P1_RUN_001`
- Manifest: `9e81ce3e9621f78a`
- Solver: SciPy RK45, `rtol=1e-9`, `atol=1e-11`, `max_step=0.005 s`
- Stopping event: `Vdot_domain`
- `tau_num = 0.9696157164357533 s`
- Event margin at localization: approximately `-3.33e-16`

The selected numerical trajectory illustrates local physical behavior only on
the displayed pre-exit interval. The exit is not interpreted as instability.

## 4. W1 Privacy Witness Result

- Run ID: `W1_RUN_001`
- Manifest: `9e81ce3e9621f78a`
- Protected agent: DG 1
- Construction: `V_1(0)` alternative perturbation `1e-4 p.u.`, public initial
  states held equal, ES-41 alternative `q(0)`, explicit private `q'` dynamics,
  and ES-60 forced public-matching weights
- Nonzero protected voltage-command difference:
  `8.520521035959294e-4 p.u.`
- Public-history residual: `0.0`
- Stopping event: finite declared witness interval end
- `tau_priv = 0.2 s`

All checked weight, split/denominator, and funnel margins remain positive on
the reported samples. This is one numerical existence witness, not arbitrary or
all-time privacy.

## 5. Generated Figures

F1--F4 are exported in PDF, SVG, and 300-dpi PNG under both manuscript and
Origin figure folders. Visual QA found and repaired initial axis-label overlap
by changing plotting layout only. Final QA is PASS.

- F1: local physical trajectories and inputs with `tau_num` marker.
- F2: normalized/transformed errors and local diagnostic quantity.
- F3: Definition 2 public-history overlap only.
- F4: explicitly labeled internal diagnostics, not observer-visible.

## 6. Origin CSV Data

Thirteen direct simulation exports are under `Python/output/tables/origin`,
including separate voltage/frequency/input/PPC tables, public-history and
equality-residual tables, private-difference/margin tables, and P1/W1 event
tables. Every row includes time and manifest ID. No table or curve was manually
edited.

## 7. MATLAB/Simulink Model

`Simulink/main.slx` was generated and executed with MATLAB/Simulink R2021b
Update 7. It contains the continuous frozen closed-loop S-function, named
DG/Plant, Controller, Communication, Privacy, Measurement/Event, and Logging
ownership subsystems, explicit public/private/plant/diagnostic sink names, and
state logging. Actual Simulink CSV and MAT outputs are retained.

Issue: the current executable model reproduces P1. The W1 alternative
construction is not exposed as a second Simulink run mode.

## 8. Python--Simulink Comparison

- Compared: `P1_RUN_001` and `SIMULINK_P1_RUN_001`
- Variables: all 24 independent states
- Common grid end: `0.965 s`
- Global maximum absolute error: `2.657815190154622e-9`
- Global RMS error: `1.0731489438639445e-10`
- Maximum normalized diagnostic: `1.2437037896032482e-8`
- Simulink configured stop minus last common Python output sample:
  `0.00462 s`
- Pre-frozen absolute threshold: `1e-5`
- Verdict: PASS

The initial comparison failed because adaptive Simulink internal samples were
linearly interpolated against Python's fixed output grid. Specified Simulink
output times and full-precision MAT comparison removed that comparison artifact
without changing equations, parameters, or initial conditions.

## 9. Reviewer Risk Audit

- No global stability, invariance, prescribed-time recovery, sharing, all-time
  privacy, or universal privacy claim is made.
- P1 figures end at the first local boundary; W1 ends at its finite witness
  boundary.
- F3 contains only observer-visible public variables.
- F4 is labeled analyst-only internal diagnostics.
- Simulation is described as illustration/consistency evidence, not proof.
- Historical adaptive/RBF/HIL parameters were not reused.
- Every plot is regenerated from retained real numerical output.

## 10. Files Created

Created/updated assets are confined to `IJSS_Simulation/` and handoff docs.
The manuscript, Blueprint, controller equations, observation model, theorem
scope, assumptions, states, and PO statuses were not modified. Python cache and
temporary MATLAB artifacts are excluded from the deliverable.

## Manuscript Integration Readiness

Ready with the stated issue. F1--F4 and their Origin tables support a restrained
Section VII numerical-results continuation using “illustrates,” “is consistent
with,” “selected admissible case,” “pre-exit interval,” and “one existence
witness.” Task-030 must not upgrade those phrases into stronger claims.

## Recommended Next Task

Task-030: manuscript integration of the reviewed numerical results and captions,
with the Simulink W1 limitation disclosed or separately closed before claiming
dual-environment reproduction of the privacy witness.

STOP: Awaiting Task-030 review gate.
