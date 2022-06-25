def n_primos(a):
#    a=1
#    while(a<2):
#        a=int(input('digite numero: '))
    i=2
    np=[]
    while(i<=a):
        j=1
        cont=0
        while(j<=i):
            if(i%j!=0):
                j+=1
            else:
                cont+=1
                j+=1
        if(cont<=2):
            np.append(int(i))
            i+=1
        else:
            i+=1
    g=len(np)
#    for i in range(g-1):
#        print(np[i])
    return g

print(n_primos(7))
