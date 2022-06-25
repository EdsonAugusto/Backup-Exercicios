ent = 5
for i in range(1,10,2):
    j = ent + 2
    for k in range(3):
        print('I={} J={}'.format(i,j))
        j -= 1
    ent += 2