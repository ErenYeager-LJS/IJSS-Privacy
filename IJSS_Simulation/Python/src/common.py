from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import yaml


ROOT = Path(__file__).resolve().parents[2]
PARAMETER_FILE = ROOT / "canonical_parameter.yaml"


def load_parameters(path: Path = PARAMETER_FILE):
    raw = path.read_bytes()
    params = yaml.safe_load(raw)
    params["manifest_id"] = hashlib.sha256(raw).hexdigest()[:16]
    return params


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def arrays(params, section, *names):
    return tuple(np.asarray(params[section][name], dtype=float) for name in names)
