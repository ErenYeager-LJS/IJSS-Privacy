# Task-029-B Simulation Execution - PR #33

## Status

**VALIDATED BASELINE ARCHIVED — F1--F5 GENERATION COMPLETE**

- PR: [#33](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/33)
- Archive:
  `IJSS_Simulation/Baselines/task_029_b_pr33_validated_2026-08-14`

- Four DGs are used across Python and Simulink.
- Droop-only operation precedes the explicit secondary activation at `5 s`.
- Five manuscript figures and the five exact Origin CSVs were regenerated.
- `main.slx` is an executable basic-block R2021b model with 32 Integrators,
  7 Scopes, and no S-function or MATLAB Function block.
- StopTime is configured as `15 s`; V/Hz voltage/frequency scopes and separate
  V/Hz error scopes are present.
- No first exit is detected through `15 s` in the selected run; the correct
  numerical statement is `t_exit > 15 s`, without an invariance claim.
- The 32-state Python--Simulink comparison passes: maximum absolute error
  `5.8557e-10` on `0--15 s` against the `1e-5` threshold.
- Public-history residual is zero on the predefined finite W1 attack window
  `0--0.50 s`.

Voltage/frequency tolerance entry and active-power sharing preservation are
observed numerical behavior in the selected case. They are not prescribed-time
recovery or active-power-sharing theorem claims. The theory remains
`LOCAL-BEFORE-EXIT`.

RT-LAB compilation/hardware execution and Simulink W1 reproduction were not
performed. Manuscript TeX and all frozen theory artifacts remain unchanged.

Full report: [task_029_b_execution_report.md](../../IJSS_Simulation/Documentation/task_029_b_execution_report.md)

STOP: Task-029-B revision complete. No manuscript or experiment extension was
started.

## Phase 3 Publication Refinement

The validated parameter tuple remains unchanged. Five final publication figure
groups and five matching publication CSV files were added. F1/F2 use
"Prescribed settling time" and "Observed restoration time"; F3 is explicitly
an active-power sharing preservation diagnostic; F4 states its finite
comparison interval without attack-window title language; F5 retains both
voltage- and frequency-side private differences, with the latter transparently
scaled by `10^12` for readability. No manuscript TeX or theory artifact changed.

Detailed report:
[task_029_b_phase_3_publication_report.md](../../IJSS_Simulation/Documentation/task_029_b_phase_3_publication_report.md)

The archive contains the accepted F1--F5 files, matching CSVs, raw/processed
results, manifests, parameter snapshot, Simulink outputs, validation results,
and SHA-256 checksums. F5 retains `q^V`, scaled `q^omega`, protected-agent,
and private-weight differences. No new simulation was run for this archive.
