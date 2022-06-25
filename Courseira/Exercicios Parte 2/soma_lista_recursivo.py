def soma_lista(lista):
    if(len(lista)<=1):
        return lista[0]
    return lista[0]+soma_lista(lista[1:])
'''
from pytest import mark
lista1=[1,2]
lista2=[1,2,3]
lista3=[1,2,3,4]
lista4=[1,2,3,4,5]
@mark.parametrize('entrada, saida',[
    (lista1,3),
    (lista2,6),
    (lista3,10),
    (lista4,15)
])
def test_somalista(entrada,saida):
    assert soma_lista(entrada)== saida
'''
