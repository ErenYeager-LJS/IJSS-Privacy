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
    publication = ROOT / "Python/output/tables/publication"
    p1 = np.load(processed / "P1_FIGURE_DATA.npz"); w1 = np.load(processed / "W1_FIGURE_DATA.npz")
    voltage_error = p1["voltage_V"] - float(params["base"]["voltage_V"])
    frequency_error = p1["frequency_Hz"] - float(params["base"]["frequency_Hz"])
    write_wide(out / "Voltage.csv", p1["t"], manifest_id, [
        ("voltage_V",p1["voltage_V"]), ("voltage_error_V",voltage_error),
        ("ppc_boundary_V",p1["rhoV"]*float(params["base"]["voltage_V"])),])
    write_wide(out / "Frequency.csv", p1["t"], manifest_id, [
        ("frequency_Hz",p1["frequency_Hz"]), ("frequency_error_Hz",frequency_error),
        ("ppc_boundary_Hz",p1["rhoW"]*float(params["base"]["frequency_Hz"])),])
    write_wide(out / "ActivePowerSharing.csv",p1["t"],manifest_id,[
        ("active_power_W",p1["active_power_W"]),("normalized_power",p1["normalized_power"]),
        ("sharing_error",p1["sharing_error"]),])
    write_wide(out / "PublicHistory.csv", w1["t"], manifest_id, [
        ("pV_nom", w1["pV_nom"]), ("pV_alt", w1["pV_alt"]),
        ("pomega_nom", w1["pW_nom"]), ("pomega_alt", w1["pW_alt"]),
        ("public_difference_l2", w1["public_residual"]),])
    write_wide(out / "PrivateDifference.csv", w1["t"], manifest_id, [
        ("qV_difference", w1["qV_diff"]), ("qomega_difference", w1["qW_diff"]),
        ("protected_command_difference", w1["cV_diff"][:, 0]),
        ("protected_voltage_state_difference", w1["V_diff"][:, 0]),
        ("forced_weight_difference_norm", np.max(np.abs(w1["weight_diff"]), axis=1)),
        ("strict_construction_margin", w1["strict_margin"]),])
    write_wide(publication / "F1_voltage_restoration_final.csv", p1["t"], manifest_id, [
        ("voltage_V",p1["voltage_V"]), ("voltage_error_V",voltage_error),
        ("ppc_boundary_V",p1["rhoV"]*float(params["base"]["voltage_V"])),])
    write_wide(publication / "F2_frequency_restoration_final.csv", p1["t"], manifest_id, [
        ("frequency_Hz",p1["frequency_Hz"]), ("frequency_error_Hz",frequency_error),
        ("ppc_boundary_Hz",p1["rhoW"]*float(params["base"]["frequency_Hz"])),])
    write_wide(publication / "F3_active_power_sharing_final.csv",p1["t"],manifest_id,[
        ("active_power_W",p1["active_power_W"]), ("normalized_power",p1["normalized_power"]),
        ("sharing_error",p1["sharing_error"]),])
    write_wide(publication / "F4_public_history_indistinguishability_final.csv", w1["t"], manifest_id, [
        ("pV_nom", w1["pV_nom"]), ("pV_alt", w1["pV_alt"]),
        ("pomega_nom", w1["pW_nom"]), ("pomega_alt", w1["pW_alt"]),
        ("public_difference_l2", w1["public_residual"]),])
    write_wide(publication / "F5_private_state_difference_final.csv", w1["t"], manifest_id, [
        ("qV_difference", w1["qV_diff"]),
        ("qomega_difference", w1["qW_diff"]),
        ("qomega_difference_scaled_1e12", 1.0e12*w1["qW_diff"]),
        ("protected_command_difference", w1["cV_diff"][:, 0]),
        ("protected_voltage_state_difference", w1["V_diff"][:, 0]),
        ("forced_weight_difference_norm", np.max(np.abs(w1["weight_diff"]), axis=1)),])
    print(json.dumps({"manifest_id": manifest_id, "origin_csv_files": 5,
        "publication_csv_files": 5}, indent=2))


if __name__ == "__main__":
    main()
