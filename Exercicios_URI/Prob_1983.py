numberTest, parameter = int(input()), ['', 0.0]
for i in range(numberTest):
	inputValue = list(map(str, input().split()))
	if float(inputValue[1]) > parameter[1]: parameter = [inputValue[0], float(inputValue[1])]
if parameter[1] >= 8.0: print(parameter[0])
else: print('Minimum note not reached')
