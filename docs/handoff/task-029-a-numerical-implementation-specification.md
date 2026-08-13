# Task-029-A: Numerical Implementation Specification

## Status

**PASS WITH ISSUES**

Task-029-A converted Task-028's two-run/four-figure architecture into a
reproducible implementation contract. No simulation was executed and no
numerical parameter, data point, figure, result, baseline, or acceptance
threshold was invented.

The authoritative specification is:

`IJSS_Simulation/Documentation/numerical_implementation_specification.md`

## 1. Repository Audit

- No tracked Python, MATLAB, Simulink, parameter, data, or simulation-figure
  source exists.
- The current manuscript and frozen Equation Specification are the only
  equation sources for implementation.
- Historical simulation/HIL content in `Standard Tex Usage/IJSS_tex.tex` is
  `LEGACY / DO NOT REUSE`.
- The pre-existing untracked `Standard Tex Usage/private.tex` remained
  read-only and was not staged.

## 2. Equation-Code Mapping

The specification maps the independent `(8N,)` state, plant, lossless power
flow, electrical/cyber graphs, PPC maps, frozen commands, public/private
wrapper, observation map, stopping domains, Lyapunov diagnostics, and privacy
witness construction to named Python and Simulink modules. Only
`V,dot(V),omega,delta,p^V,q^V,p^omega,q^omega` are integrated states;
all remaining analysis quantities are reconstructed.

## 3. Controller Implementation Specification

The controller I/O, wrapper I/O, initialization checks, continuous-time solver
semantics, and runtime identity assertions are fixed. Filters, observers,
saturation, delays, discrete communication, adaptive gains, soft starts, and
denominator regularization are prohibited because they would change the frozen
system.

## 4. Event Function Specification

- `tau_num`: earliest loss of an applicable funnel, `D_min`, `K_0`, actuator,
  envelope, or frozen regularity condition.
- `tau_priv`: earliest finite-seed end, alternative `D_min` exit, zero private
  split, weight boundary, physical/funnel/input boundary, or required
  denominator/regular-domain singularity.

Signed margins, directions, terminal rules, co-trigger reporting, and event-log
fields are specified. Events mark interpretation boundaries only; they do not
diagnose instability or theorem failure.

## 5. Parameter Freeze Table

The specification separates:

- frozen symbolic semantics;
- numerical implementation settings;
- 16 user-confirmation decisions covering plant, graphs, gains, PPC/privacy
  schedules, domains, initial states, witness, solvers, cross-platform
  tolerance, stopping policy, and baseline decision.

Task-029-B is blocked until all applicable decisions are confirmed.

## 6. Python Architecture

The planned `Python_Simulation` structure contains separate model, controller,
privacy, solver, plotting, configuration, figure, table, event, and manifest
modules. Every F1--F4 publication figure has named real-output CSV source tables
for Origin. No code or output was created in this task.

## 7. MATLAB/Simulink Architecture

The planned complete `main.slx` model separates DG, controller, communication,
privacy, measurement, and logging subsystems. Public, private/internal, plant,
and diagnostic buses remain distinct. MATLAB scripts prepare validated
parameters and export results; they do not replace the complete Simulink model.

## 8. Python-Simulink Consistency Plan

Both environments must use the same hash-identified equations, parameters,
state order, units, topology, initial states, inputs, witness, solver settings,
events, horizon, and logging grid. The comparison covers independent and
reconstructed quantities, stopping times, events, physical diagnostics, public
history, and selected private diagnostics. The numerical acceptance threshold
remains `USER CONFIRMATION REQUIRED`.

## 9. Experiment Folder Structure

The future folder tree is fully specified under `IJSS_Simulation`, including
Python, MATLAB, Simulink, cross-platform validation, outputs, and documentation.
Only the specification document exists after Task-029-A.

## 10. Task-029-B Preparation Checklist

Four gates cover user decisions, transcription/configuration, event/observation
semantics, and reproducibility. Execution is blocked until all applicable
checkboxes close.

## 11. Reviewer Risk Audit

The audit addresses controller and observation drift, theorem-scope and
composite-claim leakage, universal-privacy language, denominator
regularization, simulation-as-proof, parameter cherry-picking, legacy
contamination, post-exit use, floating-point equality, cross-platform mismatch,
and Origin data provenance.

## Scope and Files

Files created or updated:

- `IJSS_Simulation/Documentation/numerical_implementation_specification.md`
- `docs/handoff/task-029-a-numerical-implementation-specification.md`
- `docs/handoff/latest.md`

The manuscript, Blueprint, controller, observation model, equations,
assumptions, states, theorem statements, PO statuses, Sections I--VII, and
Task-028 decisions are unchanged. P1 and W1 remain independent. The theorem
scope remains `LOCAL-BEFORE-EXIT`.

STOP: Awaiting user confirmation before Task-029-B Simulation Execution.
