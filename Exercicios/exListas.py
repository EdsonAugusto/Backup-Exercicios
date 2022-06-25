'''
n=[]
i=1
while (i<=5):
        n.append(int(input(('Entre com {}ª número: '.format(i)))))
        i=i+1
for lista in n:
    print(lista)

n=[]
for i in range(10):
    n.append(int(input('Entre com {}ª número: '.format(i))))
i=9
while i>=0:
    print(n[i])
    i-=1

n=[]
m=0
for i in range(4):
    n.append(int(input('N[{}]'.format(i))))
    m=m+n[i]
print('Nota Final: {}  Media: {}'.format(m,(m/4)))

def cos(a):
    cos=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','v','y','x','z']
    cosm=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','W','V','Y','X','Z']
    for i in range(21):
        if (a==cos[i]) or (a==cosm[i]):
            return True
            break
    else:
        return False
def entcos():
    l=[]
    cons=[]
    dif=[]
    for i in range(10):
        l.append(str(input('Letra[{}]: '.format(i))))
    i=0
    while (i<=9):
        if (cos(l[i])==True):
            cons.append(str(l[i]))
            i+=1
        else:
            i+=1
    print(cons)
entcos()

def Numinf():
    num=[[],[],[],[]]
    for i in range(20):
        num[0].append(int(input('N[{}]: '.format(i))))
        if(num[0][i]!=0):
            if(num[0][i]%2==0):
                num[1].append(int(num[0][i]))
            else:
                num[2].append(int(num[0][i]))
        if (num[0][i]>1):
            tdiv=0
            j=1
            while(j<=num[0][i]):
                if(num[0][i]>1)and(num[0][i]%j==0):
                    tdiv+=1
                    j+=1
                else:
                    j+=1
            if (tdiv<=2):
                num[3].append(int(num[0][i]))
    return num
def formNum(a):
    a[0]='-'.join(map(str,a[0]))
    a[1]='-'.join(map(str,a[1]))
    a[2]='-'.join(map(str,a[2]))
    a[3]='-'.join(map(str,a[3]))
    return 'Números digitados: {}  |Pares: {}  |Impares: {}  |Primos: {}'.format(a[0],a[1],a[2],a[3])
print(formNum(Numinf()))

def Escola():
    al=[]
    n=[[],[],[],[],[],[],[],[],[],[]]
    m=[0,0,0,0,0,0,0,0,0,0]
    sit=[]
    for i in range(10):
        al.append(str(input('Aluno [{}]: '.format(i))))
        for j in range(4):
            com=True
            while(com==True):
                n[i].append(int(input('Nota [{}]: '.format(j))))
                if(n[i][j]>10):
                    del(n[i][j])
                    com=True
                else:
                    m[i]+=n[i][j]
                    com=False
        m[i]=m[i]/4
        if (m[i]>=7):
            sit.append(str('Aprovado!'))
        else:
            sit.append(str('Reprovado!'))
    return al,n,m,sit
def formEscola(a,b,c,d):
    for i in range(10):
        print('Aluno: {} | N1:{} N2:{} N3:{} N4:{} | Média: {} | Situação: {}'.format(a[i],b[i][0],b[i][1],b[i][2],b[i][3],c[i],d[i]))

ini=Escola()
a=ini[0]
b=ini[1]
c=ini[2]
d=ini[3]
print(formEscola(a,b,c,d))
'''
