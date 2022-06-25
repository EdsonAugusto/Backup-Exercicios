numberTest = int(input())
for i in range(numberTest):
	inputChoice = list(map(str, input().split()))
	inputValue = list(map(int, input().split()))
	if (sum(inputValue) % 2) == 0 and inputChoice[1] == 'PAR': print(inputChoice[0])
	elif (sum(inputValue) % 2) != 0 and inputChoice[1] != 'PAR': print(inputChoice[0])
	else: print(inputChoice[2])
