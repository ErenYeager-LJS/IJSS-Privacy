from __future__ import annotations

import numpy as np

from solver.events import margins
from solver.rhs import evaluate


def diagnostics(t,x,params):
    _,s,c,w,p=evaluate(t,x,params)
    zV=w["zV"]; zW=w["zW"]; rV=(s["pV"]+s["qV"])/2-c["cV"]; rW=(s["pW"]+s["qW"])/2-c["cW"]
    Vcl=.5*(np.sum(c["ppcV"][3]**2+c["chiV"]**2)+np.sum(c["ppcW"][3]**2)+np.sum(zV**2+rV**2+zW**2+rW**2))
    return {**s,**c,"zV":zV,"zW":zW,"rV":rV,"rW":rW,"uV":c["cV"]+rV,"uW":c["cW"]+rW,
            "RV":p["RV"],"RW":p["RW"],"Vcl":Vcl,"margins":margins(t,x,params)}
