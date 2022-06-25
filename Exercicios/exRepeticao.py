'''
def note():
    resp=True
    while(resp==True):
        n=int(input('Nota [0]|[10]: '))
        if(n>10):
            resp=True
        else:
            return 'Note: {}'.format(n)
print(note())

def login():
    resp=True
    n=str(input('Nome: '))
    while(resp==True):
        s=str(input('Senha: '))
        if(n==s):
            resp=True
        else:
            return 'Login: {}  | Senha: {}'.format(n,s)
print(login())

def cadastro():
    resp=True
    while(resp==True):
        n=str(input('Nome: '))
        if(len(n)<3):
            resp=True
        else:
            resp=False
    resp1=True
    while(resp1==True):
        i=int(input('Idade: '))
        if(i<0)or(i>120):
            resp1=True
        else:
            resp1=False
    resp2=True
    while(resp2==True):
        s=str(input('Sexo [m] | [f]: '))
        if(s=='m')or(s=='f'):
            resp2=False
        else:
            resp2=True
    resp3=True
    while(resp3==True):
        r=str(input('Estado Civil: [s] [c] [v] [d] '))
        if(r=='s')or(r=='c')or(r=='v')or(r=='d'):
            resp3=False
        else:
            resp3=True
    return 'Nome: {} | Idade: {} | Sexo: {} | Estado Civil: {}'.format(n,i,s,r)
print(cadastro())

def cpop():
    from math import ceil
    pop=[]
    por=[]
    for i in range(2):
        pop.append(int(input('População {}: '.format(i))))
        por.append(int(input('Porcetagem {}: '.format(i))))
    anos=0
    if(pop[0]>pop[1]):
        while(pop[0]>=pop[1]):
            pop[0]=((pop[0]*por[0]/100)+pop[0])
            pop[1]=((pop[1]*por[1]/100)+pop[1])
            anos+=1
        return 'População 0: {} | População 1: {} | Anos: {}'.format(ceil(pop[0]),ceil(pop[1]),anos)
    else:
        if(pop[0]<pop[1]):
            while(pop[0]<=pop[1]):
                pop[0]=((pop[0]*por[0]/100)+pop[0])
                pop[1]=((pop[1]*por[1]/100)+pop[1])
                anos+=1
        return 'População 0: {} | População 1: {} | Anos: {}'.format(ceil(pop[0]),ceil(pop[1]),anos)
print(cpop())
'''
