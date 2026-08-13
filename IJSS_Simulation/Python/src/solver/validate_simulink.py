from __future__ import annotations
import csv,json,sys
from pathlib import Path
import numpy as np
from scipy.interpolate import interp1d
from scipy.io import loadmat

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,load_parameters,write_json

p=load_parameters(); py=np.load(ROOT/'Python'/'output'/'raw'/'P1_RUN_001.npz');
data=np.genfromtxt(ROOT/'Simulink'/'output'/'SIMULINK_P1_RUN_001.csv',delimiter=',',names=True)
names=data.dtype.names[1:]; mat=loadmat(ROOT/'Simulink'/'output'/'SIMULINK_P1_RUN_001.mat')
ts=np.asarray(mat['T']).reshape(-1); xs=np.asarray(mat['X'])
tp=py['t']; xp=py['x'].T; end=min(tp[-1],ts[-1]); grid=tp[tp<=end]
fsi=interp1d(ts,xs,axis=0,kind='linear',bounds_error=True); xi=fsi(grid); err=xp[:len(grid)]-xi
absmax=np.max(np.abs(err),axis=0); rms=np.sqrt(np.mean(err**2,axis=0)); reg=float(p['comparison']['regularizer'])
norm=np.max(np.abs(err)/np.maximum(np.abs(xi),reg),axis=0); threshold=float(p['comparison']['python_simulink_threshold'])
summary={'manifest_id':p['manifest_id'],'python_run':'P1_RUN_001','simulink_run':'SIMULINK_P1_RUN_001','variables':list(names),
'common_end_s':float(end),'python_end_s':float(tp[-1]),'simulink_end_s':float(ts[-1]),'stopping_time_difference_s':float(abs(tp[-1]-ts[-1])),
'global_max_absolute_error':float(np.max(absmax)),'global_rms_error':float(np.sqrt(np.mean(err**2))),
'global_max_normalized_error':float(np.max(norm)),'acceptance_threshold':threshold,'pass':bool(np.max(absmax)<=threshold)}
out=ROOT/'Validation'/'python_vs_simulink';out.mkdir(parents=True,exist_ok=True);write_json(out/'validation_summary.json',summary)
with (out/'comparison_errors.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['variable','max_abs_error','rms_error','max_normalized_error']);w.writerows(zip(names,absmax,rms,norm))
(out/'python_vs_simulink_validation.md').write_text(f'''# Python--Simulink Validation

- Manifest: `{p['manifest_id']}`
- Compared runs: `P1_RUN_001` and `SIMULINK_P1_RUN_001`
- Compared variables: all 24 independent states
- Common interval: `0 <= t <= {end:.12g} s`
- Global maximum absolute error: `{np.max(absmax):.6e}`
- Global RMS error: `{np.sqrt(np.mean(err**2)):.6e}`
- Global maximum normalized diagnostic: `{np.max(norm):.6e}`
- Stopping-time difference: `{abs(tp[-1]-ts[-1]):.6e} s`
- Pre-frozen implementation threshold: `{threshold:.6e}` absolute
- Verdict: `{'PASS' if summary['pass'] else 'FAIL'}`

The comparison establishes implementation consistency only. It does not enlarge the local theorem scope.
''',encoding='utf-8')
print(json.dumps(summary,indent=2))
