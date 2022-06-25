s, b, saida = 2, 1, 0
while s <= 38:
	s+=2;b+=b
	saida += s/b
print('{:.2f}'.format(saida))