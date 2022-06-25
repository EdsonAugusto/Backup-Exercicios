def dimensoes(matriz):
    if(len(matriz)>1):
        dim=matriz[0]
        for i in range(1,len(matriz)):
            if(len(dim)!=len(matriz[i])):
                print('False')
        else:
            print(str(len(matriz))+'x'+str(len(matriz[i])))
    else:
        print(str(len(matriz))+'x'+str(len(matriz[0])))

#minha_matriz = [[1], [2], [3]]
#minha_matriz = [[1, 2]]
#dimensoes(minha_matriz)
