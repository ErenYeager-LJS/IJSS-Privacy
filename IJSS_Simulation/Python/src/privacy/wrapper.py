from __future__ import annotations

import numpy as np


def gain(z, gamma):
    return np.where(np.abs(z) <= gamma, 1.0, gamma/np.maximum(np.abs(z), 1e-300))


def wrapper_derivative(cV, cW, state, params, weights=None):
    pr = params["privacy"]
    zV=state["pV"]-state["qV"]; zW=state["pW"]-state["qW"]
    gV=gain(zV,float(pr["gamma_V"])); gW=gain(zW,float(pr["gamma_omega"]))
    if weights is None:
        w12V=np.asarray(pr["w12_V"],float); w21V=np.asarray(pr["w21_V"],float)
        w12W=np.asarray(pr["w12_omega"],float); w21W=np.asarray(pr["w21_omega"],float)
    else: w12V,w21V,w12W,w21W=weights
    lv=np.asarray(pr["lambda_V"],float); lw=np.asarray(pr["lambda_omega"],float)
    return {"pV":lv*(cV-state["pV"])-w21V*gV*zV,
            "qV":lv*(cV-state["qV"])+w12V*zV,
            "pW":lw*(cW-state["pW"])-w21W*gW*zW,
            "qW":lw*(cW-state["qW"])+w12W*zW,
            "zV":zV,"zW":zW,"gV":gV,"gW":gW,
            "weights":(w12V,w21V,w12W,w21W)}
