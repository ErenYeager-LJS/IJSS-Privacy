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
    else:
        raise RuntimeError(f'Unexpected empty data export: {path}')
figures=list((root/'Python/output/figures/manuscript').glob('*'))
assert len(tables)==4,len(tables);assert len(figures)==12,len(figures)
for stem in ('F1_local_physical_trajectories','F2_local_validity_ppc_diagnostics',
             'F3_public_history_indistinguishability','F4_hidden_private_differences'):
    assert (root/'Python/output/tables/origin'/f'{stem}.csv').is_file()
    for suffix in ('pdf','svg','png'):
        assert (root/'Python/output/figures/manuscript'/f'{stem}.{suffix}').is_file()
slx=root/'Simulink/main.slx';assert slx.stat().st_size>10000
with zipfile.ZipFile(slx) as archive:
    assert any('blockdiagram' in name.lower() for name in archive.namelist())
p1=json.loads((root/'Python/output/manifests/P1_RUN_001.json').read_text())
w1=json.loads((root/'Python/output/manifests/W1_RUN_001.json').read_text())
validation=json.loads((root/'Validation/python_vs_simulink/validation_summary.json').read_text())
assert p1['success'] and w1['success'] and validation['pass']
assert w1['public_history_residual']==0
audit=(root/'Simulink/block_architecture_audit.txt').read_text(encoding='utf-8')
assert 'S-Function blocks: 0' in audit and 'MATLAB Function blocks: 0' in audit
assert 'Scope blocks: 5' in audit and 'Forbidden architecture count: 0' in audit
print(f'DATA_QA_PASS tables={len(tables)} figures={len(figures)} slx_bytes={slx.stat().st_size}')
