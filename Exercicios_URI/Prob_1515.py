while True:
	inputValue = int(input())
	if inputValue != 0:
		firstMessage = ['', 2114]
		for i in range(inputValue):
			inputPlanet = list(map(str, input().split()))
			dataMessage = int(inputPlanet[1]) - int(inputPlanet[2])
			if dataMessage < firstMessage[1]: firstMessage = [inputPlanet[0], dataMessage]				
		print(firstMessage[0])
	else: break