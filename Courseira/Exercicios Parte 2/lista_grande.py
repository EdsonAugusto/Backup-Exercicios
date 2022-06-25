from random import randint
def lista_grande(n):
    list=[]
    for i in range(n):
        list.append(randint(0,n))
    return list

#print(lista_grande(50))
