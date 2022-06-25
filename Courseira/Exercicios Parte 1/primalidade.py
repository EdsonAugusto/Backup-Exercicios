n=int(input('Digite um número inteiro:'))
i=1
contp=0
while(i<n):
    if(n%i==0):
       contp+=1
       i+=1
    else:
        i+=1
if(contp<2):
    print('primo')
else:
    print('não primo')