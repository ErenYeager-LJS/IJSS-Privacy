# Task-029-B Phase 3: Publication Figure Report

## Status

**VALIDATED BASELINE ARCHIVED — F1--F5 GENERATION COMPLETE**

- Pull request: [#33](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/33)
- Baseline archive:
  `IJSS_Simulation/Baselines/task_029_b_pr33_validated_2026-08-14`

Phase 3 polishes the validated numerical outputs only. It does not alter the
system equations, controller structure, theorem assumptions, privacy mechanism,
or manuscript TeX.

## Final Parameter Record

All final figures and CSV files use manifest `f27c2278f5bdb77b` and the single
parameter source `IJSS_Simulation/canonical_parameter.yaml`.

| Group | Final values |
|---|---|
| Network | four DGs; chain electrical and cyber graphs |
| Engineering bases | `310 V`, `50 Hz`, `1000 W`, `500 var` |
| Rated powers | `[500, 600, 650, 700] W` |
| Timing | secondary activation `5.00 s`; prescribed settling-time marker `T_s=6.30 s`; horizon `15 s` |
| Controller gains | `k1_V=3`, `k2_V=30`, `kc_V=0.02`, `k1_omega=2`, `kc_omega=0.02` |
| PPC terminal bounds | `rhoinf_V=0.03`; `rhoinf_omega=0.0004` for all DGs |
| Privacy rates | `lambda_V=lambda_omega=30` for all DGs |
| Numerical thresholds | voltage `0.05 V`; frequency `0.005 Hz` |
| Privacy comparison interval | `0 <= t <= 0.50 s` |

The already validated frequency gain is retained. Its post-activation response
is smooth and enters the declared numerical threshold before `T_s`; no new
parameter tuning was performed for cosmetic purposes.

## Final Numerical Summary

| Requested item | Final result |
|---|---:|
| Secondary activation time | `5.00 s` |
| Prescribed settling time `T_s` | `6.30 s` |
| Observed voltage restoration time | `5.19 s` |
| Observed frequency restoration time | `5.32 s` |
| Maximum voltage error on `0--15 s` | `0.3720 V` |
| Maximum frequency error on `0--15 s` | `0.0350 Hz` |
| Sharing error at `15 s` | `0.0225442` |
| Public-history difference norm on `0--0.50 s` | `0.0` |

At `T_s`, the maximum voltage and frequency errors are `5.3273e-5 V` and
`2.2638e-3 Hz`. No admissibility exit is detected through `15 s`, so the
run-specific statement is `t_exit > 15 s`; this is not an invariance claim.

## Publication Figures

1. `F1_voltage_restoration_final`: voltage trajectories, physical voltage
   errors, PPC utilization, secondary activation, `T_s`, observed restoration
   time, and the detected-exit status.
2. `F2_frequency_restoration_final`: frequency trajectories, physical
   frequency errors, PPC utilization, and the same timing markers.
3. `F3_active_power_sharing_final`: active power, normalized allocation, and
   nonzero sharing error under the title *Active Power Sharing Preservation*.
   It is a selected-case preservation diagnostic, not a perfect-sharing claim.
4. `F4_public_history_indistinguishability_final`: observer-visible nominal and
   non-nominal histories and their difference norm. The title omits attack
   terminology; the finite `0--0.50 s` comparison interval is stated inside
   the figure.
5. `F5_private_state_difference_final`: internal differences in private `q^V`,
   private `q^omega`, protected-agent quantities, and private weights. Because
   the raw `q^omega` difference is approximately `1e-12`, it is displayed as
   `10^12 Delta q^omega`; both the raw and scaled values are retained in the
   matching publication CSV. The undefined-on-figure strict-margin curve is
   excluded from the publication view and remains in the complete Phase 2
   diagnostic data.

Each publication figure is exported in PDF, SVG, and 300-dpi PNG. Each has a
matching `_final.csv` source-data file. Complete Phase 2 raw, processed, and
Origin exports remain unchanged and available for audit.

The accepted F1--F5 files and their numerical dependencies are frozen in the
PR #33 baseline archive with per-file SHA-256 checksums. Subsequent work must
not silently replace this reference set.

## Claim Boundary

The figures illustrate one selected local numerical case. They do not prove
global continuation, forward invariance, theorem-level prescribed-time
recovery, exact active-power sharing, or all-time privacy.
