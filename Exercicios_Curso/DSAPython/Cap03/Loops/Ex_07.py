# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista
lista, var = [], 4
for i in range(var, 21): 
    if (i % 2 == 0): lista.append(i) 
print(lista)