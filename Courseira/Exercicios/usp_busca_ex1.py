'''Escreva um programa que leia uma sequência com N números reais e imprime a sequência eliminando os elementos repetidos.
Esse exercício pode ser dividido em 2 partes:'''
def acha(lista,x):
    for i in range(len(lista)):
        if(lista[i]==x):
            return True
    return False

def main():
    lista=[]
    n=1
    while(n!=0):
        n=float(input(('Digite um número ou 0 para sair.')))
        cond=acha(lista,n)
        if not cond:
            lista.append(n)
    return lista

print(main())
