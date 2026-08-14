from pathlib import Path
import csv
import json
import zipfile
import numpy as np
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import load_parameters

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
assert len(tables)==5,len(tables);assert len(figures)==15,len(figures)
required={
    'Voltage':'F1_voltage_restoration',
    'Frequency':'F2_frequency_restoration',
    'ActivePowerSharing':'F3_active_power_sharing',
    'PublicHistory':'F4_public_history_indistinguishability',
    'PrivateDifference':'F5_private_state_difference',
}
for csv_stem,figure_stem in required.items():
    assert (root/'Python/output/tables/origin'/f'{csv_stem}.csv').is_file()
    for suffix in ('pdf','svg','png'):
        assert (root/'Python/output/figures/manuscript'/f'{figure_stem}.{suffix}').is_file()
slx=root/'Simulink/main.slx';assert slx.stat().st_size>10000
with zipfile.ZipFile(slx) as archive:
    assert any('blockdiagram' in name.lower() for name in archive.namelist())
p1=json.loads((root/'Python/output/manifests/P1_RUN_001.json').read_text())
w1=json.loads((root/'Python/output/manifests/W1_RUN_001.json').read_text())
validation=json.loads((root/'Validation/python_vs_simulink/validation_summary.json').read_text())
assert p1['success'] and w1['success'] and validation['pass']
assert int(load_parameters()['network']['N'])==4
assert w1['public_history_residual']==0
audit=(root/'Simulink/block_architecture_audit.txt').read_text(encoding='utf-8')
assert 'S-Function blocks: 0' in audit and 'MATLAB Function blocks: 0' in audit
assert 'Scope blocks: 7' in audit and 'Forbidden architecture count: 0' in audit
print(f'DATA_QA_PASS tables={len(tables)} figures={len(figures)} slx_bytes={slx.stat().st_size}')
