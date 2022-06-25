while True:
	rangeList = int(input())
	if rangeList != 0:
		inputValue = list(map(int, input().split()))
		suspect = inputValue[:]; suspect.sort()
		print(inputValue.index(suspect[-2])+1)
	else: break