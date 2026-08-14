# IJSS-Privacy Numerical Reproduction

This package provides an illustrative three-DG numerical instance for the
frozen `LOCAL-BEFORE-EXIT` claim layer. It illustrates local behavior and one
finite privacy witness; it does not establish global continuation, invariance,
prescribed-time recovery, power sharing, or all-time privacy.

## Single Parameter Source

`canonical_parameter.yaml` is authoritative. The Python and MATLAB/Simulink
implementations both consume values derived from this file. Parameter changes
and their non-aesthetic rationale are recorded in `Documentation/`.

## Separated Data Pipeline

From the repository root:

```powershell
$env:PYTHONPATH="$PWD\IJSS_Simulation\Python\src"
python IJSS_Simulation/Python/src/solver/run_all.py
python IJSS_Simulation/Python/src/processing/build_processed_data.py
python IJSS_Simulation/Python/src/export/export_origin.py
python IJSS_Simulation/Python/src/plotting/generate_figures.py
```

The stages are intentionally one-way:

```text
simulation -> raw NPZ -> processed diagnostics -> Origin CSV -> figures
```

The plotting stage reads CSV only and never invokes a solver. Exactly four
Origin-compatible CSV files correspond to exactly four figure groups. Each
figure is exported as editable PDF/SVG plus a 300-dpi PNG preview.

## Simulink Model

Regenerate the shared parameter MAT file, then build and execute the model:

```powershell
$env:PYTHONPATH="$PWD\IJSS_Simulation\Python\src"
python IJSS_Simulation/Python/src/solver/export_matlab_parameters.py
```

```matlab
run('IJSS_Simulation/MATLAB/scripts/build_and_run_simulink.m')
```

`Simulink/main.slx` is a true block diagram. Its top level exposes three DG
subsystems, the electrical model, communication network, secondary controller,
privacy mechanism, observation/logging, and scopes. The implementation uses
basic Integrator, Sum, Gain, Product, trigonometric, switching, routing, Scope,
and logging blocks. It contains no S-function and no MATLAB Function block.

The present Simulink execution reproduces P1. The non-nominal W1 construction
remains a transparent Python execution and is not claimed as dual-environment
reproduction. The block layout is RT-LAB-oriented, but actual RT-LAB target
compilation and hardware execution remain future platform validation.

## Validation

```powershell
python IJSS_Simulation/Python/src/solver/validate_simulink.py
python IJSS_Simulation/Python/src/solver/qa_outputs.py
```

The comparison covers all 24 independent P1 states on the shared pre-exit
grid. It establishes implementation consistency only.
