def checkNumber(string, initialSize, finalSize):
	try:
		int(string[initialSize:finalSize])
	except ValueError:
		return False
	return int(string[initialSize:finalSize])


inputString = input()
key = len(inputString)

while key > 1:
	for i in range(len(inputString)-1):
