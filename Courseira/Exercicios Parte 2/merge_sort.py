def merge_sort(lista):
    if(len(lista)<=1):
        return lista
    m=len(lista)//2
    lista_a=merge_sort(lista[:m])
    lista_b=merge_sort(lista[m:])
    return merge(lista_a,lista_b)

def merge(lado_a,lado_b):
    if not lado_a:
        return lado_b
    if not lado_b:
        return lado_a
    if(lado_a[0]<lado_b[0]):
        return [lado_a[0]]+merge(lado_a[1:],lado_b)
    return [lado_b[0]]+merge(lado_a,lado_b[1:])

lista=[0,4,5,6,73,2,1,5,6,8,9,2,4]
print(lista)
print(merge_sort(lista))