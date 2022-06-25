inputValue = list(map(int, input().split()))
if inputValue[0] < inputValue[1]:
	for i in range(len(inputValue)-1):
		if inputValue[i] > inputValue[i+1]: print('N'); break
	else: print('C')
else:
	for i in range(len(inputValue)-1):
		if inputValue[i] < inputValue[i+1]: print('N'); break
	else: print('D')