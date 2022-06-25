x, y = 1, 0
while x != y:
    x, y = map(int, input().split())
    if x != y:
        if x > y: print('Decrescente')
        else: print('Crescente')