while True:
	try:
		inputValue, inputCents = input(), input()
		exitValue = ''
		while len(inputValue) >= 1:
			if len(inputValue) >= 3:
				exitValue = inputValue[len(inputValue)-3:] + ',' + exitValue
				inputValue = inputValue[:len(inputValue)-3]
			else:
				exitValue = inputValue + ',' + exitValue; inputValue = ''
		if len(inputCents) > 1: print('${}.{}'.format(exitValue[:-1], inputCents))
		else: print('${}.0{}'.format(exitValue[:-1], inputCents))
	except EOFError: break
