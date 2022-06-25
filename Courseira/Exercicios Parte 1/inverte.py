def inverte():
    cond=True
    l=[]
    while(cond):
        l.append(int(input('Digite um número: ')))
        if(l[-1]==0):
            del l[-1]
            return inverte_lista(l)
        else:
            cond=True

def inverte_lista(l):
    if(len(l)>1):
        for i in range(len(l)-1,0,-1):
            print(l[i])
    return l[0]


print(inverte())