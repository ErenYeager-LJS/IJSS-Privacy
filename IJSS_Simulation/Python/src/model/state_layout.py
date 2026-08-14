from __future__ import annotations

import numpy as np


FIELDS = ("V", "Vdot", "omega", "delta", "pV", "qV", "pW", "qW")


def slices(n):
    return {name: slice(i * n, (i + 1) * n) for i, name in enumerate(FIELDS)}


def unpack(x, n):
    s = slices(n)
    return {name: np.asarray(x[s[name]]) for name in FIELDS}


def pack(parts, n):
    return np.concatenate([np.asarray(parts[name], dtype=float) for name in FIELDS])
