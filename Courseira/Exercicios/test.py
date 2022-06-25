'''ent=input().split(' ')
a=int(ent[0])
b=int(ent[1])
c=int(ent[2])
d=int(ent[3])

if b>c and d>a and (c+d)>(a+b) and (c>=0) and (d>=0) and (a%2)==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')'''
ent=[]
n=int(input())
for i in range(n):
    ent.append(float(input()))
ent.sort()
print('{:.2f}'.format(ent[0]))
