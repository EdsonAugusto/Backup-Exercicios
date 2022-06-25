inputVector = []
for i in range(10):
	inputVector.append(int(input()))
	if inputVector[i] <= 0: inputVector[i] = 1
	print('X[{}] = {}'.format(i, inputVector[i]))