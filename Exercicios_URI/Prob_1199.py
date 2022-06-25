while True:
	inputValue = input()
	if int(inputValue, 16) >= 0:
		if 'x' in inputValue: print(int(inputValue, 16))
		else:
			if len(str(hex(int(inputValue)))) > 3: heX= str(hex(int(inputValue))); print(heX[:2]+heX[2:len(heX)].upper())
			else: print(hex(int(inputValue)))
	else: break
