def computador_escolhe_jogada(n,m):
    if(n>m):
        i=2
        while(i<=n):
            if(n%i==0)and((n//i)>1):
                print('1')
                return int(n//i)
            if(n%i!=0)and((n//i)<=1):
                print('2')
                return int(n//i)
            else:i+=1
            print('3')
    else:
        print('4')
        return n

print(computador_escolhe_jogada(9,5))