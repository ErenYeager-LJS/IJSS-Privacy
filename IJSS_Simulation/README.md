# IJSS-Privacy Numerical Reproduction

This directory contains the illustrative numerical instance for the frozen
`LOCAL-BEFORE-EXIT` manuscript. Simulation illustrates the two local theorem
families; it does not prove global continuation, invariance, convergence,
prescribed-time recovery, power sharing, or universal privacy.

## Runs

- `P1_RUN_001`: local physical trajectory, interpreted only before the detected
  `Vdot_domain` exit at `tau_num = 0.9696157164357533 s`.
- `W1_RUN_001`: one nominal/non-nominal existence witness, interpreted only on
  `0 <= t < tau_priv = 0.2 s`.
- `SIMULINK_P1_RUN_001`: Simulink reproduction of P1.

All runs use manifest `9e81ce3e9621f78a`, derived from
`canonical_parameter.yaml`. Values are simulation parameters for an
illustrative per-unit case, not measured hardware parameters.

## Requirements

- Python 3.12 with NumPy, SciPy, Matplotlib, and PyYAML.
- MATLAB/Simulink R2021b or compatible for `main.slx`.

## Python

From the repository root in PowerShell:

```powershell
$env:PYTHONPATH="$PWD\IJSS_Simulation\Python\src"
python IJSS_Simulation/Python/src/plotting/generate_outputs.py
```

This regenerates raw P1/W1 solver output, Origin CSV tables, run manifests,
and F1--F4 in PDF/SVG/PNG. Figure data flow is:

```text
raw NPZ -> reconstructed diagnostics -> Origin CSV -> plotting code -> figure
```

F3 contains only public `p^V,p^omega` histories. F4 contains internal analyst
diagnostics and is explicitly not observer-visible.

## MATLAB/Simulink

Regenerate the shared MATLAB parameter file:

```powershell
python IJSS_Simulation/Python/src/solver/export_matlab_parameters.py
```

Build and run the model:

```matlab
run('IJSS_Simulation/MATLAB/scripts/build_and_run_simulink.m')
```

The script creates and executes `Simulink/main.slx`. The continuous frozen RHS
is in `MATLAB/functions/sfun_ijss_closed_loop.m`; named model subsystems expose
the paper-equation ownership groups. The current Simulink run reproduces P1.
W1 remains a Python-only existence-witness execution in this task.

## Cross-Platform Validation

```powershell
python IJSS_Simulation/Python/src/solver/validate_simulink.py
```

Results are in `Validation/python_vs_simulink/`. Comparison is restricted to
the shared pre-exit grid and establishes implementation consistency only.

## Provenance

- Canonical source: `canonical_parameter.yaml`
- Run manifests: `Python/output/manifests/`
- Raw output: `Python/output/raw/`
- Origin tables: `Python/output/tables/origin/`
- Publication figures: `Python/output/figures/manuscript/`
- Figure provenance: `Python/output/manifests/figure_provenance.json`
- Parameter changes: `Documentation/parameter_change_log.md`

No post-exit sample is used as manuscript evidence. The stopping marker is an
interpretation boundary, not a diagnosis of instability or theorem failure.
