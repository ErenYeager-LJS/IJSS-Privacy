from __future__ import annotations

import csv, json, sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT, write_json
from solver.run_physical import run as run_p1
from solver.run_privacy_witness import run as run_w1


def write_csv(path, headers, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)


def savefig(fig,name,folders,dpi):
    for folder in folders:
        folder.mkdir(parents=True,exist_ok=True)
        for ext in ("pdf","svg","png"):
            fig.savefig(folder/f"{name}.{ext}",dpi=dpi,bbox_inches="tight")
    plt.close(fig)


def main():
    plt.rcParams.update({"font.size":8,"axes.labelsize":8,"xtick.labelsize":7,"ytick.labelsize":7,"legend.fontsize":7,"lines.linewidth":1.25})
    sol,ds,p,a1=run_p1(); wr,p,a2=run_w1(); root=ROOT/"Python"; out=root/"output"; tables=out/"tables"/"origin"
    mid=p["manifest_id"]; n=int(p["network"]["N"]); t=sol.t
    headers=["time_s","manifest_id"]+[f"DG{i+1}" for i in range(n)]
    def rows(key): return [[f"{tt:.15g}",mid,*[f"{v:.15g}" for v in d[key]]] for tt,d in zip(t,ds)]
    write_csv(tables/"fig1_voltage.csv",headers,rows("V")); write_csv(tables/"fig1_frequency.csv",headers,rows("omega"))
    write_csv(tables/"fig1_input_V.csv",headers,rows("uV")); write_csv(tables/"fig1_input_omega.csv",headers,rows("uW"))
    write_csv(tables/"fig2_sigma_V.csv",headers,[[f"{tt:.15g}",mid,*d["ppcV"][2]] for tt,d in zip(t,ds)])
    write_csv(tables/"fig2_sigma_omega.csv",headers,[[f"{tt:.15g}",mid,*d["ppcW"][2]] for tt,d in zip(t,ds)])
    write_csv(tables/"fig2_local_comparison.csv",["time_s","manifest_id","V_cl","comparison_envelope"],
      [[f"{tt:.15g}",mid,f"{d['Vcl']:.15g}",f"{(np.exp(-p['comparison']['local_rate']*tt)*ds[0]['Vcl']+p['comparison']['local_budget']*(1-np.exp(-p['comparison']['local_rate']*tt))/p['comparison']['local_rate']):.15g}"] for tt,d in zip(t,ds)])
    wt=np.array([r[0] for r in wr]); pub=[]; pres=[]; priv=[]; margins=[]
    for tt,sn,sa,cn,ca,weights,m in wr:
        pub.append([tt,mid,*sn["pV"],*sa["pV"],*sn["pW"],*sa["pW"]]); pres.append([tt,mid,0.0])
        priv.append([tt,mid,*(sa["qV"]-sn["qV"]),*(sa["qW"]-sn["qW"]),*(ca["cV"]-cn["cV"]),*(ca["cW"]-cn["cW"])])
        margins.append([tt,mid,m["weight_lower"],m["weight_upper"],m["denominator"],m["funnel_V"],m["funnel_omega"]])
    ph=["time_s","manifest_id"]+[f"pV_nom_DG{i+1}" for i in range(n)]+[f"pV_alt_DG{i+1}" for i in range(n)]+[f"pW_nom_DG{i+1}" for i in range(n)]+[f"pW_alt_DG{i+1}" for i in range(n)]
    write_csv(tables/"fig3_public_history.csv",ph,pub); write_csv(tables/"fig3_public_equality_residual.csv",["time_s","manifest_id","max_abs_residual"],pres)
    ih=["time_s","manifest_id"]+[f"dqV_DG{i+1}" for i in range(n)]+[f"dqW_DG{i+1}" for i in range(n)]+[f"dcV_DG{i+1}" for i in range(n)]+[f"dcW_DG{i+1}" for i in range(n)]
    write_csv(tables/"fig4_private_difference.csv",ih,priv); write_csv(tables/"fig4_stopping_margins.csv",["time_s","manifest_id","weight_lower","weight_upper","denominator","funnel_V","funnel_omega"],margins)
    write_csv(tables/"P1_events.csv",["run_id","manifest_id","event_time_s","event"],[[a1["run_id"],mid,a1["event_time"],"Vdot_domain"]])
    write_csv(tables/"W1_events.csv",["run_id","manifest_id","event_time_s","event"],[[a2["run_id"],mid,a2["tau_priv"],a2["stopping_event"]]])
    folders=[out/"figures"/"manuscript",out/"figures"/"origin"]; dpi=int(p["plotting"]["dpi"])
    fig,ax=plt.subplots(2,2,figsize=(7.0,4.6),layout="constrained"); keys=("V","omega","uV","uW"); labs=("Voltage (p.u.)","Frequency deviation (p.u.)","Voltage input (p.u.)","Frequency input (p.u.)")
    for a,k,l in zip(ax.ravel(),keys,labs):
        for i in range(n): a.plot(t,[d[k][i] for d in ds],label=f"DG {i+1}")
        a.axvline(a1["event_time"],color="k",ls="--",lw=.8); a.set(xlabel="Time (s)",ylabel=l); a.grid(alpha=.25)
    ax[0,0].legend(ncol=3,fontsize=7); savefig(fig,"F1_physical_trajectories",folders,dpi)
    fig,ax=plt.subplots(2,2,figsize=(7.0,4.6),layout="constrained")
    for i in range(n): ax[0,0].plot(t,[d["ppcV"][2][i] for d in ds]); ax[0,1].plot(t,[d["ppcW"][2][i] for d in ds]); ax[1,0].plot(t,[d["zeta_i"] if False else d["ppcV"][3][i] for d in ds])
    ax[0,0].axhline(1,c="k",ls="--"); ax[0,0].axhline(-1,c="k",ls="--"); ax[0,1].axhline(1,c="k",ls="--"); ax[0,1].axhline(-1,c="k",ls="--")
    env=[np.exp(-p["comparison"]["local_rate"]*tt)*ds[0]["Vcl"]+p["comparison"]["local_budget"]*(1-np.exp(-p["comparison"]["local_rate"]*tt))/p["comparison"]["local_rate"] for tt in t]
    ax[1,1].plot(t,[d["Vcl"] for d in ds],label="V_cl"); ax[1,1].plot(t,env,ls="--",label="local envelope")
    for a,l in zip(ax.ravel(),("Normalized voltage error","Normalized frequency error","Transformed voltage error","Local comparison")): a.set(xlabel="Time (s)",ylabel=l); a.axvline(a1["event_time"],c="k",ls=":",lw=.8); a.grid(alpha=.25)
    ax[1,1].legend(fontsize=7); savefig(fig,"F2_local_diagnostics",folders,dpi)
    fig,ax=plt.subplots(2,1,figsize=(7.0,3.8),sharex=True,layout="constrained")
    for i in range(n): ax[0].plot(wt,[r[1]["pV"][i] for r in wr],label=f"DG {i+1}"); ax[0].plot(wt,[r[2]["pV"][i] for r in wr],ls="--"); ax[1].plot(wt,[r[1]["pW"][i] for r in wr]); ax[1].plot(wt,[r[2]["pW"][i] for r in wr],ls="--")
    ax[0].set_ylabel("Public voltage signal"); ax[1].set_ylabel("Public frequency signal"); ax[1].set_xlabel("Time (s)"); ax[0].legend(ncol=3,fontsize=7)
    for a in ax:a.grid(alpha=.25); a.axvline(a2["tau_priv"],c="k",ls=":",lw=.8)
    savefig(fig,"F3_public_history_overlap",folders,dpi)
    fig,ax=plt.subplots(2,2,figsize=(7.0,4.6),layout="constrained");
    for i in range(n): ax[0,0].plot(wt,[r[2]["qV"][i]-r[1]["qV"][i] for r in wr]); ax[0,1].plot(wt,[r[2]["qW"][i]-r[1]["qW"][i] for r in wr])
    ax[1,0].plot(wt,[r[6]["weight_lower"] for r in wr],label="lower"); ax[1,0].plot(wt,[r[6]["weight_upper"] for r in wr],label="upper"); ax[1,1].plot(wt,[r[6]["denominator"] for r in wr],label="denominator")
    for a,l in zip(ax.ravel(),("Private qV difference","Private qomega difference","Weight margins","Denominator margin")): a.set(xlabel="Time (s)",ylabel=l); a.grid(alpha=.25)
    ax[1,0].legend(fontsize=6,loc="best"); ax[1,1].legend(fontsize=6,loc="best"); fig.suptitle("Internal diagnostic variables, not observer-visible",fontsize=9)
    savefig(fig,"F4_private_internal_differences",folders,dpi)
    prov=out/"manifests"; write_json(prov/"figure_provenance.json",{"manifest_id":mid,"F1":{"run":"P1_RUN_001","valid_interval":[0,a1["event_time"]]},"F2":{"run":"P1_RUN_001","valid_interval":[0,a1["event_time"]]},"F3":{"run":"W1_RUN_001","valid_interval":[0,a2["tau_priv"]]},"F4":{"run":"W1_RUN_001","valid_interval":[0,a2["tau_priv"]],"visibility":"internal diagnostics, not observer-visible"}})
    print(json.dumps({"P1":a1,"W1":a2},indent=2))


if __name__=="__main__": main()
