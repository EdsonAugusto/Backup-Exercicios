ent, lis = int(input()), [0, 1]
for i in range(2, ent):
    lis.append(lis[i-1]+lis[i-2])

for i in range(len(lis)):
    if i < (len(lis)-1):
        print(lis[i], end=' ')
    else:
        print(lis[i])