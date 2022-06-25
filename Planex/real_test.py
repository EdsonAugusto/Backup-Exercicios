lista=open('db.txt','r')
for arq in lista:
    test= arq.split()
    if len(test) > 3:
        print("('{} {}', '{} {}'),".format(test[0],test[1],test[2],test[3]))
    else:
        print("('{} {}', '{}'),".format(test[0],test[1],test[2]))
lista.close()
'''ent=('')
conv=ent.split()
said=''
for i in range(0,len(conv)-1,2):
    said+='({},{}),\n'.format(conv[i],conv[i+1])

print(said)'''