coluna=int(input('digite largura: '))
linha=int(input('digite altura: '))
i=1
g='#'
if(linha<=2):
    i=1
    while(linha>=i):
        print(g*coluna)
        i+=1
else:
    while(i<=(linha-2)):
        print(g*coluna)
        while(i<=(linha-2)):
            print(g,g,sep=' '*(coluna-2))
            i+=1
        print(g*coluna)