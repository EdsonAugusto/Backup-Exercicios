while True:
	inputValue = list(map(int, input().split()))
	if inputValue[0] == 0 and inputValue[1] == 0: break
	else: print(inputValue[1]*inputValue[0])