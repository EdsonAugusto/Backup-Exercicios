'''
def compS():
    s=[]
    for i in range(2):
        s.append(str(input('String[{}] '.format(i))))
    if(s[0]==s[1]):
        return 'String são iguais'
    else:
        if(len(s[0])==len(s[1])):
            return 'String são diferentes porém tamanhos são iguais'
        if(len(s[0])!=len(s[1])):
            return 'Tamanho e String são diferentes'
print(compS())

def invNome():
    n=str(input('Nome: '))
    i=int(len(n)-1)
    inv=''
    while(i>=0):
        inv+=n[i]
        i-=1
    return inv.upper()
print(invNome())

def nfil():
    n=str(input('Nome: '))
    for i in range(int(len(n))):
        print(n[i])
nfil()

def lnome():
    n=str(input('Nome: '))
    for i in range(int(len(n)+1)):
        print(n[:i])
    print('------------')
    g=len(n)
    while(g>=0):
        print(n[:g])
        g-=1
lnome()
'''
def ifev():
    cont=[0,0,0,0,0,0]
    v=('a','A','e','E','i','I','o','O','u','U',' ')
    f=str(input('Frase: '))
    c=int(len(f))
    i=0
    while(i<=c):
        j=0
        while(j<=10):
            if (j <= 10):
                if(f[i]==v[j]):
                    if(j==0)or(j==1):
                        cont[0]+=1
                        i+=1
                    elif(j==2)or(j==3):
                        cont[1]+=1
                        i+=1
                    elif(j==4)or(j==4):
                        cont[2]+=1
                        i+=1
                    elif(j==6)or(j==7):
                        cont[3]+=1
                        i+=1
                    elif(j==8)or(j==9):
                        cont[4]+=1
                        i+=1
                    elif(j==10):
                        cont[5]+=1
                        i+=1
            else:
                j+=1
            else:
                i+=1
    return 'Espaços: {} | a:{} | e:{} | i:{} | o:{} | u:{}'.format(cont[5],cont[0],cont[1],cont[2],cont[3],cont[4])
print(ifev())
