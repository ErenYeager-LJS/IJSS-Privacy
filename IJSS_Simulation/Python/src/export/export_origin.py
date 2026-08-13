from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import ROOT, load_parameters


def write_wide(path, time, manifest_id, fields):
    headers = ["time_s", "manifest_id"]
    columns = [np.asarray(time)]
    for name, values in fields:
        array = np.asarray(values)
        if array.ndim == 1:
            headers.append(name); columns.append(array)
        else:
            for k in range(array.shape[1]):
                headers.append(f"{name}_DG{k+1}"); columns.append(array[:, k])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle); writer.writerow(headers)
        for row in zip(*columns): writer.writerow([f"{row[0]:.15g}", manifest_id, *[f"{v:.15g}" for v in row[1:]]])


def main():
    params = load_parameters(); manifest_id = params["manifest_id"]
    processed = ROOT / "Python/output/processed"; out = ROOT / "Python/output/tables/origin"
    p1 = np.load(processed / "P1_FIGURE_DATA.npz"); w1 = np.load(processed / "W1_FIGURE_DATA.npz")
    write_wide(out / "F1_local_physical_trajectories.csv", p1["t"], manifest_id, [
        ("voltage_pu", p1["V"]), ("frequency_deviation_pu", p1["omega"]),
        ("voltage_tracking_error_pu", p1["e0V"]), ("frequency_tracking_error_pu", p1["e0W"]),])
    write_wide(out / "F2_local_validity_ppc_diagnostics.csv", p1["t"], manifest_id, [
        ("sigma_V", p1["sigmaV"]), ("sigma_omega", p1["sigmaW"]),
        ("zeta_V", p1["zetaV"]), ("zeta_omega", p1["zetaW"]),
        ("boundary_margin", p1["boundary_margin"]), ("local_comparison", p1["Vcl"]),
        ("comparison_envelope", p1["comparison_envelope"]),])
    write_wide(out / "F3_public_history_indistinguishability.csv", w1["t"], manifest_id, [
        ("pV_nom", w1["pV_nom"]), ("pV_alt", w1["pV_alt"]),
        ("pomega_nom", w1["pW_nom"]), ("pomega_alt", w1["pW_alt"]),
        ("max_abs_public_difference", w1["public_residual"]),])
    write_wide(out / "F4_hidden_private_differences.csv", w1["t"], manifest_id, [
        ("qV_difference", w1["qV_diff"]), ("qomega_difference", w1["qW_diff"]),
        ("protected_command_difference", w1["cV_diff"][:, 0]),
        ("protected_voltage_state_difference", w1["V_diff"][:, 0]),
        ("forced_weight_difference_norm", np.max(np.abs(w1["weight_diff"]), axis=1)),
        ("strict_construction_margin", w1["strict_margin"]),])
    print(json.dumps({"manifest_id": manifest_id, "csv_files": 4}, indent=2))


if __name__ == "__main__":
    main()
