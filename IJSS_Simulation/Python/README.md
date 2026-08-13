# Python Reference Implementation

The integrated state is
`[V,Vdot,omega,delta,pV,qV,pomega,qomega]` for each DG. Power, graph errors,
PPC coordinates, commands, residuals, inputs, margins, and local comparison
diagnostics are reconstructed from these independent coordinates.

The package separates responsibilities:

- `src/model/`: plant, graph, power-flow, state, and diagnostic definitions.
- `src/controller/`: prescribed-performance coordinates and frozen controller.
- `src/privacy/`: privacy wrapper and finite witness construction.
- `src/solver/`: P1/W1 execution and Python--Simulink validation.
- `src/processing/`: raw-output reconstruction into figure data.
- `src/export/`: Origin-compatible CSV export only.
- `src/plotting/`: CSV-driven figure generation only.

`generate_outputs.py` is a compatibility orchestrator for the four distinct
stages; plotting modules themselves never call either solver.

F3 contains observer-visible public messages only. F4 is explicitly an
internal diagnostic and is not part of the passive adversary observation.
