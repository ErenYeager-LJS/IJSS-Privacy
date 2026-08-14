# Task-029-C Read-Only Simulation Baseline Record

## Freeze Status

**READ-ONLY — VALIDATED TASK-029-B PR #33 BASELINE**

- Source task: `Task-029-B Simulation Execution`
- Source PR: [#33](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/33)
- Baseline directory:
  `IJSS_Simulation/Baselines/task_029_b_pr33_validated_2026-08-14`
- Parameter manifest: `f27c2278f5bdb77b`
- Baseline date: `2026-08-14`
- Payload entries protected by SHA-256: `43`
- `SHA256SUMS.csv` SHA-256:
  `1771d393c71e6d7a4c69a083b33499d216cf7968a610aecafc9a4bd2e51e5ef0`

This record and the referenced archive define the manuscript-preparation
baseline. They must not be replaced by regenerated or retuned results without
an explicit new simulation task and a new manifest/archive identity.

## Frozen Configuration

| Configuration item | Frozen value |
|---|---:|
| StopTime | `15 s` |
| Secondary-control activation | `5.00 s` |
| Prescribed settling-time marker `T_s` | `6.30 s` |

## Frozen Metrics

| Result family | Metric | Frozen value |
|---|---|---:|
| Voltage | Restoration time | `5.19 s` |
| Voltage | Maximum deviation | `0.3720 V` |
| Frequency | Restoration time | `5.32 s` |
| Frequency | Maximum deviation | `0.0350 Hz` |
| Power sharing | Final sharing error | `0.0225442` |
| Privacy | Public-history difference norm | `0` |
| Privacy | Evaluation window | `0--0.50 s` |

F5 retains all four approved evidence categories: private `q^V` difference,
private `q^omega` difference, protected-agent difference, and private-weight
difference. The raw frequency-side difference is retained in the CSV and is
displayed as `10^12 Delta q^omega` for readability.

## Boundary

The baseline records one selected local numerical case. `t_exit > 15 s` means
only that no exit was detected in this run. The baseline does not establish
global continuation, forward invariance, exact power sharing, theorem-level
prescribed-time recovery, or all-time privacy.
