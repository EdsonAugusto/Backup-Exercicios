fb = {1 : 'Rolien', 2 : 'Naej', 3 : 'Elehcim', 4 : 'Odranoel'}
numberTest = int(input())
for i in range(numberTest):
	feedBack = int(input())
	for k in range(feedBack):
		inputValue = int(input())
		print(fb[inputValue])
