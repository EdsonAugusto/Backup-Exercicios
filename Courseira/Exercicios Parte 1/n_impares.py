n=int(input('Digite o valor de n:'))
i=0
cont=0
cond=True
while(cond):
    if(i%2!=0):
        cont+=1
        print(i)
        i+=1
        if(cont>=n):
            cond=False
    else:
        i+=1