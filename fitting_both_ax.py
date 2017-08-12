import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf
import seaborn as sns

main_df = pd.read_csv('/home/phillip/Downloads/gamma_list_cleared.out')

negA,negB,posA,posB = -11,7.5,-71,71

main_df = main_df[main_df.A < negA]
main_df = main_df[main_df.B > negB]
main_df = main_df[main_df.A > posA]
main_df = main_df[main_df.B < posB]
main_df = main_df[main_df.gamma > 3]
main_df.drop(131,inplace=True)        ##error in an item

main_df.sort_values(['A','B'],inplace=True)  ###

def fitting(xdata,a,b,c,d,e):
    A,B = xdata['A'],xdata['B']
    quad_in_A  = a*A**2+b*A+c
    power_in_B = np.power(np.abs(B),e)
    return (power_in_B * quad_in_A) 
    
def extract_data_from_frame(df):
    ydata = df.gamma
    xdata = df[['A','B']]
    return xdata,ydata

    
xd,yd = extract_data_from_frame(main_df)
p0 = [1,0.1,1,5,-1]
mega = cf(fitting,xd,yd,p0=p0,maxfev=1000000000)[0]

"""
for A_val in np.unique(xd.A): 
    plt.figure()
    xdt,ydt = xd[xd.A==A_val],yd[xd.A==A_val]
    plt.plot(xdt.B,fitting(xdt,*mega))
    plt.scatter(xdt.B,ydt)
    plt.title(str(A_val))
    plt.ylabel('gamma')
    plt.xlabel('B')
"""
error = np.abs(np.divide(yd - fitting(xd,*mega),yd))
fit_landscape = fitting(xd,*mega)
dat_landscape = yd

plt.figure()
data = pd.DataFrame(data={'x':xd.A, 'y':xd.B, 'z':error})
data = data.pivot(index='x', columns='y', values='z')
sns.heatmap(data)
plt.xlabel('B')
plt.ylabel('A')
plt.title('Heat map of error')
#plt.savefig('/home/phillip/Documents/dpd/img/heatmap4.png')
