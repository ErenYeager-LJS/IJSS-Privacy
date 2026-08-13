from __future__ import annotations

import numpy as np


def power_flow(V, delta, params):
    B = np.asarray(params["network"]["electrical_susceptance"], dtype=float)
    p = np.asarray(params["plant"]["P_load"], dtype=float).copy()
    q = np.asarray(params["plant"]["Q_load"], dtype=float).copy()
    n = len(V)
    for i in range(n):
        for k in range(n):
            if B[i, k] == 0:
                continue
            angle = delta[i] - delta[k]
            p[i] += V[i] * V[k] * B[i, k] * np.sin(angle)
            q[i] += V[i] ** 2 * B[i, k] - V[i] * V[k] * B[i, k] * np.cos(angle)
    return p, q
