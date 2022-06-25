def encontra_impares(lista,lImpares=None):
    if(lImpares==None):
        lImpares=[]
    if(len(lista)<1):
        return lImpares
    if(lista[0]%2!=0):
        lImpares.append(lista[0])
        return encontra_impares(lista[1:],lImpares)
    else:
        return encontra_impares(lista[1:],lImpares)

#list=[2,3,4,5,6]
#print(encontra_impares(list))