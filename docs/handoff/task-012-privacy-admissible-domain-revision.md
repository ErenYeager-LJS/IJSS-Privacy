# Handoff: task-012-privacy-admissible-domain-revision

## Branch

`task-012-privacy-admissible-domain-revision`

## PR

[Create or review the Task-012 PR](https://github.com/ErenYeager-LJS/IJSS-Privacy/pull/new/task-012-privacy-admissible-domain-revision)

## Changed files

- `Blueprint_0807/blueprint_0807.md`
- `Blueprint_0807/variables_0807.md`
- `Blueprint_0807/notation_rules_0807.md`
- `Blueprint_0807/roadmap_0807.md`
- `Blueprint_0807/theorem dependencies design_0807.md`
- `Equation Specification & Derivation Stage_0807/equation_spec_0807.md`
- `Equation Specification & Derivation Stage_0807/equation_traceability_matrix_0807.md`
- `Equation Specification & Derivation Stage_0807/proof_obligations_0807.md`
- `Equation Specification & Derivation Stage_0807/local_theorem_claim_scope_alignment_0808.md`
- `Equation Specification & Derivation Stage_0807/privacy_admissible_domain_revision_0808.md`
- `docs/handoff/task-012-privacy-admissible-domain-revision.md`
- `docs/handoff/latest.md`

## Architecture decision

Task-011 Recommendation **B. MINIMAL ASSUMPTION / DOMAIN REVISION REQUIRED** has been implemented as a controlled Blueprint reopen.

- Active Blueprint: **Version 2.1, Privacy-Domain Revision**
- Historical baseline: **Blueprint Freeze Version 2.0, frozen 2026-08-07**
- Theorem strategy: **`LOCAL-BEFORE-EXIT` unchanged**

## Exact domain changes

Assumption 2 now requires, for every affected agent/channel pair:

- a channel-specific positive nonzero initial-split margin `|z_j^nu(0)| >= eta_{z,j}^nu > 0`;
- relevant nominal private-weight schedules separated from both ES-46 endpoints by `eta_{w,j}^nu > 0` on a common local seed interval;
- `2eta_{w,j}^nu < bar(w)_j^nu-underline(w)_j^nu`;
- network-wide affected-pair coverage unless PO-04 proves a smaller closed affected subset.

These are nominal design-domain conditions only. They do not assume an alternative realization, identical public history, denominator validity, or a positive perturbation radius.

## Freeze impact

- Controller changed: **NO**
- ES formulas changed: **NO**
- Lyapunov design changed: **NO**
- State definitions changed: **NO**
- Observer design changed: **NO**
- Privacy-mechanism formulas changed: **NO**
- Simulation changed: **NO**
- HIL changed: **NO**
- New assumption/domain restriction introduced: **YES, the approved Version 2.1 regular privacy design domain**

## Proof-pipeline status

- `PO-04`: `OPEN`; eligible to resume under Version 2.1. It must construct the coupled family and prove a positive perturbation radius.
- `PO-05`: `OPEN`; remains downstream and inactive until PO-04 closes.
- No proof obligation was marked proved or otherwise assigned a new status.
- Route-L exclusions for `PO-11`, `PO-16B`, `PO-02B`, `PO-12`, `PO-14`, and `PO-15` remain unchanged.

## Tests run

- `git diff --check`
- changed-file scope audit against `origin/main`
- ES-41--ES-61 formula comparison against `origin/main`
- controller, Lyapunov, state, observer, simulation, and HIL scope audit
- proof-obligation status comparison against `origin/main`
- stale Version 2.0/current-domain and Task-010 next-task reference scan in active Task-012 files

## Tests not run

No simulation, HIL, numerical experiment, or proof derivation was run because Task-012 is a controlled architecture/domain documentation revision.

## Risks and known issues

The Version 2.1 margins remove the Task-010 zero-split/full-domain blocker but do not prove privacy ambiguity. The final manuscript privacy claim remains unavailable until PO-04 and PO-05 close. Task-013 must stop for Architecture Review if the coupled alternative family cannot be constructed without another assumption or equation change.

## Rollback

Revert the Task-012 documentation commit. This restores Blueprint Version 2.0 as the active domain and also restores the Task-010 PO-04 blocker; no executable artifact requires rollback.

## Next task

`task-013-po04-privacy-alternative-existence-revised-domain`

Prove only PO-04 on the Version 2.1 regular privacy design domain. Do not begin PO-05.
