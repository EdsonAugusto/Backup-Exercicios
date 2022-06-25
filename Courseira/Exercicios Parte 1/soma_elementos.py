def soma_elementos(l):
    if(len(l)>1):
        while(len(l)>1):
            l[0]+=l[1]
            del l[1]
    return l[0]


#lis=[7,8,9]
#print(soma_elementos(lis))