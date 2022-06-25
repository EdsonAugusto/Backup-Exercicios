class Buscador:

    def busca_binaria(self,lista,elemento,min=0,max=None):
        if(max==None):
            max=len(lista)-1
        if(max<min):
            return False
        else:
            m=min+(max-min)//2
        if(lista[m]>elemento):
            return self.busca_binaria(lista,elemento,min,m-1)
        elif(lista[m]<elemento):
            return self.busca_binaria(lista,elemento,m+1,max)
        else:
            return m


from pytest import mark
list=[0,1,2,3,4,5,6,7,8]
@mark.parametrize('lista, entrada, esperado',[
    (list,0,0),
    (list,1,1),
    (list,2,2),
    (list,3,3),
    (list,4,4),
    (list,9,False),
    (list,7,7)
])
def testa_recursão_binaria(lista,entrada,esperado):
    b=Buscador()
    b.busca_binaria(lista,entrada)==esperado





