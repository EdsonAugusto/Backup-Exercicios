from random import randrange
class Ordenador:
    def selection_sort(self,lista):
        for i in range(len(lista)):
            for j in range(i+1,len(lista)):
                if(lista[i]>lista[j]):lista[i],lista[j]=lista[j],lista[i]
        return lista

    def bubble_sort(self,lista):
        for i in range(len(lista)):
            truck=False
            for j in range(len(lista)-1):
                if(lista[j]>lista[j+1]):lista [j],lista[j+1]=lista[j+1],lista[j];truck=True
            if(not truck):return lista

    def insertion_sort(self,lista):
        if(len(lista)>1):
            for i in range(len(lista)):
                for j in range(i,len(lista)-1):
                    if(lista[j]>lista[j+1]):
                        for k in range(len(lista)-1,0,-1):
                            if(lista[k]<lista[k-1]):lista[k],lista[k-1]=lista[k-1],lista[k]
        return lista

    def merge_sort(self,lista):
        if(len(lista)<=1):
            return lista
        m=len(lista)//2
        lado_a=self.merge_sort(lista[:m])
        lado_b=self.merge_sort(lista[m:])
        return self.merge(lado_a,lado_b)

    def merge(self,lado_a,lado_b):
        if not lado_a:
            return lado_b
        if not lado_b:
            return lado_a
        if(lado_a[0]<lado_b[0]):
            return [lado_a[0]]+self.merge(lado_a[1:],lado_b)
        return [lado_b[0]]+self.merge(lado_a,lado_b[1:])

    def gList(self,x):
        list=[randrange(1000) for i in range(x)]
        return list

'''
o=Ordenador()
lista=o.gList(100)
print(lista)
print(o.bubble_sort(lista))

if __name__=='__main__':
    c=int(input('Entre com o limite da lista: '))
    o=Ordenador()
    print(o.insertion_sort(o.gList(c)))
'''
o=Ordenador()
lista=[10, 20, 40, 60, 70, 80, 90, 100, 50, 30]
print(lista)
print(o.merge_sort(lista))