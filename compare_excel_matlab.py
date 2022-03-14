# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:23:34 2022

@author: Melanie

This compares the excel files to the matlab files, by comparing the file sizes

"""
import pandas as pd


pairs = [("XY_Nov1.xlsx","(11-1-19).xlsx"), #50 sec
         ("XY_Nov6.xlsx","(11-6-19).xlsx"),
         ("XY_Nov8.xlsx","(11-8-19).xlsx"),
         ("XY_Oct1.xlsx","(10-1-19 & 10-2-19).xlsx"), #20 sec
         ("XY_Oct4.xlsx","(10-4-19).xlsx"), #30 sec
         ("XY_Oct18.xlsx","(10-18-19).xlsx"),
         ("XY_Oct22.xlsx","(10-22-19).xlsx"),
         ("XY_Oct23.xlsx","(10-23-19).xlsx"), #40 sec
         ("XY_Oct25.xlsx","(10-25-19).xlsx"),
         ("XY_Oct30.xlsx","(10-30-19).xlsx"),
         ("XY_Sep25.xlsx","(9-25-19).xlsx"), #10 sec
         ("XY_Sep27.xlsx","(9-27-19).xlsx")]

names = ["_originalData","_revisedData","_11-19-2019"]

def get_sheet_names(pair):
    xl1 = pd.ExcelFile(pair[1][:-5]+names[0]+pair[1][-5:])
    xl2 = pd.ExcelFile(pair[1][:-5]+names[1]+pair[1][-5:])
    s1 = set(xl1.sheet_names)
    s2 = set(xl2.sheet_names)
    print(sorted(list(s1.difference(s2))))
    print(len(xl1.sheet_names), len(xl2.sheet_names))
    
for pair in pairs:
    print(pair[0][3:-5])
    get_sheet_names(pair)
