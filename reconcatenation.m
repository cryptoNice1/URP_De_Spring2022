close all
clear

%opening files
new_file = "XY_Oct25.mat";
file = "(10-25-19)_11-19-2019.xlsx";
sheets = ["S1", "S2", "S3", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S15", "S16", "S17"];
%getting data
n = size(sheets,2);
X = zeros(1643,n);
Y = zeros(1643,n);
for i = 1:n
    raman = readmatrix(file,"Sheet",sheets(i));
    X(:,i) = raman(:,1);
    Y(:,i) = raman(:,2);
end

save(new_file, 'X','Y')