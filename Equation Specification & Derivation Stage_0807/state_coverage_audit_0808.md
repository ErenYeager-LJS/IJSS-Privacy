# State Coverage Audit 0808

> Task ID: task-005a-state-coverage-audit
> Branch: task-005a-state-coverage-audit
> Audit only: no theorem, JECFC, controller, equation, or Lyapunov modification

## 1. Audit question

This audit asks only whether every independent coordinate of `X_min` must appear explicitly in `mathscr V_cl`. It does not prove JECFC or resolve forward invariance.

The frozen independent state is

```text
X_min = col_i(V_i,dot(V_i),omega_i,delta_i,
             p_i^V,q_i^V,p_i^omega,q_i^omega).
```

The frozen composite metric is defined on

```text
xi = col(zeta^V,chi^V,zeta^omega,z^V,z^omega,r^V,r^omega).
```

Therefore `mathscr V_cl` is not intended to be a quadratic form in every coordinate of `X_min`.

## 2. State coverage table

| Independent state | Explicit in `mathscr V_cl`? | Indirect bound in the frozen theory | Bound from physical assumptions | Required for continuation? |
|---|---|---|---|---|
| `V_i` | NO | `V_i-V_ref=rho_i^V tanh(zeta_i^V)` while the PPC map is valid | `V_i` is also a physical coordinate in the declared operating region `Delta` | YES |
| `dot(V_i)` | NO | `dot(V_i)=chi_i^V+alpha_i^V`; `chi_i^V` is explicit and `alpha_i^V` is bounded on a compact admissible domain | Included in the physical state used to define `D_min`/`Delta` | YES |
| `omega_i` | NO | `omega_i-omega_ref=rho_i^omega tanh(zeta_i^omega)` while the PPC map is valid | `omega_i` is a physical coordinate in `Delta` | YES |
| `delta_i` | NO | No Lyapunov term and no frozen algebraic reconstruction from another state | The frozen dictionary declares `Delta` to be a compact admissible operating region, and Assumption 1 places the physical plant on that region | YES |
| `p_i^V` | NO | `p_i^V=c_i^V+r_i^V+0.5z_i^V`; `r^V,z^V` are explicit and PO-06 bounds `c^V` on a compact admissible domain | Not a physical `Delta` coordinate | YES |
| `q_i^V` | NO | `q_i^V=c_i^V+r_i^V-0.5z_i^V` under the same local command bound | Not a physical `Delta` coordinate | YES |
| `p_i^omega` | NO | `p_i^omega=c_i^omega+r_i^omega+0.5z_i^omega` under the PO-06 compact-domain bound | Not a physical `Delta` coordinate | YES |
| `q_i^omega` | NO | `q_i^omega=c_i^omega+r_i^omega-0.5z_i^omega` under the PO-06 compact-domain bound | Not a physical `Delta` coordinate | YES |

Every independent state must remain finite for the PO-16A continuation alternative, but it need not appear as a separate quadratic block in `mathscr V_cl` if it is bounded by an algebraic reconstruction or by the declared operating-domain assumption.

## 3. Delta audit

**Supported outcome: C — `delta` is restricted by the operating-region assumptions.**

The frozen evidence is:

- `Blueprint_0807/variables_0807.md:24`: “`Delta` | Compact admissible operating region | ... | Public assumption | Boundedness domain”.
- `Blueprint_0807/variables_0807.md:159`: “`Delta` | Compact operating region | ... | Public assumption | Boundedness”.
- `Blueprint_0807/theorem dependencies design_0807.md:48`: “the physical plant is locally well posed on a compact admissible operating region”.
- `Equation Specification & Derivation Stage_0807/derivation_stage_3_bootstrap_0808.md:43`: every physical state is required to lie in the interior of the declared operating region `Delta` when defining `D_min`.

`delta_i` is a physical phase coordinate used by ES-3 and the power-flow phase differences in ES-6--ES-7. The frozen Blueprint does not state that `delta_i` must be stabilized by `mathscr V_cl`, nor does it reserve a phase-angle Lyapunov term. Outcome D is therefore unsupported. Outcome B is also unsupported because no frozen state identity reconstructs `delta_i` from `xi`.

## 4. Blueprint consistency

The operating-region assumption does contain a bounded-domain declaration for physical states, including `delta` as a physical coordinate. This explains why `delta` is absent from the retained metric: its admissible range belongs to the physical operating-domain contract rather than the voltage/frequency/privacy stability objective.

This audit does not convert that assumption into a proof of forward invariance. It only establishes that missing explicit `delta` coverage is not, by itself, a Lyapunov-design omission under the frozen Blueprint.

## 5. JECFC blocker classification

**Classification: 3 — only a proof presentation issue, with respect to the state-coverage question audited here.**

The previous statement that JECFC fails merely because `mathscr V_cl` does not explicitly control every coordinate of `X_min` is too strong. The frozen proof architecture intentionally combines:

1. explicit Lyapunov bounds for transformed/controller/privacy coordinates;
2. algebraic reconstruction for tracker coordinates; and
3. the compact operating-domain assumption for physical coordinates such as `delta`.

This classification does **not** prove JECFC. Whether trajectories preserve the declared operating-region and actuator margins is a separate first-exit/continuation question. The present task is not authorized to solve it.

## 6. Audit verdict

- Need Blueprint change: **NO**.
- Need controller redesign: **NO**.
- Need Lyapunov redesign: **NO**, based only on the state-coverage audit.
- Need theorem restriction: **NO for the state-coverage reason**; this audit does not assess whether another proof gap may require claim narrowing.
- Equations changed: **NO**.
- Existing derivations changed: **NO**.
- Proof obligations changed: **NO**.

Recommended next task: separately audit whether the already-declared operating-region and actuator contracts provide the forward margins required by JECFC. This recommendation is only task routing; no solution is proposed here.
