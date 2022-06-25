while True:
	try:
		inputValue, listInput = int(input()), []
		for i in range(inputValue):
			value = input()
			if len(value) == 4: listInput.append(int(value))
		listInput.sort()
		for k in range(len(listInput)):
			if len(str(listInput[k])) < 4: print('{}{}'.format('0'*(4-len(str(listInput[k]))), listInput[k]))
			else: print('{}'.format(listInput[k]))
	except EOFError: break
		

