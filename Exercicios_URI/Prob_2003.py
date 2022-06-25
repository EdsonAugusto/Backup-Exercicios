while True:
	try:
		inputHour = input()
		if int(inputHour[:1]) >= 7:
			inputHour, addition = inputHour[2:], int(inputHour[:1]) - 7
			print('Atraso maximo: {}'.format(((int(inputHour) - 60)+60+(60*addition))))
		else: print('Atraso maximo: 0')
	except EOFError: break