loop = int(input())
for i in range(loop):
    ent, div = int(input()), 0
    for d in range(ent,0,-1):
        if (ent % d) == 0:
            div += 1 
    if div <= 2:
        print('{} eh primo'.format(ent))
    else:
        print('{} nao eh primo'.format(ent))