data, jingles = ('W', 'H', 'Q', 'E', 'S', 'T', 'X'), {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}
inputValue= '0'
while inputValue != '*':
	inputValue, exitData = list(map(str, input().split('/'))), 0
	if inputValue[0] != '*':
		for i in range(len(inputValue)):
			check = 0
			for k in range(len(data)): check += jingles[data[k]] * inputValue[i].count(data[k])
			if check == 1: exitData += 1
		print(exitData)
	else: break
