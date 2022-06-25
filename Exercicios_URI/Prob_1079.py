ent = int(input())
for i in range(ent):
    med = list(map(float, input().split()))
    calc = ((med[0]*2)+(med[1]*3)+(med[2]*5))/10
    print('{:.1f}'.format(calc))