from string import ascii_lowercase

numberTest = int(input())
for k in range(numberTest):
	alpha = list(ascii_lowercase)
	inputMessage, exitMessage = input(), ''
	for i in range(len(inputMessage)):
		if inputMessage[i] in alpha: exitMessage += inputMessage[i]
	print(exitMessage[::-1])
