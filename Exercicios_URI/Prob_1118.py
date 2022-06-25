def menu():
    val = 0
    while val != 1 and val != 2:
        print('novo calculo (1-sim 2-nao)')
        val = int(input(''))
    return val

ent = 1
while ent != 2:
    paran, a = [], -1
    while a < 0 or a > 10 or len(paran) <= 1:
        a = float(input())
        if a < 0 or a > 10: print('nota invalida')
        else: paran.append(a)
    print('media = {:.2f}'.format((paran[0]+paran[1])/2))
    ent = menu()
