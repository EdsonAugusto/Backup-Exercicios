numberTest = int(input())
for i in range(numberTest):
	inputValue, exit = list(map(str, input().split())), []
	for k in range(len(inputValue)):
		if len(inputValue[k]) < 2: exit.append('0{}'.format(inputValue[k]))
		else: exit.append(inputValue[k])
		print(exit)
		if inputValue[2] == '0': print('{}:{} - A porta fechou!'.format(exit[0], exit[1]))
		else: print('{}:{} - A porta abriu!'.format(exit[0], exit[1]))