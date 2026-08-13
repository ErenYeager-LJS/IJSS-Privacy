function sfun_ijss_closed_loop(block)
setup(block);
end

function setup(block)
P=load(fullfile(fileparts(fileparts(mfilename('fullpath'))),'parameters','canonical_parameters.mat'));
n=double(P.N); block.NumDialogPrms=0; block.NumInputPorts=0; block.NumOutputPorts=1;
block.SetPreCompOutPortInfoToDynamic; block.OutputPort(1).Dimensions=8*n;
block.OutputPort(1).DatatypeID=0; block.OutputPort(1).Complexity='Real';
block.OutputPort(1).SamplingMode='Sample';
block.NumContStates=8*n; block.SampleTimes=[0 0]; block.SimStateCompliance='DefaultSimState';
block.RegBlockMethod('InitializeConditions',@Init); block.RegBlockMethod('Derivatives',@Derivatives); block.RegBlockMethod('Outputs',@Outputs);
end

function Init(block)
P=params(); block.ContStates.Data=P.x0(:);
end

function Outputs(block)
block.OutputPort(1).Data=block.ContStates.Data;
end

function Derivatives(block)
P=params(); x=block.ContStates.Data; n=double(P.N); S=splitstate(x,n);
[PV,QV]=powerflow(S.V,S.delta,P); L=diag(sum(P.A,2))-P.A;
e0V=S.V-P.Vref; e0W=S.omega-P.Wref; eV=P.b(:).*e0V+L*S.pV; eW=P.b(:).*e0W+L*S.pW;
[rhoV,drhoV,ddrhoV]=schedule(block.CurrentTime,P.rho0V(:),P.rhoinfV(:),P.TV);
[rhoW,drhoW,~]=schedule(block.CurrentTime,P.rho0W(:),P.rhoinfW(:),P.TW);
sigV=e0V./rhoV; sigW=e0W./rhoW; zetaV=atanh(sigV); zetaW=atanh(sigW);
hV=1./(rhoV.*(1-sigV.^2));
alphaV=sigV.*drhoV-P.k1V*rhoV.*(1-sigV.^2).*zetaV; chi=S.Vdot-alphaV;
dsig=(chi-P.k1V*rhoV.*(1-sigV.^2).*zetaV)./rhoV; dzeta=dsig./(1-sigV.^2);
dalpha=dsig.*drhoV+sigV.*ddrhoV-P.k1V*(drhoV.*(1-sigV.^2).*zetaV-2*rhoV.*sigV.*dsig.*zetaV+rhoV.*(1-sigV.^2).*dzeta);
alphaW=sigW.*drhoW-P.k1W*rhoW.*(1-sigW.^2).*zetaW;
FW=(-(S.omega-P.Wref)-P.kP(:).*(PV-P.Pd(:)))./P.tauP(:);
FV=(-(P.tauQ(:)+P.kV(:)).*S.Vdot-(S.V-P.Vref)-P.kQ(:).*(QV-P.Qd(:)))./(P.tauQ(:).*P.kV(:));
cV=P.tauQ(:).*P.kV(:).*(FV-dalpha+P.k2V*chi+hV.*zetaV)+P.kcV*eV;
cW=P.tauP(:).*(FW-alphaW)+P.kcW*eW;
zV=S.pV-S.qV; zW=S.pW-S.qW; gV=min(1,P.gammaV./max(abs(zV),realmin)); gW=min(1,P.gammaW./max(abs(zW),realmin));
dpV=P.lambdaV(:).*(cV-S.pV)-P.w21V(:).*gV.*zV; dqV=P.lambdaV(:).*(cV-S.qV)+P.w12V(:).*zV;
dpW=P.lambdaW(:).*(cW-S.pW)-P.w21W(:).*gW.*zW; dqW=P.lambdaW(:).*(cW-S.qW)+P.w12W(:).*zW;
uV=(S.pV+S.qV)/2; uW=(S.pW+S.qW)/2; RV=P.RVa(:)*sin(.7*block.CurrentTime); RW=P.RWa(:)*cos(.5*block.CurrentTime);
dV=S.Vdot; dVdot=FV-uV./(P.tauQ(:).*P.kV(:))+RV; domega=FW-uW./P.tauP(:)+RW; ddelta=S.omega;
block.Derivatives.Data=[dV;dVdot;domega;ddelta;dpV;dqV;dpW;dqW];
end

function S=splitstate(x,n)
names={'V','Vdot','omega','delta','pV','qV','pW','qW'};
for k=1:numel(names), S.(names{k})=x((k-1)*n+1:k*n); end
end

function [Pout,Qout]=powerflow(V,d,P)
n=double(P.N);Pout=P.Pload(:);Qout=P.Qload(:);
for i=1:n
 for k=1:n
  if P.B(i,k)~=0
   a=d(i)-d(k);Pout(i)=Pout(i)+V(i)*V(k)*P.B(i,k)*sin(a);
   Qout(i)=Qout(i)+V(i)^2*P.B(i,k)-V(i)*V(k)*P.B(i,k)*cos(a);
  end
 end
end
end

function [rho,drho,ddrho]=schedule(t,r0,ri,T)
s=t/T;if s<=1,h=1-10*s^3+15*s^4-6*s^5;dh=(-30*s^2+60*s^3-30*s^4)/T;ddh=(-60*s+180*s^2-120*s^3)/(T*T);else,h=0;dh=0;ddh=0;end
rho=ri+(r0-ri)*h;drho=(r0-ri)*dh;ddrho=(r0-ri)*ddh;
end

function P=params()
persistent C;if isempty(C),C=load(fullfile(fileparts(fileparts(mfilename('fullpath'))),'parameters','canonical_parameters.mat'));end;P=C;
end
