# Task-019 LaTeX Manuscript Architecture Mapping

> Task ID: `task-019-latex-manuscript-architecture-population`
> Stage: architecture mapping only; manuscript insertion not started
> Template: `Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex`
> Historical source: `Standard Tex Usage/IJSS_tex.tex`
> Final theorem scope: `LOCAL-BEFORE-EXIT`

## 1. Mapping decision

**Architecture mapping complete. Do not populate the `.tex` file until this mapping is approved.**

The IEEE template is the sole manuscript destination. The historical IJSS file is a source for notation, literature context, and system-description material only. Its theorem statements, proof conclusions, contribution claims, and simulation claims are not transferable without rewriting against the Task-017/018 claim layer.

No `.tex` file was modified.

## 2. Current designated template

File: `Standard Tex Usage/Privacy_Preserving_Microgrid_Structure.tex`

### Preserved format elements

- `\documentclass[journal]{IEEEtran}`;
- `amsmath`, `amsfonts`, `amssymb`, `booktabs`, `bm`, `graphicx`, `subfigure`, `color`, `multirow`, and `pifont` package structure;
- IEEE theorem-like environments for definition, proposition, assumption, theorem, proof, lemma, remark, and corollary;
- centered caption configuration;
- figure/table conventions and bibliography environment;
- equation numbering behavior and citation style.

### Current template sections

| Existing location | Current content | Task-019 treatment |
|---|---|---|
| Title/author/abstract/keywords | Format placeholders and title | Preserve format; rewrite title/abstract/keywords later to local claims |
| `Introduction` | Empty body and contribution list | Populate from approved gap and two result families only |
| `Preliminaries` | Empty | Rename to `System Model and Problem Formulation`; add subsections |
| `Prescribed Time-based Secondary Controller Design` | Empty | Replace with the approved Sections IV-VI architecture; do not retain old standalone title |
| `Illustrative Simulation` | Empty | Not part of the approved first manuscript architecture; add only after evidence and scope are approved |
| `Hardware-in-the-Loop Closed-Loop Test` | Empty | Keep out of the theory architecture until experiment evidence is separately validated |
| `Conclusion` | Empty | Summarize only local physical and local privacy results |
| Bibliography | Placeholder `thebibliography` | Preserve structure; populate only verified references |

The template's empty section placeholders may be reorganized. The document class and formatting system may not be replaced.

## 3. Historical source mapping

File: `Standard Tex Usage/IJSS_tex.tex`

| Historical section/content | Reuse status | Required handling |
|---|---|---|
| Introduction literature review | **Reusable with review** | Retain relevant microgrid distributed-control literature; remove unsupported current-paper claims about deadlines, sharing, or composite guarantees |
| Historical abstract and contribution list | **Not reusable verbatim** | Rewrite around local physical analysis and local public-history indistinguishability |
| `Preliminaries` / MG model / DG model / network power flow | **Reusable as source material** | Translate notation to frozen ES-1--ES-16 and preserve physical/cyber ownership separation |
| Projection operators and RBFNN definitions | **Not reusable** | These modules were pruned from the frozen architecture; do not reintroduce them |
| Historical control objective subsection | **Rewrite** | Replace global restoration, exact sharing, and all-time performance objectives with local-before-exit objectives |
| Error-related scalar transformation | **Reusable after scope restriction** | Use frozen ES-22--ES-40 notation; never infer all-time funnel invariance |
| Voltage recovery controller design | **Reusable selectively** | Preserve controller/notation only if it matches frozen ES-26--ES-29 and ES-62--ES-67; rewrite theorem language to local inequalities |
| Frequency recovery and power distribution | **Split** | Retain frequency-control notation and local frequency analysis; remove active-power-sharing result claims because PO-14 is open |
| Historical RBFNN lemmas and proofs | **Not reusable** | No RBFNN or adaptive projection exists in the frozen controller |
| Historical voltage/frequency theorems | **Not reusable verbatim** | Replace with one local physical theorem supported by PO-16A, PO-02A, PO-03, PO-06--PO-10, PO-13, and PO-07 |
| Historical stability analysis | **Reusable only as proof organization** | Retain Lyapunov component/composite ordering; remove global/invariance/deadline conclusions |
| Historical simulation/HIL result prose | **Not reusable as evidence** | No experiment result may be claimed in the architecture stage; any later evidence must be separately audited against the local theorem |
| Historical conclusion | **Rewrite** | State only the two approved result families and limitations |
| Historical declarations/bibliography | **Review individually** | Preserve format and verified references; remove source-specific claims not supported by the new model |

## 4. Final section hierarchy

### I. Introduction

Proposed subsections:

- `A. Distributed Secondary Control Context`;
- `B. Privacy Problem Under Complete Public-History Observation`;
- `C. Scope of This Paper`;
- `D. Contributions and Explicit Non-Claims`.

The contribution list must contain only:

1. a local closed-loop well-posedness and compact-region comparison result for the frozen secondary controller;
2. a local public-history indistinguishability construction using the Version 2.2 privacy domain, PO-04, and PO-05.

Do not list prescribed-time recovery, active-power sharing, global privacy, or a simultaneous composite theorem as achieved contributions.

### II. System Model and Problem Formulation

Proposed subsections:

- `A. Islanded Microgrid and Droop Model`;
- `B. Electrical and Cyber Graphs`;
- `C. Public/Private Coordination Interface`;
- `D. Passive Observation Map`;
- `E. Local-Before-Exit Problem Statement`.

Reuse frozen ES-1--ES-16 and the reviewed historical model exposition. The public payload and complete history must be stated before any privacy claim. Physical sensor histories and private memory remain outside the adversary observation.

### III. Definitions and Active Assumptions

Proposed subsections:

- `A. Independent and Reconstructed Coordinates`;
- `B. Admissible Open Domain and Bootstrap Region`;
- `C. Definition 1: Closed-Loop Local Solution`;
- `D. Definition 2: Public-History Indistinguishability`;
- `E. Assumption 1: Local Physical and Graph Regularity`;
- `F. Assumption 2: Version 2.2 Privacy-Domain Regularity`.

Only active local assumption clauses may be used in the final theorem statements. Alternative existence and denominator validity must appear as PO-04/PO-05 conclusions, not as assumptions.

### IV. Local Physical Analysis

Proposed subsections:

- `A. Prescribed-Performance Coordinates and Frozen Controller`;
- `B. Local Well-Posedness and First Exit`;
- `C. Command-Rate and Finite Residual Bounds`;
- `D. Voltage and Frequency Component Inequalities`;
- `E. Bootstrap Actuator/Funnel Feasibility`;
- `F. Composite Local Comparison`.

Proof organization follows PO-16A -> PO-03 -> PO-02A, with PO-01/PO-06 supporting PO-08--PO-10, PO-13, and PO-07. The output is local and compact-dependent.

### V. Local Privacy Construction and Observation Equivalence

Proposed subsections:

- `A. Version 2.2 Schedule-Regular Privacy Domain`;
- `B. Public/Private Decomposition and Residual Interface`;
- `C. PO-04: Initial Alternative Construction`;
- `D. PO-05: Post-Seed Denominator Validity and Local Continuation`;
- `E. Equality of the Complete Public History`.

PO-04 must be presented before PO-05. PO-05 must not be written as re-proving the initial/common PO-04 denominator interval. The section stops at the finite-seed or regular-domain boundary.

### VI. Theoretical Results and Proof Chain

This section is a theorem index and dependency synthesis, not a new composite result.

Proposed subsections:

- `A. Local Physical Theorem`;
- `B. Local Public-History Indistinguishability Theorem`;
- `C. Proof-Dependency Summary`;
- `D. Scope Qualifiers`.

The two theorem statements remain logically separate. Do not create a theorem that simultaneously asserts privacy, funnel invariance, deadline recovery, sharing, and global continuation.

### VII. Limitations and Discussion

Required items:

- local-before-exit boundary;
- no PO-02B residual-decay claim;
- PO-11 and PO-16B reserved for future continuation work;
- PO-12 deadline recovery excluded;
- PO-14 active-power sharing excluded;
- PO-15 simultaneous composite theorem excluded;
- passive observation threat model and excluded side channels;
- no post-`T_s` privacy claim;
- distinction between frozen Blueprint target and final manuscript theorem.

### VIII. Conclusion

Summarize only the local physical result and the local public-history result. State limitations directly. Do not restate the historical stronger target as a conclusion.

## 5. Theorem/proof environment mapping

The template's existing theorem environments are retained. The proposed semantic mapping is:

| Environment | Manuscript use |
|---|---|
| `definition` | closed-loop object and public-history indistinguishability |
| `assumption` | active local physical and Version 2.2 privacy-domain clauses |
| `lemma` | decomposition regularity, finite residual interface, or local auxiliary bounds already discharged |
| `theorem` | local physical theorem; local public-history indistinguishability theorem |
| `proof` | only proofs already authorized by the closed POs; no new proof in Task-019 mapping |
| `remark` | scope qualifiers, observation limitations, and frozen-target distinction |
| `proposition/corollary` | do not use for deadline, sharing, or composite claims; reserve for later approved local corollaries |

The equation numbering style and theorem environment declarations remain those of the designated IEEE template.

## 6. Claim gate for each section

| Section | Allowed final claims | Explicitly forbidden claims |
|---|---|---|
| I | motivation and two approved contributions | achieved deadline recovery, sharing, global privacy |
| II | frozen model and observation map | adversary access to private memory/physical sensors |
| III | active local assumptions and domains | alternative existence as an assumption; global invariance assumption |
| IV | local existence, local inequalities, finite PO-02A bound, PO-13 design-region feasibility | global stability, all-time funnel/actuator invariance, ES-51 decay |
| V | local existential public-history equivalence through PO-05 stopping boundary | all-time ES-57, cryptographic secrecy, universal ambiguity |
| VI | two separate local theorems and acyclic proof order | simultaneous composite theorem |
| VII | limitations and open-PO classification | presenting OPEN POs as proved results |
| VIII | bounded local conclusion and privacy conclusion | deadline, sharing, or global conclusion |

## 7. Approval gate before insertion

Before any LaTeX text is inserted, the following must be approved:

1. the exact title and abstract scope;
2. the section/subsection hierarchy in Section 4;
3. the two theorem names and their local quantifier boundaries;
4. the active assumption wording;
5. the decision to keep experiments outside this architecture pass.

Task-019 mapping itself introduces no new equations, states, assumptions, proofs, or theorem claims.

Blueprint Reopen Required: **NO**.

LaTeX insertion started: **NO**.
