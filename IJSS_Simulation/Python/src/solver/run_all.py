from __future__ import annotations

import json

from solver.run_physical import run as run_physical
from solver.run_privacy_witness import run as run_privacy_witness


def main():
    _, _, _, physical = run_physical()
    _, _, privacy = run_privacy_witness()
    print(json.dumps({"physical": physical, "privacy": privacy}, indent=2))


if __name__ == "__main__":
    main()
