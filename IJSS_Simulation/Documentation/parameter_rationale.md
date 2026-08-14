# Illustrative Four-DG Parameter Rationale

All values belong to manifest `f27c2278f5bdb77b`. They define one selected
local numerical case and are not measured hardware parameters.

| Group | Values/units | Selection reason |
|---|---|---|
| DG count and graphs | `N=4`; electrical/cyber chain | Restores the original four-DG manuscript configuration and keeps every DG explicit |
| Engineering bases | `310 V`, `50 Hz`, `1000 W`, `500 var` | Matches the historical IJSS case and permits engineering-unit figures |
| Rated active powers | `500, 600, 650, 700 W` | Encodes the declared capacity ratio `1:1.2:1.3:1.4` for the normalized sharing diagnostic |
| Stage timing | droop only on `[0,5) s`; secondary ON at `5 s`; evaluation at `6.30 s` | Makes the two operating stages visible; `6.30 s` is an evaluation marker, not a proved deadline |
| Configured horizon | `15 s` | Requested simulation StopTime; no admissibility exit is detected through this horizon in the selected run |
| Evaluation tolerances | voltage `0.05 V`; frequency `0.005 Hz` | Declared case-specific reporting thresholds, not PPC boundaries or theorem bounds |
| Electrical/droop parameters | values in the canonical YAML | Positive heterogeneous values consistent with the frozen model and four-DG scenario |
| Privacy witness | DG 1 voltage perturbation `1e-10` in the internal normalized coordinate; attack window `0--0.50 s` | Nonzero local alternative on the supported finite interval; no all-time claim |
| Solver | RK45, `rtol=1e-9`, `atol=1e-11`, `0.005 s` max/output step | Transparent reference integration and aligned cross-platform grid |

The migration from three to four DGs, the engineering bases, the capacity
ratings, and the two-stage timing are scenario/architecture corrections. They
were not selected by fitting the plotted curves. Numerical power sharing is
reported as a nonzero diagnostic and is not a PO-14 result.

The final tuning uses `Q_load=[0.09,0.10,0.11,0.12]`, `k2_V=30`,
`kc_V=kc_omega=0.02`, `k1_omega=2`, `rhoinf_V=0.03`, and privacy wrapper
rates of `30`. These are changes to declared numerical values only. Their
purpose is to make the droop-only deviation visible, obtain a smooth switched
response, preserve positive pre-exit margins through `15 s`, and extend the
legal finite privacy witness to `0.50 s`; they do not alter the frozen control
or privacy equations.

The Simulink display layer converts the internal normalized voltage and
frequency-deviation coordinates to `V` and `Hz`. The four physical scopes are
voltage, voltage error, frequency, and frequency error. No per-unit physical
scope or per-unit voltage/frequency CSV column is retained.
