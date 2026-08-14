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
    secondary_initially_enabled = float(params.get("scenario", {}).get("secondary_activation_s", 0.0)) <= 0.0
    if not secondary_initially_enabled:
        return pack({**base,"pV":offV,"qV":-offV,"pW":offW,"qW":-offW},n)

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
    switch=float(params.get("scenario",{}).get("secondary_activation_s",0.0))
    segments=[]; current=x0; event_time=None
    bounds=[0.0]+([switch] if 0<switch<solcfg["horizon_P1"] else [])+[float(solcfg["horizon_P1"])]
    for left,right in zip(bounds[:-1],bounds[1:]):
        mask=(grid>=left)&(grid<=right)
        segment_grid=grid[mask]
        sol=solve_ivp(lambda t,x:rhs(t,x,params),(left,right),current,t_eval=segment_grid,events=ev,
                      rtol=solcfg["rtol"],atol=solcfg["atol"],max_step=solcfg["max_step"],dense_output=True)
        if not sol.success: raise RuntimeError(sol.message)
        segments.append(sol); current=sol.y[:,-1]
        if len(sol.t_events[0]): event_time=float(sol.t_events[0][0]); break
    times=[]; states=[]
    for k,segment in enumerate(segments):
        start=1 if k else 0; times.append(segment.t[start:]); states.append(segment.y[:,start:])
    t_all=np.concatenate(times); x_all=np.concatenate(states,axis=1)
    np.savez_compressed(raw/"P1_RUN_001.npz",t=t_all,x=x_all,manifest_id=params["manifest_id"])
    ds=[diagnostics(t,x_all[:,i],params) for i,t in enumerate(t_all)]
    audit={"run_id":"P1_RUN_001","manifest_id":params["manifest_id"],"success":sol.success,"event_time":event_time,
           "minimum_margin":min(min(d["margins"].values()) for d in ds),"python":platform.python_version(),
           "solver":"scipy.solve_ivp/RK45 segmented at secondary activation","rtol":solcfg["rtol"],"atol":solcfg["atol"],"max_step":solcfg["max_step"]}
    write_json(out/"manifests"/"P1_RUN_001.json",audit)
    class CombinedSolution:
        t=t_all; y=x_all; success=True
        def sol(self,t):
            for segment in segments:
                if segment.t[0]-1e-12<=t<=segment.t[-1]+1e-12: return segment.sol(t)
            return segments[-1].sol(t)
    return CombinedSolution(),ds,params,audit


if __name__=="__main__":
    _,_,_,a=run(); print(json.dumps(a,indent=2))
