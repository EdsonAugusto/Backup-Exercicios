numberTest = int(input())
for i in range(numberTest):
	inputValue, listExit = int(input()), []
	for k in range(1, inputValue):
		if (inputValue % k) == 0: listExit.append(k)
	if sum(listExit) == inputValue: print('{} eh perfeito'.format(inputValue))
	else: print('{} nao eh perfeito'.format(inputValue))