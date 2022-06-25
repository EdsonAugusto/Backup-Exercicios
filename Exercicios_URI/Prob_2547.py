while True:
	try:
		inputValue, users = list(map(int, input().split())), []
		for i in range(inputValue[0]):
			users.append(int(input()))
		users = [x for x in users if x >= inputValue[1] and x <= inputValue[2]]
		print(len(users))
	except EOFError: break