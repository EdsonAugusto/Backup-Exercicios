inputTest = int(input())
for i in range(inputTest):
	inputValue = list(map(int, input().split()))
	print('{} cm2'.format(int((inputValue[0]*inputValue[1])/2)))