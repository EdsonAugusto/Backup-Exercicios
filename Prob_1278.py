class Justifier:

	def __init__ (self, text):
		self.text = text
		self.longerLength = 0

	def removeExcess (self):
		self.tempText = []
		for i in range(len(self.text)):
			temp = self.text[i].split(); exit = ''
			for k in range(len(temp)):
				if k != 0: exit = exit + ' ' + temp[k]
				else: exit += temp[k]
			self.tempText.append(exit)
		self.text = self.tempText
		return self.text

	def checkLongerString (self):
		for i in range(len(self.text)):
			if self.longerLength < len(self.text[i]): self.longerLength = len(self.text[i])
		return self.longerLength

	def textTab(self):
		Justifier.checkLongerString(self)
		for i in range(len(self.text)):
			if len(self.text[i]) <= self.longerLength:
				self.text[i] = ' '*(self.longerLength - len(self.text[i])) + self.text[i]
		return self.text

	def main(self):
		Justifier.removeExcess(self)
		return Justifier.textTab(self)

valueInput, exit = 1, []
while valueInput != 0:
	valueInput, listInput = int(input()), []
	if valueInput != 0: 
		for i in range(valueInput):
			exit.append([])
			exit[i].append(input())

print()

for k in range(len(exit)):
	for l in range(len(exit[k])):
		tab = Justifier(exit[k])
		end = tab.main()
		print('{}'.format(end[k][l]))
		print('')