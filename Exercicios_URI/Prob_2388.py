intInput, listInput = int(input()), []
for i in range(intInput):
	listInput.append(input())

result = []
for k in range(len(listInput)):
	tempNumber = list(map(int, listInput[k].split()))
	result.append(tempNumber[0]*tempNumber[1])
print(sum(result))
