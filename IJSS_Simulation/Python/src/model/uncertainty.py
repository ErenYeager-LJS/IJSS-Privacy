from __future__ import annotations

import numpy as np


def uncertainty(t, params):
    av = np.asarray(params["plant"]["uncertainty_amplitude_V"], dtype=float)
    aw = np.asarray(params["plant"]["uncertainty_amplitude_omega"], dtype=float)
    return av * np.sin(0.7 * t), aw * np.cos(0.5 * t)
