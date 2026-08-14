# Python--Simulink Validation

- Manifest: `f27c2278f5bdb77b`
- Compared runs: `P1_RUN_001` and `SIMULINK_P1_RUN_001`
- Compared variables: all 32 independent states
- Configured horizon: `15 s`
- Actual retained stopping time: Python `15 s`; Simulink `15 s`
- Compared strict pre-exit interval: `0 <= t <= 15 s`
- Stop-boundary sample excluded: `no`
- Global maximum absolute error: `5.855666e-10`
- Global RMS error: `2.925515e-11`
- Global maximum normalized diagnostic: `1.537581e+00`
- Stopping-time difference: `0.000000e+00 s`
- Pre-frozen implementation threshold: `1.000000e-05` absolute
- Verdict: `PASS`

The comparison establishes implementation consistency only. It does not enlarge the local theorem scope.
