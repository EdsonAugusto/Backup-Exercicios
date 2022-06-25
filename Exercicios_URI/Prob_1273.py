class Justifier:

	def __init__(self, listString): 
		self.listString = listString
		self.bigInterval = 0

	def interval(self):
		for i in range(len(self.listString)):
			if len(self.listString[i]) > self.bigInterval: 
				self.bigInterval = len(self.listString[i])
		return self.bigInterval

	def aligner(self):
		self.interval()
		for i in range(len(self.listString)):
			self.space = self.bigInterval - len(self.listString[i])
			if i < len(self.listString)-1:
				print('{}{}'.format(' '*self.space, self.listString[i]))
			else: return ('{}{}'.format(' '*self.space, self.listString[i]))

inputValue, inputVector = 1, []
while inputValue != 0:
	inputValue, inputList = int(input()), []
	if inputValue != 0:
		for i in range(inputValue): inputList.append(input()) 
		inputVector.append(inputList)
	else: break

for k in range(len(inputVector)):
	justifier = Justifier(inputVector[k])
	if k < len(inputVector)-1:
		print(justifier.aligner()); print()
	else: print(justifier.aligner())