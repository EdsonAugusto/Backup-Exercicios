def bubble_sort(lista):
    for i in range(len(lista)):
        truck = False
        for j in range(len(lista)-1):
            if (lista[j]>lista[j+1]):
                lista[j],lista[j+1]=lista[j+1],lista[j]
                print(lista)
                truck=True
        if(not truck):
            return lista


#print(bubble_sort([5,1,4,2]))