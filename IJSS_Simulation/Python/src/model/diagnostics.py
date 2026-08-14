from __future__ import annotations

import numpy as np

from solver.events import margins
from solver.rhs import evaluate


def diagnostics(t,x,params):
    _,s,c,w,p=evaluate(t,x,params)
    zV=w["zV"]; zW=w["zW"]
    targetV=c.get("cV_applied",c["cV"]); targetW=c.get("cW_applied",c["cW"])
    rV=(s["pV"]+s["qV"])/2-targetV; rW=(s["pW"]+s["qW"])/2-targetW
    Vcl=.5*(np.sum(c["ppcV"][3]**2+c["chiV"]**2)+np.sum(c["ppcW"][3]**2)+np.sum(zV**2+rV**2+zW**2+rW**2))
    return {**s,**c,"zV":zV,"zW":zW,"rV":rV,"rW":rW,"uV":targetV+rV,"uW":targetW+rW,
            "RV":p["RV"],"RW":p["RW"],"Vcl":Vcl,"margins":margins(t,x,params)}
