def timeExit (inputTime, exitTime = [0, 0, 0]):
	if inputTime > 60:
		while inputTime > 59: inputTime -= 60; exitTime[1] += 1; exitTime[2] = inputTime
		while exitTime[1] >= 60: exitTime[0] += 1; exitTime[1] -= 60 
		exitTime = list(map(str, exitTime))
	else: exitTime = ['0', '0', str(inputTime)]
	return exitTime[0]+':'+exitTime[1]+':'+exitTime[2]

ent = int(input())
print(timeExit(ent))