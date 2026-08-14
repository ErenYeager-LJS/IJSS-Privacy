# Task-029-B Simulation Engineering Revision Report

## Decision

**PASS WITH DISCLOSED PLATFORM LIMITATIONS**

The numerical package now has an executable basic-block Simulink P1 model, a
separated Python data pipeline, four reviewer-oriented figures, four directly
corresponding Origin CSV files, and a renewed 24-state cross-implementation
validation. No theory, parameter, manuscript, or claim boundary changed.

The two retained limitations are precise: W1 is executed in Python only, and
RT-LAB target compilation/hardware execution was not available in this task.

## Simulink Architecture

`Simulink/main.slx` was rebuilt rather than cosmetically wrapping the previous
core. Its top-level ownership boundaries are:

- `DG1`, `DG2`, `DG3`;
- `Electrical_Model`;
- `Communication_Network`;
- `Secondary_Controller`;
- `Privacy_Mechanism`;
- `Observation_and_Logging`;
- `Scopes`.

Each DG contains eight continuous Integrator blocks for `V`, `Vdot`, `omega`,
`delta`, `pV`, `qV`, `pomega`, and `qomega`. It accepts the corresponding
derivatives and exposes all states at named ports. Physical states, public
messages, private coordinates, commands, and control inputs remain explicit
signals rather than opaque workspace state.

The generated architecture audit reports:

- total blocks: `472`;
- continuous Integrators: `24`;
- Subsystems: `17`;
- Scope blocks: `5`;
- S-function blocks: `0`;
- MATLAB Function blocks: `0`;
- forbidden monolithic architecture count: `0`.

The model uses basic Simulink blocks for integration, algebra, PPC scheduling,
power flow, graph maps, privacy dynamics, switching, logging, and scopes. The
former Level-2 S-function was removed. Scope groups cover voltage, frequency,
control inputs, public messages, and explicitly private internal diagnostics.

This is an RT-LAB-oriented signal partition, not an assertion of completed
RT-LAB compatibility. Fixed-step target conversion, I/O mapping, model
partitioning, overruns, and hardware compilation still require the user's
RT-LAB environment.

## Single Parameter Source

Manifest `9e81ce3e9621f78a` from `canonical_parameter.yaml` remains the sole
parameter source. MATLAB parameters are mechanically exported from it. No
parameter value changed during this revision, and no parameter was tuned for
figure appearance.

## Separated Python Pipeline

The revised pipeline is:

```text
run_all.py
  -> raw P1/W1 NPZ
  -> build_processed_data.py
  -> processed diagnostic NPZ
  -> export_origin.py
  -> four Origin CSV files
  -> generate_figures.py
  -> PDF/SVG/PNG
```

Plotting imports no solver runner and reads only retained CSV data. The
compatibility orchestrator calls the four stages in order but does not collapse
their responsibilities.

## Four Figure Groups

### F1: Local Physical Trajectories

Voltage, frequency deviation, voltage tracking error, and frequency tracking
error are shown for three DGs. The dashed marker identifies the numerical exit
boundary; no post-exit claim is made.

### F2: Local Validity and PPC Diagnostics

Normalized voltage/frequency errors, transformed coordinates, minimum active
admissibility margin, and the local comparison quantity are shown only on the
pre-exit sample interval. The figure does not claim funnel invariance or global
continuation.

### F3: Public-History Indistinguishability

Only public `pV` and `pomega` histories are plotted for nominal and alternative
realizations. Solid and dashed curves overlap, and a separate panel reports the
maximum absolute public difference on the finite witness interval.

### F4: Hidden/Private State Difference

Private `q` differences, protected-agent command/state differences, forced
private-weight difference, and the strict construction margin are displayed.
The figure is prominently labeled `Internal diagnostics, not observer-visible`.

All four groups use a restrained colorblind-safe palette, consistent fonts and
units, editable PDF/SVG output, and 300-dpi PNG previews. Two rounds of rendered
PNG inspection removed label overlap and a potentially misleading comparison
overlay. Debug plots are not retained in the manuscript figure folder.

The automated figure-source preflight returned `12 PASS`, `2 WARN`, and
`0 FAIL`. The two reviewed warnings request TIFF and a literal DPI declaration;
they are non-blocking here because the required bundle is explicitly
PDF/SVG/PNG and PNG resolution is read from the canonical `300 dpi` parameter.

## Origin Data

Exactly four wide, Origin-compatible CSV files are retained:

1. `F1_local_physical_trajectories.csv`;
2. `F2_local_validity_ppc_diagnostics.csv`;
3. `F3_public_history_indistinguishability.csv`;
4. `F4_hidden_private_differences.csv`.

Every row contains time and manifest ID. Figure provenance maps each figure to
one CSV and its valid numerical interval. No curve or CSV row was hand-edited.

## Reproducibility Results

- P1: `tau_num = 0.9696157164357533 s`, trigger `Vdot_domain`.
- W1: `tau_priv = 0.2 s`, finite-seed end.
- Public-history residual: `0.0`.
- Protected command difference: `8.520521035959294e-4`.
- Python--Simulink P1 maximum absolute state error: `2.6577916534265e-9`.
- Python--Simulink global RMS state error: `1.0731365959751946e-10`.
- Frozen implementation threshold: `1e-5`.
- Cross-implementation verdict: `PASS`.

The Simulink result covers P1 only. W1 remains Python-only and is not described
as a Simulink or RT-LAB reproduction.

## Claim-Scope Audit

The package continues to use only `LOCAL-BEFORE-EXIT` language. It introduces
no global stability, forward invariance, all-time feasibility, prescribed-time
recovery, power-sharing, asymptotic residual, all-time privacy, cryptographic,
or differential-privacy claim. Numerical agreement is implementation evidence,
not proof.

## Frozen Items

Unchanged:

- Blueprint Version 2.2;
- frozen equations and controller structure;
- state definitions and observation model;
- assumptions and theorem statements;
- proof-obligation status;
- manuscript TeX;
- canonical parameters.

Simulation revision stops here. Discussion, conclusion, and manuscript
integration were not started.
