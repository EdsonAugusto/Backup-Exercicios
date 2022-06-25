while True:
	try:
		inputAlpha = input()
		inputValue = int(input())
		inputValue, secretMessage = list(map(int, input().split())), ''
		for i in range(len(inputValue)): secretMessage += inputAlpha[inputValue[i]-1]
		print(secretMessage)
	except EOFError: break

