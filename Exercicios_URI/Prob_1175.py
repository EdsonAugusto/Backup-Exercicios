inputVector = []
for i in range(20): inputVector.append(int(input()))
inputVector = inputVector[::-1]
for k in range(len(inputVector)): print('N[{}] = {}'.format(k, inputVector[k]))