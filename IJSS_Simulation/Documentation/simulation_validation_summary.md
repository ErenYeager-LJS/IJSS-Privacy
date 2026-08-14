# Task-029-C Simulation Validation Summary

## Status

**PASS — MANUSCRIPT-READY EVIDENCE PACKAGE CONSOLIDATED**

This summary reads only the frozen Task-029-B PR #33 archive. No simulation,
parameter tuning, controller modification, figure regeneration, or manuscript
TeX modification was performed in Task-029-C.

## A. System Configuration

The validated case contains four DGs and uses the frozen parameter manifest
`f27c2278f5bdb77b`. The simulation record ends at `15 s`. Physical plots use
volts and hertz; active powers use watts. The accepted publication figures and
matching CSV files are stored in the validated baseline archive.

## B. Controller Activation Timeline

| Event | Time | Interpretation |
|---|---:|---|
| Simulation start | `0 s` | Primary droop interval begins |
| Secondary control ON | `5.00 s` | Frozen secondary-control path is activated |
| Prescribed settling-time marker `T_s` | `6.30 s` | Numerical evaluation marker |
| Simulation end | `15 s` | No exit detected before this time in the selected run |

The restoration times reported below use the declared enter-and-remain
thresholds. They are numerical observations and not new theorem claims.

## C. Voltage Restoration Analysis

F1 shows a visible droop-only voltage offset before secondary activation and
restoration toward the `310 V` reference after `5.00 s`. Its annotation states
an observed restoration time of `5.19 s`. The maximum voltage deviation over
the complete record is `0.3720 V`; the maximum error is `5.3273e-5 V` at
`T_s` and `5.1781e-5 V` at `15 s`.

The maximum voltage PPC utilization computed from the archived CSV is
`0.0150`, below the unit admissible boundary. F1 states that no exit was
detected and the archived time vector reaches `15 s`.

## D. Frequency Restoration Analysis

F2 shows restoration toward the `50 Hz` reference after secondary activation.
Its annotation states an observed restoration time of `5.32 s`, consistent
with the declared `+/-0.005 Hz` numerical threshold shown in the SVG. The
maximum frequency deviation over the complete record is `0.0350 Hz`; the
maximum error is `2.2638e-3 Hz` at `T_s` and `1.8030e-3 Hz` at `15 s`.

The maximum frequency PPC utilization is `0.15335`, below the unit admissible
boundary. No exit is detected before the archived `15 s` endpoint.

## E. Active Power Sharing Preservation

F3 retains the exact title **Active Power Sharing Preservation** and shows:

1. four active-power trajectories;
2. four normalized power-allocation trajectories; and
3. the intentionally nonzero sharing error.

The final sharing error is `0.0225442`. This supports the selected-case
interpretation that voltage/frequency restoration occurs without destroying
the displayed droop-based proportional allocation. It is not a perfect- or
exact-sharing theorem.

## F. Privacy Validation

F4 contains only observer-visible nominal and non-nominal public histories.
The displayed comparison is explicitly restricted to `0 <= t <= 0.50 s`.
The maximum public-history difference norm in the archived CSV is `0`.

F5 separately demonstrates distinct hidden internal realizations. All four
approved evidence categories are retained:

| Hidden evidence | Maximum archived difference | Display treatment |
|---|---:|---|
| Private `q^V` | `9.6180e-9` | Raw difference |
| Private `q^omega` | `6.8892e-12` | Raw CSV plus `10^12` scaled subplot |
| Protected-agent command | `4.8090e-9` | Raw difference |
| Protected-agent state | `1.0000e-10` | Raw difference |
| Private weight | `0.39419` | Raw difference norm |

The purpose of F5 is existence of different hidden realizations, not comparison
of their absolute magnitudes. F4 and F5 must therefore be interpreted together
and only on the declared finite interval.

## G. Final Quantitative Metrics

| Quantity | Validated value | Evidence source |
|---|---:|---|
| StopTime | `15 s` | P1 time vector and Simulink record |
| Secondary activation | `5.00 s` | F1--F3 marker and frozen configuration |
| Prescribed settling-time marker `T_s` | `6.30 s` | F1--F3 marker and frozen configuration |
| Voltage restoration time | `5.19 s` | F1 annotation |
| Maximum voltage deviation | `0.3720 V` | F1 CSV |
| Maximum voltage PPC utilization | `0.0150` | F1 CSV |
| Frequency restoration time | `5.32 s` | F2 annotation |
| Maximum frequency deviation | `0.0350 Hz` | F2 CSV |
| Maximum frequency PPC utilization | `0.15335` | F2 CSV |
| Final sharing error | `0.0225442` | F3 CSV at `15 s` |
| Public-history difference norm | `0` | F4 CSV on `0--0.50 s` |
| Privacy evaluation window | `0--0.50 s` | F4 annotation and time vector |

## Figure-to-Text Mapping

| Figure | Purpose | Main evidence | Quantitative result |
|---|---|---|---|
| F1 | Voltage restoration performance | Four voltage trajectories, `310 V` reference, voltage errors, PPC utilization, activation/`T_s` markers, and no-exit annotation | Restoration `5.19 s`; maximum deviation `0.3720 V`; maximum PPC utilization `0.0150` |
| F2 | Frequency restoration performance | Four frequency trajectories, `50 Hz` reference, `+/-0.005 Hz` threshold, PPC utilization, activation/`T_s` markers | Restoration `5.32 s`; maximum deviation `0.0350 Hz`; maximum PPC utilization `0.15335` |
| F3 | Power sharing preservation | Active powers, normalized powers, intentionally nonzero sharing error | Final sharing error `0.0225442` |
| F4 | Observer-visible indistinguishability | Overlapping nominal/non-nominal public histories and difference-norm panel on the finite comparison interval | Public-history difference norm `0` on `0--0.50 s` |
| F5 | Hidden internal realization diversity | Private `q^V`, scaled private `q^omega`, protected-agent, and private-weight differences | All four evidence categories nonzero; raw maxima recorded in Section F |

## Validation and Manuscript Boundary

- Baseline SHA-256 manifest verification: `PASS`.
- Figure-to-CSV and figure-label consistency: `PASS`.
- Five-figure visual QA inherited from the frozen baseline: `PASS`.
- Figure validator inherited from the frozen baseline: `PASS`.
- PNG resolution: approximately `300 dpi`.
- `git diff --check`: `PASS`.
- Tracked manuscript TeX changes in Task-029-C: `0`.

Remaining manuscript risk is interpretive rather than numerical: captions and
result text must preserve the selected-case, local-before-exit, non-exact
sharing, and finite privacy-window qualifications.
