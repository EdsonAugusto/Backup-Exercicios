def how_much_i_love_you(nb_petals):
	exitResult = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
	if len(exitResult) >= nb_petals: return exitResult[nb_petals-1]
	else: 
		while len(exitResult) < nb_petals:
			exitResult += exitResult
			if len(exitResult) >= nb_petals: return exitResult[nb_petals-1]

print(how_much_i_love_you(6))
