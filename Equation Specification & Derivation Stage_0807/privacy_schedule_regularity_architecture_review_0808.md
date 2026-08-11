# Privacy Schedule Regularity Architecture Review

> Task ID: `task-014-privacy-schedule-regularity-architecture-review`
> Selected outcome: **B. MINIMAL PRIVACY-DOMAIN REGULARITY REVISION**
> Active architecture after review: Blueprint Version 2.2, Privacy-Schedule Regularity Revision
> Theorem boundary: `LOCAL-BEFORE-EXIT`

## 1. Review boundary

This is an architecture review, not a PO-04 or PO-05 proof. It asks whether the Task-013 schedule singularity can be removed by a local privacy-domain restriction while preserving the controller, ES formulas, Lyapunov design, state definitions, and passive observation model.

Task-010 showed that Version 2.0 admitted a zero initial split. Task-012 introduced Version 2.1 nonzero-split and nominal weight-interior margins. Task-013 correctly found that these margins do not control the reciprocal of the ES-43 privacy schedule in ES-60.

## 2. Exact Task-013 blocker

For one affected agent/channel pair, ES-43 gives

```text
g_j^nu z_j^nu
 = z_j^nu,                                  |z_j^nu|<=gamma_priv,j^nu,
 = gamma_priv,j^nu sign(z_j^nu),            |z_j^nu|>gamma_priv,j^nu.
```

Hence

```text
|g_j^nu z_j^nu| = min{|z_j^nu|,gamma_priv,j^nu}.
```

Public-history equality forces ES-59, and ES-60 divides its numerator by `g_j^{nu prime}z_j^{nu prime}`. Version 2.1 separates the nominal initial `z` from zero, but its frozen schedule regularity permits `gamma_priv` to be merely positive, measurable, and locally essentially bounded. Pointwise positivity does not bound its reciprocal.

Task-013 used an admitted schedule with `gamma_priv(t)=a_gamma t` for small `t>0`. For any nonzero protected initialization difference, the ES-60 numerator retains a nonzero command-difference term near the initial time, while the denominator has magnitude `a_gamma t`. The forced alternative `w_{21}'` therefore becomes unbounded and violates ES-46 on every interval beginning at zero.

The failure chain is

```text
no local lower bound for gamma_priv
 -> no local lower bound for |g'z'|
 -> unbounded reciprocal in ES-60
 -> forced w_21' leaves ES-46
 -> no admissible alternative realization
 -> PO-04 remains unproved.
```

## 3. Precise required property

Pointwise nonzero and strict pointwise positivity are insufficient. The construction needs a uniform positive lower bound for each affected public privacy schedule on a fixed nontrivial finite seed interval:

```text
gamma_priv,j^nu(t) >= eta_{gamma,j}^nu > 0,
                         t in I_s=[0,T_s].
```

Equivalently,

```text
sup_{t in I_s} 1/gamma_priv,j^nu(t)
 <= 1/eta_{gamma,j}^nu < infinity.
```

This is the exact schedule property required. It does not alone bound the whole ES-60 denominator because `z'` can also vanish. The privacy singular set must therefore retain both strata:

```text
Sigma_priv
 = union_{affected (j,nu)}
   ({z_j^nu=0} union {gamma_priv,j^nu=0}).
```

Version 2.1 already supplies a nominal nonzero initial split. On a fixed finite interval, the exact ES-49 nominal solution and bounded positive weights yield a positive nominal `z` separation. Alternative `z'` separation and the positive perturbation radius remain PO-04/PO-05 work and are not assumed by Version 2.2.

## 4. Does Version 2.1 already imply the property?

**No.**

The Version 2.1 text says `gamma_priv>0` locally and the derivation-stage regularity record explicitly permits measurability and local essential boundedness without continuity. Neither statement gives a positive essential infimum on an interval. A positive measurable function can approach zero arbitrarily close to the initial time while never taking the value zero.

Interpreting the phrase "decay schedule" as monotonic or continuous would add content that the frozen derivation explicitly declined to assume. Task-013's blocker is therefore valid.

## 5. Continuity and compactness audit

If `gamma_priv,j^nu` were known to be continuous and strictly positive on the fixed compact interval `I_s`, the extreme-value theorem would yield a positive minimum. However:

1. continuity is not part of Version 2.1;
2. compactness of `I_s` alone does not turn pointwise positivity of a measurable function into uniform separation;
3. compactness of an alternative trajectory cannot be invoked before PO-04 constructs that trajectory;
4. assuming the alternative stays in a compact nonsingular tube would assume the conclusion needed to prove PO-04.

The non-circular solution is to impose the lower margin directly on the public designer-selected schedule over the fixed seed interval. This is weaker than adding global continuity and stronger only where the quotient proof needs it. It is verifiable before any alternative trajectory exists.

## 6. Local singular-domain representation

The singular set `Sigma_priv` is representable as part of the boundary of a time-state privacy domain. Version 2.2 separates the public schedule from the `gamma_priv=0` stratum on `I_s`. The state-dependent `z=0` stratum remains an exit boundary.

The admissible construction interval ends at the earliest of:

- the fixed seed horizon `T_s`;
- the first physical/PPC-domain exit already used by the local theory;
- the first privacy-domain exit toward `z=0` or an ES-46 weight boundary;
- any earlier loss of a required local definition.

This stopping rule is compatible with `LOCAL-BEFORE-EXIT`. It does not require or assert that any state trajectory remains in the domain forever.

## 7. Domain restriction versus invariance

The schedule margin is a design-time property of a public exogenous function on a fixed finite interval. It is not a dynamical invariance theorem.

The state-dependent part of the privacy domain is treated through first exit. Version 2.2 does not state that `z'`, the alternative weights, the physical trajectory, or actuator inputs can never reach their boundaries. PO-04 must construct a nontrivial local alternative before the stopping boundary, and PO-05 remains responsible for its downstream denominator/extension questions.

The schedule may decay toward zero after `T_s`; no global lower bound is introduced. Therefore Version 2.2 does not conflict with the intended decaying privacy schedule or silently restore global continuation.

## 8. Architecture decision

**OUTCOME B — MINIMAL PRIVACY-DOMAIN REGULARITY REVISION**

The blocker can be repaired at the Privacy Domain / Assumption 2 layer. The active architecture becomes:

> **Blueprint Version 2.2 — Privacy-Schedule Regularity Revision**

The exact added contract is:

- declare a common finite privacy seed interval `I_s=[0,T_s]`, `T_s>0`;
- for every affected pair, declare `eta_{gamma,j}^nu>0` with the same command unit as `gamma_priv,j^nu`;
- require `gamma_priv,j^nu(t)>=eta_{gamma,j}^nu` for every `t in I_s`;
- define the local privacy singular boundary using both `z=0` and `gamma_priv=0`;
- stop the privacy conclusion at the earliest seed-horizon or regular-domain exit;
- make no invariance claim and impose no lower bound after `T_s`.

This is a genuine Assumption 2/privacy-domain revision, not a fact already contained in Version 2.1.

## 9. Version change map

| Layer | Version 2.1 | Version 2.2 |
|---|---|---|
| Initial split | Channel-specific nonzero margin | Unchanged |
| Nominal private weights | Strict ES-46 interior margin | Unchanged |
| `gamma_priv` | Pointwise positive/measurable locally | Uniform positive lower margin on fixed finite `I_s` |
| Singular boundary | Split singularity implicit | Explicit union of `z=0` and `gamma_priv=0` |
| Time scope | Common local seed interval | Explicit stop at `T_s` or first regular-domain exit |
| Invariance | Not proved | Still not assumed or proved |
| Alternative existence | PO-04 open | PO-04 still open; eligible for a new proof attempt |

## 10. Frozen-component statement

- Controller: **UNCHANGED**
- ES equations, including ES-43, ES-46, and ES-58--ES-61: **UNCHANGED**
- Lyapunov design: **UNCHANGED**
- State definitions: **UNCHANGED**
- Observation model: **UNCHANGED**
- `LOCAL-BEFORE-EXIT` theorem strategy: **UNCHANGED**
- Global continuation/invariance claims: **NOT ADDED**

The new symbols are public design-domain constants and a finite interval, not states or controller parameters.

## 11. Proof-state statement

**PO-04 remains OPEN and NOT PROVED at the end of Task-014.**

Task-014 removes the Task-013 blocker only at architecture level. It does not construct an alternative realization, prove public-history equality, produce a perturbation radius, or begin PO-05.

## 12. Next task

`task-015-po04-privacy-alternative-existence-v2-2-domain`

That task should re-attempt PO-04 only, using the Version 2.2 schedule margin and the explicit finite-seed/first-exit boundary. It must not begin PO-05.
