from string import ascii_uppercase

class Cifra_Cesar:

	def __init__(self, secretKey, message):
		self.secretKey = secretKey
		self.message = message
		self.listAlpha = list(ascii_uppercase)
		self.dicAlpha = {' ': ' '}
		self.secretMessage = ''

	def cipher(self):
		self.alphaEncoded = self.listAlpha[self.secretKey:] + self.listAlpha[:self.secretKey]
		for i in range(len(self.listAlpha)):
			self.dicAlpha[self.alphaEncoded[i]] = self.listAlpha[i]
		return self.dicAlpha

	def decoding(self):
		self.cipher()
		for letter in range(len(self.message)):
			self.secretMessage += self.dicAlpha[self.message[letter]]
		return self.secretMessage

numberOfMessages = int(input())
for i in range(numberOfMessages):
	originalMessage = input()
	secretNumber = int(input())
	cif = Cifra_Cesar(secretNumber, originalMessage)
	print(cif.decoding())