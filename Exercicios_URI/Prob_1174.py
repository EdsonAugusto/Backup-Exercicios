ent, said, i = [], [], 0
while len(ent) <= 99:
    ent.append(float(input()))
    if ent[-1] <= 10:
        said.append(len(ent)-1)
        print('A[{}] = {}'.format(i,ent[-1]))
    i+=1
