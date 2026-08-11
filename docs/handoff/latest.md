# Latest Handoff

Current task: `task-012-privacy-admissible-domain-revision`

Branch: `task-012-privacy-admissible-domain-revision`

PR: [Create or review the Task-012 PR](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/new/task-012-privacy-admissible-domain-revision)

Full handoff: [task-012-privacy-admissible-domain-revision.md](task-012-privacy-admissible-domain-revision.md)

## Current decision

Task-011 Recommendation **B. MINIMAL ASSUMPTION / DOMAIN REVISION REQUIRED** is implemented. The active architecture is **Blueprint Version 2.1, Privacy-Domain Revision**; Version 2.0 remains the historical frozen baseline. The controller, all ES formulas, Lyapunov design, states, observers, theorem numbering, simulation, HIL, and `LOCAL-BEFORE-EXIT` theorem strategy are unchanged.

Assumption 2 now restricts the privacy-admissible design domain using channel-specific nonzero initial-split margins and nominal private-weight interior margins on a common local seed interval for every affected agent/channel pair. These margins do not assume an alternative realization, identical public history, denominator validity, or a positive perturbation radius.

## Proof pipeline

- `PO-04`: remains `OPEN`, but is eligible to resume on the Version 2.1 regular privacy design domain.
- `PO-05`: remains `OPEN`, downstream and inactive until PO-04 closes.
- No proof-obligation status changed.
- Route-L exclusions remain unchanged.

## Next task

`task-013-po04-privacy-alternative-existence-revised-domain`

Prove only PO-04's coupled alternative existence and positive perturbation radius on the revised domain. Do not begin PO-05.
