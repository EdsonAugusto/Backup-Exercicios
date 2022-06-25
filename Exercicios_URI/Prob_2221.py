numberTest = int(input())
def checkBonus(level, bonus):
	if (level % 2) == 0: return bonus
	else: return 0

force = lambda a, d, l, b: ((a+d)/2)+checkBonus(l,b) 
for i in range(numberTest):
	bonus = int(input())
	inputD, inputG = list(map(int, input().split())), list(map(int, input().split()))
	inputD.append(force(inputD[0], inputD[1], inputD[2], bonus))
	inputG.append(force(inputG[0], inputG[1], inputG[2], bonus))
	if inputD[3] == inputG[3]: print('Empate')
	elif inputD[3] > inputG[3]: print('Dabriel')
	else: print('Guarte')