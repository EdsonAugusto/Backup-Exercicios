n=[]
paran=('a','b','c')
for i in range(3):
    cont=True
    while(cont==True):
        n.append(float(input('{}: '.format(paran[i]))))
        if(n[0]==0):
            del(n[0])
            cont=True
        else:
            cont=False
delta=n[1]**2-4*(n[0]*n[2])
if(delta==0):
    x=-(n[1])/(2*n[0])
    print('a raiz desta equação é {}'.format(x))
if(delta>0):
    import math
    x=[]
    x.append((-n[1]+math.sqrt(delta))/(2*n[0]))
    x.append((-n[1]-math.sqrt(delta))/(2*n[0]))
    if(x[0]<x[1]):
        print('as raízes da equação são {} e {}'.format(x[0],x[1]))
    else:
        print('as raízes da equação são {} e {}'.format(x[1],x[0]))
else:
    print('esta equação não possui raízes reais')
