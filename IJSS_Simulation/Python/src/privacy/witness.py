from __future__ import annotations

import numpy as np

from privacy.wrapper import gain


def forced_weights(t, nominal_state, nominal_ctl, nominal_wr, alt_state, alt_ctl, qdot_alt, params):
    pr=params["privacy"]
    out=[]
    for suffix,pkey,qkey,gamma,lkey in (("V","pV","qV","gamma_V","lambda_V"),("omega","pW","qW","gamma_omega","lambda_omega")):
        ckey="cV" if suffix=="V" else "cW"; zkey="zV" if suffix=="V" else "zW"
        lam=np.asarray(pr[lkey],float); z=nominal_wr[zkey]; g=nominal_wr["gV" if suffix=="V" else "gW"]
        w21=nominal_wr["weights"][1 if suffix=="V" else 3]
        zp=alt_state[pkey]-alt_state[qkey]; gp=gain(zp,float(pr[gamma]))
        denom21=gp*zp; denom12=zp
        w21p=(lam*(alt_ctl[ckey]-nominal_ctl[ckey])+w21*g*z)/denom21
        w12p=(qdot_alt[qkey]-lam*(alt_ctl[ckey]-alt_state[qkey]))/denom12
        out.extend((w12p,w21p))
    return tuple(out)
