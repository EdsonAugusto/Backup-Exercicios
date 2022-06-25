inputNumberCheck = int(input())
inputHeroes = ''

for i in range(inputNumberCheck):
	inputHeroes = input()
	inputHeroes = list(inputHeroes.split())
	if inputHeroes[0] == 'Thor': print('Y')
	else: print('N')