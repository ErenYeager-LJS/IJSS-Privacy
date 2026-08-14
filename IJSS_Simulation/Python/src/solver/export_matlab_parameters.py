from pathlib import Path
import sys
import numpy as np
from scipy.io import savemat

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,load_parameters
from solver.run_physical import initial_state

p=load_parameters(); plant=p['plant']; ctl=p['controller']; pr=p['privacy']; ppc=p['ppc']; d=p['domain']; scenario=p['scenario']; base=p['base']
payload={'manifest_id':p['manifest_id'],'N':p['network']['N'],'B':np.array(p['network']['electrical_susceptance'],float),
'A':np.array(p['network']['cyber_adjacency'],float),'b':np.array(p['network']['pinning'],float),
'Vref':plant['V_ref'],'Wref':plant['omega_ref'],'tauP':np.array(plant['tau_P']), 'tauQ':np.array(plant['tau_Q']),
'kP':np.array(plant['k_P']),'kQ':np.array(plant['k_Q']),'kV':np.array(plant['k_V']),
'Pd':np.array(plant['P_d']),'Qd':np.array(plant['Q_d']),'Pload':np.array(plant['P_load']),'Qload':np.array(plant['Q_load']),
'RVa':np.array(plant['uncertainty_amplitude_V']),'RWa':np.array(plant['uncertainty_amplitude_omega']),
'k1V':ctl['k1_V'],'k2V':ctl['k2_V'],'kcV':ctl['kc_V'],'k1W':ctl['k1_omega'],'kcW':ctl['kc_omega'],
'rho0V':np.array(ppc['rho0_V']),'rhoinfV':np.array(ppc['rhoinf_V']),'rho0W':np.array(ppc['rho0_omega']),'rhoinfW':np.array(ppc['rhoinf_omega']),'TV':ppc['T_V'],'TW':ppc['T_omega'],
'lambdaV':np.array(pr['lambda_V']),'lambdaW':np.array(pr['lambda_omega']),'w12V':np.array(pr['w12_V']),'w21V':np.array(pr['w21_V']),'w12W':np.array(pr['w12_omega']),'w21W':np.array(pr['w21_omega']),'gammaV':pr['gamma_V'],'gammaW':pr['gamma_omega'],
'x0':initial_state(p),'rtol':p['solver']['rtol'],'atol':p['solver']['atol'],'maxstep':p['solver']['max_step'],
'stoptime':p['solver']['horizon_P1'],'tsec':scenario['secondary_activation_s'],
'eventtol':p['solver']['event_tolerance'],
'teval':scenario['prescribed_evaluation_s'],'Vbase':base['voltage_V'],'fbase':base['frequency_Hz'],
'Pbase':base['active_power_W'],'Prated':np.array(base['active_power_rated_W'])}
dest=ROOT/'MATLAB'/'parameters'/'canonical_parameters.mat';dest.parent.mkdir(parents=True,exist_ok=True);savemat(dest,payload,do_compression=True);print(dest)
