close all
clear

% Read in the data 
disp = xlsread(     '200F 10s Displacement.csv');
force = xlsread(    '200F 10s Force.csv');
area = fscanf(fopen('200F 10s Area.txt','r'),'%f');
file_name =       "UTinfo 10s.xlsx";
n = size(area,1);

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

%Outputting data
results = [UTStretch, UTStress, E];
writematrix(results,file_name);