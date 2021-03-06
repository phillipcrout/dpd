import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import os

##for reproducibility
file_direct = os.path.realpath(__file__)
slash = '/'
fd = file_direct.split(sep='/')[:-1]
folder = slash.join(fd)+'/'
os.chdir(folder)


df = pd.read_csv('data/outpute4.txt',header=None,sep='\t',names=['A','B','d'])
#df2 = pd.read_csv('data/outpute5.txt',header=None,sep='\t',names=['A','B','d'])

def theoretical_density(df):
    df['td'] = 3.1 + -1.121*df.A*(df.B-1.136)**(-0.852)

theoretical_density(df)
#theoretical_density(df2)

for B_val in np.unique(df.B):
    plt.figure()
    plt.scatter(df.A[df.B==B_val],df.d[df.B==B_val],color='b')
    plt.scatter(df.A[df.B==B_val],df.td[df.B==B_val],color='r')
    plt.ylabel('Density')
    plt.xlabel('A')
    plt.title('B = ' + str(B_val))
    plt.savefig('./images/density_A_at_B_' + str(B_val) + '.png')
    plt.show()

"""
df['dif'] = df.td - df.d # thus > 0

data = pd.DataFrame(data={'x':df.A, 'y':df.B, 'z':df.d})
data = data.pivot(index='x', columns='y', values='z')

fig = plt.figure()
ax = fig.add_subplot(111)

sns.heatmap(data,cmap='viridis',alpha=0.5,ax=ax)
ax.plot([0,14],[3,6], marker='x',color='red') 
plt.xlabel('B')
plt.ylabel('A')
plt.title('Density')
#plt.savefig('Heat_Map.png')
"""