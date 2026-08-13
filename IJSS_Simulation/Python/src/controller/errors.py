from __future__ import annotations

import numpy as np

from model.graphs import graph_data


def errors(V, omega, pV, pW, params):
    _, L, b = graph_data(params)
    e0v = V - float(params["plant"]["V_ref"])
    e0w = omega - float(params["plant"]["omega_ref"])
    return e0v, e0w, b * e0v + L @ pV, b * e0w + L @ pW
