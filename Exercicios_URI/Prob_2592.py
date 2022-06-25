while True:
	inputValue, attempts = int(input()), 0
	if inputValue != 0:
		sort = False
		while not sort:
			goToSort = list(map(int, input().split()))
			if goToSort == sorted(goToSort): attempts += 1; sort = True
			else: attempts += 1; sort = False
		print(attempts)
	else: break