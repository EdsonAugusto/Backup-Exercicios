n=int(input('Digite um número inteiro:'))
t=int(len(str(n)))
i=0
soma=0
while(i<=t):
    soma+=n%10
    n=n//10
    i+=1
print(soma)