from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,load_parameters,write_json

COLORS=("#0072B2","#D55E00","#009E73","#CC79A7")
GREY="#4D4D4D"


def load_csv(name,folder="origin"):
    path=ROOT/"Python/output/tables"/folder/name
    return np.genfromtxt(path,delimiter=",",names=True,encoding="utf-8"),path


def style():
    mpl.rcParams.update({"font.family":"sans-serif","font.sans-serif":["Arial","Helvetica","DejaVu Sans"],
        "font.size":7.5,"axes.labelsize":7.5,"axes.titlesize":8,"xtick.labelsize":7,
        "ytick.labelsize":7,"legend.fontsize":6.8,"axes.spines.right":False,
        "axes.spines.top":False,"axes.linewidth":0.7,"lines.linewidth":1.25,
        "legend.frameon":False,"svg.fonttype":"none","pdf.fonttype":42,"savefig.facecolor":"white"})


def save(fig,name,dpi):
    folder=ROOT/"Python/output/figures/publication"
    folder.mkdir(parents=True,exist_ok=True)
    fig.savefig(folder/f"{name}.pdf",bbox_inches="tight")
    fig.savefig(folder/f"{name}.svg",bbox_inches="tight")
    fig.savefig(folder/f"{name}.png",dpi=dpi,bbox_inches="tight")
    plt.close(fig)


def phase_markers(ax,t_sec,t_eval):
    ax.axvspan(ax.get_xlim()[0],t_sec,color="#EAEAEA",alpha=0.30,zorder=0)
    ax.axvline(t_sec,color=GREY,ls="--",lw=0.9)
    ax.axvline(t_eval,color="#D55E00",ls=(0,(3,2)),lw=0.9)


def label_phases(ax,t_sec,t_eval):
    ax.annotate("Secondary ON",xy=(t_sec,1),xycoords=("data","axes fraction"),
        xytext=(-4,-3),textcoords="offset points",rotation=90,ha="right",va="top",fontsize=6.3,color=GREY)
    ax.annotate(r"Prescribed settling time $T_s$",xy=(t_eval,1),xycoords=("data","axes fraction"),
        xytext=(4,-3),textcoords="offset points",rotation=90,ha="left",va="top",fontsize=6.3,color="#D55E00")


def settling_time(t,error,t_sec,tolerance):
    bad=np.flatnonzero((t>=t_sec)&(error>tolerance))
    return float(t[bad[-1]+1]) if len(bad) and bad[-1]+1<len(t) else float(t_sec)


def ppc_utilization(ax,t,errors,boundary):
    utilization=np.max(np.abs(errors)/boundary[:,None],axis=1)
    ax.plot(t,utilization,color="#009E73",lw=1.0,label=r"$\max_i |e_i|/\rho_i$")
    ax.axhline(1.0,color=GREY,lw=0.8,ls=":",label="Admissible boundary")
    ax.set_ylim(0,1.05)
    return utilization


def plot_agents(ax,t,data,prefix):
    for i,color in enumerate(COLORS,1): ax.plot(t,data[f"{prefix}_DG{i}"],color=color,label=f"DG {i}")


def voltage_figure(data,p,dpi):
    t=data["time_s"]; t_sec=float(p["scenario"]["secondary_activation_s"]); t_eval=float(p["scenario"]["prescribed_evaluation_s"])
    ref=float(p["base"]["voltage_V"]); tol=float(p["scenario"]["voltage_tolerance_V"])
    errors=np.column_stack([data[f"voltage_error_V_DG{i}"] for i in range(1,5)])
    boundary=data["ppc_boundary_V_DG1"]; conv=settling_time(t,np.max(np.abs(errors),axis=1),t_sec,tol)
    fig,axes=plt.subplots(3,1,figsize=(7.05,5.15),sharex=True,layout="constrained",gridspec_kw={"height_ratios":[1.2,1,0.62]})
    plot_agents(axes[0],t,data,"voltage_V"); axes[0].axhline(ref,color="black",lw=0.8,label=r"$V_{ref}=310$ V")
    for i,color in enumerate(COLORS,1): axes[1].plot(t,errors[:,i-1],color=color,label=f"DG {i}")
    axes[1].axhline(tol,color="#7A3E9D",lw=.7,ls="--",label=r"Numerical validation threshold $\pm0.05$ V"); axes[1].axhline(-tol,color="#7A3E9D",lw=.7,ls="--")
    ppc_utilization(axes[2],t,errors,boundary)
    for ax in axes: ax.set_xlim(t[0],t[-1]); phase_markers(ax,t_sec,t_eval); ax.grid(color="#D9D9D9",lw=0.45,alpha=0.7)
    axes[0].set_ylabel("Voltage (V)"); axes[1].set_ylabel("Voltage error (V)")
    axes[2].set(xlabel="Time (s)",ylabel="PPC utilization")
    axes[0].legend(ncol=5,loc="upper center"); axes[1].legend(ncol=2,loc="lower right"); axes[2].legend(ncol=2,loc="upper right"); label_phases(axes[0],t_sec,t_eval)
    axes[1].annotate(fr"Observed restoration time: {conv:.2f} s",xy=(conv,0),xytext=(8,12),textcoords="offset points",fontsize=6.5,color="#7A3E9D",arrowprops={"arrowstyle":"->","lw":.6,"color":"#7A3E9D"})
    axes[2].text(0.995,0.22,r"No exit detected: $t_{exit}>15$ s",transform=axes[2].transAxes,ha="right",va="bottom",fontsize=6.3,color=GREY)
    save(fig,"F1_voltage_restoration_final",dpi)


def frequency_figure(data,p,dpi):
    t=data["time_s"]; t_sec=float(p["scenario"]["secondary_activation_s"]); t_eval=float(p["scenario"]["prescribed_evaluation_s"])
    ref=float(p["base"]["frequency_Hz"]); tol=float(p["scenario"]["frequency_tolerance_Hz"])
    errors=np.column_stack([data[f"frequency_error_Hz_DG{i}"] for i in range(1,5)])
    boundary=data["ppc_boundary_Hz_DG1"]; conv=settling_time(t,np.max(np.abs(errors),axis=1),t_sec,tol)
    fig,axes=plt.subplots(3,1,figsize=(7.05,5.15),sharex=True,layout="constrained",gridspec_kw={"height_ratios":[1.2,1,0.62]})
    plot_agents(axes[0],t,data,"frequency_Hz"); axes[0].axhline(ref,color="black",lw=0.8,label=r"$f_{ref}=50$ Hz")
    for i,color in enumerate(COLORS,1): axes[1].plot(t,errors[:,i-1],color=color,label=f"DG {i}")
    axes[1].axhline(tol,color="#7A3E9D",lw=.7,ls="--",label=r"Numerical validation threshold $\pm0.005$ Hz"); axes[1].axhline(-tol,color="#7A3E9D",lw=.7,ls="--")
    ppc_utilization(axes[2],t,errors,boundary)
    for ax in axes: ax.set_xlim(t[0],t[-1]); phase_markers(ax,t_sec,t_eval); ax.grid(color="#D9D9D9",lw=0.45,alpha=0.7)
    axes[0].set_ylabel("Frequency (Hz)"); axes[1].set_ylabel("Frequency error (Hz)")
    axes[2].set(xlabel="Time (s)",ylabel="PPC utilization")
    axes[0].legend(ncol=5,loc="upper center"); axes[1].legend(ncol=2,loc="lower right"); axes[2].legend(ncol=2,loc="upper right"); label_phases(axes[0],t_sec,t_eval)
    axes[1].annotate(fr"Observed restoration time: {conv:.2f} s",xy=(conv,0),xytext=(8,12),textcoords="offset points",fontsize=6.5,color="#7A3E9D",arrowprops={"arrowstyle":"->","lw":.6,"color":"#7A3E9D"})
    axes[2].text(0.995,0.22,r"No exit detected: $t_{exit}>15$ s",transform=axes[2].transAxes,ha="right",va="bottom",fontsize=6.3,color=GREY)
    save(fig,"F2_frequency_restoration_final",dpi)


def power_figure(data,p,dpi):
    t=data["time_s"]; t_sec=float(p["scenario"]["secondary_activation_s"]); t_eval=float(p["scenario"]["prescribed_evaluation_s"])
    fig,axes=plt.subplots(3,1,figsize=(7.05,5.25),sharex=True,layout="constrained",gridspec_kw={"height_ratios":[1,1,0.72]})
    plot_agents(axes[0],t,data,"active_power_W"); plot_agents(axes[1],t,data,"normalized_power")
    axes[2].plot(t,data["sharing_error"],color="#D55E00")
    axes[0].set_ylabel("Active power (W)"); axes[1].set_ylabel(r"$P_i/P_{i,rated}$")
    axes[2].set(xlabel="Time (s)",ylabel="Sharing error")
    for ax in axes:
        ax.set_xlim(t[0],t[-1]); phase_markers(ax,t_sec,t_eval); ax.grid(color="#D9D9D9",lw=0.45,alpha=0.7)
    axes[0].legend(ncol=4,loc="upper center"); label_phases(axes[0],t_sec,t_eval)
    for label,ax in zip(("(a)","(b)","(c)"),axes):
        ax.text(0.006,0.88,label,transform=ax.transAxes,ha="left",va="top",fontweight="bold")
    fig.suptitle("Active Power Sharing Preservation",fontsize=8.5,fontweight="bold")
    save(fig,"F3_active_power_sharing_final",dpi)


def public_figure(data,tau,dpi):
    t=data["time_s"]; fig,axes=plt.subplots(3,1,figsize=(7.05,5.1),sharex=True,layout="constrained",gridspec_kw={"height_ratios":[1,1,0.72]})
    for i,color in enumerate(COLORS,1):
        axes[0].plot(t,data[f"pV_nom_DG{i}"],color=color,label=f"DG {i}, nominal")
        axes[0].plot(t,data[f"pV_alt_DG{i}"],color=color,ls="--",label=f"DG {i}, non-nominal")
        axes[1].plot(t,data[f"pomega_nom_DG{i}"],color=color)
        axes[1].plot(t,data[f"pomega_alt_DG{i}"],color=color,ls="--")
    axes[2].plot(t,data["public_difference_l2"],color="#D55E00"); axes[2].set_ylim(-1e-14,1e-14)
    axes[0].set_ylabel(r"Public $p^V$"); axes[1].set_ylabel(r"Public $p^\omega$")
    axes[2].set(xlabel="Time (s)",ylabel=r"$\|y-y'\|_2$")
    axes[0].legend(ncol=4,loc="upper center",bbox_to_anchor=(0.5,1.35))
    for ax in axes: ax.axvline(tau,color=GREY,ls="--",lw=0.8); ax.grid(color="#D9D9D9",lw=0.45,alpha=0.7)
    axes[2].text(0.78,0.88,fr"Displayed comparison: $0\leq t\leq {tau:.2f}$ s",
        transform=axes[2].transAxes,ha="right",va="top",fontsize=6.5,color=GREY)
    fig.suptitle("Observer-visible public information",fontsize=8.5,fontweight="bold")
    save(fig,"F4_public_history_indistinguishability_final",dpi)


def private_figure(data,tau,dpi):
    t=data["time_s"]; fig,axes=plt.subplots(2,2,figsize=(7.05,4.55),layout="constrained")
    for i,color in enumerate(COLORS,1):
        axes[0,0].plot(t,data[f"qV_difference_DG{i}"],color=color,label=f"DG {i}")
        axes[0,1].plot(t,data[f"qomega_difference_scaled_1e12_DG{i}"],color=color,label=f"DG {i}")
    axes[1,0].plot(t,data["protected_command_difference"],color="#D55E00",label="Command difference")
    axes[1,0].plot(t,data["protected_voltage_state_difference"],color="#0072B2",ls="--",label="Protected-state difference")
    axes[1,1].plot(t,data["forced_weight_difference_norm"],color="#CC79A7",label="Private-weight difference")
    labels=(r"Private $q^V$ difference",r"Private $q^\omega$ difference (scaled)",
        "Protected-agent difference","Private-weight difference")
    for ax,label in zip(axes.flat,labels):
        ax.axvline(tau,color=GREY,ls="--",lw=0.8); ax.set(xlabel="Time (s)",ylabel=label); ax.grid(color="#D9D9D9",lw=0.45,alpha=0.7)
    axes[0,0].legend(ncol=4,loc="best"); axes[0,1].text(0.02,0.96,r"Displayed as $10^{12}\Delta q^\omega$",
        transform=axes[0,1].transAxes,ha="left",va="top",fontsize=6.3,color=GREY)
    axes[1,0].legend(); axes[1,1].legend()
    fig.suptitle("Distinct internal realizations (not observer-visible)",fontsize=8.5,fontweight="bold")
    save(fig,"F5_private_state_difference_final",dpi)


def main():
    style(); p=load_parameters(); dpi=int(p["plotting"]["dpi"])
    w1=json.loads((ROOT/"Python/output/manifests/W1_RUN_001.json").read_text(encoding="utf-8"))
    voltage,pv=load_csv("F1_voltage_restoration_final.csv","publication")
    frequency,pf=load_csv("F2_frequency_restoration_final.csv","publication")
    power,pp=load_csv("F3_active_power_sharing_final.csv","publication")
    public,ph=load_csv("F4_public_history_indistinguishability_final.csv","publication")
    private,pd=load_csv("F5_private_state_difference_final.csv","publication")
    voltage_figure(voltage,p,dpi); frequency_figure(frequency,p,dpi); power_figure(power,p,dpi)
    public_figure(public,w1["tau_priv"],dpi); private_figure(private,w1["tau_priv"],dpi)
    write_json(ROOT/"Python/output/manifests/figure_provenance.json",{"manifest_id":p["manifest_id"],
        "F1_final":{"csv":pv.name,"scope":"selected four-DG local numerical case"},
        "F2_final":{"csv":pf.name,"scope":"selected four-DG local numerical case"},
        "F3_final":{"csv":pp.name,"scope":"sharing-preservation diagnostic; no PO-14 claim"},
        "F4_final":{"csv":ph.name,"interval":[0,w1["tau_priv"]],"visibility":"observer-visible public only"},
        "F5_final":{"csv":pd.name,"interval":[0,w1["tau_priv"]],"visibility":"internal diagnostics"}})
    print("Generated five publication figures in PDF, SVG, and PNG.")


if __name__=="__main__": main()
