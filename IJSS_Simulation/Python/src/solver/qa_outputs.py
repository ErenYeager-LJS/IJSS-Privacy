from pathlib import Path
import csv
import json
import zipfile
import numpy as np

root=Path(__file__).resolve().parents[3]
tables=list((root/'Python/output/tables/origin').glob('*.csv'))
for path in tables:
    with path.open(encoding='utf-8') as handle:
        columns=len(next(csv.reader(handle)))
    if columns>2 and not path.name.endswith('_events.csv'):
        numeric=np.genfromtxt(path,delimiter=',',skip_header=1,usecols=range(2,columns))
        if not np.all(np.isfinite(np.atleast_1d(numeric))):
            raise RuntimeError(f'Nonfinite data in {path}')
    elif path.name.endswith('_events.csv'):
        event_time=np.genfromtxt(path,delimiter=',',skip_header=1,usecols=2)
        if not np.all(np.isfinite(np.atleast_1d(event_time))):
            raise RuntimeError(f'Nonfinite event time in {path}')
figures=list((root/'Python/output/figures/manuscript').glob('*'))
assert len(tables)==13,len(tables);assert len(figures)==12,len(figures)
slx=root/'Simulink/main.slx';assert slx.stat().st_size>10000
with zipfile.ZipFile(slx) as archive:
    assert any('blockdiagram' in name.lower() for name in archive.namelist())
p1=json.loads((root/'Python/output/manifests/P1_RUN_001.json').read_text())
w1=json.loads((root/'Python/output/manifests/W1_RUN_001.json').read_text())
validation=json.loads((root/'Validation/python_vs_simulink/validation_summary.json').read_text())
assert p1['success'] and w1['success'] and validation['pass']
assert w1['public_history_residual']==0
print(f'DATA_QA_PASS tables={len(tables)} figures={len(figures)} slx_bytes={slx.stat().st_size}')
