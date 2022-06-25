inputValue, matrix = int(input()), []
inputOperation, exit = input(), 0

for i in range(12):
	matrix.append([])
	for k in range(12):
		matrix[i].append(float(input()))
		if i == inputValue:
			exit += matrix[i][k]

if inputOperation == 's': print('{:.1f}'.format(exit))
else: print('{:.1f}'.format(exit/12))