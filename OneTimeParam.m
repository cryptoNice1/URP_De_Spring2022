function [mus,gammas] = OneTimeParam(stress,strain)
    n = size(stress,2);

    mus = zeros(n,1);
    gammas = zeros(n,1);

    for i = 1:n
        StressAll = rmmissing(stress(:,i));
        StrainAll = rmmissing(strain(:,i));

        VWParams = VWMatModelParam(StressAll,StrainAll);
        mus(i,1) = VWParams(1);
        gammas(i,1) = VWParams(2);
    end
    
end