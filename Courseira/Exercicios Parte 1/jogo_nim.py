from math import *
def computador_escolhe_jogada(n,m):
    if(n<=m)or(n==m):
        return n
    else:
        i=m+1
        while(i>=1):
            if(n%i==0)and((n//i)>1):
                print('1')
                return int(n//i)
            if(n%i==0)and((n//i)<=1):
                if(n==m):
                    return n
                else:
                    print('2')
                    return ceil(n//i)
            if(n%i!=0)and((n/i)>1):
                print('3')
                return ceil(n%i)
            if(n%i!=0)and((n/i)<1):
                return n
            else:i-=1


def usuario_escolhe_jogada(n,m):
    if(n>1):
        print('Agora restam {} peças no tabuleiro.'.format(n))
    else:
        print('Agora restam uma peça no tabuleiro.')
    rit=m+1
    while(rit>m)or(rit<1):
        print()
        rit=int(input('Quantas peças você vai tirar? '))
        if(rit>m)or(rit<1):
            print()
            print('Oops! Jogada inválida! Tente de novo.')
    if(rit>1):
        print('Voce tirou {} peças.'.format(rit))
        return rit
    else:
        print('Voce tirou uma peça.')
        return rit

def main():
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
        partida()
    else:
        print('Voce escolheu um campeonato!')
        print()
        i=1
        while(i<=3):
            print('****Rodada {}****'.format(i))
            print()
            partida()
            i+=1
        print('**** Final do campeonato! ****')
        print()
        print('Placar: Você 0 X 3 Computador')

def partida():
        n=0
        m=0
        while(n<=1)and(m<=0)or(m>=n):
            n=int(input('Quantas peças? '))
            m=int(input('Limite de peças por jogada? '))
            if(n<=1)and(m<=0)or(m>=n):
                print()
                print('Ops, escolha inválida! Tente de novo.')
                print(n%(m+1)==0)
        if(n%(m+1)==0):
            print()
            print('Usuario começa!')
            print()
            while (n>0):
                c=usuario_escolhe_jogada(n,m)
                n-=c
                comp=computador_escolhe_jogada(n,m)
                n-=comp
            #return 'Fim do jogo! O computador ganhou!'
        else:
            print()
            print('Computador começa!')
            print()
            while(n>0):
                comp=computador_escolhe_jogada(n,m)
                n-=comp
                print(comp)
                #if(n<=0):
                    #return 'Fim do jogo! O computador ganhou!'
                us=usuario_escolhe_jogada(n,m)
                n-=us
        return 'Fim do jogo! O computador ganhou!'

print(main())