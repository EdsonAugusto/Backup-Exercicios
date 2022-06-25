'''def insertion_numeros(lista,i=0):
    if len(lista) <= 1 or i > len(lista)-1:
        return lista
    else:
        if i < 1 and lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
            return insertion_numeros(lista,i+1)
        if lista[i] < lista[i-1] and i > 0:
            lista[i], lista[1-1] = lista[i-1], lista[i]
            return insertion_numeros(lista,0)

        else:
            return insertion_numeros(lista,i+1)


'''

def insertion_numeros(lista):
    if len(lista) > 1:
        i=0
        while i < len(lista)-1:
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                print(lista)
                if i > 0 and len(lista)-2 > i:
                    i=0
                else:
                    return lista
            else:
                print(lista)
                i+=1
        return lista
    else:
        return lista
test=[1,23,4,5,6,3,2,5,6]
print(insertion_numeros(test))