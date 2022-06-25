'''while True:
    try:
        ent=[]
        n=int(input())
        for i in range(n):
            ent.append(float(input()))
        ent.sort()
        print('{:.2f}'.format(ent[0]))
    except EOFError:
        break'''
alunos = list(map(int,input().split()))
print(alunos)