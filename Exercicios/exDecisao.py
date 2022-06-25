'''
def num_maior(a,b):
    if (a>b):
        return a
    else:
        return b
n=[]
for i in range(2):
    n.append(int(input('Parametro: ')))
print('O maior numero é ',num_maior(n[0],n[1]))

def PosNeg(a):
    if (a>0):
        return 'Número Positivo'
    elif (a<0):
        return  'Número Negativo'
    else:
        return 'Número Neutro'
num=int(input('Numero: '))
print(PosNeg(num))

def MasFen(l):
    if (l=='m'):
        return 'Masculino'
    if (l=='f'):
        return 'Feminino'
    else:
        return 'Sexo Invalido'
s=str(input('Entre com o sexo: M/F '))
print(MasFen(s))

def VogCos(a):
    v=['a','e','i','o','u']
    vm=['A','E','I','O','U']
    c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    cm=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    comp=False
    i=0
    while (comp==False):
        i=0
        while (i<=20):
            if (a==c[i]) or (a==cm[i]):
                return 'consoante'
                comp=True
            if (a!=c[i]) and (a!=cm[i]):
                i=i+1
            if (i>=20):
                i=0
                for i in range(5):
                    if (a == v[i]) or (a == vm[i]):
                        return 'Vogal'
                        comp=True
                    else:
                        return 'Invalido: Não é uma letra'
                        comp=True
p=str(input('Entre com a letra: '))
print(VogCos(p))

def nota(a,b):
    m=(a+b)/2
    if (m>=10):
        return 'Parabéns Aprovado c/ distinção - Média: ',m
    else:
        if (m>=7):
            return 'Aprovado - Média: ',m
        else:
            return 'Reprovado - Média: ',m
n=[]
for i in range(2):
    n.append(int(input('N{}: '.format(i))))
print(nota(n[0],n[1]))

def MaiorMenor(a,b,c):
    if (a>b) and (a>c) and (b>c):
        return 'Maior: {} Menor: {}'.format(a,c)
    if (a>b) and (a>c) and (c>b):
        return 'Maior: {} Menor: {}'.format(a,b)
    if (b>a) and (b>c) and (a>c):
        return 'Maior: {} Menor: {}'.format(b,c)
    if (b>a) and (b>c) and (c>a):
        return 'Maior: {} Menor: {}'.format(b,a)
    if (c>a) and (c>b) and (a>b):
        return 'Maior: {} Menor: {}'.format(c,b)
    else:
        return 'Maior: {} Menor: {}'.format(c,a)
n=[]
for i in range(3):
    n.append(int(input('Numero {}: '.format(i))))
print(MaiorMenor(n[0],n[1],n[2]))

def decrescente(a,b,c):
    if (a<b) and (a<c):
        if (b<c):
            return (a,b,c)
    if (a<b) and (a<c) and (c<b):
            return  (a,c,b)
    if (b<a) and (b<c) and (a<c):
            return (b,a,c)
    if (b<a) and (b<c) and (c<a):
            return (b,c,a)
    if (c<a) and (c<b) and (a<b):
            return (c,a,b)
    else:
        return (c,b,a)
n=[]
for i in range(3):
    n.append(int(input('Numero {}: '.format(i))))
print(decrescente(n[0],n[1],n[2]))

def menorPreco(a,b,c):
    if (a<b) and (a<c):
        return 'Compre A'
    if (b<a)and(b<c):
        return 'Compre B'
    if (c<b)and(c<a):
        return 'Compre C'
n=[]
for i in range(3):
    n.append(float(input('N[{}]'.format(i))))
print(menorPreco(n[0],n[1],n[2]))

def comp():
    cont=True
    while(cont==True):
        c=str(input('[m] Manha [v] Vespertino [n] Noturno: '))
        if(c=='m')or(c=='v')or(c=='n'):
            cont=False
        else:
            cont=True
    if(c=='m'):
        return 'Bom Dia!'
    elif(c=='v'):
        return 'Boa Tarde!'
    else:
        return 'Boa Noite!'
print(comp())


def rSalario():
    r=(20,15,10,5)
    cont=True
    while(cont==True):
        s=float(input('Salario: '))
        if(s<0):
            cont=True
        else:
            cont=False
    if(s<280):
        return 'Salario: {} | Reajuste: {} | % {} | Atualizado: {}'.format(s,(s*r[0])/100,r[0],((s*r[0])/100)+s)
    if(s>280)and(s<700):
        return 'Salario: {} | Reajuste: {} | % {} | Atualizado: {}'.format(s,(s*r[1])/100,r[1],((s*r[1])/100)+s)
    if(s>700)and(s<1500):
        return 'Salario: {} | Reajuste: {} | % {} | Atualizado: {}'.format(s,(s*r[2])/100,r[2],((s*r[2])/100)+s)
    else:
        return 'Salario: {} | Reajuste: {} | % {} | Atualizado: {}'.format(s,(s*r[3])/100,r[3],((s*r[3])/100)+s)
print(rSalario())

def dSemana():
    sem=('Domingo','Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sabado')
    cont=True
    while(cont==True):
        ent=int(input('[0]{} |[1]{} |[2]{} |[3]{} |[4]{} |[5]{} |[6]{}: '.format(sem[0],sem[1],sem[2],sem[3],sem[4],sem[5],sem[6])))
        if(ent<0)or(ent>6):
            cont=True
        else:
            cont=False
    if(ent==0):
        return 'Bom {}!'.format(sem[0])
    elif(ent==1):
        return 'Boa {}!'.format(sem[1])
    elif(ent==2):
        return 'Boa {}!'.format(sem[2])
    elif(ent==3):
        return 'Boa {}!'.format(sem[3])
    elif(ent==4):
        return 'Boa {}!'.format(sem[4])
    elif(ent==5):
        return 'Otima {}!'.format(sem[5])
    else:
        return 'Bom {}!'.format(sem[6])
print(dSemana())

def sNota():
    cont=True
    while(cont==True):
        m=float(input('Media Anual: '))
        if(m<0)or(m>10):
            cont=True
        else:
            cont=False
    if(m>=9)and(m<=10):
        return 'Media: {} - A | Situação: Aprovado'.format(m)
    if(m>=7.5)and(m<9):
        return 'Media: {} - B | Situação: Aprovado'.format(m)
    if(m>=6)and(m<7.5):
        return 'Media: {} - C | Situação: Aprovado'.format(m)
    if(m>=4)and(m<6):
        return 'Media: {} - D | Situação: Reprovado'.format(m)
    if(m<=4):
        return 'Media: {} - E | Situação: Reprovado'.format(m)
print(sNota())

def dTrian():
    cont=True
    t=[]
    while(cont==True):
        for i in range(3):
            t.append(float(input('T[{}]: '.format(i))))
        if((t[0]+t[1])<t[2])or((t[0]+t[2])<t[1])or((t[1]+t[2])<t[0]):
            for j in range(3):
                del(t[0])
            cont=True
        else:
            cont=False
    if(t[0]==t[1])and(t[0]==t[2]):
        return 'Triangulo Equilatero'
    if(t[0]==t[1])or(t[0]==t[2])or(t[1]==t[2]):
        return 'Triangulo Isosceles'
    else:
        return 'Triangulo Escaleno'
print(dTrian())

def bhaskara():
    n=[]
    paran=('a','b','c')
    for i in range(3):
        cont=True
        while(cont==True):
            n.append(float(input('{}: '.format(paran[i]))))
            if(n[0]==0):
                del(n[0])
                cont=True
            else:
                cont=False
    delta=n[1]**2-4*(n[0]*n[2])
    if(delta==0):
        x=-(n[1])/(2*n[0])
        return 'X= {}'.format(x)
    if(delta!=0):
        import math
        x=[]
        x.append((-n[1]+math.sqrt(delta))/(2*n[0]))
        x.append((-n[1]-math.sqrt(delta))/(2*n[0]))
        return 'X¹: {}  |  X²: {}  |Delta: {}'.format(x[0],x[1],delta)
    if(delta<=-1):
        return 'Delta não possui raizes reias'
print(bhaskara())

def bisexto(a):
    bi=1900
    if(a==bi):
        return 'Bisexto'
    if(a>bi):
        while(a>bi):
            bi+=4
        if(a==bi):
            return 'Bisexto'
        else:
            return 'Normal'
    if(a<bi):
        while(a<bi):
            bi-=4
        if(a==bi):
            return 'Bisexto'
        else:
            return 'Normal'

def formData():
    mes=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    f=('Formato Invalido')
    cont=True
    while(cont==True):
        data=str(input('Digite a data [dd/mm/aaaa]: '))
        if(len(data)<=10):
            if(len(data)==8):
                d=int(data[0]+data[1])
                m=int(data[2]+data[3])
                a=int(data[4]+data[5]+data[6]+data[7])
                if(m<1)or(m>12):
                    print(f)
                    cont=True
                else:
                    if(d>days[m-1])or(d<1):
                        print(f)
                        cont=True
                    else:
                        an=bisexto(a)
                        return '{}/{}/{} | Ano: {} | Extenso: {} de {} de {} '.format(d,m,a,an,d,mes[(m-1)],a)
            if(len(data)==10):
                d=int(data[0]+data[1])
                m=int(data[3]+data[4])
                a=int(data[6]+data[7]+data[8]+data[9])
                if (m<1)or(m>12):
                    print(f)
                    cont=True
                else:
                    if(d>days[m-1])or(d<1):
                        print(f)
                        cont=True
                    else:
                        an=bisexto(a)
                        return '{}/{}/{} | Ano: {} | Extenso: {} de {} de {} '.format(d,m,a,an,d,mes[m-1],a)
            else:
                #print(f)
                cont=True
print(formData())
'''
