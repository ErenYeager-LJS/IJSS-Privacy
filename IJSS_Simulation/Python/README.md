# Python Reference Implementation

The integrated state is exactly
`[V,Vdot,omega,delta,pV,qV,pomega,qomega]` for every DG. Powers, controller
errors, PPC coordinates, commands, residuals, inputs, margins, and Lyapunov
diagnostics are reconstructed from that state.

`src/solver/run_physical.py` executes P1.
`src/solver/run_privacy_witness.py` executes one W1 witness.
`src/plotting/generate_outputs.py` regenerates all tables and figures.
`src/solver/validate_simulink.py` compares P1 with Simulink.

The public observation export contains only public messages and declared
metadata. Private/internal tables are analyst diagnostics, not adversary input.
