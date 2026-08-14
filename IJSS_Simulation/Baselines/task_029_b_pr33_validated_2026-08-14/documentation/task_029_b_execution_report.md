# Task-029-B Simulation Execution - PR #33

## Status

**VALIDATED BASELINE ARCHIVED — F1--F5 GENERATION COMPLETE**

- Pull request: [#33](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/33)
- Validated baseline:
  `IJSS_Simulation/Baselines/task_029_b_pr33_validated_2026-08-14`

## 1. System Configuration

The package now uses four DGs throughout the electrical graph, cyber graph,
controller vectors, privacy states, normalized power calculation, Python
solver, and Simulink implementation. The engineering bases are `310 V`,
`50 Hz`, `1000 W`, and `500 var`.

## 2. Control Parameters and Sequence

Primary droop alone is applied for `0 <= t < 5 s`. At `t_sec=5 s`, an
explicit switch activates the frozen secondary command path. The marked
`6.30 s` point is a predefined evaluation time, not a proved prescribed-time
deadline. The configured simulation horizon is `15 s`.

## 3. Physical Results

Immediately before activation (`4.90 s`), the maximum voltage and frequency
errors are `0.30907 V` and `0.028793 Hz`, respectively. This makes the
droop-only offset visible. After activation, the errors enter and remain in
the declared `0.05 V` and `0.005 Hz` numerical thresholds at `5.19 s` and
`5.32 s`. At the predefined `6.30 s` evaluation time, the corresponding
maximum errors are `5.3273e-5 V` and `2.2638e-3 Hz`. These are selected-case
observations, not a theorem-level deadline-recovery result.

Active powers at the same time are
`[256.36, 303.40, 322.08, 343.16] W`. Normalized values are
`[0.51272, 0.50567, 0.49550, 0.49024]`, with sharing error `0.0224831`.
The error is deliberately displayed rather than described as zero: Fig. 3 is
an active-power sharing preservation diagnostic and does not discharge PO-14.
The post-activation maximum sharing error is `0.0227445`, and the value at
`15 s` is `0.0225442`.

No admissibility exit is detected in P1 through `15 s`; accordingly the report
uses only the run-specific statement `t_exit > 15 s`. The minimum monitored
margin is `0.1488`. Maximum voltage and frequency PPC utilizations are
`0.0150` and `0.15335`, both strictly below the unit admissibility boundary.
The first-exit guard remains active, but its non-triggering in this run is not
an invariance or continuation claim.

## 4. Privacy Result

The independent W1 witness uses the predefined privacy attack window
`0--0.50 s` and stops at its finite-seed boundary. The public-history residual
is `0.0`, while the protected-command difference reaches `4.8090e-9` and the
private-weight difference reaches `0.39419`. Fig. 4 contains only
observer-visible public histories; Fig. 5 is explicitly internal diagnostic
information. No all-time or cryptographic privacy claim is made.

## 5. Simulink Model

`main.slx` was rebuilt and executed in MATLAB/Simulink R2021b. Its visible
top-level ownership includes DG1--DG4, `Electrical_Model`,
`Power_Calculation`, `Primary_Droop_Controller`, `Secondary_Controller`,
`Secondary_Activation_Switch`, `Communication_Network`,
`Privacy_Mechanism`, `Observation_and_Logging`, and `Scopes`.

The architecture audit reports 573 blocks, 32 continuous Integrators,
23 Subsystems, 7 Scopes, 0 S-functions, 0 MATLAB Function blocks, and 0
forbidden monolithic blocks. The activation switch is in the actual command
and applied-input path. MATLAB Function blocks are not used for the system.

The physical scopes are `Voltage_V_Scope`, `Voltage_Error_V_Scope`,
`Frequency_Hz_Scope`, and `Frequency_Error_Hz_Scope`. The first two receive
volts and the latter two receive hertz. Internal normalized states remain
unchanged and are not presented as physical-scope units.

The 32-state Python--Simulink comparison covers the full `0--15 s` interval.
Both implementations finish at `15 s`; no boundary sample is excluded. The
maximum absolute error is `5.8557e-10` and the global RMS error is
`2.9255e-11`; the result passes the predeclared `1e-5` threshold.

This is an RT-LAB-oriented basic-block model, not completed RT-LAB target
validation. Fixed-step conversion, real-time partitioning, I/O mapping,
overrun checks, target compilation, and hardware execution remain user-side
platform work. W1 remains Python-only.

## 6. Generated Files

Five figure groups were generated in PDF/SVG/PNG:

1. `F1_voltage_restoration`;
2. `F2_frequency_restoration`;
3. `F3_active_power_sharing`;
4. `F4_public_history_indistinguishability`;
5. `F5_private_state_difference`.

Their exact Origin CSVs are `Voltage.csv`, `Frequency.csv`,
`ActivePowerSharing.csv`, `PublicHistory.csv`, and `PrivateDifference.csv`.
Plotting reads these CSVs and does not invoke the solver.

Rendered visual inspection passed for all five PNGs. F1 and F2 separate the
engineering-unit errors from a dimensionless PPC-utilization panel, so the
numerical thresholds remain legible while the true unit admissibility boundary
is retained. The figure-source validator returned 12 PASS, 2 reviewed WARN,
and 0 FAIL. The warnings concern TIFF and literal-DPI detection; this task
requires PDF/SVG/PNG, and PNG export uses the canonical 300-dpi configuration.

## 7. Final Numerical Validation Summary

| Item | Final value | Interpretation boundary |
|---|---:|---|
| Secondary activation time | `5.00 s` | Declared numerical switch time |
| Predefined evaluation time | `6.30 s` | Plot/evaluation marker, not a proved deadline |
| Observed voltage threshold-entry time | `5.19 s` | Enter-and-remain test at `0.05 V` |
| Observed frequency threshold-entry time | `5.32 s` | Enter-and-remain test at `0.005 Hz` |
| PPC boundary status | `t_exit > 15 s` | No exit detected in this selected run; no invariance claim |
| Maximum voltage error | `0.3720 V` | Maximum over the complete `0--15 s` record |
| Maximum frequency error | `0.0350 Hz` | Maximum over the complete `0--15 s` record |
| Sharing error at `15 s` | `0.0225442` | Preservation diagnostic, not exact sharing |
| Public-history difference | `0.0` | Only on the predefined `0--0.50 s` W1 attack window |

The maximum errors include initial transients. Immediately before secondary
activation, their values are `0.30907 V` and `0.028793 Hz`; the observed
threshold-entry times above quantify the subsequent restoration.

## 8. Frozen Boundary Audit

No manuscript TeX, Blueprint, frozen equation, controller equation,
observation model, assumption, theorem statement, state definition, or
proof-obligation status was changed. Results remain numerical evidence for a
selected local case and do not establish prescribed-time recovery, exact
power sharing, global continuation, or all-time privacy.
