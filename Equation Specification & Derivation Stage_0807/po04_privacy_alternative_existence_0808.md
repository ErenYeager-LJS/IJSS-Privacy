# PO-04 Privacy Alternative Existence Audit

**Task:** `task-010-po04-privacy-alternative-existence`

**Date:** 2026-08-08

**Theory boundary:** Blueprint Freeze Version 2.0; Equation Freeze; final manuscript scope `LOCAL-BEFORE-EXIT`

## 1. PO-04 exact target

PO-04 requires, for the frozen admissible privacy class, at least one protected value `S_i' != S_i` with an alternative initialization, private path, and private-weight pair satisfying ES-58--ES-61 and every clause of `A_i(S_i)`. The nominal and alternative realizations must generate exactly the same legally observed public history on a common admissible local interval. Merely relabeling the nominal realization is insufficient.

This audit tests that existence claim only. It does not attempt the general denominator/extension result assigned to PO-05 and does not invoke any continuation result after the first admissibility exit.

## 2. Frozen observation model

By ES-14--ES-16, the passive eavesdropper observes:

- every transmitted message `m_j=[p_j^V,p_j^omega]^T` for every agent and every time in the observation interval;
- the public topology, communication timing, and protocol metadata `H_c`;
- `G_c`, `a_ij`, `b_i`, the references, funnel schedules, deadlines, and every controller parameter declared public.

The eavesdropper does not observe physical sensor histories, `c_i`, `hat(c)_i`, `r_i`, the private substates `q_i`, the private weights `w_i`, physical uncertainty, or local controller memory.

Consequently, observation equality under unchanged metadata requires

```text
p_j'(t)=p_j(t)
```

in both channels for every public agent trajectory on the common interval. Changing the public tracking rate or any other declared controller parameter is not permitted.

## 3. Two realizations and allowed differences

For one agent `i`, let `R` denote a nominal admissible realization. Its private data include `S_i=c_i(0)`, `q_i(0)`, the private path `q_i(.)`, the weights `w_{i,12}(.)` and `w_{i,21}(.)`, and the unobserved local physical/controller history compatible with them. Its public history contains `p_i(.)` and the metadata in ES-16.

Let `R'` denote a proposed alternative. It may differ in `S_i'`, `q_i'(0)`, `q_i'(.)`, `w_{i,12}'(.)`, `w_{i,21}'(.)`, and compatible unobserved local histories. It must retain the same `p_i(.)`, all other public messages, and all public metadata. Both realizations must satisfy ES-41--ES-46 and ES-58--ES-61, and `R'` must satisfy every admissibility clause listed after ES-61.

At least one component of `S_i'-S_i` must be nonzero. The following audit applies channel by channel, so suppress the channel superscript and write that nonzero component as `epsilon`.

## 4. Frozen construction at a permitted nominal initialization

The frozen initialization ES-41 permits the nominal split

```text
p_i(0)=q_i(0)=c_i(0).
```

It obeys ES-41 and gives `z_i(0)=0` by ES-42. Positive private weights can be selected inside ES-46, so this split is not excluded from the frozen admissible class. PO-16A supplies a nontrivial local solution from an admissible initial point.

Moreover, ES-49 is homogeneous in `z_i`. Uniqueness therefore gives

```text
z_i(t)=0
```

throughout the nominal local interval, and hence `g_i(t)z_i(t)=0` there.

Now choose any genuinely non-nominal protected initialization in one channel:

```text
c_i'(0)=c_i(0)+epsilon,    epsilon != 0.
```

The same initial public message and ES-41 force ES-58, not merely as an optional construction:

```text
p_i'(0)=p_i(0),
q_i'(0)=2c_i'(0)-p_i(0)=c_i(0)+2epsilon,
z_i'(0)=p_i'(0)-q_i'(0)=-2epsilon.
```

Thus `R'` would be genuinely non-nominal, but its initial alternative difference has the sign opposite to the protected perturbation.

## 5. Public-history equality forces an inadmissible weight

Assume, for contradiction, that `R'` produces the same public history on a common interval `[0,tau]`, with `tau>0`. Then `p_i'=p_i`. The two public-state trajectories are absolutely continuous local solutions, so their derivatives agree almost everywhere. Subtracting their ES-44/ES-45 public-state equations yields, almost everywhere,

```text
0 = lambda_tr,i(c_i'-c_i)
    -w_{i,21}'g_i'z_i'
    +w_{i,21}g_i z_i.
```

For the permitted nominal split, `g_i z_i=0`. Therefore public-history equality necessarily imposes ES-59 in the reduced form

```text
w_{i,21}'g_i'z_i' = lambda_tr,i(c_i'-c_i).
```

This identity is independent of how the later private path `q_i'(.)` is selected. It follows from the public equation itself and cannot be bypassed by ES-61.

The local solutions and command maps are continuous before exit. Since

```text
c_i'(0)-c_i(0)=epsilon,
z_i'(0)=-2epsilon,
```

there is a sufficiently short common interval on which `c_i'-c_i` retains the sign of `epsilon` and `z_i'` retains the opposite sign. The ES-43 factor `g_i'` is nonnegative and, for a positive privacy schedule, strictly positive. Hence `g_i'z_i'` has the sign opposite to `c_i'-c_i`. ES-59 then requires

```text
w_{i,21}'(t)<0
```

almost everywhere on that short interval. In the unsaturated ES-43 branch, its limiting initial value is `-lambda_tr,i/2`; saturation can change its magnitude but not its sign. If the schedule were zero so that `g_i'=0`, ES-59 would instead be impossible because its right-hand side is nonzero.

ES-46 requires `w_{i,21}'(t) >= underline(w)_i > 0`. The required alternative therefore violates the frozen private-weight admissibility interval. The contradiction holds for whichever channel contains a nonzero component of `S_i'-S_i`; perturbing both channels does not avoid it.

This is an interval contradiction, not a reliance on evaluating an almost-everywhere differential equation at the single instant `t=0`.

## 6. Non-nominality, local admissibility, and equality results

| Required PO-04 item | Audit result |
|---|---|
| Genuinely distinct protected value | Algebraically available by `epsilon != 0`. |
| Same initial public state | Forced by ES-16 and implemented by ES-58. |
| Same public trajectory | Necessarily imposes ES-59 almost everywhere. |
| Positive bounded alternative weights | Fails for the admissible zero-split nominal realization because ES-59 forces `w_{i,21}'<0`. |
| Alternative private-path freedom | Cannot repair the sign conflict because ES-58 fixes `z_i'(0)` and ES-59 follows from the public equation. |
| Common local interval | Cannot contain an admissible alternative with identical public history for this nominal realization. |

Therefore the requested local admissibility proof and public-history equality proof cannot both be completed. The obstacle arises before any forward-invariance, global-continuation, or asymptotic question.

## 7. Denominator and PO-05 boundary

For the nonzero perturbation above, `z_i'(0)=-2epsilon`, so continuity would keep `z_i'` nonzero on a sufficiently short interval. With a positive ES-43 schedule, `g_i'z_i'` is also nonzero there. Thus the decisive counterexample is not an isolated-zero denominator at `t=0`; it is the negative weight forced by the numerator/denominator sign in ES-60.

More generally, membership in `A_i(S_i)` already requires candidate-specific validity of the ES-60 and ES-61 divisions. PO-04 cannot silently defer every denominator fact while using those formulas. A candidate with strict nonzero initial denominators could establish a short nonvanishing interval by frozen continuity without proving PO-05's general continuation/extension claim. That observation prevents an automatic PO-04/PO-05 cycle, but it does not rescue the full frozen admissible class because the zero-split counterexample fails ES-46 first.

A second, independent local-neighborhood concern remains: ES-46 supplies positive public lower and upper bounds but does not require each nominal private weight trajectory to have a strict interior distance from both endpoints. A generic small-perturbation argument for the forced alternative weights would need such a margin. Introducing that margin is forbidden in Task-010 and is unnecessary to the decisive sign counterexample.

## 8. Dependency and circularity audit

| Potential dependency | Result |
|---|---|
| PO-05 | Candidate-specific local nonvanishing is logically needed to use ES-60/ES-61, while the broader validity/extension proof remains PO-05. The present blocker is already conclusive without proving PO-05. |
| PO-11 | Not used. |
| PO-16B | Not used. |
| PO-02B | Not used. |
| PO-12 | Not used. |
| PO-14 | Not used. |
| PO-15 | Not used. |
| Global continuation | Not used. |
| Funnel invariance | Not used. |

The frozen PO-04 route therefore stops locally at ES-46/ES-59. Starting PO-05 would not resolve the negative-weight contradiction and is not authorized by this task.

## 9. Exact mathematical blocker

The frozen admissible class includes `p_i(0)=q_i(0)=c_i(0)`. For that nominal realization, every nonzero protected initialization perturbation preserving the same public message forces the alternative difference to have the opposite sign. Public-trajectory equality then forces a negative `w_{i,21}'`, contrary to the strictly positive ES-46 lower bound.

Excluding this counterexample would require at least a restriction on the initial decomposition and would still leave the lack of guaranteed interior private-weight margins to audit. Both would be new proof-level conditions forbidden by Task-010. No division-free alternative construction exists in ES-58--ES-61, and changing that construction would modify the frozen privacy mechanism.

## 10. Final PO-04 verdict

**B. PO-04 BLOCKED — ARCHITECTURE REVIEW REQUIRED**

PO-04 is not provable for the current frozen admissible class. No Blueprint, equation, controller, privacy mechanism, state, assumption, theorem number, proof-ledger status, simulation file, or HIL file is changed by this audit.

## 11. Exact next task recommendation

`task-011-privacy-construction-architecture-review`

That Architecture Review must decide whether the privacy theorem's admissible domain can be defensibly restricted or whether ES-58--ES-61 must be replaced by a construction compatible with positive bounded weights. It must not begin PO-05 under the current blocker.
