# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:46:38 2022

@author: Melanie

This file finds the column number for force and displacement files that corresponds
to each sample of the burn conditions
"""

import pandas as pd
import numpy as np

pairs = [("XY_Nov1.xlsx","(11-1-19).xlsx"), #50 sec
         ("XY_Nov6.xlsx","(11-6-19).xlsx"),
         ("XY_Nov8.xlsx","(11-8-19).xlsx"),
         ("XY_Oct1.xlsx","(10-1-19 & 10-2-19).xlsx"), #20 sec
         ("XY_Oct4.xlsx","(10-4-19).xlsx"),
         ("XY_Oct18.xlsx","(10-18-19).xlsx"), #30 sec
         ("XY_Oct22.xlsx","(10-22-19).xlsx"),
         ("XY_Oct23.xlsx","(10-23-19).xlsx"), #40 sec
         ("XY_Oct25.xlsx","(10-25-19).xlsx"),
         ("XY_Oct30.xlsx","(10-30-19).xlsx"),
         ("XY_Sep25.xlsx","(9-25-19).xlsx"), #10 sec
         ("XY_Sep27.xlsx","(9-27-19).xlsx")]

def program(name):
    #reading in file names, removing NaN values
    ramanAndNotebook = pd.read_excel("RamanAndNotebook.xlsx", sheet_name = name, header = None, usecols = [2])[5:].astype('str').to_numpy()
    names = [name[0]+".csv" for name in ramanAndNotebook if name[0][0] == "b"]
    
    #reading in displacement and forces
    disps = pd.read_excel("200F"+names[0][9:11]+"s Displacement.xlsx",nrows=16)
    forces = pd.read_excel("200F"+names[0][9:11]+"s Force.xlsx",nrows=16)
     
    if disps.shape != forces.shape:
        print("bro")
    
    for name in names:
        #reading in the displacement and force of each sample
        try:
            file = pd.read_csv(name)
        except:
            print("huh???")
            continue
        
        d = file.iloc[:,1][1:16]
        f = file.iloc[:,2][1:16]
        
        """The first column corresponds to 'in notebook measurements
        Second column is displacement column
        Third column is force column"""
        for j in range(disps.shape[1]):
            disp = disps.iloc[:,j][1:16]
            if d.astype(float).equals(disp.astype(float)):
                print(name[22:-4],j+1,end=" ")
                break
        
        for j in range(forces.shape[1]):
            force = forces.iloc[:,j][1:16]
            if force.astype(float).equals(f.astype(float)):
                print(j+1)
                break 

def calling(i):
    print("\n"+str(pairs[i][0])+str(pairs[i][1]))
    pair = pairs[i] #Change this number!
    name = pair[0][3:-5]
    program(name)

    
# for i in range(len(pairs)):
#     calling(i)
