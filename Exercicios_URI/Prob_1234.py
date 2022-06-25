class RelatedSearches:

	def __init__(self, string):
		self.string = string
		

	def variationInSequence(self):
		self.exitString, self.control = '', True
		for i in range(len(self.string)):
			if self.string[i] != ' ':
				if self.control == True: self.exitString += self.string[i].upper(); self.control = False
				else: self.exitString += self.string[i].lower(); self.control = True 
			else: self.exitString += ' '
		return self.exitString


while EOFError:
	try:
		sequenciaDancante = input()
		exit = RelatedSearches(sequenciaDancante)
		print(exit.variationInSequence())
	except: 
		break