root=fileparts(fileparts(fileparts(mfilename('fullpath'))));
addpath(fullfile(root,'MATLAB','functions'));
P=load(fullfile(root,'MATLAB','parameters','canonical_parameters.mat'));
mdl='main'; outdir=fullfile(root,'Simulink'); if ~exist(outdir,'dir'),mkdir(outdir);end
if bdIsLoaded(mdl),close_system(mdl,0);end
new_system(mdl); open_system(mdl);
set_param(mdl,'Solver','ode45','RelTol',num2str(P.rtol),'AbsTol',num2str(P.atol),'MaxStep',num2str(P.maxstep),'StopTime',num2str(P.stoptime),...
 'OutputOption','SpecifiedOutputTimes','OutputTimes',sprintf('0:0.005:%.15g',P.stoptime),...
 'SaveOutput','on','OutputSaveName','yout','SaveTime','on','TimeSaveName','tout');
add_block('simulink/User-Defined Functions/Level-2 MATLAB S-Function',[mdl '/Frozen_Closed_Loop'],'FunctionName','sfun_ijss_closed_loop','Position',[80 130 230 190]);
add_block('simulink/Sinks/Terminator',[mdl '/PlantBus'],'Position',[300 40 320 60]);
add_block('simulink/Sinks/Terminator',[mdl '/PublicBus'],'Position',[300 90 320 110]);
add_block('simulink/Sinks/Terminator',[mdl '/PrivateInternalBus'],'Position',[300 140 320 160]);
add_block('simulink/Sinks/Terminator',[mdl '/DiagnosticsBus'],'Position',[300 190 320 210]);
busnames={'PlantBus','PublicBus','PrivateInternalBus','DiagnosticsBus'};
for k=1:4,add_line(mdl,'Frozen_Closed_Loop/1',[busnames{k} '/1'],'autorouting','on');end
names={'DG_and_Plant_Subsystem','Controller_Subsystem','Communication_Subsystem','Privacy_Subsystem','Measurement_and_Event_Subsystem','Logging_Subsystem'};
ys=[270 340 410 480 550 620];
for k=1:numel(names)
 add_block('simulink/Ports & Subsystems/Subsystem',[mdl '/' names{k}],'Position',[80 ys(k) 330 ys(k)+45]);
 delete_line_if_present([mdl '/' names{k}]);
 delete_block([mdl '/' names{k} '/In1']);delete_block([mdl '/' names{k} '/Out1']);
end
add_block('simulink/Sinks/To Workspace',[mdl '/State_Logging'],'VariableName','sim_state','SaveFormat','Structure With Time','Position',[500 135 610 175]);add_line(mdl,'Frozen_Closed_Loop/1','State_Logging/1','autorouting','on');
save_system(mdl,fullfile(outdir,'main.slx')); simout=sim(mdl);
S=simout.get('sim_state'); T=S.time; X=S.signals.values; if ndims(X)>2,X=squeeze(X);end
if size(X,1)~=numel(T),X=X';end
vnames={'V1','V2','V3','Vdot1','Vdot2','Vdot3','omega1','omega2','omega3','delta1','delta2','delta3','pV1','pV2','pV3','qV1','qV2','qV3','pW1','pW2','pW3','qW1','qW2','qW3'};
Tout=array2table([T X],'VariableNames',[{'time_s'},vnames]);outpath=fullfile(root,'Simulink','output');if ~exist(outpath,'dir'),mkdir(outpath);end
writetable(Tout,fullfile(outpath,'SIMULINK_P1_RUN_001.csv'));save(fullfile(outpath,'SIMULINK_P1_RUN_001.mat'),'T','X','P');
close_system(mdl,0);

function delete_line_if_present(sub)
ln=find_system(sub,'FindAll','on','Type','line');if ~isempty(ln),delete_line(ln);end
end
