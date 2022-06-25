while True:
	numberTest = int(input())
	if numberTest >= 1:
		p1, p2 = 0, 0
		for i in range(numberTest):
			inputValue = list(map(int, input().split()))
			if inputValue[0] > inputValue[1]: p1 += 1
			elif inputValue[0] < inputValue[1]: p2 += 1 
		print('{} {}'.format(p1, p2))
	else: break