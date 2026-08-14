# Task-029-B PR #33 Validated Baseline

## Status

**VALIDATED BASELINE — F1--F5 GENERATION COMPLETE**

- Task: `Task-029-B Simulation Execution`
- Pull request: [#33](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/33)
- Archive date: `2026-08-14`
- Parameter manifest: `f27c2278f5bdb77b`
- Source branch: `task-029-b-simulation-execution`

This directory is a read-only reference snapshot of the accepted numerical
baseline. Phase 3 did not rerun the simulation, change parameters, retune the
controller, or modify manuscript TeX.

## Validated Metrics

| Item | Baseline value |
|---|---:|
| Simulink StopTime | `15 s` |
| Secondary-control activation | `5.00 s` |
| Prescribed settling-time marker `T_s` | `6.30 s` |
| Voltage restoration time | `5.19 s` |
| Maximum voltage error | `0.3720 V` |
| Frequency restoration time | `5.32 s` |
| Maximum frequency error | `0.0350 Hz` |
| Final sharing error | `0.0225442` |
| Public-history difference norm | `0` |
| Privacy evaluation window | `0--0.50 s` |

F5 preserves voltage-side private `q^V`, scaled frequency-side private
`q^omega`, protected-agent, and private-weight differences. The plotted
frequency-side difference is transparently displayed as `10^12 Delta
q^omega`; raw and scaled columns are both archived.

## Validation Record

- Five-figure visual QA: `PASS`.
- Figure-source validator: `PASS` (`12 PASS`, `0 FAIL`; two reviewed export
  warnings because TIFF was not requested and DPI is supplied through the
  canonical parameter source).
- PNG resolution: approximately `300 dpi`.
- `git diff --check`: `PASS` at baseline freeze.
- Tracked manuscript TeX changes: `0`.
- No admissibility exit detected through `15 s`; this is recorded only as the
  selected-run observation `t_exit > 15 s`.

## Contents

- `configuration/`: canonical YAML and MATLAB parameter snapshots.
- `source_snapshot/`: final CSV exporter and figure generator.
- `python/raw/`, `python/processed/`, `python/manifests/`: P1/W1 numerical
  results and provenance.
- `python/figures/`: accepted F1--F5 in PDF, SVG, and PNG.
- `python/tables/`: five matching publication CSV files.
- `simulink/`: `main.slx`, architecture audit, and final MATLAB/CSV outputs.
- `validation/`: full Python--Simulink comparison results.
- `documentation/`: final execution and Phase 3 publication reports.
- `SHA256SUMS.csv`: SHA-256 and byte length for every archived payload file.

This baseline supports one selected local numerical case. It does not create a
global-continuation, forward-invariance, exact-sharing, theorem-level
prescribed-time-recovery, or all-time-privacy claim.
