import pytest
def busca_binaria(lista,elemento,min=0,max=None):
    if(max==None):
        max=len(lista)-1
    if(max<min):
        return False
    else:
        m=min+(max-min)//2
    if(lista[m]>elemento):
        return busca_binaria(lista,elemento,min,m-1)
    elif(lista[m]<elemento):
        return busca_binaria(lista,elemento,m+1,max)
    else:
        return m

list=[0,1,2,3,4,5,6,7]
@pytest.mark.parametrize('lista, valor, esperado',[
    (list,0,0),
    (list,1,1),
    (list,4,4),
    (list,9,False),
    (list,10,False)
    ])
def testa_binario(lista,valor,esperado):
    assert busca_binaria(lista,valor)==esperado