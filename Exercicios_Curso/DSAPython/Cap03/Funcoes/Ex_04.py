# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def funcRecebe(a, *vartuple):
    print(a)
    for lis in vartuple:
        print(lis)


print(funcRecebe(5))