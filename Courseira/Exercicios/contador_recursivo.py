from pytest import mark
from time import time
import timeit

def contador_recursivo(n):
    if(n<1):
        return n
    contador_recursivo(n-1)
    print(n)

def cont(n):
    for i in range(n):print(i)

ini=time()
print(contador_recursivo(6))
fim=time()
print(ini-fim)

ini1=time()
print(cont(6))
fim1=time()
print(ini1-fim1)

@mark.parametrize ('entrada, saida',[
    (5,5),
    (7,7),
    (4,4)])
def test_contador(entrada,saida):
    ini=time()
    print(contador_recursivo(6))
    #assert contador_recursivo(entrada)==saida
    fim=time()
    return ini-fim