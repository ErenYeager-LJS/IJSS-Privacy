from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import ROOT, load_parameters, write_json

COLORS = ("#0072B2", "#D55E00", "#009E73")
ALT = "#5B5B5B"


def load_csv(name):
    path = ROOT / "Python/output/tables/origin" / name
    return np.genfromtxt(path, delimiter=",", names=True, encoding="utf-8"), path


def style():
    mpl.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 7.5, "axes.labelsize": 7.5, "axes.titlesize": 8,
        "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 6.8,
        "axes.spines.right": False, "axes.spines.top": False, "axes.linewidth": 0.7,
        "lines.linewidth": 1.25, "legend.frameon": False, "svg.fonttype": "none",
        "pdf.fonttype": 42, "savefig.facecolor": "white",
    })


def panel(ax, label):
    ax.text(-0.13, 1.04, label, transform=ax.transAxes, fontweight="bold", va="bottom")
    ax.grid(True, color="#D9D9D9", linewidth=0.45, alpha=0.7)


def save(fig, name, dpi):
    folders = [ROOT / "Python/output/figures/manuscript", ROOT / "Python/output/figures/origin"]
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        fig.savefig(folder / f"{name}.pdf", bbox_inches="tight")
        fig.savefig(folder / f"{name}.svg", bbox_inches="tight")
        fig.savefig(folder / f"{name}.png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def mark_exit(ax, tau):
    ax.axvline(tau, color="#333333", linestyle=(0, (3, 2)), linewidth=0.8)


def figure1(data, tau, dpi):
    t = data["time_s"]
    fig, axes = plt.subplots(2, 2, figsize=(7.05, 4.45), sharex=True, layout="constrained")
    specs = [
        ("voltage_pu", "Voltage (p.u.)", "a"),
        ("frequency_deviation_pu", "Frequency deviation (p.u.)", "b"),
        ("voltage_tracking_error_pu", "Voltage tracking error (p.u.)", "c"),
        ("frequency_tracking_error_pu", "Frequency tracking error (p.u.)", "d"),
    ]
    for ax, (prefix, ylabel, tag) in zip(axes.flat, specs):
        for i, color in enumerate(COLORS, 1): ax.plot(t, data[f"{prefix}_DG{i}"], color=color, label=f"DG {i}")
        mark_exit(ax, tau); ax.set_ylabel(ylabel); panel(ax, tag)
    axes[0, 0].legend(ncol=3, loc="best")
    axes[1, 0].set_xlabel("Time (s)"); axes[1, 1].set_xlabel("Time (s)")
    save(fig, "F1_local_physical_trajectories", dpi)


def figure2(data, tau, dpi):
    t = data["time_s"]
    fig, axes = plt.subplots(2, 2, figsize=(7.05, 4.55), layout="constrained")
    for i, color in enumerate(COLORS, 1):
        axes[0, 0].plot(t, data[f"sigma_V_DG{i}"], color=color, label=f"DG {i}")
        axes[0, 0].plot(t, data[f"sigma_omega_DG{i}"], color=color, linestyle="--")
        axes[0, 1].plot(t, data[f"zeta_V_DG{i}"], color=color)
        axes[0, 1].plot(t, data[f"zeta_omega_DG{i}"], color=color, linestyle="--")
    axes[0, 0].axhline(1, color=ALT, linewidth=0.7); axes[0, 0].axhline(-1, color=ALT, linewidth=0.7)
    axes[0, 0].set_ylabel(r"Normalized error $sigma$")
    axes[0, 1].set_ylabel(r"Transformed coordinate $zeta$")
    axes[1, 0].plot(t, data["boundary_margin"], color="#CC79A7")
    axes[1, 0].axhline(0, color=ALT, linewidth=0.7)
    axes[1, 0].set_ylabel("Minimum admissibility margin")
    axes[1, 1].plot(t, data["local_comparison"], color="#0072B2")
    axes[1, 1].set_ylabel("Local comparison quantity")
    axes[0, 0].legend(ncol=3, loc="best")
    for ax, tag in zip(axes.flat, "abcd"):
        mark_exit(ax, tau); panel(ax, tag); ax.set_xlabel("Time (s)")
    save(fig, "F2_local_validity_ppc_diagnostics", dpi)


def figure3(data, tau, dpi):
    t = data["time_s"]
    fig, axes = plt.subplots(3, 1, figsize=(7.05, 5.0), sharex=True, layout="constrained",
                             gridspec_kw={"height_ratios": [1, 1, 0.72]})
    for i, color in enumerate(COLORS, 1):
        axes[0].plot(t, data[f"pV_nom_DG{i}"], color=color, label=f"DG {i}, nominal")
        axes[0].plot(t, data[f"pV_alt_DG{i}"], color=color, linestyle="--", label=f"DG {i}, alternative")
        axes[1].plot(t, data[f"pomega_nom_DG{i}"], color=color)
        axes[1].plot(t, data[f"pomega_alt_DG{i}"], color=color, linestyle="--")
    axes[2].plot(t, data["max_abs_public_difference"], color="#D55E00")
    axes[2].set_ylim(-1e-14, 1e-14)
    axes[0].set_ylabel(r"Public $p^V$")
    axes[1].set_ylabel(r"Public $p^omega$")
    axes[2].set_ylabel("Max. absolute\npublic difference")
    axes[2].set_xlabel("Time (s)")
    axes[0].legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.32), columnspacing=1.1)
    for ax, tag in zip(axes, "abc"):
        ax.axvline(tau, color=ALT, linestyle=(0, (3, 2)), linewidth=0.8); panel(ax, tag)
    save(fig, "F3_public_history_indistinguishability", dpi)


def figure4(data, tau, dpi):
    t = data["time_s"]
    fig, axes = plt.subplots(2, 2, figsize=(7.05, 4.55), layout="constrained")
    for i, color in enumerate(COLORS, 1):
        axes[0, 0].plot(t, data[f"qV_difference_DG{i}"], color=color, label=f"DG {i}")
        axes[0, 1].plot(t, data[f"qomega_difference_DG{i}"], color=color)
    axes[1, 0].plot(t, data["protected_command_difference"], color="#D55E00", label="Command difference")
    axes[1, 0].plot(t, data["protected_voltage_state_difference"], color="#0072B2", linestyle="--", label="Voltage-state difference")
    axes[1, 1].plot(t, data["forced_weight_difference_norm"], color="#CC79A7", label="Forced-weight difference")
    axes[1, 1].plot(t, data["strict_construction_margin"], color="#009E73", linestyle="--", label="Strict margin")
    labels = [r"Private $q^V$ difference", r"Private $q^omega$ difference",
              "Protected-agent difference", "Weight difference / margin"]
    for ax, tag, label in zip(axes.flat, "abcd", labels):
        ax.axvline(tau, color=ALT, linestyle=(0, (3, 2)), linewidth=0.8)
        ax.set(xlabel="Time (s)", ylabel=label); panel(ax, tag)
    axes[0, 0].legend(ncol=3, loc="best"); axes[1, 0].legend(loc="best"); axes[1, 1].legend(loc="best")
    fig.suptitle("Internal diagnostics, not observer-visible", fontsize=8.5, fontweight="bold")
    save(fig, "F4_hidden_private_differences", dpi)


def main():
    style(); params = load_parameters(); dpi = int(params["plotting"]["dpi"])
    p1_manifest = json.loads((ROOT / "Python/output/manifests/P1_RUN_001.json").read_text(encoding="utf-8"))
    w1_manifest = json.loads((ROOT / "Python/output/manifests/W1_RUN_001.json").read_text(encoding="utf-8"))
    f1, p1csv = load_csv("F1_local_physical_trajectories.csv")
    f2, p2csv = load_csv("F2_local_validity_ppc_diagnostics.csv")
    f3, p3csv = load_csv("F3_public_history_indistinguishability.csv")
    f4, p4csv = load_csv("F4_hidden_private_differences.csv")
    figure1(f1, p1_manifest["event_time"], dpi); figure2(f2, p1_manifest["event_time"], dpi)
    figure3(f3, w1_manifest["tau_priv"], dpi); figure4(f4, w1_manifest["tau_priv"], dpi)
    write_json(ROOT / "Python/output/manifests/figure_provenance.json", {
        "manifest_id": params["manifest_id"],
        "F1": {"csv": p1csv.name, "interval": [0, p1_manifest["event_time"]]},
        "F2": {"csv": p2csv.name, "interval": [0, p1_manifest["event_time"]]},
        "F3": {"csv": p3csv.name, "interval": [0, w1_manifest["tau_priv"],], "visibility": "public only"},
        "F4": {"csv": p4csv.name, "interval": [0, w1_manifest["tau_priv"]], "visibility": "internal diagnostics"},
    })
    print("Generated four CSV-driven figures in PDF, SVG, and PNG.")


if __name__ == "__main__":
    main()
