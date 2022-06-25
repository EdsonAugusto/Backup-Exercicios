inputNumber, k = int(input()), 0
for i in range(1000):
	print('N[{}] = {}'.format(i, k))
	if k < inputNumber-1: k+=1 
	else: k = 0