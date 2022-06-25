i,med=0,0
while i <= 1:
    ent = float(input())
    if ent >= 0 and ent <= 10:
        med+=ent
        i+=1
    else:
        print('nota invalida')
print('media = {}'.format(med/2))
