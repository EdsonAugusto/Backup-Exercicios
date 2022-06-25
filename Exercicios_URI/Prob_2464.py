from string import ascii_lowercase

class Crip:

	def __init__ (self, alpha, message):
		self.alpha = alpha
		self.message = message
		self.encrypting = {}
		self.alphabet = list(ascii_lowercase)
		self.stringExit = ''

	def crip (self):
		for i in range(len(self.alphabet)): 
			self.encrypting[self.alphabet[i]] = self.alpha[i]
		return self.encrypting

	def decryption (self):
		self.crip()
		for i in range(len(self.message)):
			self.stringExit += self.encrypting[self.message[i]]
		return self.stringExit

inputAlpha, inputMessage = input(), input()
encryption = Crip(inputAlpha, inputMessage)
print(encryption.decryption())
