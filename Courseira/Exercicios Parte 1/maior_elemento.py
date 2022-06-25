def maior_elemento(l):
    acum=l[0]
    if(len(l)>1):
        for i in range(len(l)):
            if(l[i]>acum):
                acum=l[i]
    return acum

#lis=[1,3,4,5,9,7,4]
#print(maior_elemento(lis))