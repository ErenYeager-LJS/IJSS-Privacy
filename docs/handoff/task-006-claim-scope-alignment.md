# Handoff: task-006-claim-scope-alignment

## Branch

`task-006-claim-scope-alignment`

## PR

Not created yet.

## Changed files

- `Equation Specification & Derivation Stage_0807/claim_scope_alignment_0808.md`
- `docs/handoff/task-006-claim-scope-alignment.md`
- `docs/handoff/latest.md`

## What changed

Created a claim-traceability audit for the frozen theory. Fourteen claim rows map each claim to its equation basis, proof obligations, exact current status, permitted wording, forbidden stronger wording, and theorem/section destination. The report fixes the strongest current boundary as local-before-exit and records stale blueprint/equation-roadmap overclaims without changing those frozen files.

The final decision is `PATH B`: `PO-11`, `PO-16B`, `PO-02B`, and the existing privacy/sharing obligations must be closed before manuscript integration of the intended global/composite theorem set.

## Tests run

- Read-only source and proof-ledger audit completed.
- Cross-document stale-claim search completed for theorem, `PO-11`, `PO-16B`, `PO-02B`, ES-102, and ES-103 references.
- `git diff --check` pending after final edits.

## Tests not run

No numerical, simulation, HIL, or proof derivation test was run because this task explicitly forbids new derivations and experiment changes.

## Risks and known issues

- Blueprint and equation-specification documents retain intended theorem wording. They are explicitly flagged in the report rather than rewritten, preserving the frozen architecture and theorem numbering.
- The current proof supports local compact-dependent inequalities, not global continuation or all-time actuator/funnel invariance.

## Rollback

Revert the single task commit; no equations, controller files, Blueprint, or proof-obligation statuses are altered.

## Next task

Resolve the non-circular joint exit/continuation condition for `PO-11`/`PO-16B`, then address `PO-02B`, `PO-12`, and `PO-14` before manuscript integration.

