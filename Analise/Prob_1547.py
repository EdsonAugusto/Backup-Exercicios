maximumTest = int(input())
for i in range(maximumTest):
	inputValue, reportedValues  = list(map(int, input().split())), list(map(int, input().split()))
	if inputValue[1] in reportedValues: print(reportedValues.index(inputValue[1])+1)
	else:
		nextValue = reportedValues[:]
		nextValue.append(inputValue[1]); nextValue.sort(); indexValue = nextValue.index(inputValue[1])
		if max(nextValue) == inputValue[1]: indexValue -= 1; nextValue = nextValue[indexValue]
		else: indexValue += 1; nextValue = nextValue[indexValue]
		print(reportedValues.index(nextValue)+1)







'''maximumTest = int(input())
for i in range(maximumTest):
	inputValue, reportedValues = list(map(int, input().split())), list(map(int, input().split()))
	if inputValue[1] in reportedValues: print(reportedValues.index(inputValue[1])+1)
	else:
		for k in range(len(reportedValues)):
			nextValue = abs(inputValue[1] - reportedValues[k])
			if nextValue == 1: print(reportedValues.index(reportedValues[k])+1); break
'''
	
	
'''else:
	nextValue = reportedValues[:]
	nextValue.append(inputValue[1]); nextValue.sort(); indexValue = nextValue.index(inputValue[1])
	if max(nextValue) == inputValue[1]: indexValue -= 1; nextValue = nextValue[indexValue]
	else: indexValue += 1; nextValue = nextValue[indexValue]
	print(reportedValues.index(nextValue)+1)'''
