while True:
	try:
		inputString = input()
		if inputString == 'esquerda': print('ingles')
		elif inputString == 'direita': print('frances')
		elif inputString == 'nenhuma': print('portugues')
		elif inputString == 'as duas': print('caiu')
	except EOFError: break