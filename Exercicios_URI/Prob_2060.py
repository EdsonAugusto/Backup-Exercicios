inputNumberTest, inputCases = int(input()), input()
inputCases = list(map(int, inputCases.split()))
casesToCheck, exitcases = [2, 3, 4, 5], [0, 0, 0, 0]

for k in range(len(casesToCheck)):
	for i in range(len(inputCases)):
		if (inputCases[i] % casesToCheck[k]) == 0:
			exitcases[k] += 1

for i in range(0, len(casesToCheck)):
	print('{} Multiplo(s) de {}'.format(exitcases[i], casesToCheck[i]))