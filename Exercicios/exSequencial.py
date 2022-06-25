'''''
print('Olá mundo')

n=int(input('Entre com um número: '))
print('O numero informado foi: ',n)

l=[]
i=0
for i in range(2):
    l.append(int(input('Entre c/ paramentro p/ soma: ')))
print(l[0]+l[1])

n=[]
for i in range(4):
    n.append(int(input('Entre c/ a nota: ')))
print((n[0]+n[1]+n[2]+n[3])/4)

m=int(input('Entre com os metros :'))
print('Metros: {} Centimetros: {}'.format(m,(m*100)))

r=int(input('Entre com o valor do raio:'))
print('Area do Circulo',3.14*r**2,'cm')

l=int(input('Entre com o valor do lado: '))
print('Area do quadrado: ',l**2,'Dobro da Area: ',(l**2)**2)

p=[]
d=['Ganho por horas: ','Horas trabalhadas: ']
for i in range(2):
    p.append(int(input('{}'.format(d[i]))))
print('Ganho do mês: ',(p[0]*p[1])*26)

f=int(input('Graus em Farenheit: '))
print('Graus Celsius: ',5*(f-32)/9)

c=int(input('Graus Celsius: '))
print('Graus Fahrenheit: ',c*1.8+32)

e=['Número inteiro: ','Número real: ']
ent=[]
for i in range(2):
    ent.append(int(input(e[0])))
ent.append(float(input(e[1])))
print('Produto no dobro do primeiro com metade do segundo: ',ent[0]*2+ent[1]/2)
print('Soma do triplo do primeiro com o terceiro: ',ent[0]*3+ent[2])
print('Terceiro elevado ao cubo: ',ent[2]**3)

a=float(input('Altura: '))
calc=[72.7*a-58,62.1*a-44.7]
print('Homens: ',calc[0],' Mulheres:',calc[1])

p=int(input('Pesca Kg: '))
k=[p-50,(p-50)*4]
print('Quilo excedente:',k[0], 'Multa: ',k[1])

entp=['Valor Horas: ', 'Horas Trabalhadas: ']
paran=[]
for i in range(2):
    paran.append(int(input(entp[i])))
bruto=paran[0]*paran[1]
calc=[11*bruto/100,8*bruto/100,5*bruto/100]
print('Valor Bruto: ', bruto)
print('IR 11%: ',calc[0])
print('INSS 8%: ',calc[1])
print('Sindicato 5%: ',calc[2])
print('Total de desconto: ',calc[0]+calc[1]+calc[2])
print('Valor Liquido: ',bruto-(calc[0]+calc[1]+calc[2]))

l=int(input('Lado M²: '))
l=l**2
t=54
tot=1
while (t<l):
    if (l>t):
        t=t+54
        tot=tot+1
print('M²: ',l)
print('Total de tintas: ',tot)
'''''


m=int(input('Entre com o valor do lado²: '))
m=m**2
comp=['Metros:',' Galão 3,6L: ', ' Lata 18L: ']
tin=[21.8,108,216]
cont=[0,0]
test=True
while(test==False):
    if (m>=tin[0]) and (m<tin[1]):
        tin[0]=tin[0]+tin[0]
        cont[0]=cont[0]+1
        test=True
    if (m>=tin[1])and(m>=tin[2]):
        tin[1]=tin[1]+tin[0]
        cont[0]=cont[0]+1
        if (cont[1]<=1):
            cont[1]=cont[1]+1
        else:
            test=True
    if (m>=tin[2]):
        tin[2]=tin[2]+tin[1]
        cont[1]=cont[1]+1
        if (cont[1]<2):
            cont[1]=cont[1]+1
        else:
            test = True
    #lse:
      #  test=False
print(comp[0],m,comp[1],cont[0],comp[2],cont[1])

