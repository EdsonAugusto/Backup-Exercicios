from math import *
def computador_escolhe_jogada(n,m):
    if(n>m):
        i=m+1
        while(i>=1):
            if(n%i==0)and((n//i)>1):
                return int(n//i)
            else:
                if(n%i==0)and((n//i)<= 1):
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
    while(ent<1)or(ent>m):
        ent=(int(input('Quantas peças você vai tirar? ')))
        if(ent<1)or(ent>m):
            print()
            print('Oops! Jogada inválida! Tente de novo')
            print()
    return ent

def partida():
    n=0
    while(n<2)or(m>n)or(m<1)or(n==m):
        n=int(input('Quantas peças? '))
        m=int(input('Limite de peças por jogada? '))
        print()
        if(n<2)or(m>n)or(m<1)or(n==m):
            print('Oops! Entrada inválida! Tente de novo!')
    if (n%(m+1)==0):
        print('Voce começa!')
        print()
        while(n>1):
            us=usuario_escolhe_jogada(n,m)
            n-=us
            if(us>1)and(n>1):
                print('Voce tirou {} peças.'.format(us))
                print('Restam {} peças.'.format(n))
                print()
            if(us>1)and(n<=1):
                print('Voce tirou {} peças.'.format(us))
                print('Resta uma peças')
                print()
            if(us<=1)and(n>1):
                print('Voce tirou uma peça')
                print('Restam {} peças'.format(n))
                print()
            else:
                print('Voce tirou uma peça')
                print('Resta uma peças')
                print()
            comp=computador_escolhe_jogada(n,m)
            n-=comp
            if(comp>1):
                print('Computador tirou {} peças'.format(comp))
                if(n<1):
                    break
            else:
                print('Computador tirou uma peça')
                if(n<1):
                    break
            print('Restam {} pecas'.format(n))
            print()
    else:
        print('Computador começa!')
        print()
        while(n>=1):
            comp=computador_escolhe_jogada(n,m)
            n-=comp
            if(comp>1):
                print('Computador tirou {} peças.'.format(comp))
                if(n<1):
                    break
            else:
                print('Computador tirou uma peça.')
                if(n<1):
                    break
            print('Restam {} pecas'.format(n))
            print()
            us=usuario_escolhe_jogada(n,m)
            n-=us
            if(us>1)and(n>1):
                print('Voce tirou {} peças.'.format(us))
                print('Restam {} peças.'.format(n))
                print()
            if(us>1)and(n<1):
                print('Voce tirou {} peças'.format(us))
                print('Resta uma peças')
                print()
            if(us<=1)and(n>2):
                print('Voce tirou uma peça')
                print('Restam {} peças.'.format(n))
                print()
            else:
                print('Voce tirou uma peça')
                print('Resta uma peças')
                print()

def main():
    ent=0
    while(ent!=1)and(ent!=2):
        print('Bem-vindo ao jogo do NIM! Escolha:')
        print()
        print('1 - para jogar uma partida isolada')
        ent=int(input('2 - para jogar um campeonato '))
        print()
        if(ent!=1)and(ent!=2):
            print('Ops, escolha inválida! Tente de novo.')
            print()
    if(ent==1):
        print('Voce escolheu uma partida isolada!')
        print()
        partida()
        print()
        return 'Fim de jogo! Computador ganhou!'
    else:
        print('Voce escolheu um campeonato!')
        print()
        i=1
        while(i<=3):
            print('****Rodada {}****'.format(i))
            print()
            partida()
            print()
            print('Fim de jogo! Computador ganhou!')
            i+=1
        print()
        print('**** Final do campeonato! ****')
        print()
        return 'Placar: Você 0 X 3 Computador'

print(main())