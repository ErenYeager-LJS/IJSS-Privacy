from __future__ import annotations

from controller.secondary import controller
from model.plant import plant_derivative
from model.state_layout import pack, unpack
from privacy.wrapper import wrapper_derivative


def evaluate(t, x, params):
    n=int(params["network"]["N"]); s=unpack(x,n); ctl=controller(t,s,params)
    enabled = float(t >= float(params.get("scenario", {}).get("secondary_activation_s", 0.0)))
    cV = enabled*ctl["cV"]; cW = enabled*ctl["cW"]
    wr=wrapper_derivative(cV,cW,s,params)
    hatV=enabled*(s["pV"]+s["qV"])/2; hatW=enabled*(s["pW"]+s["qW"])/2
    plant=plant_derivative(t,s,ctl,hatV,hatW,params)
    dx={"V":plant["V"],"Vdot":plant["Vdot"],"omega":plant["omega"],"delta":plant["delta"],
        "pV":wr["pV"],"qV":wr["qV"],"pW":wr["pW"],"qW":wr["qW"]}
    ctl={**ctl,"cV_applied":cV,"cW_applied":cW,"secondary_enabled":enabled}
    return pack(dx,n),s,ctl,wr,plant


def rhs(t,x,params): return evaluate(t,x,params)[0]
