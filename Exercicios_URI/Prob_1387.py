inputValue = [1, 1]
while inputValue[0] != 0 and inputValue[1] != 0:
	inputValue = input()
	inputValue = list(map(int, inputValue.split()))
	if inputValue[0] != 0 and inputValue[1] != 0:
		print(inputValue[0]+inputValue[1])