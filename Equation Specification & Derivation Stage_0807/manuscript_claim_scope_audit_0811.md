# Task-018 Manuscript Claim-Scope Audit Against Task-017

> Task ID: `task-018-manuscript-latex-architecture-preparation`
> Audit stage: before manuscript writing
> Governing decision: Task-017 PASS with Minor Revision
> Final theorem boundary: `LOCAL-BEFORE-EXIT`

## 1. Audit decision

**Claim-scope audit: PASS WITH MINOR REVISION.**

The manuscript can be prepared from the approved final claim layer, but the historical full draft must not be copied into the new manuscript without claim filtering. The designated IEEE template is a format skeleton; it contains no substantive theorem statements. The older `IJSS_tex.tex` contains stronger historical claims that must be rewritten or omitted before any LaTeX prose is transferred.

No LaTeX file was modified in this audit.

## 2. Files inspected

### Designated manuscript template

`Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex`

The file preserves the required `IEEEtran` journal class, citation package style, equation/theorem environment declarations, figure/table packages, bibliography structure, and the requested high-level section placeholders. Its abstract, keywords, contributions, and body are empty. There are no existing theorem statements to preserve semantically.

### Historical full draft

`Standard Tex Usage/IJSS_tex.tex`

This is not the approved final claim layer. It contains the historical IJSS control manuscript and several claims that exceed the current privacy/control proof boundary. It may be used as a source for notation, literature, and model exposition only after claim-level review.

### Governing claim documents

- `Equation Specification & Derivation Stage_0807/final_proof_chain_manuscript_readiness_audit_0808.md`
- `Equation Specification & Derivation Stage_0807/local_theorem_claim_scope_alignment_0808.md`
- `Equation Specification & Derivation Stage_0807/proof_obligations_0807.md`
- `Equation Specification & Derivation Stage_0807/equation_traceability_matrix_0807.md`
- `Blueprint_0807/blueprint_0807.md`
- `Blueprint_0807/theorem dependencies design_0807.md`

The final claim layer overrides stronger historical target wording for manuscript purposes. Frozen files remain unchanged.

## 3. Approved manuscript claim layer

Only two result families may be written as final manuscript results.

### 3.1 Local physical theorem

The closed loop has a unique maximal local solution from an admissible independent initial state. Before the first admissibility exit, and on the selected compact bootstrap/design region, the plant, PPC, controller, reconstruction, and privacy-wrapper maps are well defined; the local voltage, frequency, privacy, and composite comparison inequalities hold; the finite PO-02A residual bound is available; and PO-13 actuator feasibility holds only within its verified design region.

This is a local-before-exit result. It is not global existence, forward invariance, all-time boundedness, all-time funnel preservation, or all-time actuator feasibility.

### 3.2 Local public-history indistinguishability theorem

On the Blueprint Version 2.2 schedule-regular privacy domain, there exists a non-nominal admissible private realization with `S' != S` that generates the same complete passive public history as the nominal realization. PO-04 supplies the initial/common construction interval; PO-05 supplies the post-seed local regular continuation. The claim stops at the earliest finite-seed or regular-domain exit.

This is an existential, local, passive-observation claim. It is not universal ambiguity, global privacy, cryptographic secrecy, differential privacy, transparent reconstruction, or protection against physical-sensor/private-memory access.

The two theorem families must be presented separately. The manuscript must not merge them into a simultaneous privacy/performance/sharing theorem.

## 4. Historical stronger claims requiring rewrite or omission

| Historical source and location | Stronger wording detected | Required Task-018 action |
|---|---|---|
| `Standard Tex Usage/IJSS_tex.tex:48-52` | Abstract claims prescribed-time recovery and accurate active-power sharing as achieved results | Rewrite abstract to local physical and local public-history claims; remove achieved sharing language |
| `Standard Tex Usage/IJSS_tex.tex:80-85` | Introduction/contributions claim voltage and frequency convergence within prescribed time and active-power distribution | Replace with local-before-exit regularity/comparison and separate local privacy construction; do not claim deadline recovery or sharing |
| `Standard Tex Usage/IJSS_tex.tex:193-203` | Practical prescribed-time definition quantifies over all initial states and all times after a deadline | Do not use this definition as the final theorem definition unless explicitly restricted to the frozen local domain; prefer the Task-017 local claim layer |
| `Standard Tex Usage/IJSS_tex.tex:231-243` | Problem objectives include asymptotic/global restoration, exact power distribution, and post-deadline tolerance maintenance | Retain only as historical motivation if needed; do not state as current objectives/results |
| `Standard Tex Usage/IJSS_tex.tex:298-314` | Lemma interprets bounded transformed coordinates as funnel satisfaction for all `t >= 0` | Rewrite as a local-before-first-exit implication; no all-time funnel invariance |
| `Standard Tex Usage/IJSS_tex.tex:447-458` | Voltage theorem claims convergence within preset time and strict prescribed performance | Replace with the local physical theorem boundary; do not invoke PO-11/PO-16B or deadline recovery |
| `Standard Tex Usage/IJSS_tex.tex:548-566` | Theorem discussion claims global prescribed-time stability and power-sharing preservation | Remove from final theorem discussion; sharing is outside the selected theorem scope |
| `Standard Tex Usage/IJSS_tex.tex:598-604` | Frequency theorem claims prescribed-time convergence and prescribed performance | Replace with local frequency inequality and local comparison result |
| `Blueprint_0807/theorem dependencies design_0807.md` | Blueprint Theorems 1-4 describe invariance, deadline recovery, sharing, and composite guarantee | Preserve as frozen historical design intent only; do not copy into manuscript theorem statements |
| `Blueprint_0807/blueprint_0807.md` | Main contribution and theorem hierarchy include deadline, sharing, and joint theorem targets | Use only for historical architecture context; final contribution text must follow Task-017 |
| `Equation Specification & Derivation Stage_0807/equation_spec_0807.md:595-600` | ES-57 uses an all-time observation-equivalence target (`for every t >= 0`) | Keep ES unchanged; rewrite manuscript claim as the Version 2.2 finite-seed/first-exit result and label ES-57 as frozen target notation if cited |

## 5. Open-PO impact on manuscript claims

| PO | Status | Manuscript treatment |
|---|---|---|
| PO-04 | PROVED | Required for and included in the local public-history theorem |
| PO-05 | PROVED | Required for and included after the PO-04 seed interval |
| PO-02B | OPEN | Future work only; no ES-51 decay or asymptotic residual claim |
| PO-11 | OPEN | Future work only; no funnel forward-invariance claim |
| PO-12 | OPEN | Outside final theorem scope; no deadline recovery |
| PO-14 | OPEN | Outside final theorem scope; no active-power sharing theorem |
| PO-15 | OPEN | Outside final theorem scope; no simultaneous composite theorem |
| PO-16B | OPEN | Future work only; no forward/global continuation or operating-region invariance |

No OPEN PO is a prerequisite for the two approved final theorem families. No PO status is changed by this audit.

## 6. Assumption wording audit

The manuscript-facing active assumptions must be limited to:

- local plant/map regularity and bounded physical data on the selected compact region;
- fixed connected undirected properly pinned cyber graph and permitted reference access;
- strict initial funnel/domain feasibility;
- PO-13 design-region actuator feasibility;
- admissible bounded privacy initialization and positive private tracking/weight margins;
- nominal nonzero-split and nominal private-weight interior margins;
- positive finite-seed `gamma_priv` lower margin on `I_s=[0,T_s]`;
- passive eavesdropper with complete public-history access and no private-memory or physical-sensor access;
- no active communication attack model.

The following must not be presented as proved consequences of the final theorem:

- ES-51 residual decay;
- global/forward continuation;
- all-time invariance;
- deadline recovery;
- sharing or equilibrium closure;
- alternative existence or denominator validity as Assumption 2 premises.

The frozen assumption ledger is not edited. Manuscript prose must avoid importing stronger unused clauses as if they were discharged proof results.

## 7. Section-by-section claim placement

The required section hierarchy is compatible with the claim layer:

1. **Introduction:** motivation, gap, contribution preview, and explicit non-claims.
2. **System Model and Problem Formulation:** frozen plant, cyber graph, public/private ownership, and passive observation object.
3. **Definitions and Active Assumptions:** Definitions 1-2 and only the active local assumption clauses.
4. **Local Physical Analysis:** PO-16A, PO-02A, PO-03, PO-06, PO-08-PO-10, PO-13, and PO-07 in their local scopes.
5. **Local Privacy Construction and Observation Equivalence:** PO-04 followed by PO-05; complete public history, not a single message.
6. **Theoretical Results and Proof Chain:** two separate theorem statements and their dependency order; no Theorem 2/3/4 stronger claims.
7. **Limitations and Discussion:** explicitly list all six remaining OPEN POs and the excluded claims.
8. **Conclusion:** summarize only the local physical and local privacy results.

The IEEE formatting, citation style, equation numbering, theorem environments, figure/table conventions, and bibliography structure from `Privacy_Preserving_Microgrid_Structure.tex` remain unchanged.

## 8. Mandatory wording controls before LaTeX drafting

The following words or constructions require explicit scope qualifiers or removal:

- `for all t >= 0`, `global`, `globally`, `asymptotic`, `invariant`, `forward invariant`, `guarantees by T_V/T_omega`, `accurate active-power sharing`, `simultaneous`, `composite guarantee`, and `post-deadline`;
- any statement that uses ES-57's all-time quantifier without replacing it with the Version 2.2 stopping-boundary scope;
- any statement that calls the public-history result cryptographic, differential-private, attack-resilient, or side-channel secure;
- any statement that presents Blueprint Theorems 1-4 as already proved.

Permitted qualifiers include `locally`, `before the first admissibility exit`, `on the selected compact bootstrap/design region`, `up to the finite-seed/regular-domain stopping boundary`, `existence-based`, and `under the passive observation model`.

## 9. Audit conclusion and next action

The claim-scope audit is complete. The minor revision is editorial and claim-layer based; it does not require architecture reopening, equation changes, controller changes, new states, new assumptions, or new proofs.

**Next action:** begin LaTeX architecture population from the designated IEEE template, using only the two approved theorem families and the wording controls above. Do not transfer the historical `IJSS_tex.tex` theorem/result prose verbatim.

Blueprint Reopen Required: **NO**.

LaTeX writing started in this audit: **NO**.
