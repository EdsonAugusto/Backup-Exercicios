while True:
	try:
		inputValue = int(input())
		print(inputValue-1)
	except EOFError: 
		break