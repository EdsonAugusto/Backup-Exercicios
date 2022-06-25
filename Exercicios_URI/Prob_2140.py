inputValue, notes = [1, 1], [100, 50, 20, 10, 5, 2]
result = 0
while inputValue[0] != 0 or inputValue[1] != 0:
	inputValue[0], inputValue[1]= map(int, input().split())
	if inputValue[0] != 0 or inputValue[1] != 0:
		result = inputValue[1] - inputValue[0]
		i=0; exit = 0
		while i <= len(notes)-1:
			if notes[i] <= result:
				result -= notes[i]; exit += 1; i = 0
			else: i += 1
		if exit == 2: print('possible')
		else: print('impossible')