i = 1
while True:
	inputValue = int(input())
	if inputValue >= 0: print('Experiment {}: {} full cycle(s)'.format(i, inputValue//2)); i+=1
	else: break
