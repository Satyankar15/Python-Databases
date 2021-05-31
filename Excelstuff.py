# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:02:08 2020

@author: satya
"""

import os
import openpyxl

abc=dict()
folder=r"C:\Users\satya\Desktop\Desktop Documents"
os.chdir(folder)
workbook=openpyxl.load_workbook('Life Wasted.xlsx')
sheet=workbook['Test Sheet']
#cell=sheet['D7']
for i in range(2,12):
    game='C'+str(i)
    #game=sheet[game].value
    hrs='D'+str(i)
    #hrs=sheet[hrs].value
    #print("Cell value of cell is "+str(sheet['C7'].value)+","+str(cell.value))
    print(str(i-1)+". "+str(sheet[game].value)+" "+str(sheet[hrs].value))
    abc[game]=hrs

#for i,j in abc.items():
   # print("Game "+i+" Hours "+str(j))