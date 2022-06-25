'''
while (test==False):
    if (tin[0]>=m) and (tin[1]>m):
        test = True
        print(comp[0], m, comp[1], cont[0], comp[2], cont[1])
    else:
        #del(cont[0])
        #del(cont[0])
        #cont.append(1)
        #cont.append(0)
        tin[0]=tin[0]+tin[0]
        cont[0]=cont[0]+1
        test=False
    if (tin[1]<=m)and(tin[2]>m):
        #del (cont[0])
        #del (cont[0])
        #cont.append(1)
        #cont.append(0)
        tin[1]=tin[1]+tin[0]
        cont[0]=cont[0]+1
        if (cont[1]<=1):
            cont[1]=cont[1]+1
        else:
            test=False
    if (tin[2]<=m):
        tin[2]=tin[2]+tin[1]
        cont[1]=cont[1]+1
        if (cont[1]<2):
            cont[1]=cont[1]+1
        else:
            test = False
    else:
        test=True
        print(comp[0],m,comp[1],cont[0],comp[2],cont[1])
'''
def OpcaoCompra(m):
    m=m**2
    qpin=[21.8,108,216]
    cont=True
    totcomp=[0,0]
    while(cont!=False):
        if(m>(qpin[2]+qpin[1])):
            while(m>(qpin[2]+qpin[1])):
                qpin[2]=qpin[2]+qpin[1]
                totcomp[1]=totcomp[1]+3
            cont=True
        if(m>qpin[2])and(m<=(qpin[2]+qpin[1])):
            qpin[2]=qpin[2]+qpin[0]
            totcomp[1]=totcomp[1]+2
            totcomp[0]=totcomp[0]+1
            cont=True
        if(m>qpin[1])and(m<=qpin[2]):
            qpin[1]=qpin[1]+qpin[0]
            totcomp[1]=totcomp[1]+1
            totcomp[0]=totcomp[0]+1
            cont=True
        if(m>qpin[0])and(m<=qpin[1]):
            qpin[0]=qpin[0]+qpin[0]
            totcomp[0]=totcomp[0]+1
            cont=True
        if(m<=qpin[0]):
            totcomp[0]=totcomp[0]+1
            cont=True

        else:
            cont=False
    return 'Metro²: {}  Galão 3.6L: {}  Latão 18L: {}'.format(m,totcomp[0],totcomp[1])


e=int(input('Entre com o valor do L: '))
print(OpcaoCompra(e))