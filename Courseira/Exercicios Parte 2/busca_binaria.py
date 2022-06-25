def busca(lista,x):
    crit=0
    ind=[]
    f=len(lista)-1
    while(crit<=f):
        mid=(crit+f)//2
        ind.append(mid)
        if(lista[mid]==x):
            for i in ind:print(i)
            return mid
        if(x<lista[mid]):
            f=mid-1
        else:
            crit=mid+1
    for i in ind:print(i)
    return False
