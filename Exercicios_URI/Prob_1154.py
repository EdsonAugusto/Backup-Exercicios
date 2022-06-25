vector = []
while True:
	inputValue = int(input())
	if inputValue >= 0: vector.append(inputValue)
	else: break
print('{:.2f}'.format(sum(vector)/len(vector)))