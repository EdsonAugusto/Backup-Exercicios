def maior_primo(n):
    if(n>1):
        i=n-1
        cont=1
        while(i>0)and(cont<=2):
            while(i>0):
                if(n%i==0):
                    cont+=1
                    i-=1
                else:
                    if(n%i!=0):
                        i-=1
            if(cont<=2):
                return n
            else:
                if(cont>2):
                    n-=1
                    i=n-1
                    cont=1
    else:
        return 'Digite numero maior que 1'
print(maior_primo(4967))
