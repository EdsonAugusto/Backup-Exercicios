rangeCall, callList = list(map(int, input().split())), []

for i in range(rangeCall[0]):
	callList.append(input())
callList.sort()
print(callList[rangeCall[1]-1])

