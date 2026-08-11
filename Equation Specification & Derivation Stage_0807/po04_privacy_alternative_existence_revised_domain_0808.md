# PO-04 Privacy Alternative Existence on the Revised Domain

> Task ID: `task-013-po04-privacy-alternative-existence-revised-domain`
> Active architecture: Blueprint Version 2.1, Privacy-Domain Revision
> Proof scope: PO-04 only; `LOCAL-BEFORE-EXIT`

## 1. Task-010 contradiction review

Suppress the channel superscript and consider one affected agent/channel pair. Under Blueprint Version 2.0, ES-41 admitted

```text
p_i(0)=q_i(0)=c_i(0),
```

so ES-42 gave `z_i(0)=0`. ES-49 then kept the nominal difference at zero and ES-43 gave `g_i z_i=0` on the nominal local interval.

For a protected perturbation `c_i'(0)=c_i(0)+epsilon`, `epsilon!=0`, equality of the initial public message and ES-58 forced

```text
q_i'(0)=c_i(0)+2epsilon,
z_i'(0)=-2epsilon.
```

If the complete public histories were equal, then `p_i'=p_i`; subtracting the two ES-44/ES-45 public equations forced ES-59. Near the initial time its numerator had the sign of `epsilon`, while `g_i'z_i'` had the opposite sign. Hence ES-60 required `w_{i,21}'<0`, contradicting the positive ES-46 lower bound. This was the Task-010 zero-split contradiction.

## 2. What Version 2.1 repairs

Version 2.1 excludes the nominal zero-split stratum by requiring

```text
|z_j^nu(0)| >= eta_{z,j}^nu > 0
```

for every affected pair. It also places each relevant nominal private weight strictly inside ES-46 on the common local seed interval.

At zero protected perturbation, the primed and nominal quantities coincide. Provided `g_j^nu z_j^nu` is nonzero, ES-60 then returns the nominal `w_{j,21}^nu`, rather than the negative value forced in the Version 2.0 zero-split case. Thus Version 2.1 removes the specific Task-010 sign contradiction and provides room for a continuity argument around an interior nominal weight.

That repair is necessary but not sufficient. A positive perturbation radius requires uniform local control of the ES-60 quotient. Version 2.1 gives a margin for `z_j^nu(0)` and for the nominal weights, but it gives no local positive lower envelope or right-continuity condition for `gamma_priv,j^nu` and therefore none for `g_j^nu z_j^nu`.

## 3. Nominal realization

Let `R` be a nominal realization in the Version 2.1 regular privacy domain on a declared seed interval.

| Class | Nominal objects |
|---|---|
| Public dynamic variables | `p_j^V`, `p_j^omega` for every agent |
| Public design and metadata | `G_c`, `a_jk`, `b_j`, references, funnel schedules, deadlines, public controller parameters, communication timing, and `H_c` |
| Private decomposition variables | `q_j^nu`, `z_j^nu`, `w_{j,12}^nu`, `w_{j,21}^nu`, and local correction-factor values |
| Protected variables | `S_i=[c_i^V(0),c_i^omega(0)]^T` |
| Other hidden variables | `c_j^nu`, `hat(c)_j^nu`, `r_j^nu`, physical sensor/state histories, uncertainty histories, and local controller memory |
| Observed variables | Exactly the public messages and metadata in ES-16; no private state or physical sensor history |

For each affected pair, Version 2.1 guarantees a nonzero nominal initial split and a nominal weight-interior margin. ES-46 supplies positive finite weight bounds. PO-16A supplies a local Caratheodory solution on the open independent-state domain. None of these facts assumes an alternative realization or public-history equality.

The frozen schedule regularity is materially weaker: `gamma_priv,j^nu(t)` is required to be positive on the locally considered times, measurable, and locally essentially bounded; the existing derivation explicitly states that continuity is not assumed. No frozen clause requires

```text
ess inf_{0<t<T} gamma_priv,j^nu(t) > 0
```

for any `T>0`.

## 4. Frozen alternative construction and free perturbation

For a candidate alternative `R'`, select one component of the protected vector and write

```text
c_i'(0)=c_i(0)+epsilon,  epsilon!=0.
```

Keep all public initial messages unchanged and apply ES-58:

```text
p_j'(0)=p_j(0),
q_j'(0)=2c_j'(0)-p_j(0)
```

for every affected pair. For the protected component,

```text
z_i'(0)=z_i(0)-2epsilon.
```

Because `z_i(0)!=0`, one can choose `epsilon` nonzero and sufficiently small so that `z_i'(0)!=0`; the Task-010 opposite-sign obstruction is therefore absent.

The natural network-wide frozen construction is to impose `p_j'=p_j`, retain the nominal interior choice `w_{j,12}'=w_{j,12}`, solve the coupled alternative physical/private local system, and then use ES-59/ES-60 to recover `w_{j,21}'`. At `epsilon=0`, this construction reduces to `R` and both recovered weights equal their nominal interior values.

This construction would support a strict-margin continuity argument only if the ES-60 quotient were uniformly regular on a nontrivial common interval. The next section shows that the frozen Version 2.1 class does not guarantee that property, so no admissible nonzero `epsilon` can be certified for the whole revised domain.

## 5. Admissibility obstruction on the revised domain

### 5.1 An admitted schedule

Let `T_s>0`, let `a_gamma>0` have the appropriate channel-command-rate unit, and let `beta>0`. The frozen measurable schedule class admits, on and after the initial time,

```text
gamma_priv(0)=gamma_0>0,
gamma_priv(t)=a_gamma t,                         0<t<=T_s,
gamma_priv(t)=a_gamma T_s exp[-beta(t-T_s)],     t>T_s.
```

This schedule is positive at every time, measurable, locally essentially bounded, and tends to zero. No frozen equation requires right-continuity or monotonicity at the initial time. The same schedule is public and is used by `R` and `R'`.

Choose nominal private weights as constant values inside the Version 2.1 interior margins and choose a nominal nonzero split satisfying the Version 2.1 separation. ES-49 and local continuity keep the nominal split separated from zero on a sufficiently short interval. Any candidate with sufficiently small `epsilon` also has `z_i'(0)!=0`, and continuity keeps `z_i'` separated from zero on a possibly shorter interval.

For all sufficiently small `t>0`, `gamma_priv(t)` is smaller than both split magnitudes. ES-43 therefore gives

```text
g_i(t)z_i(t)=gamma_priv(t) sign(z_i(t)),
g_i'(t)z_i'(t)=gamma_priv(t) sign(z_i'(t)).
```

Both ES-60 denominators are pointwise nonzero for `t>0`, but their magnitude is `a_gamma t` and has no positive lower bound as `t` approaches zero from the right.

### 5.2 Forced weight violates ES-46

Let

```text
d_i(t)=c_i'(t)-c_i(t).
```

Every admissible local physical/controller trajectory is continuous, and `d_i(0)=epsilon!=0`. Hence there is `T_epsilon>0` such that

```text
|d_i(t)| >= |epsilon|/2,  0<t<T_epsilon.
```

Public-history equality forces ES-59 and ES-60. Using the ES-46 nominal upper bound gives, for sufficiently small positive `t`,

```text
|w_{i,21}'(t)|
 >= lambda_tr,i |epsilon|/[2 gamma_priv(t)] - bar(w)_i
 = lambda_tr,i |epsilon|/[2 a_gamma t] - bar(w)_i.
```

The right-hand side tends to infinity as `t` approaches zero from the right. Consequently, for every `epsilon!=0`, there are positive times arbitrarily close to zero at which

```text
|w_{i,21}'(t)| > bar(w)_i.
```

This violates ES-46 on every nontrivial interval starting at zero. Reducing `|epsilon|` only moves the violation closer to zero; it does not create a positive admissible perturbation radius. The result is independent of the selected private path and occurs before any global continuation question.

### 5.3 Admissibility checklist

| Required property | Result |
|---|---|
| Revised nominal nonzero-split domain | Satisfied |
| Nominal private-weight interior margin | Satisfied |
| Alternative initial split for small nonzero `epsilon` | Can be kept nonzero |
| Pointwise ES-60 division for `t>0` | Defined in the counterexample |
| Alternative ES-46 weight bound | Fails on every interval `[0,T_local)` with `T_local>0` |
| Local boundedness of alternative private weights | Fails |
| Required regularity of an admissible alternative | Fails |
| Global invariance or continuation | Not used |

## 6. Public-history equality audit

Under ES-14--ES-16, identical passive public histories require

```text
p_j'^V(t)=p_j^V(t),
p_j'^omega(t)=p_j^omega(t)
```

for every agent and every time in the common interval, together with identical public metadata.

Subtracting the nominal and alternative public equations in ES-44--ES-45 gives, almost everywhere,

```text
0 = lambda_tr,j(c_j'-c_j)
    -w_{j,21}'g_j'z_j'
    +w_{j,21}g_jz_j.
```

Thus ES-59 is not an optional design choice: it is the exact cancellation required for public equality. For the admitted schedule in Section 5, that cancellation forces the unbounded ES-60 weight. An admissible `R'` therefore cannot generate the same complete public history as `R` on any nontrivial interval beginning at zero.

The observer cannot be declared unable to distinguish two realizations because the second admissible realization does not exist in this admitted case. Public equality cannot be obtained by changing metadata, tracking rates, or public schedules because all are part of ES-16.

## 7. Non-nominality audit

The parameter `epsilon` is a genuine protected private degree of freedom: `epsilon!=0` gives `S_i'!=S_i` and changes the ES-58 private initialization. It is not a variable renaming, coordinate transformation, or relabeling of the nominal realization.

However, genuine non-nominality alone is insufficient. Every nonzero `epsilon` in the admitted schedule case forces an ES-46 violation. Therefore no genuinely non-nominal admissible realization has been constructed, and PO-04 cannot be marked proved.

## 8. PO-05 boundary

| Expression or issue | Classification | Reason |
|---|---|---|
| Nominal `z_j^nu(0)` | **A. Guaranteed by Version 2.1** | The revised domain supplies the declared nonzero initial margin. |
| Candidate `z_i'(0)=z_i(0)-2epsilon` | **B. Candidate-local PO-04 check** | A sufficiently small nonzero perturbation can keep this initial value nonzero without proving later persistence. |
| `g_i'(t)z_i'(t)` in the Section 5 counterexample | **B. Nonzero but not uniformly separated** | It equals `a_gamma t sign(z_i')` for small `t>0`; division is pointwise defined, yet the quotient violates ES-46. |
| General persistence of `z_i'` and `g_i'z_i'`, isolated zeros, or compatible extension | **C. Requires PO-05** | These downstream continuation/extension questions are not proved here. |

The blocker is not a zero denominator silently assigned to PO-05. It is the absence of a frozen local lower-envelope condition needed to turn the nominal weight-interior margin into a positive perturbation radius. PO-05 cannot repair an ES-46 violation that occurs while the denominator remains pointwise nonzero.

## 9. Final PO-04 verdict

**B. PO-04 BLOCKED — ARCHITECTURE REVIEW REQUIRED**

Blueprint Version 2.1 removes the Task-010 zero-split sign contradiction but still admits positive measurable privacy schedules for which `g_i'z_i'` has no local positive lower bound. ES-60 then forces every genuinely non-nominal alternative weight outside ES-46 arbitrarily close to the initial time. No new assumption, state, equation, controller component, or PO-05 result is introduced in this audit.

## 10. Next task recommendation

`task-014-privacy-schedule-regularity-architecture-review`

That review must decide whether the privacy-admissible domain may require a local positive lower envelope or sufficient right-regularity of `gamma_priv` on the common seed interval, or whether the privacy claim/construction must be revised. It must not begin PO-05 while PO-04 remains blocked.
