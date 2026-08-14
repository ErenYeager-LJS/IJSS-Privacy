from __future__ import annotations

import json, sys
import copy
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT, load_parameters, write_json
from controller.secondary import controller
from model.plant import plant_derivative
from model.state_layout import pack, unpack
from privacy.witness import forced_weights
from privacy.wrapper import wrapper_derivative
from solver.rhs import evaluate, rhs
from solver.run_physical import initial_state


def run():
    params=load_parameters(); n=int(params["network"]["N"]); cfg=params["solver"]
    params=copy.deepcopy(params); params["scenario"]["secondary_activation_s"]=0.0
    t1=float(cfg["horizon_W1"]); grid=np.arange(0,t1+cfg["output_step"]/2,cfg["output_step"])
    x0=initial_state(params)
    nominal=solve_ivp(lambda t,x:rhs(t,x,params),(0,t1),x0,rtol=cfg["rtol"],atol=cfg["atol"],
                      max_step=cfg["max_step"],dense_output=True)
    if not nominal.success: raise RuntimeError(nominal.message)
    sn0=unpack(x0,n); ca0=controller(0,sn0,params)
    physical0=np.concatenate([sn0[k] for k in ("V","Vdot","omega","delta")])
    physical0[0]+=float(params["witness"]["physical_voltage_perturbation"])
    sa0={k:physical0[i*n:(i+1)*n] for i,k in enumerate(("V","Vdot","omega","delta"))}
    sa0.update({"pV":sn0["pV"],"qV":sn0["qV"].copy(),"pW":sn0["pW"],"qW":sn0["qW"].copy()})
    cpa0=controller(0,sa0,params)
    sa0["qV"]=2*cpa0["cV"]-sa0["pV"]; sa0["qW"]=2*cpa0["cW"]-sa0["pW"]
    y0=np.concatenate([physical0,sa0["qV"],sa0["qW"]])

    def assemble(t,y):
        xn=nominal.sol(t); _,sn,cn,wn,_=evaluate(t,xn,params); dn=rhs(t,xn,params); dsn=unpack(dn,n)
        sa={k:y[i*n:(i+1)*n] for i,k in enumerate(("V","Vdot","omega","delta"))}
        sa["pV"]=sn["pV"]; sa["pW"]=sn["pW"]
        sa["qV"]=y[4*n:5*n]; sa["qW"]=y[5*n:6*n]
        ca=controller(t,sa,params)
        lamV=np.asarray(params["privacy"]["lambda_V"],float); lamW=np.asarray(params["privacy"]["lambda_omega"],float)
        targetV=np.asarray(params["privacy"]["w12_V"],float); targetW=np.asarray(params["privacy"]["w12_omega"],float)
        qdot={"qV":lamV*(ca["cV"]-sa["qV"])+targetV*(sa["pV"]-sa["qV"]),
              "qW":lamW*(ca["cW"]-sa["qW"])+targetW*(sa["pW"]-sa["qW"])}
        weights=forced_weights(t,sn,cn,wn,sa,ca,qdot,params)
        hatV=(sa["pV"]+sa["qV"])/2; hatW=(sa["pW"]+sa["qW"])/2
        pa=plant_derivative(t,sa,ca,hatV,hatW,params)
        return np.concatenate([pa[k] for k in ("V","Vdot","omega","delta")]+[qdot["qV"],qdot["qW"]]),sn,cn,wn,sa,ca,weights,qdot

    def alt_rhs(t,y): return assemble(t,y)[0]
    alt=solve_ivp(alt_rhs,(0,t1),y0,rtol=cfg["rtol"],atol=cfg["atol"],max_step=cfg["max_step"],dense_output=True)
    if not alt.success: raise RuntimeError(alt.message)
    records=[]; lower=float(params["privacy"]["weight_lower"]); upper=float(params["privacy"]["weight_upper"])
    stop=t1; stop_id="finite_seed_end"
    for t in grid:
        dy,sn,cn,wn,sa,ca,weights,qd=assemble(t,alt.sol(t))
        allw=np.concatenate(weights); z=np.concatenate([sa["pV"]-sa["qV"],sa["pW"]-sa["qW"]])
        margins={"weight_lower":float(np.min(allw-lower)),"weight_upper":float(np.min(upper-allw)),
                 "denominator":float(np.min(np.abs(z))),"funnel_V":float(np.min(1-np.abs(ca["ppcV"][2]))),
                 "funnel_omega":float(np.min(1-np.abs(ca["ppcW"][2])))}
        bad=[(k,v) for k,v in margins.items() if v<=0]
        if bad: stop=float(t); stop_id=min(bad,key=lambda kv:kv[1])[0]; break
        records.append((float(t),sn,sa,cn,ca,weights,margins))
    if len(records)<2: raise RuntimeError(f"Witness interval collapsed at {stop}: {stop_id}")
    raw=ROOT/"Python"/"output"/"raw"; raw.mkdir(parents=True,exist_ok=True)
    times=np.array([r[0] for r in records]); np.savez_compressed(raw/"W1_RUN_001.npz",t=times,
        nominal=np.stack([nominal.sol(t) for t in times],axis=1),alternative=np.stack([alt.sol(t) for t in times],axis=1),manifest_id=params["manifest_id"])
    public_res=max(float(np.max(np.abs(r[1]["pV"]-r[2]["pV"]))) for r in records)
    public_res=max(public_res,max(float(np.max(np.abs(r[1]["pW"]-r[2]["pW"]))) for r in records))
    report={"run_id":"W1_RUN_001","manifest_id":params["manifest_id"],"success":True,"tau_priv":stop,
            "stopping_event":stop_id,"public_history_residual":public_res,
            "protected_difference_V":float(cpa0["cV"][0]-ca0["cV"][0]),"samples":len(records)}
    write_json(ROOT/"Python"/"output"/"manifests"/"W1_RUN_001.json",report)
    return records,params,report


if __name__=="__main__":
    _,_,r=run(); print(json.dumps(r,indent=2))
