while True:
	try:
		inputValue, cont = int(input()), 0
		if inputValue >= 2:
			while inputValue >= 2:
				cont += 1
				inputValue /= 2
			print(cont)
		else: print(0)
	except EOFError: break