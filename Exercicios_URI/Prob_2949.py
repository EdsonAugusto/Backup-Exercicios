inputValue, inputClass = int(input()), []
for i in range(inputValue):
	temp = list(map(str, input().split()))
	inputClass.append(temp[1])
print('{} Hobbit(s) \n{} Humano(s) \n{} Elfo(s) \n{} Anao(s) \n{} Mago(s)'.format(inputClass.count('X'),inputClass.count('H'), inputClass.count('E'),inputClass.count('A'), inputClass.count('M')))