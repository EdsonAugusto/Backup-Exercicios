n=[]
for i in range(3):
    n.append(int(input('Numero {}:'.format(i))))
if(n[0]<n[1])and(n[1]<n[2]):
    print('crescente')
else:
    print('não está em ordem crescente')