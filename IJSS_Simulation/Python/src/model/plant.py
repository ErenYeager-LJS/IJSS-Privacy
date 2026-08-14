from __future__ import annotations

import numpy as np

from model.uncertainty import uncertainty


def plant_derivative(t, state, ctl, uV, uW, params):
    tauP=np.asarray(params["plant"]["tau_P"],float)
    tauQ=np.asarray(params["plant"]["tau_Q"],float)
    kV=np.asarray(params["plant"]["k_V"],float)
    RV,RW=uncertainty(t,params)
    return {"V":state["Vdot"], "Vdot":ctl["FV"]-uV/(tauQ*kV)+RV,
            "omega":ctl["FW"]-uW/tauP+RW, "delta":state["omega"], "RV":RV,"RW":RW}
