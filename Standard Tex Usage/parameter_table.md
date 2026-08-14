# Simulation Parameter Table

> Source: frozen manifest `f27c2278f5bdb77b` in
> `IJSS_Simulation/canonical_parameter.yaml`. No value in this table was tuned
> or inferred during Task-029-D.

## A. System and Timeline

| Parameter | Value | Unit / interpretation |
|---|---:|---|
| Number of DGs, $N$ | `4` | DG1--DG4 |
| Simulation horizon | `15.0` | s |
| Secondary activation | `5.00` | s |
| Settling-time evaluation marker | `6.30` | s; numerical marker, not proved deadline |
| Voltage restoration threshold | `+/-0.05` | V |
| Frequency restoration threshold | `+/-0.005` | Hz |
| Privacy evaluation window | `0--0.50` | s |

## B. Engineering Bases and References

| Parameter | Value | Unit / interpretation |
|---|---:|---|
| Voltage base / displayed reference | `310.0` | V |
| Frequency base / displayed reference | `50.0` | Hz |
| Active-power base | `1000.0` | W |
| Reactive-power base | `500.0` | var |
| Rated active powers | `[500, 600, 650, 700]` | W for DG1--DG4 |
| Internal voltage reference, $V_{\mathrm{ref}}$ | `1.0` | p.u. |
| Internal frequency-deviation reference, $\omega_{\mathrm{ref}}$ | `0.0` | p.u. deviation |

## C. Electrical and Cyber Graphs

Electrical susceptance matrix:

$$
B_e=\begin{bmatrix}
0&2.0&0&0\\
2.0&0&1.8&0\\
0&1.8&0&1.6\\
0&0&1.6&0
\end{bmatrix}.
$$

Cyber adjacency matrix:

$$
A_c=\begin{bmatrix}
0&1&0&0\\
1&0&1&0\\
0&1&0&1\\
0&0&1&0
\end{bmatrix},\qquad
b=\begin{bmatrix}1&0&0&0\end{bmatrix}^{T}.
$$

## D. Plant Parameters

| Parameter | DG1 | DG2 | DG3 | DG4 |
|---|---:|---:|---:|---:|
| $\tau_P$ | `0.50` | `0.50` | `0.50` | `0.50` |
| $\tau_Q$ | `0.40` | `0.40` | `0.40` | `0.40` |
| $k_P$ | `0.0800` | `0.0666666667` | `0.0615384615` | `0.0571428571` |
| $k_Q$ | `0.10` | `0.10` | `0.10` | `0.10` |
| $k_V$ | `0.50` | `0.50` | `0.50` | `0.50` |
| $P_d$ | `0.25` | `0.30` | `0.325` | `0.35` |
| $Q_d$ | `0.08` | `0.09` | `0.10` | `0.11` |
| $P_{\mathrm{load}}$ | `0.25` | `0.30` | `0.325` | `0.35` |
| $Q_{\mathrm{load}}$ | `0.09` | `0.10` | `0.11` | `0.12` |
| Voltage uncertainty amplitude | `0.00020` | `0.00015` | `0.00010` | `0.00012` |
| Frequency uncertainty amplitude | `0.00010` | `0.00012` | `0.00008` | `0.00009` |

Except for the engineering bases declared above, plant values in this table
are the canonical internal per-unit values.

## E. Secondary-Controller Gains

| Parameter | Value |
|---|---:|
| $k_1^V$ | `3.0` |
| $k_2^V$ | `30.0` |
| $k_c^V$ | `0.02` |
| $k_1^\omega$ | `2.0` |
| $k_c^\omega$ | `0.02` |

## F. PPC Parameters

| Parameter | DG1 | DG2 | DG3 | DG4 |
|---|---:|---:|---:|---:|
| $\rho_0^V$ | `0.08` | `0.08` | `0.08` | `0.08` |
| $\rho_\infty^V$ | `0.030` | `0.030` | `0.030` | `0.030` |
| $\rho_0^\omega$ | `0.03` | `0.03` | `0.03` | `0.03` |
| $\rho_\infty^\omega$ | `0.0004` | `0.0004` | `0.0004` | `0.0004` |

| PPC transition parameter | Value | Unit |
|---|---:|---|
| $T_V$ | `1.5` | s |
| $T_\omega$ | `0.5` | s |

## G. Privacy-Mechanism Parameters

| Parameter | Value |
|---|---:|
| $\lambda_V$ | `[30, 30, 30, 30]` |
| $\lambda_\omega$ | `[30, 30, 30, 30]` |
| $w_{12}^V$ | `[1, 1, 1, 1]` |
| $w_{21}^V$ | `[1, 1, 1, 1]` |
| $w_{12}^\omega$ | `[1, 1, 1, 1]` |
| $w_{21}^\omega$ | `[1, 1, 1, 1]` |
| Private-weight lower bound | `0.20` |
| Private-weight upper bound | `3.00` |
| $\gamma_V$ | `0.20` |
| $\gamma_\omega$ | `0.20` |
| Canonical finite privacy-seed parameter (`privacy.T_s`) | `0.80 s` |
| Protected agent index in zero-based implementation | `0` |
| Physical voltage perturbation | `1.0e-10` |
| Private-path decay | `1.0` |

The canonical `privacy.T_s=0.80 s` is not the same quantity as the `6.30 s`
settling-time evaluation marker used in F1--F3. The symbols must be separated
before manuscript LaTeX integration.

## H. Domain and Actuator Limits

| Parameter | Value |
|---|---:|
| Voltage domain | `[0.85, 1.15]` p.u. |
| $\lvert\dot V\rvert$ limit | `2.00` |
| $\lvert\omega\rvert$ limit | `0.50` |
| $\lvert\delta\rvert$ limit | `2.00` |
| $\mathcal K_0$ state absolute limit | `100.0` |
| Voltage actuator absolute limit | `50.0` |
| Frequency actuator absolute limit | `50.0` |
| Minimum denominator threshold | `1.0e-8` |

## I. Initial Conditions

| State / offset | DG1 | DG2 | DG3 | DG4 |
|---|---:|---:|---:|---:|
| $V(0)$ | `1.0012` | `1.0010` | `1.0008` | `1.0011` |
| $\dot V(0)$ | `0` | `0` | `0` | `0` |
| $\omega(0)$ | `0.0007` | `0.0005` | `0.0004` | `0.0006` |
| $\delta(0)$ | `0.010` | `0.005` | `-0.003` | `-0.008` |
| Public voltage offset | `0.010` | `-0.008` | `0.006` | `-0.005` |
| Public frequency offset | `0.008` | `-0.006` | `0.005` | `-0.004` |

## J. Solver and Validation Settings

| Parameter | Value |
|---|---:|
| Physical-run horizon | `15.0 s` |
| Privacy-witness horizon | `0.50 s` |
| Output step | `0.005 s` |
| Relative tolerance | `1.0e-9` |
| Absolute tolerance | `1.0e-11` |
| Maximum step | `0.005 s` |
| Event tolerance | `1.0e-8` |
| Local comparison rate | `0.10` |
| Local comparison budget | `5.0` |
| Numerical regularizer | `1.0e-10` |
| Python--Simulink acceptance threshold | `1.0e-5` |
| Figure resolution | `300 dpi` |
| Configured figure width | `7.0 in` |

## K. Frozen Result Metrics

| Metric | Validated value |
|---|---:|
| Voltage restoration time | `5.19 s` |
| Maximum voltage deviation | `0.3720 V` |
| Maximum voltage PPC utilization | `0.0150` |
| Frequency restoration time | `5.32 s` |
| Maximum frequency deviation | `0.0350 Hz` |
| Maximum frequency PPC utilization | `0.15335` |
| Final sharing error | `0.0225442` |
| Public-history difference norm | `0` on `0--0.50 s` |
| Python--Simulink maximum absolute state difference | `5.8557e-10` |
