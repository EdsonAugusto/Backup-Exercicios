inputValue, numbersDrawn, scoreMade = list(map(int, input().split())), list(map(int, input().split())), 0
for i in range(len(inputValue)):
	if inputValue[i] in numbersDrawn: scoreMade += 1
if scoreMade < 3: print('azar') 
elif scoreMade == 3: print('terno')
elif scoreMade == 4: print('quadra')
elif scoreMade == 5: print('quina')
else: print('sena')