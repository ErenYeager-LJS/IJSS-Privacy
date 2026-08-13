from __future__ import annotations

import numpy as np


def graph_data(params):
    A = np.asarray(params["network"]["cyber_adjacency"], dtype=float)
    b = np.asarray(params["network"]["pinning"], dtype=float)
    if not np.allclose(A, A.T) or np.any(A < 0):
        raise ValueError("Cyber adjacency must be symmetric and nonnegative")
    L = np.diag(A.sum(axis=1)) - A
    if np.linalg.matrix_rank(L + np.diag(b)) != len(b):
        raise ValueError("Pinned cyber matrix is singular")
    return A, L, b
