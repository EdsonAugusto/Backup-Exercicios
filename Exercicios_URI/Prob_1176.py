def fib(ent):
    lis = [0, 1]
    for i in range(2,ent+1):
        lis.append(lis[i-1]+lis[i-2])
    return lis
ent = int(input())
for i in range(ent):
    tes = int(input())
    said = fib(tes)
    print('Fib({}) = {}'.format(tes, said[tes]))