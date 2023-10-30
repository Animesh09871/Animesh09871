#Using numpy

import numpy as np
'''
v = np.array
print(v)

v0=np.zeros((2,5),int)
print(v0)
v1=np.ones((7,3),float)
print(v1)
v3=np.empty((2,2),complex))
print(v3)
'''
'''
v5=np.array([[8,9,7,5],[5,7,8,9]])
print(v5.shape)

v5=np.array([[8,9,7,5],[5,7,8,9]])
print(v5)
v6=v5.reshape(4,2)

print (v6)
print(v6[2:])

v7=np.arange(7)
print(v7)

v9=np.arange(20,100,5)
print(v9)

v7=np.arange(7,60)
print(v7)
'''
'''
v10=np.linspace(1,20,4)
print(v10)
'''



'''
np.sum(v11)
np.max(v11)
np.min(v11)
np.std(v11)
np.sqrt(v11)
np.average(v11)
np.median(v11)

print(np.sum(v11))
print(np.max(v11))
print(np.std(v11))
print(np.sqrt(v11))
print(np.sum(v11))
print(np.average(v11))
print(np.median(v11))

v12=v11.min(axis=0)
print(v12)

'''
'''
v11=np.array([[20,21,26,28],[5,68,60,50]])
v12=np.array([[1,23,4,56],[6,7,8,9]])
v13=np.vstack((v11,v12))
v13=np.hstack((v11,v12))
print(v13)
for i in np.nditer(v13):
    print(i)
    '''

import pandas as pd
'''
s1=pd.Series([5,6,7,8,9,20.01])
print(s1)

hills = {'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  'Sgòr an Lochain Uaine': (1258, 57.057999, -3.725416)}

print(hills['Cairn Toul'])

f1=pd.DataFrame(hills)
print(f1)

hills2 = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}

f2=pd.DataFrame(hills2)
print(f2)

f3 = pd.DataFrame(hills2, columns=['Hill Name', 'Height', 'Latitude', 'Longitude'])
print(f3)

print(f3.head(2))
#tail(3)

print(f3['Height'])
print(f3.Height <1300)

f4 = f3[f3.height<1300]
print(f4)

f3['Region'] = ['grampian','cairngorm', 'cairngorm', 'cairngorm',]

'''
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#load data into dataframe using pandas
fh=pd.read_csv('scottish_hills.csv')
#print(fh.head(20))

#verify if pandas library methods such as sort work on your data
sfh=fh.sort_values(by=['Height'], ascending=False)
print(sfh.head(5))

#graphblock1 for creating first visualization of scatter plot
x=fh.Height
y=fh.Latitude
plt.scatter(x,y)
plt.savefig('scatter_plot.png')
plt.show()

#graphblock2 updating graph with a different marker sign
plt.scatter(x,y, marker='x')
plt.savefig('scatter_plot.png')
plt.show()

#graphblock3 add a red colored line to my graph
ss=linregress(x,y)
m= ss.slope
b= ss.intercept
plt.plot(x, m*x + b, color='red')
plt.show()

#plot the graph by adding labels to it
ss=linregress(x,y)
m= ss.slope
b= ss.intercept
plt.xlabel('Mount',fontsize=20)
plt.ylabel('Latitude',fontsize=15)
plt.plot(x, m*x + b, color='red')
plt.show()







