# Derivation Stage 2.5 0807

> Blueprint Freeze Version 2.0
> Frozen: 2026-08-07
> Lyapunov Metric Normalization and Consistency Repair

## 1. Audit conclusion

The frozen notation does not state a per-unit convention for `chi_i^V`, `r_i^V`, `z_i^V`, `r_i^omega`, or `z_i^omega`. The notation rules define `zeta` and `sigma` as dimensionless, while `chi_i^V` is a difference of voltage velocities and the privacy states retain the units of their channel commands. Therefore the original unweighted sums in ES-83 and ES-87 are not dimensionally homogeneous in raw physical units.

This is a proof-metric inconsistency, not a plant/controller or privacy-mechanism error. The smallest repair is a constant positive diagonal metric. It introduces no state, gain adaptation, observer, communication variable, or controller signal.

## 2. Lyapunov Metric Convention

Use the reserved proof-matrix family `P_L` in two constant diagonal blocks:

```text
P_L^V   = diag(p_zeta^V I_N, p_chi^V I_N),
P_L^priv= diag(p_c^V I_{2N}, p_c^omega I_{2N}),
```

All entries are constant and strictly positive. `p_zeta^V` supplies the common proof-energy unit for the dimensionless transformed voltage coordinate; `p_chi^V` supplies the reciprocal squared unit of the voltage-rate coordinate; `p_c^V` and `p_c^omega` supply reciprocal squared command units. The entries are selected once and are not controller gains or dynamic states. The frequency candidate ES-85 is already homogeneous because `zeta_i^omega` is dimensionless. The blocks are selected so every component of ES-89 has one common dimensionless proof value.

The repaired candidates are exactly the updated ES-83 and ES-87. No plant or controller equation is rescaled.

## 3. PO-08 revalidation

### Exact derivative and cancellation audit

Using ES-65--ES-66 in the repaired ES-83 gives

```text
dot(mathscr V_V)
 = sum_i[-p_zeta^V k_1^V(zeta_i^V)^2
         -p_chi^V k_2^V(chi_i^V)^2
         +(p_zeta^V-p_chi^V)h_i^V zeta_i^V chi_i^V
         -p_chi^V beta_{e,i}^V chi_i^V e_i^V
         -p_chi^V beta_{r,i}^V chi_i^V r_i^V
         +p_chi^V chi_i^V R_i^V].
```

The original exact cancellation is recovered only if `p_zeta^V=p_chi^V`. A dimensionally meaningful metric generally has unequal unit-bearing entries, so the general proof must retain
`(p_zeta^V-p_chi^V)h_i^V zeta_i^V chi_i^V` and bound it.

Define `Delta_p^V=p_zeta^V-p_chi^V` and use `h_i^V<=h_bar_i^V`. For `eps_V0>0`,

```text
|Delta_p^V h_i^V zeta_i^V chi_i^V|
 <= 0.5 eps_V0(zeta_i^V)^2
    +0.5(Delta_p^V)^2(h_bar_i^V)^2(chi_i^V)^2/eps_V0.
```

Retain the Stage-2 aggregate disturbance

```text
D_i^V=|k_c^V e_i^V|/(tau_Qi k_Vi)
      +|r_i^V|/(tau_Qi k_Vi)+bar(R)_i^V.
```

For `eps_V2>0`,

```text
p_chi^V|chi_i^V|D_i^V
 <= 0.5 eps_V2(chi_i^V)^2
    +(p_chi^V)^2(D_i^V)^2/(2eps_V2).
```

Thus the repaired ES-94 is

```text
dot(mathscr V_V)
 <= -sum_i[p_zeta^V k_1^V-0.5eps_V0](zeta_i^V)^2
    -sum_i[p_chi^V k_2^V-0.5eps_V2
            -0.5(Delta_p^V)^2(h_bar_i^V)^2/eps_V0](chi_i^V)^2
    +sum_i(p_chi^V)^2(D_i^V)^2/(2eps_V2).
```

The repaired ES-95 conditions are

```text
p_zeta^V k_1^V > 0.5eps_V0,
p_chi^V k_2^V > 0.5eps_V2
                   +0.5(Delta_p^V)^2(h_bar_i^V)^2/eps_V0,
for every i.
```

The pointwise derivative chain is therefore closed on the PO-16 domain. The full trajectory theorem still requires PO-16 and later composite graph/gain closure.

**PO-08 status: PROVED SUBJECT TO PO-16.**

## 4. PO-09 revalidation

ES-85 contains only the dimensionless transformed frequency error. The metric repair does not alter ES-85, ES-86, ES-70, or the transformation gain. Consequently the Stage-2 derivation remains valid:

```text
dot(mathscr V_omega)
 <= -sum_i[k_1^omega-0.5eps_omega](zeta_i^omega)^2
    +sum_i(h_bar_i^omega)^2[D_i^omega]^2/(2eps_omega),
```

with `k_1^omega>0.5eps_omega` (or the separated-epsilon condition). No new frequency cross term is created and no frequency equation changes.

**PO-09 status: PROVED SUBJECT TO PO-16.** The dependency is unchanged.

## 5. PO-10 revalidation

For `nu in {V,omega}`, the repaired ES-87 multiplies the original component derivative by the constant positive channel weight `p_c^nu`:

```text
0.5 d/dt[p_c^nu z_i^nu^2+p_c^nu r_i^nu^2]
 = -p_c^nu kappa_i^nu z_i^nu^2
   -p_c^nu lambda_tr,i^nu r_i^nu^2
   +0.5p_c^nu r_i^nu Delta_w,i^nu z_i^nu
   -p_c^nu r_i^nu dot(c_i^nu).
```

Using the Stage-2 Young parameters,

```text
a_z=min_{i,nu}p_c^nu[lambda_tr,i^nu+underline(w)_i^nu
                       -w_delta_bar_i^nu^2/(4eps_r1)],
a_r=min_{i,nu}p_c^nu[lambda_tr,i^nu-eps_r1/4-eps_r2/2],
d_c=max_{i,nu}p_c^nu/(2eps_r2).
```

The common positive factor `p_c^nu` multiplies both the nominal dissipation and the Young penalties. It therefore does not change the private-weight feasibility condition:

```text
w_delta_bar_i^nu^2 < 16lambda_tr,i^nu
                       (lambda_tr,i^nu+underline(w)_i^nu)
```

is still sufficient for a nonempty choice of positive `eps_r1,eps_r2` channel by channel. The metric changes the numerical values of `a_z,a_r,d_c`, but not their sign feasibility logic. No ES-51 decay is used.

**PO-10 status: PROVED SUBJECT TO PO-03.** PO-03 already carries the PO-16 compact-tube dependency; no separate PO-02 dependency is introduced.

## 6. Propagation audit

| Equation/result | Classification | Consequence |
|---|---|---|
| ES-83 | Equation update | Replaced unweighted sum by `P_L^V` diagonal metric. |
| ES-84 | Equation update | Added metric weights and the residual voltage cross term `Delta_p^V h zeta chi`. |
| ES-85 | Unchanged | Frequency transformed error is dimensionless and homogeneous. |
| ES-86 | Unchanged | No frequency metric change. |
| ES-87 | Equation update | Added channel-specific constant privacy metric weights. |
| ES-88 | Equation update | Multiplied each privacy-channel component by its constant metric weight. |
| ES-89 | Proof update | Sum remains valid because all blocks are dimensionless under the metric convention. |
| ES-92 | Equation update | Added `p_chi^V` and its square in the aggregate Young bound. |
| ES-94 | Equation update | Added `eps_V0`, metric-weighted dissipation, and metric-weighted disturbance term. |
| ES-95 | Equation update | Replaced the unweighted voltage gain condition by the weighted condition. |
| ES-98 | Unchanged | Frequency chain is independent of ES-83/ES-87. |
| ES-99--ES-101 | Constant update / proof update | `a_z,a_r,d_c` acquire `p_c^nu`; private-weight feasibility inequality is unchanged. |
| ES-102 | Proof update only | Future `a_cl,d_R,d_priv` must use the repaired weighted constants; ES-102 identifier and form remain. |

No controller, plant, graph, privacy-observation, or theorem-hierarchy equation was altered.

## 7. Normalization policy and freeze impact

The project now uses **constant weighted quadratic proof metrics**, not an unstated per-unit convention. Physical signals keep their physical units; the diagonal entries of `P_L^V` and `P_L^priv` convert each quadratic coordinate into a common dimensionless proof value. There are no scaling states and no time-varying or adaptive weights.

The repair is a genuine proof-metric consistency repair. It is not a notation-only issue because the original sums were not homogeneous under the frozen physical-unit definitions. It is not a controller or privacy mathematical error.

`equation_spec_0807.md` was updated with the metric convention and the affected ES-83/84, ES-87/88, ES-92, ES-94/95, and ES-99--ES-101 forms. `proof_obligations_0807.md` and `equation_traceability_matrix_0807.md` were updated with the corrected dependencies, metric symbols, and statuses. Blueprint Reopen Required: **NO**.

## 8. Stage-2.5 final report

1. ES-83 requires modification: **YES**.
2. ES-87 requires modification: **YES**.
3. Metric chosen: constant positive-definite diagonal blocks `P_L^V` and `P_L^priv` with fixed unit-bearing entries.
4. Affected equations: ES-83, ES-84, ES-87, ES-88, ES-92, ES-94, ES-95, ES-99, ES-100, ES-101; ES-89 and ES-102 receive proof updates only.
5. PO-08 status: **PROVED SUBJECT TO PO-16**.
6. PO-09 status: **PROVED SUBJECT TO PO-16**; unchanged mathematically.
7. PO-10 status: **PROVED SUBJECT TO PO-03**; PO-03 transitively contains PO-16.
8. PO-07 can begin: **NO**; only its preparation ledger is allowed at this stage.
9. Equation Freeze impact: remains conditional until PO-16, metric-weight feasibility, and downstream composite closure are complete.
10. Blueprint Reopen Required: **NO**.
11. Issue type: **genuine proof-metric consistency error**, repaired without changing controller logic.
