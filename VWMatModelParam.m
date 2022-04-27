function VWParams = VWMatModelParam(StressAll,StrainAll)
% StressAll: column vector (no. of columns=1) containing stress data for 1 tissue sample
% StrainAll: column vector (no. of columns=1) containing corresponding strain data for the tissue sample

% Size (no. of rows) of 'StressAll' MUST BE same as 'StrainAll'.

% Trim the stress-strain data only for up to 70% of the max. stress
[StrsMax,Imax]=max(StressAll);
StrsCutoff=0.7*StrsMax;
idx=find(StressAll(1:Imax)<=StrsCutoff,1,'last');

strs=StressAll(1:idx);
strn=StrainAll(1:idx);

% Least squares algorithm options
options = optimoptions('lsqcurvefit','FiniteDifferenceType', 'central', 'FunctionTolerance', 1e-8, 'OptimalityTolerance', 1e-8, 'MaxFunctionEvaluations', 1000,'Display','off');

% Veronda-Westmann model fitting
% Initialize the parameters to be optimized
xVW0=[0,0];

% Least squares fitting algorithm
[xVW,resnormVW,resVW, flagVW, outputVW] = lsqcurvefit(@funcVW,xVW0,strn,strs,[0,0], [inf inf], options);

% Rsquare value of the model
RsqVW = 1-sum((strs-funcVW(xVW,strn)).^2)/sum((strs-mean(funcVW(xVW,strn))).^2);

% Final Veronda-Westmann model parameters: 
% xVW(1)= Mu;
% xVW(2) = Gamma;

VWParams=xVW;

% Function that calculates model prediction value of stress
function strs=funcVW(par,strn)

lambdaU=1+strn;
I1bar=(lambdaU.^2)+(2./lambdaU);
% I2bar=(lambdaU.^(-2))+(2*lambdaU);

% U=((par(1)/par(2))*(exp(par(2)*(I1bar-3))-1))-par(1)*(I2bar-3);
dUdI1=par(1)*exp(par(2)*(I1bar-3));
dUdI2=-par(1);

strs=2*(1-(lambdaU.^(-3))).*((lambdaU.*dUdI1)+dUdI2);

end
end