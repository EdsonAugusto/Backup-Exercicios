def insideOut (string):
	middleString = lambda string: [string[len(string)//2:], string[:len(string)//2]]
	exit = middleString(string)
	return exit[1][::-1] + exit[0][::-1]

loop = int(input())
for i in range(loop): inputData = input(); print(insideOut(inputData))


'''
# Bloco de teste
ent = ('I ENIL SIHTHSIREBBIG S', 'LEVELKAYAK', 'H YPPAHSYADILO', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE')
saida = ('THIS LINE IS GIBBERISH', 'LEVELKAYAK', 'HAPPY HOLIDAYS', 'MLKJIHGFEDCBAZYXWVUTSRQPON', 'FRENCH HENS TWO DOVES AND A PARTRIDGE')

for i in range(len(ent)):
	print('Teste [{}] -------------------------------------------'.format(i))
	print(' - input prog: {} \n - exit prog: {} \n - expected: {} \n - result {}'.format(ent[i], insideOut(ent[i]), saida[i], insideOut(ent[i]) == saida[i]))

print(insideOut('VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE'))'''