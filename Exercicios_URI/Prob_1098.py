import math
ent, i = (1,2,3), 0
while i <= 2:
    for j in range(len(ent)):
        if (type(i) == int) or (i==1.0) or (i >= 1.9):
            print('I={} J={}'.format(math.ceil(i), int(ent[j]+i)))
        else:
            print('I={:.1f} J={:.1f}'.format(i, ent[j]+i))
    i += 0.2