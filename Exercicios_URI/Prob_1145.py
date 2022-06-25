inputValue = list(map(int, input().split()))

for i in range(1, inputValue[1], inputValue[0]):
	for k in range(i, i+inputValue[0]):
		if k < i+inputValue[0]-1:
			print('{}'.format(k), end = ' ')
		else: print('{}'.format(k), end = '\n')