def checkerPlug(x, y):
	for i in range(len(x)):
		if x[i] == y[i]:
			return 'N'
	return 'Y'

plugueX = list(map(int, input().split()))
plugueY = list(map(int, input().split()))
	
print(checkerPlug(plugueX, plugueY))