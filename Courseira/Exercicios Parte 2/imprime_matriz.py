def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            if(len(matriz[i])-1>k):
                print(matriz[i][k],end=' ')
            else:
                print(matriz[i][k])
minha=[[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha)