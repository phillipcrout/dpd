import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

path = '/data/'

df = pd.read_csv(path+"outpute4.txt",header=None,sep='\t',names=['A','B','d'])
df2 = pd.read_csv(path+'outpute5.txt',header=None,sep='\t',names=['A','B','d'])

def theoretical_density(df):
    df['td'] = 3.1 + -1.121*df.A*(df.B-1.136)**(-0.852)

theoretical_density(df)
theoretical_density(df2)

B_val = 50
plt.scatter(df.A[df.B==B_val],df.d[df.B==B_val],color='b',)
plt.scatter(df2.A,df2.d,color='b')
plt.scatter(df2.A,df2.td,color='r')
plt.ylabel('Density')
plt.xlabel('B')
#plt.savefig('Constant_A.png')
plt.show()

df['dif'] = df.td - df.d # thus > 0

data = pd.DataFrame(data={'x':df.A, 'y':df.B, 'z':df.dif})
data = data.pivot(index='x', columns='y', values='z')

fig = plt.figure()
ax = fig.add_subplot(111)

sns.heatmap(data,cmap='viridis',alpha=0.5,ax=ax)
ax.plot([0,14],[3,6], marker='x',color='red') 
plt.xlabel('B')
plt.ylabel('A')
plt.title('Heat map of deviation from theory')
#plt.savefig('Heat_Map.png')
