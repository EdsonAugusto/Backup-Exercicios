valueInput, requests = list(map(int, input().split())), list(map(int, input().split()))
func, exit = lambda x, y: x>y, 0
for i in range(len(valueInput)):
	if func(valueInput[i], requests[i]) == False:
		exit += valueInput[i] - requests[i]
print(abs(exit))
