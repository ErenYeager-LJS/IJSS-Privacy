# Figure Caption Drafts

> Captions are written for the frozen Task-029-B/Task-029-C evidence package.
> They do not modify the tracked manuscript or the validated figures.

## F1. Voltage Restoration

**Fig. 1. Voltage restoration in the selected four-DG numerical case.**
(a) DG1--DG4 voltage trajectories relative to the $310$ V reference;
(b) voltage tracking errors; and (c) PPC utilization. Primary droop control
operates before the secondary controller is activated at $5.00$ s. The
observed restoration time is $5.19$ s under the $\pm0.05$ V enter-and-remain
criterion, the maximum voltage deviation is $0.3720$ V, and the maximum PPC
utilization is $0.0150$. The vertical marker at $6.30$ s is the prescribed
settling-time evaluation marker. No admissibility exit was detected before the
$15$ s endpoint in this selected run; this observation is not an invariance or
global-continuation claim.

## F2. Frequency Restoration

**Fig. 2. Frequency restoration in the selected four-DG numerical case.**
(a) DG1--DG4 frequency trajectories relative to the $50$ Hz reference;
(b) frequency tracking errors with the $\pm0.005$ Hz restoration band; and
(c) PPC utilization. Secondary control is activated at $5.00$ s. The observed
restoration time is $5.32$ s, the maximum frequency deviation is $0.0350$ Hz,
and the maximum PPC utilization is $0.15335$. The response satisfies the
numerical criterion before the $6.30$ s evaluation marker. The plot does not
establish a prescribed-time recovery theorem or all-time funnel invariance.

## F3. Active Power Sharing Preservation

**Fig. 3. Active power sharing preservation during secondary restoration.**
(a) DG1--DG4 active-power trajectories; (b) normalized power-allocation
trajectories; and (c) sharing error. The final sharing error is $0.0225442$.
The selected case indicates that secondary voltage/frequency restoration does
not destroy the displayed droop-based proportional allocation. The nonzero
error is retained explicitly; perfect sharing and a general active-power
sharing theorem are not claimed.

## F4. Public-History Indistinguishability

**Fig. 4. Observer-visible public-history comparison for the selected privacy
witness.** Nominal and non-nominal public coordination histories are compared
only over $0\leq t\leq0.50$ s under the declared passive observation map. The
public-history difference norm is zero on this interval. Private substates,
private weights, locally reconstructed commands, and raw physical states are
not observer-visible signals in this figure. The result is a finite-interval,
existence-based observation-equivalence demonstration, not cryptographic,
differential, or all-time privacy.

## F5. Distinct Internal Realizations

**Fig. 5. Distinct hidden internal realizations associated with the identical
public history in Fig. 4.** The panels retain the private $q^V$ difference,
the scaled frequency-side difference $10^{12}\Delta q^\omega$, protected-agent
differences, and the private-weight difference. The raw $q^\omega$ values are
preserved in the corresponding CSV. These quantities are internal evidence and
are not available to the passive observer. Their purpose is to demonstrate
distinct voltage- and frequency-side hidden realizations, not to compare
privacy strength through their absolute magnitudes.

## Caption Consistency Check

| Figure | Required metric or boundary | Caption status |
|---|---|---|
| F1 | `5.19 s`, `0.3720 V`, PPC `<1`, no exit before `15 s` | Included |
| F2 | `5.32 s`, `0.0350 Hz`, `+/-0.005 Hz`, PPC `<1` | Included |
| F3 | Final sharing error `0.0225442`, non-exact interpretation | Included |
| F4 | Public difference norm `0`, window `0--0.50 s` | Included |
| F5 | `q^V`, scaled `q^omega`, protected-agent, private-weight differences | Included |
