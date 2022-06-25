ent = int(input())
for i in range(ent):
    paran, cont = float(input()), 0
    while paran >= 0.9:
        paran = paran/2
        cont+=1
        if paran <= 1:
            break
    print('{} dias'.format(cont))