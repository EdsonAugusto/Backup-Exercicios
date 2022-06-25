# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e imprima a lista
from random import randrange

def altLista(l, num = randrange(0,5)):
    l.append(num)
    return l

lista = [0, 1, 2, 3]

for i in range(2):
    lista = altLista(lista)

print(lista)