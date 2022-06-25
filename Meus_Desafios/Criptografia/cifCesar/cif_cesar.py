from string import ascii_lowercase, ascii_uppercase


class Cipher_Cesar:

	def __init__ (self):
		self.alphabLower = list(ascii_lowercase)
		self.alphabUpper = list(ascii_uppercase)
		self.secretDic = [{}, {}]
		self.exitMessage = ''

	def simpleDictGenerator (self, numSecret, mode):
		numSecret -= 1
		for i in range(len(ascii_lowercase)):
			if mode == 'encrypt':
				self.secretDic[0][self.alphabLower[i]] = self.alphabLower[numSecret]
				self.secretDic[1][self.alphabUpper[i]] = self.alphabUpper[numSecret]
			elif mode == 'decrypt':
				self.secretDic[0][self.alphabLower[numSecret]]= self.alphabLower[i]
				self.secretDic[1][self.alphabUpper[numSecret]] = self.alphabUpper[i]
			numSecret += 1
			if numSecret >= len(self.alphabLower): numSecret = 0
		return self.secretDic

	def cesarSimple (self, numSecret, message, mode='encrypt'):
		self.secretDic = self.simpleDictGenerator(numSecret, mode)
		for i in range(len(message)):
			if message[i] in self.alphabLower: self.exitMessage += self.secretDic[0][message[i]]
			elif message[i] in self.alphabUpper: self.exitMessage += self.secretDic[1][message[i]]
			else: self.exitMessage += message[i]
		return self.exitMessage

	def cesarAdvanced (self, numSecret, message, mode='encrypt'):
		pass

cif = Cipher_Cesar()
#print(cif.cesarSimple(26, 'test Test TEst TESt'))
print(cif.cesarSimple(26, 'sdrs Sdrs SDrs SDRs', 'decrypt'))