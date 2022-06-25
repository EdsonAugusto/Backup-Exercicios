inputTest = int(input())
for i in range(inputTest):
	inputNumber = list(map(int, input().split()))
	r = (3*inputNumber[0])**2 + inputNumber[1]**2
	b = 2*(inputNumber[0]**2) + (5*inputNumber[1])**2
	c = -100*inputNumber[0] + inputNumber[1]**3
	if r > b and r > c: print('Rafael ganhou')
	elif b > r and b > c: print('Beto ganhou')
	else: print('Carlos ganhou')