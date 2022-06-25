def ordenada(lista):
    for i in range(len(lista)):
        if(i<len(lista)-1):
            if(lista[i]>lista[i+1]):
                return False
    return True

#list=[0,4,5,6]
#print(ordenada(list))