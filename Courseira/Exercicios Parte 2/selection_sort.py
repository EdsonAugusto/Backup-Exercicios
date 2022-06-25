def ordena(lista):
    if(len(lista)>1):
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if(lista[i]>lista[j]):
                    lista[i], lista[j] = lista[j], lista[i]
    return lista

#list=[0,4,5,8,0,9,88,4]
#print(ordena(list))