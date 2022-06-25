def insertion_sort(lista):
    if(len(lista)>1):
        for i in range(len(lista)):
            for j in range(i,len(lista)-1):
                if (lista[j]>lista[j+1]):
                    for k in range(len(lista)-1,0,-1):
                        if(lista[k]<lista[k-1]):lista[k],lista[k-1]=lista[k-1],lista[k]
    return lista
'''
list=[10, 20, 40, 60, 70, 80, 90, 100, 50, 30]
print(list)
print(insertion_sort(list))
'''