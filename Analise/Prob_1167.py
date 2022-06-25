while True:
	inputValue, competitor = int(input()), ['', 0]
	if inputValue != 0:
		inputCompetitor = list(map(str, input().split()))
		if int(inputCompetitor[1]) > competitor[1]: inputValue = inputCompetitor
	else: break
