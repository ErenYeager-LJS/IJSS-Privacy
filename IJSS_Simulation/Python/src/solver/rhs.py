from __future__ import annotations

from controller.secondary import controller
from model.plant import plant_derivative
from model.state_layout import pack, unpack
from privacy.wrapper import wrapper_derivative


def evaluate(t, x, params):
    n=int(params["network"]["N"]); s=unpack(x,n); ctl=controller(t,s,params)
    wr=wrapper_derivative(ctl["cV"],ctl["cW"],s,params)
    hatV=(s["pV"]+s["qV"])/2; hatW=(s["pW"]+s["qW"])/2
    plant=plant_derivative(t,s,ctl,hatV,hatW,params)
    dx={"V":plant["V"],"Vdot":plant["Vdot"],"omega":plant["omega"],"delta":plant["delta"],
        "pV":wr["pV"],"qV":wr["qV"],"pW":wr["pW"],"qW":wr["qW"]}
    return pack(dx,n),s,ctl,wr,plant


def rhs(t,x,params): return evaluate(t,x,params)[0]
