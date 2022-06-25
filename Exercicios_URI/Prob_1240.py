numberTest = int(input())
for i in range(numberTest):
	inputValue = list(map(str, input().split()))
	if len(inputValue[0]) < len(inputValue[1]): print('nao encaixa')
	else:
		size = len(inputValue[0]) - len(inputValue[1])
		if (inputValue[0][size:] == inputValue[1]): print('encaixa')
		else: print('nao encaixa')

