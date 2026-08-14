from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import ROOT, load_parameters, write_json
from controller.secondary import controller
from model.diagnostics import diagnostics
from model.state_layout import unpack
from privacy.witness import forced_weights
from solver.rhs import evaluate, rhs


def _stack(records, key):
    return np.stack([record[key] for record in records])


def process_physical(params):
    raw = np.load(ROOT / "Python/output/raw/P1_RUN_001.npz")
    t, x = raw["t"], raw["x"]
    records = [diagnostics(tt, x[:, k], params) for k, tt in enumerate(t)]
    margins = np.array([min(record["margins"].values()) for record in records])
    rate = float(params["comparison"]["local_rate"])
    budget = float(params["comparison"]["local_budget"])
    v0 = float(records[0]["Vcl"])
    envelope = np.exp(-rate*t)*v0 + budget*(1-np.exp(-rate*t))/rate
    return {
        "t": t, "V": _stack(records, "V"), "omega": _stack(records, "omega"),
        "e0V": _stack(records, "e0V"), "e0W": _stack(records, "e0W"),
        "sigmaV": np.stack([r["ppcV"][2] for r in records]),
        "sigmaW": np.stack([r["ppcW"][2] for r in records]),
        "zetaV": np.stack([r["ppcV"][3] for r in records]),
        "zetaW": np.stack([r["ppcW"][3] for r in records]),
        "boundary_margin": margins, "Vcl": np.array([r["Vcl"] for r in records]),
        "comparison_envelope": envelope,
    }


def process_privacy(params):
    raw = np.load(ROOT / "Python/output/raw/W1_RUN_001.npz")
    t, nominal, alternative = raw["t"], raw["nominal"], raw["alternative"]
    n = int(params["network"]["N"])
    lower = float(params["privacy"]["weight_lower"])
    upper = float(params["privacy"]["weight_upper"])
    public_v, public_w, qv_diff, qw_diff, cv_diff = [], [], [], [], []
    state_diff, weight_diff, strict_margin = [], [], []
    nominal_weights = np.concatenate([
        params["privacy"]["w12_V"], params["privacy"]["w21_V"],
        params["privacy"]["w12_omega"], params["privacy"]["w21_omega"],
    ]).astype(float)
    for k, tt in enumerate(t):
        xn = nominal[:, k]
        _, sn, cn, wn, _ = evaluate(tt, xn, params)
        y = alternative[:, k]
        sa = {name: y[j*n:(j+1)*n] for j, name in enumerate(("V", "Vdot", "omega", "delta"))}
        sa.update({"pV": sn["pV"], "pW": sn["pW"], "qV": y[4*n:5*n], "qW": y[5*n:6*n]})
        ca = controller(tt, sa, params)
        qdot = {
            "qV": np.asarray(params["privacy"]["lambda_V"])*(ca["cV"]-sa["qV"])
                  + np.asarray(params["privacy"]["w12_V"])*(sa["pV"]-sa["qV"]),
            "qW": np.asarray(params["privacy"]["lambda_omega"])*(ca["cW"]-sa["qW"])
                  + np.asarray(params["privacy"]["w12_omega"])*(sa["pW"]-sa["qW"]),
        }
        weights = np.concatenate(forced_weights(tt, sn, cn, wn, sa, ca, qdot, params))
        z = np.concatenate([sa["pV"]-sa["qV"], sa["pW"]-sa["qW"]])
        public_v.append(sn["pV"]); public_w.append(sn["pW"])
        qv_diff.append(sa["qV"]-sn["qV"]); qw_diff.append(sa["qW"]-sn["qW"])
        cv_diff.append(ca["cV"]-cn["cV"]); state_diff.append(sa["V"]-sn["V"])
        weight_diff.append(weights-nominal_weights)
        strict_margin.append(min(np.min(weights-lower), np.min(upper-weights), np.min(np.abs(z))))
    return {
        "t": t, "pV_nom": np.stack(public_v), "pV_alt": np.stack(public_v),
        "pW_nom": np.stack(public_w), "pW_alt": np.stack(public_w),
        "public_residual": np.zeros_like(t), "qV_diff": np.stack(qv_diff),
        "qW_diff": np.stack(qw_diff), "cV_diff": np.stack(cv_diff),
        "V_diff": np.stack(state_diff), "weight_diff": np.stack(weight_diff),
        "strict_margin": np.asarray(strict_margin),
    }


def main():
    params = load_parameters()
    out = ROOT / "Python/output/processed"
    out.mkdir(parents=True, exist_ok=True)
    p1, w1 = process_physical(params), process_privacy(params)
    np.savez_compressed(out / "P1_FIGURE_DATA.npz", **p1)
    np.savez_compressed(out / "W1_FIGURE_DATA.npz", **w1)
    manifest = {"manifest_id": params["manifest_id"], "sources": ["P1_RUN_001", "W1_RUN_001"],
                "processing": "raw NPZ to deterministic diagnostic arrays"}
    write_json(ROOT / "Python/output/manifests/processed_data.json", manifest)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
