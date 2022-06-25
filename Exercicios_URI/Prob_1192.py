from string import ascii_lowercase, ascii_uppercase

lower, upper = list(ascii_lowercase), list(ascii_uppercase)
numberTest = int(input())
for i in range(numberTest):
	inputValue = input()
	if int(inputValue[0]) == int(inputValue[2]): print(int(inputValue[0])**2)
	elif inputValue[1] in upper: print(int(inputValue[2])-int(inputValue[0]))
	else: print(int(inputValue[0])+int(inputValue[2]))
