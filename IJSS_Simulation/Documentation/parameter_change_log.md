# Simulation Parameter Change Log

## Task-029-B Four-DG Revision

- Current manifest: `f27c2278f5bdb77b`.
- Replaced the superseded three-DG illustrative instance with the required
  four-DG chain.
- Set engineering bases to `310 V`, `50 Hz`, `1000 W`, and `500 var`.
- Added rated active powers `500, 600, 650, 700 W` for the normalized sharing
  diagnostic.
- Added an explicit droop-only interval `[0,5) s`, secondary activation at
  `5 s`, a predefined evaluation marker at `6.30 s`, and a configured `15 s`
  simulation horizon.
- Converted Simulink voltage/frequency scope signals to `V` and `Hz`, and
  added voltage-error (`V`) and frequency-error (`Hz`) scopes.
- Retained the basic-block first-exit stop guard. With the final numerical
  tuple, no exit is detected through the configured `15 s` horizon; this is
  reported only as `t_exit > 15 s` for the selected run.
- Increased the local monitoring box only as needed to retain this selected
  case through the displayed interval; no invariance conclusion is attached.
- Added a visible reactive-load offset, increased the existing voltage damping
  gain, reduced the existing frequency/coordination gains, and accelerated the
  existing privacy wrapper. These parameter-only refinements expose the
  droop-only deviation, smooth the switched restoration, and retain a finite
  `0--0.50 s` privacy witness without changing an equation or state.

These changes implement the requested four-DG scenario and two-stage control
sequence. They are not curve-fitting changes and do not alter frozen equations,
controller structure, assumptions, theorem statements, or proof status.
