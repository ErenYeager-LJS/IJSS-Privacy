# Privacy-Admissible Domain Revision 0808

> Task ID: `task-012-privacy-admissible-domain-revision`
> Active architecture: Blueprint Version 2.1, Privacy-Domain Revision
> Historical baseline: Blueprint Freeze Version 2.0, frozen 2026-08-07
> Theorem strategy: `LOCAL-BEFORE-EXIT`

## 1. Approved resolution

Task-011 selected **B. MINIMAL ASSUMPTION / DOMAIN REVISION REQUIRED**. The Task-010 zero-split counterexample is genuinely admitted by the Version 2.0 privacy domain, so PO-04 cannot be repaired on that full domain by proof rearrangement alone.

Task-012 implements the approved controlled Blueprint reopen. Version 2.0 remains the historical baseline. Version 2.1 changes only the privacy-admissible design-domain contract in Assumption 2 and its dependent claim/traceability prose. It does not change the controller, any ES formula, the Lyapunov design, state definitions, observer content, simulation, HIL, theorem numbering, or the `LOCAL-BEFORE-EXIT` strategy.

## 2. Previous domain deficiency

Version 2.0 allowed an affected channel to start with `p_j^nu(0)=q_j^nu(0)=c_j^nu(0)`, hence `z_j^nu(0)=0`, while its private weights merely satisfied the closed ES-46 positive interval. For a nonzero protected perturbation with the same public initial value, ES-58 gives a nonzero alternative split. The ES-59 public-trajectory identity then forces an alternative private weight through the wrong sign near the initial time in the Task-010 counterexample, violating the positive ES-46 lower bound.

The old phrases "private-weight margins" and "local admissibility" did not quantify separation from zero or from the ES-46 endpoints. They therefore could not legally exclude that counterexample. The deficiency was a domain defect, not an algebraic defect in ES-41--ES-61.

## 3. Revised domain conditions

For each channel `nu in {V,omega}` and every agent/channel pair affected through the coupled alternative construction, Version 2.1 requires a declared channel-consistent split margin

```text
|z_j^nu(0)| >= eta_{z,j}^nu > 0.
```

On a declared common local seed interval, every relevant designer-selected nominal private-weight schedule must satisfy

```text
underline(w)_j^nu + eta_{w,j}^nu
 <= w_{j,12}^nu(t), w_{j,21}^nu(t)
 <= bar(w)_j^nu - eta_{w,j}^nu,

2 eta_{w,j}^nu
 < bar(w)_j^nu - underline(w)_j^nu.
```

The `eta_{z,j}^nu` margins have the corresponding channel-command units. The `eta_{w,j}^nu` margins have the corresponding private-weight units. They are public design-domain constants, not states, adaptive gains, masking signals, or alternative perturbations. ES-46 itself remains unchanged.

## 4. Non-circularity

Assumption 2 supplies only nominal regularity and strict design margins. It does not assume any of the conclusions assigned to PO-04 or PO-05. In particular, it does not assume:

- a non-nominal protected value or alternative realization;
- equality of nominal and alternative public histories;
- a positive admissible perturbation radius;
- validity of ES-58--ES-61 for an alternative;
- persistence of the alternative denominators.

PO-04 must construct a coupled local alternative family from the revised nominal domain, establish continuous compatibility, and prove a strictly positive perturbation radius that stays within the declared margins. PO-05 remains downstream and must validate the denominators and alternative-weight feasibility for the family actually produced by PO-04. Thus the assumption does not contain the privacy conclusion it is later used to prove.

## 5. Network-wide applicability

A protected-agent perturbation can change hidden commands outside that agent through the frozen electrical and coordination coupling. A condition imposed only on the protected agent would therefore leave open the same zero-split or endpoint obstruction on another affected channel.

Version 2.1 applies the split and weight margins to every affected agent/channel pair. Until PO-04 proves that a smaller affected subset is closed under the coupled construction, the operational interpretation is network-wide for both voltage and frequency channels. This is the weakest presently defensible quantifier because no smaller closed affected set has yet been proved.

## 6. Version 2.0 to 2.1 change map

| Artifact layer | Version 2.0 | Version 2.1 change |
|---|---|---|
| Blueprint status | Frozen historical target | Active privacy-domain revision; Version 2.0 retained as baseline |
| Assumption 2 | Bounded admissible private substates and weights | Adds channel-specific nonzero initial-split and nominal weight-interior margins on a common local seed interval |
| Privacy domain | Full bounded admissible class | Regular nominal design domain on every affected agent/channel pair |
| Alternative existence | Open PO-04 | Still open; now eligible to resume on the revised domain |
| Denominator validity | Open PO-05 | Still open and downstream of PO-04 |
| Privacy claim | Conditional local existence-based ambiguity | Same target, explicitly restricted to the Version 2.1 regular domain |
| Controller and privacy dynamics | Frozen | Unchanged |
| ES formulas | Frozen | Unchanged |
| Lyapunov design and states | Frozen | Unchanged |
| Theorem strategy | `LOCAL-BEFORE-EXIT` | Unchanged |

## 7. Equation-freeze audit

The formula-level Equation Freeze remains intact. Task-012 changes assumption, domain, traceability, and claim-scope prose only. In particular:

- ES-41, ES-42, and ES-43 are unchanged;
- ES-44, ES-45, and ES-46 are unchanged;
- ES-47--ES-50 are unchanged;
- ES-54--ES-57 are unchanged;
- ES-58--ES-61 are unchanged.

The new margins restrict the nominal design domain around these formulas; they do not alter the formulas or introduce a replacement privacy mechanism.

## 8. Privacy-claim scope

After PO-04 and PO-05 close, the strongest retained privacy target is the existence of at least one genuinely non-nominal private realization with identical passive public history on a common local-before-exit interval, for nominal realizations in the Version 2.1 regular privacy design domain.

The revision does not support privacy over the historical unrestricted Version 2.0 class. It does not support all-initialization or all-perturbation ambiguity, global ambiguity, global continuation, transparent reconstruction, cryptographic secrecy, differential privacy, information-theoretic secrecy, or protection against private-memory or physical-sensor access.

## 9. Proof-obligation consequences

- `PO-04`: remains `OPEN`; eligible to resume under Version 2.1. It must construct the coupled alternative family and prove a positive perturbation radius.
- `PO-05`: remains `OPEN`; downstream and inactive until PO-04 closes.
- `PO-11`, `PO-16B`, and `PO-02B`: remain outside the active Route-L continuation pipeline.
- `PO-12`, `PO-14`, and `PO-15`: remain outside the final local manuscript theorem scope under the Task-009 classification.
- No proof obligation is discharged or assigned a new status by Task-012.

## 10. Exact next task

`task-013-po04-privacy-alternative-existence-revised-domain`

Task-013 should prove only PO-04 on the Version 2.1 regular privacy design domain: construct the coupled non-nominal alternative family, prove identical passive public history on the common local-before-exit interval, and quantify a positive admissible perturbation radius. It must not begin PO-05 or alter the Blueprint, controller, ES formulas, states, Lyapunov design, simulation, or HIL.

## Final decision

- Architecture contradiction discovered: **NO**
- Blueprint reopen completed: **YES, controlled Version 2.1 privacy-domain revision only**
- Equation formula reopen required: **NO**
- PO-04 may resume: **YES**
- PO-05 may resume now: **NO**
- Recommended next task: `task-013-po04-privacy-alternative-existence-revised-domain`
