### annoyingly can't fit the minimum.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf
    
def exploratory_plotter(df,col):
    for coll in np.unique(main_df[col]):
        to_plot = main_df[main_df[col]==coll]
        plt.figure()
        plt.scatter(to_plot['B'],to_plot['gamma'])
        plt.title(str(coll))
        
def trial_plotting_function(B_value,prefactor,decayconstant,constant,sqr):
    term_1 = prefactor*np.exp(-1*B_value*decayconstant) 
    term_2 = sqr*(B_value-60)**2 
    term_3 = constant
    return term_1+term_2+term_3
    
def finding_A_coef(df):
    array_output = []
    A_values = []
    for A in np.unique(main_df['A']):    
        if A < -15:
            main_df_1 = main_df[main_df['A']==A]
            start_values = [50,0.1,50,10]
            x_data = main_df_1['B']
            y_data = main_df_1['gamma']
            out = cf(trial_plotting_function,x_data,y_data,start_values)
            array_output.append(out[0])
            A_values.append(A)
    return array_output,A_values

main_df = pd.read_csv('/home/phillip/Downloads/gamma_list_cleared.out')
#main_df = main_df[main_df['A']!=5]

#exploratory_plotter(main_df,'A')
output,A_values = finding_A_coef(main_df)
statistics = np.std(output,axis=0)/np.mean(output,axis=0)
## plotting element

for A_value in np.arange(-100,-15,10):
    to_plot = main_df[main_df['A']==A_value]
    B_range = np.linspace(5,100,1000)
    index = A_values.index(A_value)
    param = output[index]
    
    plt.figure()    
    plt.scatter(to_plot['B'],to_plot['gamma'])
    plt.plot(B_range,trial_plotting_function(B_range,param[0],
         param[1],param[2],param[3]),color='r')
    plt.title('At an A value of' + str(A_value))
    plt.xlabel('B Value')
    plt.ylabel('Surface Tension')
    if A_value == -40:
        plt.scatter(xd.B[xd.A==-40],store,marker='x',color='g')
        plt.savefig('A_40_B_variable_double.png')
        

