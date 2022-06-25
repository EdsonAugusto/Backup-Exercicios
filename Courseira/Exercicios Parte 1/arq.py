# if(m>(n%(m+1)))or(n%(m+1)==0):
# return 'sim'
# else:
# return 'nao'

#print(n/(m+1),(n%(m+1)==0),'a')
# print(n/(m+1),(n%(m+1)==0),'b')

#/Inicio jogo pt1
'''
def inicio():
    ent=0
    while(ent!=1)and(ent!=2):
        print('Bem-vindo ao jogo do NIM! Escolha:')
        print('1 - para jogar uma partida isolada')
        ent=int(input('2 - para jogar um campeonato '))
        print()
        if(ent!=1)and(ent!=2):
            print('Ops, escolha inválida! Tente de novo.')
            print()
    if(ent==1):
        print('Voce escolheu uma partida isolada!')
        print()
        n=0
        m=0
        while(n<=1)and(m<=0)or(m>=n):
            n=int(input('Quantas peças? '))
            m=int(input('Limite de peças por jogada? '))
            if(n<=1)and(m<=0)or(m>=n):
                print()
                print('Ops, escolha inválida! Tente de novo.')
                print()
        if(m>(n%(m+1)))or(n%(m+1)==0):
            print()
            print('Usuario começa!')
            print()
            while(n>0):
                c=usuario_escolhe_jogada(m)
                n-=c
                print(n)
                comp=computador_escolhe_jogada(n,m)
                n-=comp
                print(n)
        else:
            print()
            print('Computador começa!')
            print()
            while(n>0):
                comp=computador_escolhe_jogada(n,m)
                n-=comp
                print(n)
                us=usuario_escolhe_jogada(n,m)
                n-=us
                print(n)

    else:
        print('Voce escolheu um campeonato!')
        return 'Funciona 2'

print(inicio())
'''
'''
def computador_escolhe_jogada(n,m):
    if(n/(m+1)>0)and(n%(m+1)==0):
        if(n==1):
            print('Computador tirou uma peça.')
            return n
        else:
            if(n!=1):
                print('Computador tirou {} peças'.format(int(n/(m+1))))
                return int(n/(m+1))
    else:
        if(n>m):
            print('Computador tirou {} peças'.format(m))
            return m
        else:
            if(n>1):
                print('Computador tirou {} peças'.format(n))
                return n
            else:
                print('Computador tirou um peças')
                return n
'''
'''
def computador_escolhe_jogada(n,m):
    if(n>m):
        cond=False
        i=2
        while(cond):
            if(i%(m+1)==0)and((i//(m+1))>1):
                #print('1')
                return (i//(m+1))
            if(i%(m+1)==0)and((i//(m+1))<=1):
                #print('2')
                return (i//(m+1))
            else:
                i+=1
                cond=(i%(m+1)==0)
            #print('3')
    else:
        #print('4')
        if(n<m)and(n>0):
            return n
  '''
'''
from math import *
def computador_escolhe_jogada(n,m):
    if(n>m):
        i=m+1
        while(i>=1):
            print(i)
            if(n%i==0)and((n//i)>1):
                print('1')
                return int(n//i)
            else:
                if(n%i==0)and((n//i)<=1):
                    print('2')
                    return ceil(n%i)
                else:
                    if(n%i!=0)and((n/i)>1):
                        print('3')
                #print(i)
                        print(ceil(n%i))
                        return ceil(n%i)
                    else:i-=1
                    #print('4')
    else:
        #if(n==m):

        print('5')
        return n
'''

'''
def computador_escolhe_jogada(n,m):
    if(n==m):
        return n
    if(n>m):
        i=m+1
        while(i>=1):
            if(n%i==0)and((n//i)>1):
                print('1')
                return int(n//i)
            else:
                if(n%i==0)and((n//i)<=1):
                    print('2')
                    return m
                else:
                    if(n%i!=0)and((n/i)>1):
                        print('3')
                        return ceil(n%i)
                    else:
                        if(n%i!=0)and((n/i)<1):
                            return n
                        else:i-=1
    if(n<=m):
        return n
'''
'''
#def computador_escolhe_jogada(n,m):
#        if(n/(m+1)>0)or(n%(m+1)==0):
#            print(n/(m+1),(n%(m+1)==0))
#            return int(n/(m+1))
#        else:
#            print(n/(m+1),(n%(m+1)==0))
#            return m
#print(computador_escolhe_jogada(5,3))
#def usuario_escolhe_jogada(n,m):
#    rit=m+1
#    while(rit>m):
#        rit=int(input('Quantas peças você vai tirar? '))
#        if(rit>m):
#            print('Oops! Jogada inválida! Tente de novo.')
#    return rit
def computador_escolhe_jogada(n,m):
    if(n/(m+1)>0)or(n%(m+1)==0):
        if(n==1):
            print('Computador tirou uma peça.')
            return n
        else:
            if(n!=1):
                print('Computador tirou {} peças'.format(str(int(n/(m+1)))))
                return int(n/(m+1))
    else:
        return n
print(computador_escolhe_jogada(4,2))
'''
from math import *
def computador_escolhe_jogada(n,m):
    if(n>m):
        i=m+1
        while(i>=1):
            if(n%i==0)and((n//i)>1):
                return int(n//i)
            else:
                if(n%i==0)and((n//i)<=1):
                    print(ceil(n%i))
                    return ceil(n%i)
                else:
                    if(n%i!=0)and((n/i)>1):
                        return ceil(n%i)
                    else:
                        i-=1
    else:
        return n

def usuario_escolhe_jogada(n,m):
    ent=0
    while(ent<1)or(ent > m):
        ent=(int(input('Quantas peças você vai tirar? ')))
        if(ent<1)and(ent>m):
            print('Oops! Jogada inválida! Tente de novo')
    if(ent>1):
        print('Você tirou {} peças.'.format(ent))
        return ent
    else:
        print('Você tirou uma peça.')
        return ent

def partida():
    n=0
    while(n<2)or(m>n)or(m<1)or(n==m):
        n=int(input('Quantas peças? '))
        m=int(input('Limite de peças por jogada? '))
        print()
        if(n<2)or(m>n)or(m<1)or(m==n):
            print('Oops! Entrada inválida! Tente de novo!')
            print()
    if(n%(m+1)==0):
        print('Voce começa!')
        print()
        while(n>=1):
            us=usuario_escolhe_jogada(n,m)
            n-=us
            print('Restam {} pecas'.format(n))
            print()
            comp=computador_escolhe_jogada(n,m)
            n-=comp
            if(comp>=2):
                print('Computador tirou {} peças.'.format(comp))
                if(n==0):
                    return 'Fim de jogo! Computador ganhou!'
            else:
                print('Computador tirou uma peça.')
        if(n<1):
            print()
            return 'Fim de jogo! Computador ganhou!'
        else:
            print('Restam {} pecas'.format(n))
            print()
    else:
        print('Computador começa!')
        print()
        while(n>=0):
            comp=computador_escolhe_jogada(n,m)
            n-=comp
            if (comp>=2):
                print('Computador tirou {} peças.'.format(comp))
            else:
                if(n>=2):
                    print('Computador tirou uma peça.')
                    print()
                else:
                    print('Computador tirou uma peça.')
                    return 'Fim de jogo! Computador ganhou!'
                print('Restam {} pecas'.format(n))
                print()
                us=usuario_escolhe_jogada(n,m)
                n-=us
                print('Restam {} pecas'.format(n))
                print()
    if(n<1):
        return 'Fim de jogo! Computador ganhou!'