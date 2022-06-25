paran = 1
while paran != 0:
    paran = int(input())
    for i in range(1,(paran+1)):
        if paran != 0 and paran > i:
            print(i,end=' ')
        else:
            print(i,end='')
    if paran != 0: 
        print()