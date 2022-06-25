n=input('Digite um número inteiro:')
t=int(len(n))
if(t>=2):
    n=int(n)
    cond=True
    while(t>0)and(cond):
        comp=(n%10)
        comp1=((n//10)%10)
        cond=(comp!=comp1)
        n=(n//10)
        t-=1
    if(not cond):
        print('sim')
    else:
        if(cond):
            print('não')
else:
    print('nao')