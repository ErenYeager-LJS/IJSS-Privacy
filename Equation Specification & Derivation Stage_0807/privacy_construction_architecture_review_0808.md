# Privacy Construction Architecture Review

**Task:** `task-011-privacy-construction-architecture-review`

**Date:** 2026-08-08

**Review boundary:** Blueprint Freeze Version 2.0 and Equation Freeze remain unchanged in this task. The final manuscript strategy remains `LOCAL-BEFORE-EXIT`.

## 1. Review question and classification

The question is whether the frozen privacy construction can support a genuinely non-nominal private realization with the same complete public history, despite the Task-010 zero-split counterexample, and what the smallest defensible architecture resolution would be.

The audit classifies the issue as follows:

| Issue class | Finding |
|---|---|
| Proof bug | **NO.** The Task-010 sign calculation follows necessarily from the frozen public-state equation. |
| Proof boundary | **NO as the primary cause.** Restricting time to a local-before-exit interval does not remove the sign contradiction. |
| Assumption-domain issue | **YES, primary.** The frozen admissible class includes a singular zero-split stratum and does not require an interior private-weight margin. |
| Privacy-construction issue | **YES on the full frozen domain.** ES-58--ES-61 cannot cover the zero-split stratum while ES-46 keeps the weights positive. |
| Blueprint-level issue | **YES if the minimal domain repair is adopted.** Assumption 2 currently does not state the required restricted design domain. |
| Claim-level issue | **YES until resolution.** The retained local privacy claim cannot quantify over the full frozen admissible class. |

The smallest viable resolution is an explicit restriction of the privacy-admissible design domain. It is not already implicit in the frozen assumptions.

## 2. Independent reproduction of the Task-010 blocker

Suppress the channel superscript and consider one agent and one channel. ES-41 permits

```text
p_i(0)=q_i(0)=c_i(0),
```

so ES-42 gives `z_i(0)=0`. ES-49 is homogeneous in `z_i`; local uniqueness therefore gives `z_i(t)=0` and `g_i(t)z_i(t)=0` on the nominal local interval.

Let the protected command initialization change by `epsilon != 0` while the public initial message remains unchanged. ES-41 and ES-58 then force

```text
c_i'(0)=c_i(0)+epsilon,
p_i'(0)=p_i(0),
q_i'(0)=2c_i'(0)-p_i(0),
z_i'(0)=p_i'(0)-q_i'(0)=-2epsilon.
```

Complete public-history equality under ES-14--ES-16 requires `p_i'=p_i`. The two locally absolutely continuous public trajectories therefore have equal derivatives almost everywhere. Subtracting their ES-44/ES-45 public equations gives

```text
w_{i,21}'g_i'z_i'
 = lambda_tr,i(c_i'-c_i)+w_{i,21}g_i z_i.
```

For the zero-split nominal realization, the last nominal term is zero. By continuity, on a sufficiently short interval `c_i'-c_i` keeps the sign of `epsilon`, while `z_i'` keeps the opposite sign. The positive ES-43 factor does not change the sign of `z_i'`. The equality consequently requires `w_{i,21}'<0` almost everywhere on that interval. This contradicts ES-46, which requires `w_{i,21}' >= underline(w)_i >0`.

This derivation uses neither PO-05 nor continuation beyond the local interval. ES-61 cannot repair it because `w_{i,12}'` does not appear in the public `p_i` equation. Changing a private path after initialization cannot alter the forced initial sign relation.

## 3. Frozen-domain admission check

The counterexample is genuinely admitted:

1. ES-41 requires only the sum `p_i(0)+q_i(0)=2c_i(0)` and permits equality of all three values.
2. ES-42 then permits `z_i(0)=0`.
3. ES-46 permits positive bounded nominal weights but imposes no nonzero-split condition.
4. Assumption 2 states only that private substates and coupling parameters are initialized in an admissible bounded set and that the decomposition is well defined.
5. No frozen definition, initialization rule, traceability entry, or proof obligation excludes `z_i(0)=0`.
6. The local plant/controller domain does not exclude the split, because `p_i=q_i=c_i` also gives the valid reconstruction residual `r_i(0)=0`.

The traceability and PO-04 prose mention private-weight margins and compatible alternative paths, but neither supplies a quantitative distance from both ES-46 endpoints or a nonzero initial split. Interpreting those phrases as if they already excluded the counterexample would strengthen the frozen assumption after the fact.

## 4. Class A: proof-only alternative audit

### 4.1 Frozen degrees of freedom

The available alternative degrees of freedom are `S_i'`, `q_i'(0)`, a differentiable private path `q_i'(.)`, and the two private weights. They are constrained as follows:

- same public history fixes `p_i'=p_i`;
- ES-41 and ES-58 fix `q_i'(0)` once `S_i'` and the common `p_i(0)` are chosen;
- the public equation forces ES-59 and ES-60;
- the private equation forces ES-61 once the private path is selected;
- ES-46 keeps both weights positive and bounded.

### 4.2 Alternatives considered

| Attempt | Why it fails on the frozen zero-split case |
|---|---|
| Reverse the sign of `epsilon` | Both `epsilon` and `z_i'(0)=-2epsilon` reverse, so their signs remain opposite. |
| Perturb both voltage and frequency components | Every nonzero perturbed component has the same channel-wise contradiction. |
| Select another `q_i'(.)` after `t=0` | ES-58 already fixes `q_i'(0)` and the short-interval sign of `z_i'`; ES-61 cannot change ES-59. |
| Select `w_{i,12}'` first | `w_{i,12}'` does not enter the public-state equality that forces the negative `w_{i,21}'`. |
| Use ES-43 saturation | Saturation changes magnitude, not the sign of `g_i'z_i'`. |
| Defer the issue to PO-05 | The alternative denominator may be nonzero locally; the contradiction is the weight sign. |
| Change public metadata or tracking gains | ES-16 declares them public and identical between the two realizations. |

No already-frozen proof-only construction avoids the contradiction. Recommendation A is rejected.

## 5. Class B: admissible-domain and assumption restriction audit

### 5.1 Minimum robust restricted domain

A local perturbation argument can operate around a regular nonzero-split nominal realization because, at zero perturbation, ES-60 returns the nominal `w_{i,21}`. The minimum robust design-domain contract would need all of the following, expressed only with existing variables:

1. every agent/channel whose hidden command may change along the coupled alternative realization has an initial split separated from zero, `|z_j^nu(0)| >= eta_z >0`;
2. the relevant designer-selected nominal private-weight schedules remain inside, rather than merely on, the ES-46 interval by a declared margin `eta_w>0` on the common local seed interval;
3. the protected perturbation is nonzero but small enough that `z_j^{nu prime}` does not change sign or reach zero on that interval;
4. the local plant/input compatibility clause is formulated as a coupled alternative system on this nonsingular domain, with its continuous dependence on the perturbation proved rather than assumed;
5. the same restriction is applied network-wide wherever electrical coupling changes hidden commands, rather than only to the single protected agent.

The network-wide clause is necessary for a robust theorem: a hidden reconstruction change at agent `i` can alter physical network trajectories and therefore other hidden commands. Preserving every observed `p_j` may require adjustment of the corresponding private realization for more than one agent.

For the exact vector target ES-54--ES-57, the weakest quantifier needs at least one perturbable channel per protected agent. A claim that each voltage and frequency component is separately ambiguous would require the nonzero-split/interior-margin conditions channel by channel.

### 5.2 Why this restriction is sufficient at architecture level

At zero perturbation, the alternative and nominal realizations coincide, `z_j^{nu prime}=z_j^nu`, and the forced ES-60 ratio equals the nominal `w_{j,21}^nu`. A nonzero split makes both ES-60 and ES-61 locally nonsingular. A strict weight-interior margin leaves room for a sufficiently small nonzero perturbation if the coupled alternative system has the required local continuous dependence. One may keep `w_{j,12}^{nu prime}` at a nominal interior choice and solve the corresponding private/physical local system, then use ES-60 to enforce the fixed public path.

This is an architecture feasibility argument, not a PO-04 proof. The new assumption/domain clauses supply only the nonzero and interior margins; they must not assume that the alternative exists. The revised PO-04 would still have to construct the coupled local family, prove its local continuous dependence from the restricted nonsingular vector field, and quantify the allowed perturbation radius. PO-05 would then verify the resulting local denominator persistence.

### 5.3 Classification

The restriction removes the Task-010 counterexample without changing ES-41, ES-46, or ES-58--ES-61. It is, however, a **genuine strengthening of Assumption 2 and the admissible privacy design domain**, not a clarification already implicit in the frozen text. It adds nonzero-separation and interior-margin requirements that are absent today.

Class B is viable and is the least invasive resolution.

## 6. Class C: alternative-construction equation revision audit

An equation-level repair is possible but is not minimal.

ES-59 is not an independently selectable formula; it is the identity obtained from the public equation. Likewise, ES-58 follows from the common public initial state together with ES-41. Therefore editing only ES-59, ES-60, or ES-61 would be mathematically inconsistent.

The earliest coherent equation-level change would be to revise the ES-41/ES-58 initialization map so that the alternative private split has an independent sign-compatible initialization degree of freedom instead of the forced relation `z_i'(0)=z_i(0)-2epsilon`. That would generally permit a nonzero initial reconstruction residual. It would require coordinated revision of the initialization contract, ES-47--ES-50 initial-residual consequences, local residual bounds, the alternative construction, and their proof dependencies.

Changing the sign of the ES-44/ES-45 public coupling is not a smaller repair because it changes ES-49 and can destroy the existing positive-weight difference decay used by PO-01 and PO-10. Allowing negative weights by changing ES-46 also violates the required positive-weight architecture and invalidates existing stability estimates.

Class C could preserve the passive observation model and physical controller, but it would reopen both Blueprint and Equation Freeze and create a substantially larger privacy-wrapper proof program. It is a fallback only if the restricted design domain in Class B is rejected.

## 7. Class D: privacy claim rescoping audit

Without changing any frozen artifact, a weaker manuscript statement could say that public-history ambiguity is available only for nominal realizations already lying in a regular, nonzero-split, weight-interior subset for which the compatible alternative construction exists.

This would honestly exclude the zero-split counterexample, preserve the passive-eavesdropper model, and retain a conditional local ambiguity statement. However, merely saying “whenever a compatible alternative exists” would be tautological. A meaningful claim must disclose the same substantive nonzero-split and margin conditions identified in Class B.

Claim-only rescoping would materially weaken the contribution because the mechanism would no longer protect the full stated admissible class and the admissible subset would not be part of the system contract. Formalizing the subset as a designer-selectable privacy domain under Assumption 2 is mathematically cleaner and more reviewable. Recommendation D is therefore not preferred.

## 8. Minimality comparison

| Test | A. Proof only | B. Domain/assumption restriction | C. Equation revision | D. Claim rescope | E. Unsupported |
|---|---|---|---|---|---|
| Removes exact zero-split counterexample | No | Yes, by exclusion | Yes | Yes, by exclusion from claim | No repair |
| Preserves passive-eavesdropper model | Yes | Yes | Yes | Yes | N/A |
| Preserves physical controller | Yes | Yes | Yes, if initialization-only route is used | Yes | N/A |
| Preserves local-before-exit theorem strategy | Yes | Yes | Requires revalidation | Yes | N/A |
| Preserves positive bounded weights | No valid construction | Yes | Possible, but requires redesign | Yes on stated subset | N/A |
| Requires a new/stronger assumption | No | **Yes** | Possibly, plus equations | Claim condition instead | N/A |
| Requires Equation Freeze reopening | No | **No ES formula change** | **Yes** | No | N/A |
| Requires Blueprint reopening | No | **Yes** | **Yes** | No, if kept manuscript-facing only | N/A |
| Creates proof work | PO-04 still blocked | Revised PO-04 and PO-05 | Multiple residual/privacy obligations | Conditional claim validation | Privacy theorem removed |
| Publication-worthy privacy claim | No | **Yes, if the design restriction is explicit and justified** | Potentially yes | Weaker and conditional | No |

Class B is smaller than Class C because it retains the complete privacy mechanism and all ES formulas. It is stronger and less tautological than Class D because the eligible privacy design domain becomes part of the theorem contract rather than an after-the-fact claim qualifier.

## 9. Freeze impacts

### Blueprint Freeze

**Blueprint reopening would be required if Recommendation B is adopted.** The nonzero-split and weight-interior conditions materially narrow Assumption 2 and the admissible privacy domain. They cannot be inserted as a “clarification” while continuing to label Blueprint Freeze Version 2.0 unchanged.

Task-011 itself does not reopen or edit the Blueprint.

### Equation Freeze

**Equation Freeze reopening is not required for Recommendation B at the formula level.** ES-41--ES-61, including ES-46, remain unchanged. The architecture-resolution task would have to update assumption/admissibility prose and traceability consistently, then record that the equation formulas were not changed.

If the project instead selects Class C, Equation Freeze and Blueprint must both reopen.

## 10. Manuscript privacy contribution impact

Recommendation B changes the defensible contribution from ambiguity over the entire previously stated bounded privacy class to ambiguity on an explicit designer-selectable regular privacy domain. The retained statement remains meaningful:

- the protected initial virtual coordination state has at least one non-nominal private explanation;
- the complete passive public history is identical on a common local-before-exit interval;
- the controller, public payload, and positive bounded private weights are retained;
- no cryptographic, differential-privacy, sensor-access, global, or all-initialization claim is added.

The restriction must be visible in the theorem assumptions and limitations. Hiding it only in a proof would overstate the result. Because the split and private weights are design choices rather than exogenous plant disturbances, the restricted-domain claim can remain publication-worthy, subject to later PO-04 and PO-05 closure.

## 11. Final recommendation

**B. MINIMAL ASSUMPTION / DOMAIN REVISION REQUIRED**

No proof-only closure exists on the full frozen admissible class. A controlled revision of the privacy admissibility domain is the smallest viable resolution: exclude zero/singular initial splits on the affected network channels and require explicit interior private-weight margins for the local alternative family. This preserves the controller, observation model, positive bounded weights, ES formulas, and local-before-exit strategy.

PO-04 may not resume until that architecture resolution is approved and propagated. PO-05 may not resume before the revised PO-04 closes.

## 12. Exact next task

`task-012-privacy-admissible-domain-revision`

That task should perform the controlled Blueprint/Assumption-2 domain revision, align the non-frozen manuscript claim and proof dependencies, and leave every ES formula unchanged. It must not prove PO-04 or begin PO-05.
