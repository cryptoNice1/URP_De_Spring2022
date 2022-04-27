function [UTStretch,UTStress,E] = MaterialProperties(force,disp,area)

n = size(force,2);

%computing stress,strain, and toughness
UTStretch = zeros(n,1);
UTStress = zeros(n,1);
E = zeros(n,1);

for i = 1:size(area,1)
    [M,I]=max(force(:,i)); %M picks the max. value, I picks the max. index
    UTStretch(i,1) = disp(I,i)/9.53;
    UTStress(i,1) = force(I,i)/area(i);
    E(i,1) = trapz((disp(1:I,i)/9.53),(force(1:I,i)/area(i)));
end

end