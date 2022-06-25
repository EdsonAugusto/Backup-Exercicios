inputValue, exit = list(map(int, input().split())), [0, 0]
for i in range(inputValue[1]):
	tempAction = input()
	if tempAction == 'fechou': exit[0]+=1
	elif tempAction == 'clicou': exit[1]+=1
print((inputValue[0]+exit[0])-exit[1])