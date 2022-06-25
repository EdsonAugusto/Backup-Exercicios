while True:
	try: 
		value = int(input())
		inputValues = list(map(int, input().split()))
		inputValues.sort()
		if inputValues[-1] < 10: print(1)
		elif inputValues[-1] >= 10 and inputValues[-1] < 20: print(2)
		else: print(3)
	except EOFError: break