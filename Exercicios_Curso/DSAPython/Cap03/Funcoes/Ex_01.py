# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro)e  depois faça uma chamada à função para listar os números
def par():
    for i in range(2,21,2): print(i)

def par1():
    i=2
    while (i <= 20): print(i); i += 2
    
par()
par1()