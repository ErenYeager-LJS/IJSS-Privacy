from __future__ import annotations

import numpy as np

from controller.errors import errors
from controller.ppc import frequency_alpha, voltage_alpha
from model.power_flow import power_flow


def controller(t, state, params):
    V, Vdot, omega, delta = (state[k] for k in ("V", "Vdot", "omega", "delta"))
    P, Q = power_flow(V, delta, params)
    e0v, e0w, ev, ew = errors(V, omega, state["pV"], state["pW"], params)
    plant = params["plant"]
    tauP = np.asarray(plant["tau_P"], float); tauQ = np.asarray(plant["tau_Q"], float)
    kP = np.asarray(plant["k_P"], float); kQ = np.asarray(plant["k_Q"], float)
    kV = np.asarray(plant["k_V"], float)
    Fw = (-(omega-float(plant["omega_ref"]))-kP*(P-np.asarray(plant["P_d"],float)))/tauP
    Fv = (-(tauQ+kV)*Vdot-(V-float(plant["V_ref"]))
          -kQ*(Q-np.asarray(plant["Q_d"],float)))/(tauQ*kV)
    av, dav, chi, ppcv = voltage_alpha(t, e0v, Vdot, params)
    aw, ppcw = frequency_alpha(t, e0w, params)
    ctl = params["controller"]
    cV = tauQ*kV*(Fv-dav+float(ctl["k2_V"])*chi+ppcv[4]*ppcv[3])+float(ctl["kc_V"])*ev
    cW = tauP*(Fw-aw)+float(ctl["kc_omega"])*ew
    return {"P":P,"Q":Q,"e0V":e0v,"e0W":e0w,"eV":ev,"eW":ew,"FV":Fv,"FW":Fw,
            "alphaV":av,"alphaW":aw,"chiV":chi,"cV":cV,"cW":cW,"ppcV":ppcv,"ppcW":ppcw}
