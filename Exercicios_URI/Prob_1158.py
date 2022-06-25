inputNumberTest = int(input())
for i in range(inputNumberTest):
	inputNumber, sumNumber = input(), 0
	inputNumber, k = list(map(int, inputNumber.split())), 0
	while k < inputNumber[1]:
		if (inputNumber[0] % 2) != 0:
			sumNumber += inputNumber[0]
			inputNumber[0] += 1; k += 1
		else: inputNumber[0] += 1
	print(sumNumber)