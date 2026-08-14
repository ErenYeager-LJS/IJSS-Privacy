# Simulation Parameter Change Log

## Revision 1

- Superseded manifest: `0832d7e5ba038038`
- Superseded manifest after ES-41 initialization repair: `eb0f41998868bdab`
- `k_c^V`: `0.35` -> `0.10`
- `k_c^omega`: `0.30` -> `0.10`
- Reason: with the selected three-node path graph, `lambda_max(L_c)=3`.
  The initial choice put `I-k_c^V L_c` close to the ES-21a singular surface,
  amplifying the algebraically consistent initial command. The replacement is
  separated from all reciprocal Laplacian eigenvalues and preserves the frozen
  controller structure.
- Failed behavior: after enforcing ES-41-consistent initialization, the first
  local event occurred near `0.01065 s`; W1 integration also lost numerical
  regularity.
- Disposition: every output from the superseded manifests is obsolete and must
  be regenerated. This is a parameter-instance correction, not curve-driven
  aesthetic tuning.
