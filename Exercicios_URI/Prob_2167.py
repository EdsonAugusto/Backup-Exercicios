inputValue = int(input())
inputVel = input()
inputVel = list(map(int, inputVel.split()))
for i in range(1,inputValue):
	if inputVel[i-1] > inputVel[i]:print(i+1); break
else: print(0)