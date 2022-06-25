from string import ascii_lowercase


class Encryption:

	def __init__ (self, key, message):
		self.key = key
		self.message = message.lower()
		self.alpha = list(ascii_lowercase)
		self.cipher = {}
		self.decryptedMessage = ''


	def cryptor (self):
		self.secret = self.alpha[self.key:] + self.alpha[:self.key]
		for i in range(len(self.alpha)): self.cipher[self.secret[i]] = self.alpha[i]
		return self.cipher

	def decipher (self):
		self.cryptor()
		for i in range(len(self.message)):
			if self.message[i] in self.alpha: 
				self.decryptedMessage += self.cipher[self.message[i]]
			else: self.decryptedMessage += self.message[i]
		return self.decryptedMessage

test = Encryption(3, 'd oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr')
print(test.decipher())

