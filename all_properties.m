close all
clear

titles = ["200F10s.xlsx","200F20s.xlsx","200F30s.xlsx","200F40s.xlsx","200F50s.xlsx"];
areas = ["A10s.xlsx","A20s.xlsx","A30s.xlsx","A40s.xlsx","A50s.xlsx"];
i = 1;
final_matrix = [];
for i = 1:5
    %Getting all properties
    stress = readmatrix(titles(i),'Sheet','Stress');
    strain = readmatrix(titles(i),'Sheet','Strain');
    force = readmatrix(titles(i),'Sheet','Forces');
    disp = readmatrix(titles(i),'Sheet','Displacements');
    area = readmatrix(areas(i),'Sheet','Sheet1');

    %Getting the parameters
    [Mu,Gamma] = OneTimeParam(stress,strain);
    [UTStretch,UTStress,E] = MaterialProperties(force,disp,area);
    label = i*ones(size(Mu,1),1);

    final_matrix = vertcat(final_matrix,[label,Mu,Gamma,UTStretch,UTStress,E]);
end

%Writing to a matrix
writematrix(final_matrix,"All Data.xlsx",'Sheet',1)