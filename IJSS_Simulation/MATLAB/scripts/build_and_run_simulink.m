function build_and_run_simulink
% Build and execute the RT-LAB-oriented basic-block P1 model.
root = fileparts(fileparts(fileparts(mfilename('fullpath'))));
P = load(fullfile(root,'MATLAB','parameters','canonical_parameters.mat'));
mdl = 'main'; outdir = fullfile(root,'Simulink');
if ~exist(outdir,'dir'), mkdir(outdir); end
if bdIsLoaded(mdl), close_system(mdl,0); end
new_system(mdl); load_system('simulink');
set_param(mdl,'Solver','ode45','RelTol',nstr(P.rtol),'AbsTol',nstr(P.atol), ...
    'MaxStep',nstr(P.maxstep),'StopTime',nstr(P.stoptime), ...
    'OutputOption','SpecifiedOutputTimes', ...
    'OutputTimes',sprintf('0:0.005:%.15g',P.stoptime), ...
    'SaveOutput','off','SaveTime','off','SignalLogging','off');

% Top-level ownership follows deployable signal-flow boundaries. No S-function
% or MATLAB Function block implements the closed loop.
for i=1:P.N
    add_dg([mdl sprintf('/DG%d',i)],P,i,[40,45+160*(i-1),175,165+160*(i-1)]);
end
add_block('simulink/Signal Routing/Mux',[mdl '/State_Assembly'], ...
    'Inputs','8','Position',[230 80 235 455]);
add_passthrough([mdl '/Physical_Derivatives'],4,[1010 65 1085 235]);
add_passthrough([mdl '/Privacy_Derivatives'],4,[1010 285 1085 455]);

add_electrical([mdl '/Electrical_Model'],P,[340 40 570 210]);
add_passthrough([mdl '/Power_Calculation'],2,[595 175 635 235]);
add_passthrough([mdl '/Primary_Droop_Controller'],2,[595 40 635 105]);
add_communication([mdl '/Communication_Network'],P,[340 245 570 405]);
add_controller([mdl '/Secondary_Controller'],P,[655 35 930 245]);
add_activation_switch([mdl '/Secondary_Activation_Switch'],P,[955 35 995 125]);
add_privacy([mdl '/Privacy_Mechanism'],P,[655 285 930 455]);
add_logging([mdl '/Observation_and_Logging'],[1160 40 1390 270]);
add_scopes([mdl '/Scopes'],P,[1160 315 1390 575]);
add_exit_guard([mdl '/First_Exit_Stop_Guard'],P,[1010 500 1130 550]);

% Gather each state family without buses so signal ownership is explicit and
% compatible with deterministic partitioning workflows.
families={'V','Vdot','omega','delta','pV','qV','pW','qW'};
for k=1:8
    add_block('simulink/Signal Routing/Mux',[mdl '/' families{k}], ...
        'Inputs',num2str(P.N),'Position',[205,45+50*(k-1),210,75+50*(k-1)]);
    for i=1:P.N
        add_line(mdl,sprintf('DG%d/%d',i,k),sprintf('%s/%d',families{k},i),'autorouting','on');
    end
    add_line(mdl,[families{k} '/1'],sprintf('State_Assembly/%d',k),'autorouting','on');
end

% Physical/electrical signal path.
for k=1:4, add_line(mdl,[families{k} '/1'],sprintf('Electrical_Model/%d',k),'autorouting','on'); end
add_line(mdl,'Secondary_Activation_Switch/3','Electrical_Model/5','autorouting','on');
add_line(mdl,'Secondary_Activation_Switch/4','Electrical_Model/6','autorouting','on');
for k=1:4, add_line(mdl,sprintf('Electrical_Model/%d',k),sprintf('Physical_Derivatives/%d',k),'autorouting','on'); end

% Public communication and frozen secondary-controller paths.
commInputs={'V','omega','pV','pW'};
for k=1:4, add_line(mdl,[commInputs{k} '/1'],sprintf('Communication_Network/%d',k),'autorouting','on'); end
ctlTop={'V','Vdot','omega'};
for k=1:3, add_line(mdl,[ctlTop{k} '/1'],sprintf('Secondary_Controller/%d',k),'autorouting','on'); end
add_line(mdl,'Electrical_Model/7','Primary_Droop_Controller/1','autorouting','on');
add_line(mdl,'Electrical_Model/8','Primary_Droop_Controller/2','autorouting','on');
add_line(mdl,'Primary_Droop_Controller/1','Secondary_Controller/4','autorouting','on');
add_line(mdl,'Primary_Droop_Controller/2','Secondary_Controller/5','autorouting','on');
add_block('simulink/Sinks/Terminator',[mdl '/Power_Monitor_Terminator'],'Position',[605 205 625 225]);
add_block('simulink/Signal Routing/Mux',[mdl '/Power_Monitor_Mux'],'Inputs','2','Position',[585 180 590 235]);
add_line(mdl,'Electrical_Model/5','Power_Calculation/1','autorouting','on');
add_line(mdl,'Electrical_Model/6','Power_Calculation/2','autorouting','on');
add_line(mdl,'Power_Calculation/1','Power_Monitor_Mux/1','autorouting','on');
add_line(mdl,'Power_Calculation/2','Power_Monitor_Mux/2','autorouting','on');
add_line(mdl,'Power_Monitor_Mux/1','Power_Monitor_Terminator/1');
for k=1:4, add_line(mdl,sprintf('Communication_Network/%d',k),sprintf('Secondary_Controller/%d',k+5),'autorouting','on'); end

% Privacy wrapper: public p and private q remain separate signals.
add_line(mdl,'Secondary_Controller/1','Secondary_Activation_Switch/1','autorouting','on');
add_line(mdl,'Secondary_Controller/2','Secondary_Activation_Switch/2','autorouting','on');
add_line(mdl,'Secondary_Activation_Switch/1','Privacy_Mechanism/1','autorouting','on');
add_line(mdl,'Secondary_Activation_Switch/2','Privacy_Mechanism/2','autorouting','on');
for k=5:8, add_line(mdl,[families{k} '/1'],sprintf('Privacy_Mechanism/%d',k-2),'autorouting','on'); end
add_line(mdl,'Privacy_Mechanism/5','Secondary_Activation_Switch/3','autorouting','on');
add_line(mdl,'Privacy_Mechanism/6','Secondary_Activation_Switch/4','autorouting','on');
for k=1:4, add_line(mdl,sprintf('Privacy_Mechanism/%d',k),sprintf('Privacy_Derivatives/%d',k),'autorouting','on'); end

% Return vector derivatives to the corresponding scalar DG integrators.
for k=1:4
    add_block('simulink/Signal Routing/Demux',[mdl sprintf('/d%s_split',families{k})], ...
        'Outputs',num2str(P.N),'Position',[1115,40+50*(k-1),1120,70+50*(k-1)]);
    add_line(mdl,sprintf('Physical_Derivatives/%d',k),sprintf('d%s_split/1',families{k}),'autorouting','on');
    for i=1:P.N, add_line(mdl,sprintf('d%s_split/%d',families{k},i),sprintf('DG%d/%d',i,k),'autorouting','on'); end
end
for k=5:8
    add_block('simulink/Signal Routing/Demux',[mdl sprintf('/d%s_split',families{k})], ...
        'Outputs',num2str(P.N),'Position',[1115,265+50*(k-5),1120,295+50*(k-5)]);
    add_line(mdl,sprintf('Privacy_Derivatives/%d',k-4),sprintf('d%s_split/1',families{k}),'autorouting','on');
    for i=1:P.N, add_line(mdl,sprintf('d%s_split/%d',families{k},i),sprintf('DG%d/%d',i,k),'autorouting','on'); end
end

% Observer-facing and internal diagnostic logging are distinct ports.
logSignals={'State_Assembly/1','pV/1','pW/1','Privacy_Mechanism/5','Privacy_Mechanism/6', ...
    'Secondary_Controller/3','Secondary_Controller/4','Secondary_Controller/5', ...
    'Secondary_Controller/6','Secondary_Controller/7'};
for k=1:numel(logSignals), add_line(mdl,logSignals{k},sprintf('Observation_and_Logging/%d',k),'autorouting','on'); end
scopeSignals={'V/1','omega/1','Privacy_Mechanism/5','Privacy_Mechanism/6','pV/1','pW/1','qV/1','qW/1'};
for k=1:numel(scopeSignals), add_line(mdl,scopeSignals{k},sprintf('Scopes/%d',k),'autorouting','on'); end
add_line(mdl,'Secondary_Controller/3','First_Exit_Stop_Guard/1','autorouting','on');

save_system(mdl,fullfile(outdir,'main.slx'));
set_param(mdl,'SimulationCommand','update');
simout=sim(mdl);
S=simout.get('sim_state'); T=S.time; X=S.signals.values;
if ndims(X)>2, X=squeeze(X); end
if size(X,1)~=numel(T), X=X'; end
families={'V','Vdot','omega','delta','pV','qV','pW','qW'}; vnames={};
for k=1:numel(families), for i=1:P.N, vnames{end+1}=sprintf('%s%d',families{k},i); end, end
Tout=array2table([T X],'VariableNames',[{'time_s'},vnames]);
opath=fullfile(outdir,'output'); if ~exist(opath,'dir'), mkdir(opath); end
writetable(Tout,fullfile(opath,'SIMULINK_P1_RUN_001.csv'));
save(fullfile(opath,'SIMULINK_P1_RUN_001.mat'),'T','X','P');
write_model_audit(mdl,fullfile(outdir,'block_architecture_audit.txt'));
save_system(mdl); close_system(mdl,0); close_system('simulink',0);
end

function add_dg(path,P,i,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',double(pos(:)')); clear_sub(path);
names={'dV','dVdot','domega','ddelta','dpV','dqV','dpomega','dqomega'};
outs={'V','Vdot','omega','delta','pV','qV','pomega','qomega'};
for k=1:8
    add_block('simulink/Sources/In1',[path '/' names{k}],'Port',num2str(k),'Position',[25,20+38*(k-1),55,34+38*(k-1)]);
    add_block('simulink/Continuous/Integrator',[path '/' outs{k}], ...
        'InitialCondition',nstr(P.x0(i+(k-1)*P.N)),'Position',[95,17+38*(k-1),125,37+38*(k-1)]);
    add_block('simulink/Sinks/Out1',[path '/' outs{k} '_out'],'Port',num2str(k),'Position',[170,20+38*(k-1),200,34+38*(k-1)]);
    add_line(path,[names{k} '/1'],[outs{k} '/1']); add_line(path,[outs{k} '/1'],[outs{k} '_out/1']);
end
end

function add_passthrough(path,n,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
for k=1:n
    inport(path,sprintf('in%d',k),k,15,15+40*(k-1));
    outport(path,sprintf('out%d',k),k,105,15+40*(k-1));
    add_line(path,sprintf('in%d/1',k),sprintf('out%d/1',k));
end
end

function add_electrical(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
inNames={'V','Vdot','omega','delta','uV','uomega'};
for k=1:6, inport(path,inNames{k},k,20,25+55*(k-1)); end
% Power-flow network uses one explicit basic-block subsystem per nonzero edge.
for k=[1 4]
    add_block('simulink/Signal Routing/Demux',[path sprintf('/split_%d',k)],'Outputs',num2str(P.N),'Position',[85,20+55*(k-1),90,55+55*(k-1)]);
    add_line(path,[inNames{k} '/1'],sprintf('split_%d/1',k));
end
edgeMap=[];
for i=1:P.N, for j=i+1:P.N, if P.B(i,j)~=0, edgeMap(end+1,:)=[i j]; end, end, end
for e=1:size(edgeMap,1)
    i=edgeMap(e,1); j=edgeMap(e,2);
    add_edge([path sprintf('/Line_%d%d',i,j)],P.B(i,j),[135 20+105*(e-1) 270 105+105*(e-1)]);
    for j=1:2
        node=edgeMap(e,j);
        add_line(path,sprintf('split_1/%d',node),sprintf('Line_%d%d/%d',edgeMap(e,1),edgeMap(e,2),j),'autorouting','on');
        add_line(path,sprintf('split_4/%d',node),sprintf('Line_%d%d/%d',edgeMap(e,1),edgeMap(e,2),j+2),'autorouting','on');
    end
end
% Assemble P and Q at all nodes. Active edge flow is signed by edge orientation.
for i=1:P.N
    incident=find(edgeMap(:,1)==i | edgeMap(:,2)==i);
    psigns='+';
    for e=incident', if edgeMap(e,1)==i, psigns=[psigns '+']; else, psigns=[psigns '-']; end, end
    qsigns=repmat('+',1,1+numel(incident));
    sumblock(path,sprintf('Psum%d',i),psigns,[315,20+38*(i-1)]);
    constant(path,sprintf('Pload%d',i),P.Pload(i),[275,22+38*(i-1)]);
    add_line(path,sprintf('Pload%d/1',i),sprintf('Psum%d/1',i));
    sumblock(path,sprintf('Qsum%d',i),qsigns,[315,190+38*(i-1)]);
    constant(path,sprintf('Qload%d',i),P.Qload(i),[275,192+38*(i-1)]);
    add_line(path,sprintf('Qload%d/1',i),sprintf('Qsum%d/1',i));
    port=2;
    for e=incident'
        add_line(path,sprintf('Line_%d%d/1',edgeMap(e,1),edgeMap(e,2)),sprintf('Psum%d/%d',i,port),'autorouting','on');
        qport=2+(edgeMap(e,2)==i);
        add_line(path,sprintf('Line_%d%d/%d',edgeMap(e,1),edgeMap(e,2),qport),sprintf('Qsum%d/%d',i,port),'autorouting','on');
        port=port+1;
    end
end
add_block('simulink/Signal Routing/Mux',[path '/P'],'Inputs',num2str(P.N),'Position',[380 25 385 145]);
add_block('simulink/Signal Routing/Mux',[path '/Q'],'Inputs',num2str(P.N),'Position',[380 190 385 310]);
for i=1:P.N, add_line(path,sprintf('Psum%d/1',i),sprintf('P/%d',i)); add_line(path,sprintf('Qsum%d/1',i),sprintf('Q/%d',i)); end
% Vector droop drift maps.
bias_gain_sum(path,'Perr','P/1',-P.Pd(:),diag(P.kP(:)),[430 20]);
bias_gain_sum(path,'Werr','omega/1',-P.Wref,eye(P.N),[430 70]);
sumblock(path,'FWsum','++',[570 55]); add_line(path,'Werr_Gain/1','FWsum/1'); add_line(path,'Perr_Gain/1','FWsum/2');
gainblock(path,'FW','FWsum/1',diag(-1./P.tauP(:)),[625 55]);
bias_gain_sum(path,'Qerr','Q/1',-P.Qd(:),diag(-P.kQ(:)),[430 135]);
bias_gain_sum(path,'Verr','V/1',-P.Vref,-eye(P.N),[430 190]);
gainblock(path,'VdotTerm','Vdot/1',diag(-(P.tauQ(:)+P.kV(:))),[430 245]);
sumblock(path,'FVsum','+++',[570 190]); add_line(path,'VdotTerm/1','FVsum/1'); add_line(path,'Verr_Gain/1','FVsum/2'); add_line(path,'Qerr_Gain/1','FVsum/3');
gainblock(path,'FV','FVsum/1',diag(1./(P.tauQ(:).*P.kV(:))),[625 190]);
% Physical derivatives and bounded illustrative uncertainty.
gainblock(path,'uVterm','uV/1',diag(-1./(P.tauQ(:).*P.kV(:))),[760 30]);
gainblock(path,'uWterm','uomega/1',diag(-1./P.tauP(:)),[760 155]);
clock_trig_vector(path,'RV',0.7,'sin',P.RVa(:),[745 75]);
clock_trig_vector(path,'RW',0.5,'cos',P.RWa(:),[745 200]);
sumblock(path,'dVdot','+++',[900 75]); add_line(path,'FV/1','dVdot/1'); add_line(path,'uVterm/1','dVdot/2'); add_line(path,'RV_Vector/1','dVdot/3');
sumblock(path,'domega','+++',[900 200]); add_line(path,'FW/1','domega/1'); add_line(path,'uWterm/1','domega/2'); add_line(path,'RW_Vector/1','domega/3');
outNames={'dV','dVdot_out','domega_out','ddelta','P_out','Q_out','FV_out','FW_out'};
src={'Vdot/1','dVdot/1','domega/1','omega/1','P/1','Q/1','FV/1','FW/1'};
for k=1:8, outport(path,outNames{k},k,995,20+38*(k-1)); add_line(path,src{k},[outNames{k} '/1'],'autorouting','on'); end
end

function add_edge(path,B,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
for k=1:4, inport(path,sprintf('in%d',k),k,15,15+35*(k-1)); end
sumblock(path,'angle','+-',[75 95]); add_line(path,'in3/1','angle/1'); add_line(path,'in4/1','angle/2');
trigblock(path,'sin','angle/1','sin',[125 75]); trigblock(path,'cos','angle/1','cos',[125 115]);
product(path,'ViVk',{'in1/1','in2/1'},[75 35]); product(path,'Praw',{'ViVk/1','sin/1'},[185 55]); gainblock(path,'Pflow','Praw/1',B,[240 55]);
product(path,'V1sq',{'in1/1','in1/1'},[185 100]); product(path,'V2sq',{'in2/1','in2/1'},[185 135]); product(path,'crosscos',{'ViVk/1','cos/1'},[185 170]);
sumblock(path,'Q1raw','+-',[245 110]); add_line(path,'V1sq/1','Q1raw/1'); add_line(path,'crosscos/1','Q1raw/2');
sumblock(path,'Q2raw','+-',[245 155]); add_line(path,'V2sq/1','Q2raw/1'); add_line(path,'crosscos/1','Q2raw/2');
gainblock(path,'Q1','Q1raw/1',B,[300 110]); gainblock(path,'Q2','Q2raw/1',B,[300 155]);
for k=1:3, outport(path,sprintf('out%d',k),k,370,45+50*(k-1)); end
add_line(path,'Pflow/1','out1/1'); add_line(path,'Q1/1','out2/1'); add_line(path,'Q2/1','out3/1');
end

function add_communication(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'V','omega','pV','pomega'}; for k=1:4, inport(path,names{k},k,20,25+60*(k-1)); end
L=diag(sum(P.A,2))-P.A; Bp=diag(P.b(:));
bias_gain_sum(path,'e0V','V/1',-P.Vref,eye(P.N),[105 25]);
bias_gain_sum(path,'e0omega','omega/1',-P.Wref,eye(P.N),[105 85]);
gainblock(path,'pinV','e0V_Gain/1',Bp,[255 25]); gainblock(path,'LpV','pV/1',L,[255 145]);
gainblock(path,'pinW','e0omega_Gain/1',Bp,[255 85]); gainblock(path,'LpW','pomega/1',L,[255 205]);
sumblock(path,'eV','++',[390 65]); add_line(path,'pinV/1','eV/1'); add_line(path,'LpV/1','eV/2');
sumblock(path,'eW','++',[390 165]); add_line(path,'pinW/1','eW/1'); add_line(path,'LpW/1','eW/2');
src={'e0V_Gain/1','e0omega_Gain/1','eV/1','eW/1'}; outn={'e0V_out','e0omega_out','eV_out','eomega_out'};
for k=1:4, outport(path,outn{k},k,485,30+60*(k-1)); add_line(path,src{k},[outn{k} '/1']); end
end

function add_controller(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'V','Vdot','omega','FV','FW','e0V','e0omega','eV','eomega'};
for k=1:9, inport(path,names{k},k,15,15+38*(k-1)); end
add_block('simulink/Signal Routing/Mux',[path '/Reserved_Physical_Monitor'],'Inputs','2','Position',[70 10 75 55]);
add_block('simulink/Sinks/Terminator',[path '/Reserved_Physical_Terminator'],'Position',[95 25 115 45]);
add_line(path,'V/1','Reserved_Physical_Monitor/1'); add_line(path,'omega/1','Reserved_Physical_Monitor/2');
add_line(path,'Reserved_Physical_Monitor/1','Reserved_Physical_Terminator/1');
add_voltage_ppc([path '/Voltage_PPC'],P,[120 20 370 150]);
add_frequency_ppc([path '/Frequency_PPC'],P,[120 190 370 290]);
add_block('simulink/Sinks/Terminator',[path '/Unused_alphaV'],'Position',[395 20 415 40]); add_line(path,'Voltage_PPC/1','Unused_alphaV/1');
add_block('simulink/Sinks/Terminator',[path '/Unused_rhoomega'],'Position',[395 190 415 210]); add_line(path,'Frequency_PPC/1','Unused_rhoomega/1');
add_line(path,'e0V/1','Voltage_PPC/1'); add_line(path,'Vdot/1','Voltage_PPC/2');
add_line(path,'e0omega/1','Frequency_PPC/1');
% cV=tauQ*kV*(FV-dalpha+k2*chi+h*zeta)+kc*eV
gainblock(path,'k2chi','Voltage_PPC/3',P.k2V,[420 50]);
product(path,'hzeta',{'Voltage_PPC/5','Voltage_PPC/4'},[420 95]);
sumblock(path,'cVinner','+-++',[520 65]); add_line(path,'FV/1','cVinner/1'); add_line(path,'Voltage_PPC/2','cVinner/2'); add_line(path,'k2chi/1','cVinner/3'); add_line(path,'hzeta/1','cVinner/4');
gainblock(path,'cVphysical','cVinner/1',diag(P.tauQ(:).*P.kV(:)),[610 65]); gainblock(path,'cVgraph','eV/1',P.kcV,[610 110]);
sumblock(path,'cV','++',[705 80]); add_line(path,'cVphysical/1','cV/1'); add_line(path,'cVgraph/1','cV/2');
% cW=tauP*(FW-alphaW)+kcW*eW
sumblock(path,'cWinner','+-',[520 220]); add_line(path,'FW/1','cWinner/1'); add_line(path,'Frequency_PPC/2','cWinner/2');
gainblock(path,'cWphysical','cWinner/1',diag(P.tauP(:)),[610 210]); gainblock(path,'cWgraph','eomega/1',P.kcW,[610 255]);
sumblock(path,'cW','++',[705 225]); add_line(path,'cWphysical/1','cW/1'); add_line(path,'cWgraph/1','cW/2');
src={'cV/1','cW/1','Voltage_PPC/6','Frequency_PPC/3','Voltage_PPC/4','Frequency_PPC/4','Voltage_PPC/3'};
outs={'cV_out','comega_out','sigmaV','sigmaomega','zetaV','zetaomega','chiV'};
for k=1:7, outport(path,outs{k},k,810,25+43*(k-1)); add_line(path,src{k},[outs{k} '/1'],'autorouting','on'); end
end

function add_voltage_ppc(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
inport(path,'e0',1,15,35); inport(path,'Vdot',2,15,75);
add_schedule([path '/Schedule'],P.rho0V(:),P.rhoinfV(:),P.TV,P.tsec,[70 15 220 95]);
divide(path,'sigma','e0/1','Schedule/1',[265 25]);
trigblock(path,'zeta','sigma/1','atanh',[330 25]);
product(path,'sigma2',{'sigma/1','sigma/1'},[330 70]); constant(path,'ones',ones(P.N,1),[330 110]);
sumblock(path,'oneMinus','+-',[410 85]); add_line(path,'ones/1','oneMinus/1'); add_line(path,'sigma2/1','oneMinus/2');
product(path,'rhoShape',{'Schedule/1','oneMinus/1'},[475 85]);
product(path,'stDrho',{'sigma/1','Schedule/2'},[475 20]);
product(path,'shapeZeta',{'rhoShape/1','zeta/1'},[545 85]); gainblock(path,'k1shapeZeta','shapeZeta/1',P.k1V,[610 85]);
sumblock(path,'alpha','+-',[680 40]); add_line(path,'stDrho/1','alpha/1'); add_line(path,'k1shapeZeta/1','alpha/2');
sumblock(path,'chi','+-',[750 65]); add_line(path,'Vdot/1','chi/1'); add_line(path,'alpha/1','chi/2');
sumblock(path,'dsNum','+-',[680 125]); add_line(path,'chi/1','dsNum/1'); add_line(path,'k1shapeZeta/1','dsNum/2'); divide(path,'dsigma','dsNum/1','Schedule/1',[750 125]);
divide(path,'dzeta','dsigma/1','oneMinus/1',[820 125]);
product(path,'term1',{'dsigma/1','Schedule/2'},[880 15]);
product(path,'term2',{'sigma/1','Schedule/3'},[880 50]);
product(path,'dRhoShapeZeta',{'Schedule/2','oneMinus/1','zeta/1'},[880 85]);
product(path,'twoRhoSigmaDsZeta',{'Schedule/1','sigma/1','dsigma/1','zeta/1'},[880 120]); gainblock(path,'times2','twoRhoSigmaDsZeta/1',2,[965 120]);
product(path,'rhoShapeDzeta',{'rhoShape/1','dzeta/1'},[880 155]);
sumblock(path,'bracket','+-+',[1040 115]); add_line(path,'dRhoShapeZeta/1','bracket/1'); add_line(path,'times2/1','bracket/2'); add_line(path,'rhoShapeDzeta/1','bracket/3');
gainblock(path,'k1bracket','bracket/1',P.k1V,[1120 115]);
sumblock(path,'dalpha','++-',[1200 55]); add_line(path,'term1/1','dalpha/1'); add_line(path,'term2/1','dalpha/2'); add_line(path,'k1bracket/1','dalpha/3');
divide(path,'h','ones/1','rhoShape/1',[1040 175]);
src={'alpha/1','dalpha/1','chi/1','zeta/1','h/1','sigma/1'}; outs={'alpha_out','dalpha_out','chi_out','zeta_out','h_out','sigma_out'};
for k=1:6, outport(path,outs{k},k,1300,20+35*(k-1)); add_line(path,src{k},[outs{k} '/1'],'autorouting','on'); end
end

function add_frequency_ppc(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path); inport(path,'e0',1,15,45);
add_schedule([path '/Schedule'],P.rho0W(:),P.rhoinfW(:),P.TW,P.tsec,[70 15 220 95]);
add_block('simulink/Sinks/Terminator',[path '/Unused_ddrho'],'Position',[245 135 265 155]); add_line(path,'Schedule/3','Unused_ddrho/1');
divide(path,'sigma','e0/1','Schedule/1',[265 25]); trigblock(path,'zeta','sigma/1','atanh',[330 25]);
product(path,'sigma2',{'sigma/1','sigma/1'},[330 70]); constant(path,'ones',ones(P.N,1),[330 110]);
sumblock(path,'oneMinus','+-',[410 85]); add_line(path,'ones/1','oneMinus/1'); add_line(path,'sigma2/1','oneMinus/2');
product(path,'rhoShape',{'Schedule/1','oneMinus/1'},[475 85]); product(path,'stDrho',{'sigma/1','Schedule/2'},[475 20]);
product(path,'shapeZeta',{'rhoShape/1','zeta/1'},[545 85]); gainblock(path,'k1shapeZeta','shapeZeta/1',P.k1W,[610 85]);
sumblock(path,'alpha','+-',[680 45]); add_line(path,'stDrho/1','alpha/1'); add_line(path,'k1shapeZeta/1','alpha/2');
src={'Schedule/1','alpha/1','sigma/1','zeta/1'}; outs={'rho_out','alpha_out','sigma_out','zeta_out'};
for k=1:4, outport(path,outs{k},k,770,25+42*(k-1)); add_line(path,src{k},[outs{k} '/1']); end
end

function add_schedule(path,r0,ri,T,tsec,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
add_block('simulink/Sources/Clock',[path '/Clock'],'Position',[15 20 40 40]);
constant(path,'ActivationTime',tsec,[15 65]);
sumblock(path,'LocalClockRaw','+-',[70 35]); add_line(path,'Clock/1','LocalClockRaw/1'); add_line(path,'ActivationTime/1','LocalClockRaw/2');
constant(path,'ZeroTime',0,[70 75]); add_block('simulink/Math Operations/MinMax',[path '/LocalClock'],'Function','max','Inputs','2','Position',[120 35 155 65]);
add_line(path,'LocalClockRaw/1','LocalClock/1'); add_line(path,'ZeroTime/1','LocalClock/2');
gainblock(path,'s','LocalClock/1',1/T,[180 20]);
constant(path,'one',1,[70 65]); sumblock(path,'oneMinusS','+-',[130 55]); add_line(path,'one/1','oneMinusS/1'); add_line(path,'s/1','oneMinusS/2');
product(path,'s2',{'s/1','s/1'},[190 15]); product(path,'s3',{'s2/1','s/1'},[245 15]);
gainblock(path,'m6s','s/1',-6,[190 55]); constant(path,'fifteen',15,[190 95]); sumblock(path,'polyInner','++',[250 75]); add_line(path,'fifteen/1','polyInner/1'); add_line(path,'m6s/1','polyInner/2');
product(path,'sPoly',{'s/1','polyInner/1'},[315 55]); constant(path,'minusTen',-10,[315 95]); sumblock(path,'poly','++',[375 75]); add_line(path,'minusTen/1','poly/1'); add_line(path,'sPoly/1','poly/2');
product(path,'s3poly',{'s3/1','poly/1'},[435 45]); sumblock(path,'hpre','++',[495 45]); add_line(path,'one/1','hpre/1'); add_line(path,'s3poly/1','hpre/2');
product(path,'om2',{'oneMinusS/1','oneMinusS/1'},[245 125]); product(path,'dhpre',{'s2/1','om2/1'},[315 125]); gainblock(path,'dhscale','dhpre/1',-30/T,[385 125]);
gainblock(path,'twoS','s/1',2,[245 165]); sumblock(path,'oneMinus2s','+-',[315 165]); add_line(path,'one/1','oneMinus2s/1'); add_line(path,'twoS/1','oneMinus2s/2');
product(path,'ddhpre',{'s/1','oneMinusS/1','oneMinus2s/1'},[385 165]); gainblock(path,'ddhscale','ddhpre/1',-60/(T*T),[455 165]);
constant(path,'Tconst',T,[435 205]); add_block('simulink/Logic and Bit Operations/Relational Operator',[path '/beforeT'],'Operator','<=','Position',[500 205 535 235]); add_line(path,'LocalClock/1','beforeT/1'); add_line(path,'Tconst/1','beforeT/2');
for item={'h','dh','ddh'}
    nm=item{1}; add_block('simulink/Signal Routing/Switch',[path '/' nm],'Threshold','0.5','Position',[580,45+60*(find(strcmp({'h','dh','ddh'},nm))-1),620,75+60*(find(strcmp({'h','dh','ddh'},nm))-1)]);
    constant(path,[nm 'zero'],0,[520 65+60*(find(strcmp({'h','dh','ddh'},nm))-1)]);
end
add_line(path,'hpre/1','h/1'); add_line(path,'beforeT/1','h/2'); add_line(path,'hzero/1','h/3');
add_line(path,'dhscale/1','dh/1'); add_line(path,'beforeT/1','dh/2'); add_line(path,'dhzero/1','dh/3');
add_line(path,'ddhscale/1','ddh/1'); add_line(path,'beforeT/1','ddh/2'); add_line(path,'ddhzero/1','ddh/3');
gap=r0-ri; gainblock(path,'rhoGap','h/1',gap,[675 35]); constant(path,'rhoInf',ri,[675 75]); sumblock(path,'rho','++',[755 50]); add_line(path,'rhoGap/1','rho/1'); add_line(path,'rhoInf/1','rho/2');
gainblock(path,'drho','dh/1',gap,[675 115]); gainblock(path,'ddrho','ddh/1',gap,[675 175]);
src={'rho/1','drho/1','ddrho/1'}; for k=1:3, outport(path,sprintf('out%d',k),k,850,45+65*(k-1)); add_line(path,src{k},sprintf('out%d/1',k)); end
end

function add_activation_switch(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'cV','comega','hatV','hatomega'};
for k=1:4, inport(path,names{k},k,15,20+48*(k-1)); end
add_block('simulink/Sources/Clock',[path '/Clock'],'Position',[70 10 95 30]);
constant(path,'ActivationTime',P.tsec,[70 45]);
add_block('simulink/Logic and Bit Operations/Relational Operator',[path '/Enabled'],'Operator','>=','Position',[125 20 160 50]);
add_line(path,'Clock/1','Enabled/1'); add_line(path,'ActivationTime/1','Enabled/2');
constant(path,'ZeroVector',zeros(P.N,1),[125 175]);
for k=1:4
    add_block('simulink/Signal Routing/Switch',[path sprintf('/Switch_%s',names{k})], ...
        'Threshold','0.5','Position',[210,15+48*(k-1),250,45+48*(k-1)]);
    add_line(path,[names{k} '/1'],sprintf('Switch_%s/1',names{k}));
    add_line(path,'Enabled/1',sprintf('Switch_%s/2',names{k}));
    add_line(path,'ZeroVector/1',sprintf('Switch_%s/3',names{k}));
    outport(path,[names{k} '_out'],k,300,22+48*(k-1));
    add_line(path,sprintf('Switch_%s/1',names{k}),sprintf('%s_out/1',names{k}));
end
end

function add_privacy(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'cV','comega','pV','qV','pomega','qomega'}; for k=1:6, inport(path,names{k},k,15,20+45*(k-1)); end
privacy_channel(path,'V','cV','pV','qV',P.lambdaV(:),P.w12V(:),P.w21V(:),P.gammaV,95);
privacy_channel(path,'W','comega','pomega','qomega',P.lambdaW(:),P.w12W(:),P.w21W(:),P.gammaW,225);
src={'dpV/1','dqV/1','dpW/1','dqW/1','uV/1','uW/1'}; outs={'dpV_out','dqV_out','dpomega_out','dqomega_out','uV_out','uomega_out'};
for k=1:6, outport(path,outs{k},k,730,25+45*(k-1)); add_line(path,src{k},[outs{k} '/1'],'autorouting','on'); end
end

function privacy_channel(path,sfx,c,p,q,lambda,w12,w21,gamma,y)
sumblock(path,['z' sfx],'+-',[105 y]); add_line(path,[p '/1'],['z' sfx '/1']); add_line(path,[q '/1'],['z' sfx '/2']);
sumblock(path,['cp' sfx],'+-',[105 y-35]); add_line(path,[c '/1'],['cp' sfx '/1']); add_line(path,[p '/1'],['cp' sfx '/2']);
sumblock(path,['cq' sfx],'+-',[105 y+35]); add_line(path,[c '/1'],['cq' sfx '/1']); add_line(path,[q '/1'],['cq' sfx '/2']);
gainblock(path,['lamP' sfx],['cp' sfx '/1'],diag(lambda),[185 y-35]); gainblock(path,['lamQ' sfx],['cq' sfx '/1'],diag(lambda),[185 y+35]);
add_block('simulink/Math Operations/Abs',[path '/absz' sfx],'Position',[185,y,215,y+25]); add_line(path,['z' sfx '/1'],['absz' sfx '/1']);
constant(path,['tiny' sfx],realmin,[185,y+70]); add_block('simulink/Math Operations/MinMax',[path '/safeabs' sfx],'Function','max','Inputs','2','Position',[255,y+20,290,y+50]); add_line(path,['absz' sfx '/1'],['safeabs' sfx '/1']); add_line(path,['tiny' sfx '/1'],['safeabs' sfx '/2']);
constant(path,['gamma' sfx],gamma,[255 y+70]); divide(path,['ratio' sfx],['gamma' sfx '/1'],['safeabs' sfx '/1'],[330 y+35]);
constant(path,['ones' sfx],ones(numel(lambda),1),[330,y+75]); add_block('simulink/Math Operations/MinMax',[path '/g' sfx],'Function','min','Inputs','2','Position',[400,y+35,435,y+65]); add_line(path,['ratio' sfx '/1'],['g' sfx '/1']); add_line(path,['ones' sfx '/1'],['g' sfx '/2']);
product(path,['gz' sfx],{['g' sfx '/1'],['z' sfx '/1']},[475 y]); gainblock(path,['w21gz' sfx],['gz' sfx '/1'],diag(w21),[535 y]); gainblock(path,['w12z' sfx],['z' sfx '/1'],diag(w12),[535 y+40]);
sumblock(path,['dp' sfx],'+-',[625 y-25]); add_line(path,['lamP' sfx '/1'],['dp' sfx '/1']); add_line(path,['w21gz' sfx '/1'],['dp' sfx '/2']);
sumblock(path,['dq' sfx],'++',[625 y+35]); add_line(path,['lamQ' sfx '/1'],['dq' sfx '/1']); add_line(path,['w12z' sfx '/1'],['dq' sfx '/2']);
sumblock(path,['pq' sfx],'++',[535 y+80]); add_line(path,[p '/1'],['pq' sfx '/1']); add_line(path,[q '/1'],['pq' sfx '/2']); gainblock(path,['u' sfx],['pq' sfx '/1'],0.5,[625 y+80]);
end

function add_logging(path,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'all_states','public_pV','public_pomega','uV','uomega','sigmaV','sigmaomega','zetaV','zetaomega','chiV'};
for k=1:10, inport(path,names{k},k,15,15+32*(k-1)); end
add_block('simulink/Sinks/To Workspace',[path '/State_Log'],'VariableName','sim_state','SaveFormat','Structure With Time','Position',[145 15 260 45]); add_line(path,'all_states/1','State_Log/1');
add_block('simulink/Signal Routing/Mux',[path '/Public_History'],'Inputs','2','Position',[115 65 120 115]); add_line(path,'public_pV/1','Public_History/1'); add_line(path,'public_pomega/1','Public_History/2');
add_block('simulink/Sinks/To Workspace',[path '/Public_Log'],'VariableName','sim_public','SaveFormat','Structure With Time','Position',[165 75 275 105]); add_line(path,'Public_History/1','Public_Log/1');
add_block('simulink/Signal Routing/Mux',[path '/Control_Inputs'],'Inputs','2','Position',[115 130 120 180]); add_line(path,'uV/1','Control_Inputs/1'); add_line(path,'uomega/1','Control_Inputs/2');
add_block('simulink/Sinks/To Workspace',[path '/Control_Log'],'VariableName','sim_control','SaveFormat','Structure With Time','Position',[165 140 275 170]); add_line(path,'Control_Inputs/1','Control_Log/1');
add_block('simulink/Signal Routing/Mux',[path '/Internal_Diagnostics'],'Inputs','5','Position',[115 200 120 295]);
for k=6:10, add_line(path,[names{k} '/1'],sprintf('Internal_Diagnostics/%d',k-5)); end
add_block('simulink/Sinks/To Workspace',[path '/Diagnostic_Log'],'VariableName','sim_diagnostics','SaveFormat','Structure With Time','Position',[165 230 275 260]); add_line(path,'Internal_Diagnostics/1','Diagnostic_Log/1');
end

function add_scopes(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
names={'V','omega','uV','uomega','public_pV','public_pomega','private_qV','private_qomega'};
for k=1:8, inport(path,names{k},k,15,15+38*(k-1)); end
gainblock(path,'Voltage_V','V/1',P.Vbase,[80 15]);
gainblock(path,'Frequency_Deviation_Hz','omega/1',P.fbase,[80 60]);
constant(path,'Frequency_Base_Hz',P.fbase,[160 90]);
sumblock(path,'Frequency_Hz','++',[220 60]); add_line(path,'Frequency_Deviation_Hz/1','Frequency_Hz/1'); add_line(path,'Frequency_Base_Hz/1','Frequency_Hz/2');
constant(path,'Voltage_Base_V',P.Vbase,[160 15]);
sumblock(path,'Voltage_Error_V','+-',[220 15]); add_line(path,'Voltage_V/1','Voltage_Error_V/1'); add_line(path,'Voltage_Base_V/1','Voltage_Error_V/2');
scope_pair(path,'Voltage_V_Scope','Voltage_V',300,15); scope_pair(path,'Voltage_Error_V_Scope','Voltage_Error_V',390,15);
scope_pair(path,'Frequency_Hz_Scope','Frequency_Hz',300,60); scope_pair(path,'Frequency_Error_Hz_Scope','Frequency_Deviation_Hz',390,60);
add_block('simulink/Signal Routing/Mux',[path '/Control_Mux'],'Inputs','2','Position',[95 130 100 175]); add_line(path,'uV/1','Control_Mux/1'); add_line(path,'uomega/1','Control_Mux/2');
add_block('simulink/Sinks/Scope',[path '/Control_Input_Scope'],'Position',[150 135 205 170]); add_line(path,'Control_Mux/1','Control_Input_Scope/1');
add_block('simulink/Signal Routing/Mux',[path '/Public_Mux'],'Inputs','2','Position',[95 195 100 240]); add_line(path,'public_pV/1','Public_Mux/1'); add_line(path,'public_pomega/1','Public_Mux/2');
add_block('simulink/Sinks/Scope',[path '/Public_Message_Scope'],'Position',[150 200 205 235]); add_line(path,'Public_Mux/1','Public_Message_Scope/1');
add_block('simulink/Signal Routing/Mux',[path '/Private_Mux'],'Inputs','2','Position',[95 260 100 305]); add_line(path,'private_qV/1','Private_Mux/1'); add_line(path,'private_qomega/1','Private_Mux/2');
add_block('simulink/Sinks/Scope',[path '/Internal_Private_Scope'],'Position',[150 265 205 300]); add_line(path,'Private_Mux/1','Internal_Private_Scope/1');
end

function add_exit_guard(path,P,pos)
add_block('simulink/Ports & Subsystems/Subsystem',path,'Position',pos); clear_sub(path);
inport(path,'sigmaV',1,15,35);
add_block('simulink/Math Operations/Abs',[path '/abs_sigmaV'],'Position',[70 30 105 55]); add_line(path,'sigmaV/1','abs_sigmaV/1');
constant(path,'FunnelBoundary',(1-P.eventtol)*ones(P.N,1),[125 75]);
add_block('simulink/Logic and Bit Operations/Relational Operator',[path '/AtOrBeyondBoundary'],'Operator','>=','Position',[175 35 210 65]);
add_line(path,'abs_sigmaV/1','AtOrBeyondBoundary/1'); add_line(path,'FunnelBoundary/1','AtOrBeyondBoundary/2');
add_block('simulink/Signal Attributes/Data Type Conversion',[path '/BoundaryDouble'],'OutDataTypeStr','double','Position',[235 35 275 65]); add_line(path,'AtOrBeyondBoundary/1','BoundaryDouble/1');
gainblock(path,'BoundaryCount','BoundaryDouble/1',ones(1,P.N),[305 35]);
add_block('simulink/Sinks/Stop Simulation',[path '/StopAtFirstExit'],'Position',[395 35 450 65]); add_line(path,'BoundaryCount/1','StopAtFirstExit/1');
end

function scope_pair(path,name,src,x,y)
add_block('simulink/Sinks/Scope',[path '/' name],'Position',[x y x+55 y+30]);
line=add_line(path,[src '/1'],[name '/1']); set_param(line,'Name',src);
end

function write_model_audit(mdl,path)
blocks=find_system(mdl,'Type','Block'); types=get_param(blocks,'BlockType');
if ischar(types), types={types}; end
forbidden={'S-Function','MATLABSystem'};
fid=fopen(path,'w'); fprintf(fid,'Model: %s\nTotal blocks: %d\n',mdl,numel(blocks));
u=unique(types); for k=1:numel(u), fprintf(fid,'%s: %d\n',u{k},sum(strcmp(types,u{k}))); end
fprintf(fid,'S-Function blocks: %d\n',sum(strcmp(types,'S-Function')));
fprintf(fid,'MATLAB Function blocks: %d\n',numel(find_system(mdl,'MaskType','MATLAB Function')));
fprintf(fid,'Scope blocks: %d\n',sum(strcmp(types,'Scope')));
fprintf(fid,'Forbidden architecture count: %d\n',sum(ismember(types,forbidden))+numel(find_system(mdl,'MaskType','MATLAB Function')));
fclose(fid);
end

function clear_sub(path)
lines=find_system(path,'FindAll','on','SearchDepth',1,'Type','line'); if ~isempty(lines), delete_line(lines); end
blocks=find_system(path,'SearchDepth',1,'Type','Block'); blocks=setdiff(blocks,{path}); for k=1:numel(blocks), delete_block(blocks{k}); end
end
function inport(path,name,port,x,y), add_block('simulink/Sources/In1',[path '/' name],'Port',num2str(port),'Position',[x,y,x+30,y+14]); end
function outport(path,name,port,x,y), add_block('simulink/Sinks/Out1',[path '/' name],'Port',num2str(port),'Position',[x,y,x+30,y+14]); end
function constant(path,name,value,pos), rect=double([pos(1),pos(2),pos(1)+35,pos(2)+20]); add_block('simulink/Sources/Constant',[path '/' name],'Value',nstr(value),'Position',rect); end
function sumblock(path,name,signs,pos), rect=double([pos(1),pos(2),pos(1)+30,pos(2)+30]); assert(numel(rect)==4,'%s position has %d values',name,numel(rect)); add_block('simulink/Math Operations/Sum',[path '/' name],'Inputs',signs,'Position',rect); end
function gainblock(path,name,src,gain,pos), rect=double([pos(1),pos(2),pos(1)+55,pos(2)+25]); add_block('simulink/Math Operations/Gain',[path '/' name],'Gain',nstr(gain),'Multiplication','Matrix(K*u)','Position',rect); add_line(path,src,[name '/1']); end
function product(path,name,sources,pos), rect=double([pos(1),pos(2),pos(1)+35,pos(2)+25]); add_block('simulink/Math Operations/Product',[path '/' name],'Inputs',repmat('*',1,numel(sources)),'Multiplication','Element-wise(.*)','Position',rect); for k=1:numel(sources), add_line(path,sources{k},sprintf('%s/%d',name,k)); end, end
function divide(path,name,num,den,pos), rect=double([pos(1),pos(2),pos(1)+35,pos(2)+25]); add_block('simulink/Math Operations/Product',[path '/' name],'Inputs','*/','Multiplication','Element-wise(.*)','Position',rect); add_line(path,num,[name '/1']); add_line(path,den,[name '/2']); end
function trigblock(path,name,src,op,pos), rect=double([pos(1),pos(2),pos(1)+45,pos(2)+25]); add_block('simulink/Math Operations/Trigonometric Function',[path '/' name],'Operator',op,'Position',rect); add_line(path,src,[name '/1']); end
function bias_gain_sum(path,name,src,bias,gain,pos), add_block('simulink/Math Operations/Bias',[path '/' name],'Bias',nstr(bias),'Position',[pos(1) pos(2) pos(1)+50 pos(2)+25]); add_line(path,src,[name '/1']); gainblock(path,[name '_Gain'],[name '/1'],gain,[pos(1)+75 pos(2)]); end
function clock_trig_vector(path,name,freq,op,amps,pos), add_block('simulink/Sources/Clock',[path '/' name '_Clock'],'Position',[pos(1) pos(2) pos(1)+25 pos(2)+20]); gainblock(path,[name '_Frequency'],[name '_Clock/1'],freq,[pos(1)+45 pos(2)]); trigblock(path,[name '_Trig'],[name '_Frequency/1'],op,[pos(1)+120 pos(2)]); gainblock(path,[name '_Vector'],[name '_Trig/1'],amps,[pos(1)+190 pos(2)]); end
function s=p_signs(i), if i==1, s='++'; elseif i==2, s='+-+'; else, s='+-'; end, end
function s=q_signs(i), if i==2, s='+++'; else, s='++'; end, end
function s=nstr(x), s=mat2str(double(x),17); end
