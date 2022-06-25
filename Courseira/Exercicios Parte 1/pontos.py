x=[]
y=[]
for i in range(2):
    x.append(int(input('x{}:'.format(i))))
for i in range(2):
    y.append(int(input('y{}:'.format(i))))
from math import *
coord=sqrt((x[0]-x[1])**2+(y[0]-y[1])**2)
if(coord>=10):
    print('longe')
else:
    print('perto')

