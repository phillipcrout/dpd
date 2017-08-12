import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf

main_df = pd.read_csv('/home/phillip/Downloads/gamma_list_cleared.out')
main_df = main_df[main_df.A<-11]

def constant_A_function(B,prefactor,decayconstant,A2,A1,A0):
    return prefactor*np.exp(-decayconstant*B)+ A2*B**2 + A1*B + A0

def constant_B_function(A,B2,B1,B0):
    return B2*A**2 + B1*A + B0

def extract_data_from_frame(df):
    ydata = df.gamma
    xdata = df.A
    if len(np.unique(xdata)) < 2:
        xdata = df.B
    return xdata,ydata
    

A_list,coef_list = [],[]
for A_value in np.unique(main_df.A):
    constant_A_frame = main_df[main_df['A']==A_value]
    xdata,ydata = extract_data_from_frame(constant_A_frame)
    start_value = [50,0.1,50,10,1]
    coef = cf(constant_A_function,xdata,ydata,start_value)
    A_list.append(A_value)
    coef_list.append(coef[0])
    
alpha = [x[0] for x in coef_list]
beta =  [x[1] for x in coef_list]
phi =   [x[2] for x in coef_list]
delta = [x[3] for x in coef_list]