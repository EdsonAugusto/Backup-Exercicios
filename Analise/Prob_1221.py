class Number_Prime:

	def __init__(self):
		pass

	def checkPrime(self, x):
		self.x = x
		for i in range((self.x//2)+1, 0, -1):
			if self.x % i == 0: return 'Not Prime'
		return 'Prime'


inputValue = int(input())
for i in range(inputValue):
	ent = Number_Prime()
	inputNumber = int(input())
	print(ent.checkPrime(inputNumber))



'''numberTest = int(input())
for i in range(numberTest):
	inputTest = int(input())
	inputSelection = Number_Prime(inputTest)
	print(inputSelection.primeNumber())'''


'''def nextPrime(self, x):
self.condition, self.x = True, x
while self.condition:
	self.x += 1
	for i in range(2, self.x):
		if (self.x % i == 0): break; self.condition = True
	else: self.condition = False
return self.x'''

'''	def primeNumber(self):
		self.inputCheck, self.checkCondition = 2, True
		for i in range(self.prime//2, 0, -1):
			print(self.inputCheck)
			if(self.prime % self.inputCheck == 0) and self.prime != self.inputCheck: return 'Not Prime'
			elif(self.prime % self.inputCheck != 0) and (self.prime != self.inputCheck) and ((self.prime / self.inputCheck) > self.inputCheck):
				self.inputCheck = self.nextPrime(self.inputCheck)
		return 'Prime'
'''