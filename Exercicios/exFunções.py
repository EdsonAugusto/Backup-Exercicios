'''
def rep(a):
    n=[]
    for i in range(a):
        n.append(a)
        c=''.join(map(str,n))
        #str(n)[1:-1:3]
    return c
d=int(input('Entre com a parada: '))
i=1
while(i<=d):
    print(rep(i))
    i=i+1

def repc(a):
    n=[]
    for i in range(a):
        n.append(i)
        c=' '.join(map(str,n))
    return c
p=int(input('Entre com a parada: '))
b=1
while(b<=(p+1)):
    print(repc(b))
    b=b+1

def soma(a,b,c):
    return '{} + {} + {} = {}'.format(a,b,c,(a+b+c))
n=[]
for i in range(3):
   n.append(int(input('N[{}]: '.format(i))))
print(soma(n[0],n[1],n[2]))

def pOn(a):
    if (a>0):
        return 'Positivo'
    if (a==0):
        return 'Neutro'
    else:
        return 'Negativo'
f=int(input('Numero: '))
print(pOn(f))

def somaImposto(a):
    imp=(a*10)/100
    return 'Imposto R$: {}  Valor Total R$: {}'.format(imp,(a+imp))
im=int(input('Entre com o valor da compra: '))
print(somaImposto(im))

import os
def entdes():
    pg=['AM','PM','Horario: ']
    #th=int(input('{}: 1[{}]  2[{}] '.format(pg[2],pg[0],pg[1])))
    ent=str(input('{}'.format(pg[2])))
    ent1=int(ent[0]+ent[1])
    os.system('cls')
    if(ent1<=12):
        print('{} {}'.format(conh(ent),pg[0]))
    else:
        print('{} {}'.format(conh(ent),pg[1]))

def conh(a):
    a1=a[0]+a[1]
    a2=a[2]+a[3]
    if (a1=='00'):
        return '12:{}'.format(a2)
    elif (a1=='13'):
        return '01:{}'.format(a2)
    elif (a1=='14'):
        return '02:{}'.format(a2)
    elif (a1=='15'):
        return '03:{}'.format(a2)
    elif (a1=='16'):
        return '04:{}'.format(a2)
    elif (a1=='17'):
        return '05:{}'.format(a2)
    elif (a1=='18'):
        return '06:{}'.format(a2)
    elif (a1=='19'):
        return '07:{}'.format(a2)
    elif (a1=='20'):
        return '08:{}'.format(a2)
    elif (a1=='21'):
        return '09:{}'.format(a2)
    elif (a1=='22'):
        return '10:{}'.format(a2)
    elif (a1=='23'):
        return '11:{}'.format(a2)
    else:
        return '{}:{}'.format(a1,a2)
resp=True

while resp==True:
    entdes()
    resp=str(input('Converta novamente: [s]Sim [n]Não '))
    if(resp=='n'):
        resp=False
    else:
        resp=True

def valorPagamento():
    pg=('Dias em Atraso: ','Valor da parcela: ')
    v=[]
    for i in range(2):
       v.append(float(input('{}'.format(pg[i]))))
    if (v[0]>0):
        vm=((v[1]*3)/100)+v[1]
        vj=(((v[0]*0.1)*vm)/100+vm)
        return vj
    else:
        return v[1]
param=[0,0,0]
resp=True
while(resp==True):
    param[1]=valorPagamento()
    print(param[1])
    param[2]+=param[1]
    param[0]+=1
    resp1=str(input('Deseja pagar outro Boleto: '))
    if (resp1=='s'):
        resp=True
    else:
        resp=False
        print('Total de boletos pagos: {}  Total Caixa: {} '.format(param[0],param[2]))

def numinv(a):
    return len(str(a))
n=int(input('Numero: '))
print('{} Casa'.format(numinv(n)))

def numrev(a):
    c=len(str(a))
    f=str(a)
    g=int(c-1)
    rev=[]
    while(g>=0):
        rev.append(int(f[g]))
        g=g-1
    return ''.join(map(str,rev))
n=int(input('Numero: '))
print(numrev(n))

def craps():
    import random
    c=random.randint(2,12)
    return c
def pCraps():
    resp=True
    rod=0
    p_craps=0
    while(resp==True):
        d=int(craps())
        rod+=1
        if(d==7)or(d==11):#and(rod==1):
            p_craps+=d
            resp=False
            return 'Ganhou | Pontos: {} | Rododa: {}'.format(p_craps,rod)
        if(d==2)or(d==12):
            p_craps+=d
            resp=False
            return 'Perdeu | Pontos: {} | Rododa: {}'.format(p_craps,rod)
        else:
            p_craps=d

            print('Reniciar | Pontos: {} | Rododa: {}'.format(p_craps,rod))
            resp = True
print(pCraps())
'''

