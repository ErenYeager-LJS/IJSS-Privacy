# Illustrative Parameter Rationale

All values belong to manifest `9e81ce3e9621f78a`. They are simulation-design
choices for a dimensionless/per-unit illustrative case and are not measured
hardware parameters.

| Manifest group | Values/units | Selection reason |
|---|---|---|
| DG count | `N=3` | Smallest nontrivial connected network that keeps public/private trajectories readable |
| Electrical graph | path, susceptances `2.0,1.5 p.u.` | Connected lossless illustrative network with distinct line strengths |
| Cyber graph/pins | unit-weight path; DG 1 and 3 pinned | Fixed connected undirected graph satisfying the frozen graph/pinning condition and distinct from the electrical graph |
| References | `V_ref=1 p.u.`, `omega_ref=0 p.u.` deviation | Conventional per-unit nominal voltage and frequency-deviation coordinate |
| Time constants | `tau_P=0.18--0.22 s`, `tau_Q=0.23--0.27 s` | Positive heterogeneous inverter-filter-scale simulation values |
| Droop/voltage coefficients | `k_P=0.08--0.09`, `k_Q=0.10--0.11`, `k_V=0.28--0.32` in compatible p.u. units | Moderate heterogeneous positive values avoiding identical-agent symmetry |
| Loads/setpoints | `P=0.18--0.22 p.u.`, `Q=0.05--0.07 p.u.` | Balanced initial illustrative loading; no hardware provenance claimed |
| Uncertainty | amplitudes at most `0.002 p.u./s` with low-frequency sinusoids | Small deterministic locally bounded terms consistent with Assumption 1 |
| Controller gains | `k1V=3 s^-1`, `k2V=4 s^-1`, `k1omega=3.5 s^-1`, `kcV=kcW=0.1` compatible units | Positive local damping choices; coordination gains remain separated from ES-21a singular values |
| PPC radii | voltage `0.10 -> 0.025 p.u.`, frequency `0.05 -> 0.012 p.u.`, `T=2 s` | Strictly contain the selected initial errors; schedule times are not interpreted as recovery deadlines |
| Privacy rates/weights | `lambda=2 s^-1`, nominal weights `1 s^-1`, legal interval `[0.2,3] s^-1`, `gamma=0.2 p.u.` | Positive interior values with room for the forced W1 weights |
| Physical domain | `V in [0.85,1.15] p.u.`, `|Vdot|<0.5 p.u./s`, `|omega|<0.2 p.u.`, `|delta|<0.5 rad` | Explicit local illustrative operating box used only to detect interpretation exit |
| Compact/input bounds | state infinity norm `<4`, input magnitudes `<10 p.u.` | Loose finite bootstrap/actuator bounds; not claimed as physical hardware limits |
| Initial state | values listed in YAML, all strict-domain and funnel interior | Heterogeneous admissible perturbation about the reference |
| Witness | DG 1 voltage perturbation `1e-4 p.u.` | Small nonzero construction yielding a legal finite local witness without search over alternatives |
| Solver | RK45, `rtol=1e-9`, `atol=1e-11`, max step/output step `0.005 s` | Tight transparent reference integration and aligned cross-platform output grid |
| Comparison | absolute threshold `1e-5`, regularizer `1e-10` | Pre-run implementation-consistency convention; never inserted into dynamics |

The `K_0` and actuator numbers are numerical monitoring bounds only. Remaining
inside them in this example is not described as invariance or hardware
feasibility beyond the displayed local interval.
