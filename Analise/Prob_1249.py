from string import ascii_uppercase, ascii_lowercase

class Rot13:

	def __init__ (self, inputString, alfUpper, alfLower):
		self.inputString = inputString
		self.alfUpper = alfUpper
		self.alfLower = alfLower
	
		self.alfUpper = list(ascii_uppercase)
		self.alfLower = list(ascii_lowercase)

	def crip (self):
		pass

test = Rot13('test', 'test', 'test')

print(test.alfUpper)
