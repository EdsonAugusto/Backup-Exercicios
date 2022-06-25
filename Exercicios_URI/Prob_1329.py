while True:
	inputValue = int(input())
	if inputValue != 0:
		inputNumber = list(map(int, input().split()))
		print('Mary won {} times and John won {} times'.format(inputNumber.count(0), inputNumber.count(1)))
	else: break