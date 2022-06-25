a, b = 1, 1
while a > 0 and b > 0:
    paran = []
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        if a > b:
            a, b = b, a
        for i in range(a,b+1):
            print(i,end=' ')
            paran.append(i)
        print('Sum=%d'%sum(paran))
