inputValue = 1
while inputValue != 0:
	inputValue, i, sumExit = int(input()), 1, 0
	if inputValue != 0:
		while i <= 5:
			if (inputValue % 2) == 0:
				sumExit += inputValue
				inputValue += 2
				i += 1
			else: inputValue += 1
		print(sumExit)
	else: break