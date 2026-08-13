from __future__ import annotations

import json, platform, subprocess, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT, load_parameters, write_json
from controller.secondary import controller
from model.diagnostics import diagnostics
from model.state_layout import pack
from solver.events import event
from solver.rhs import rhs


def initial_state(params):
    n=int(params["network"]["N"]); ini=params["initial"]
    base={k:np.asarray(ini[k],float) for k in ("V","Vdot","omega","delta")}
    offV=np.asarray(ini["public_offset_V"],float); offW=np.asarray(ini["public_offset_omega"],float)
    def consistency(public):
        pV=public[:n]; pW=public[n:]
        provisional={**base,"pV":pV,"qV":pV,"pW":pW,"qW":pW}
        c0=controller(0,provisional,params)
        return np.r_[pV-c0["cV"]-offV,pW-c0["cW"]-offW]
    solved=root(consistency,np.r_[offV,offW])
    if not solved.success or np.linalg.norm(consistency(solved.x),np.inf)>1e-10:
        raise RuntimeError("Failed to solve ES-41-consistent public initialization")
    pV=solved.x[:n]; pW=solved.x[n:]
    provisional={**base,"pV":pV,"qV":pV,"pW":pW,"qW":pW}; c0=controller(0,provisional,params)
    state={**base,"pV":pV,"qV":2*c0["cV"]-pV,"pW":pW,"qW":2*c0["cW"]-pW}
    return pack(state,n)


def run():
    params=load_parameters(); out=ROOT/"Python"/"output"; raw=out/"raw"; raw.mkdir(parents=True,exist_ok=True)
    x0=initial_state(params); solcfg=params["solver"]; grid=np.arange(0,solcfg["horizon_P1"]+solcfg["output_step"]/2,solcfg["output_step"])
    ev=lambda t,x:event(t,x,params); ev.terminal=True; ev.direction=-1
    sol=solve_ivp(lambda t,x:rhs(t,x,params),(0,solcfg["horizon_P1"]),x0,t_eval=grid,events=ev,
                  rtol=solcfg["rtol"],atol=solcfg["atol"],max_step=solcfg["max_step"],dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    np.savez_compressed(raw/"P1_RUN_001.npz",t=sol.t,x=sol.y,manifest_id=params["manifest_id"])
    event_time=float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
    ds=[diagnostics(t,sol.y[:,i],params) for i,t in enumerate(sol.t)]
    audit={"run_id":"P1_RUN_001","manifest_id":params["manifest_id"],"success":sol.success,"event_time":event_time,
           "minimum_margin":min(min(d["margins"].values()) for d in ds),"python":platform.python_version(),
           "solver":"scipy.solve_ivp/RK45","rtol":solcfg["rtol"],"atol":solcfg["atol"],"max_step":solcfg["max_step"]}
    write_json(out/"manifests"/"P1_RUN_001.json",audit)
    return sol,ds,params,audit


if __name__=="__main__":
    _,_,_,a=run(); print(json.dumps(a,indent=2))
