from __future__ import annotations

import numpy as np

from solver.rhs import evaluate


def margins(t,x,params):
    _,s,c,w,_=evaluate(t,x,params); d=params["domain"]
    vals={
      "funnel_V":float(np.min(1-np.abs(c["ppcV"][2]))),
      "funnel_omega":float(np.min(1-np.abs(c["ppcW"][2]))),
      "V_domain":float(min(np.min(s["V"]-d["V"][0]),np.min(d["V"][1]-s["V"]))),
      "Vdot_domain":float(d["Vdot_abs"]-np.max(np.abs(s["Vdot"]))),
      "omega_domain":float(d["omega_abs"]-np.max(np.abs(s["omega"]))),
      "delta_domain":float(d["delta_abs"]-np.max(np.abs(s["delta"]))),
      "K0":float(d["state_abs_K0"]-np.max(np.abs(x))),
      "actuator_V":float(d["actuator_abs_V"]-np.max(np.abs((s["pV"]+s["qV"])/2))),
      "actuator_omega":float(d["actuator_abs_omega"]-np.max(np.abs((s["pW"]+s["qW"])/2))),
    }
    return vals


def event(t,x,params): return min(margins(t,x,params).values())
event.terminal=True; event.direction=-1
