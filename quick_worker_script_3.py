### annoyingly can't fit the minimum.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf
    
def trial_plotting_function(A_value,prefactor,decay_constant,constant,quad,lin):
    #term_1 = prefactor * np.exp(-1*decay_constant*A_value)
    term_1 = 0    
    term_2 = constant
    term_3 = quad * A_value**2
    term_4 = lin *A_value
    return term_1 + term_2 + term_3 + term_4
    
def finding_B_coef(df):
    array_output = []
    B_values = []
    for B in np.unique(main_df['B']):    
        if B > -5:
            main_df_1 = main_df[main_df['B']==B]
            start_values = [1,1,1,1,1]
            x_data = main_df_1['A'][main_df['A']>-95]
            y_data = main_df_1['gamma'][main_df['A']>-95]
            out = cf(trial_plotting_function,x_data,y_data,start_values)
            array_output.append(out[0])
            B_values.append(B)
    return array_output,B_values

main_df = pd.read_csv('/home/phillip/Downloads/gamma_list_cleared.out')
output,B_values = finding_B_coef(main_df)
statistics = np.std(output,axis=0)/np.mean(output,axis=0)
## plotting element

for B_value in np.unique(main_df.B):
    to_plot = main_df[main_df['B']==B_value]
    A_range = np.linspace(-100,0,1000)
    index = B_values.index(B_value)
    param = output[index]
    
    plt.figure()    
    plt.scatter(to_plot['A'],to_plot['gamma'])
    plt.plot(A_range,trial_plotting_function(A_range,param[0],param[1],param[2],
    param[3],param[4]),color='r')
    
