class MultiplesOf13:
	
	def __init__(self, initialValue, endValue):
		self.initialValue = initialValue
		self.endValue = endValue

	def checkMultiples(self):
		self.valueExit, self.truc = 0, lambda x, y: x > y
		self.verification = self.truc(self.initialValue, self.endValue)
		if self.verification: self.initialValue, self.endValue = self.endValue, self.initialValue
		for i in range(self.initialValue, self.endValue+1):
			if (i % 13 != 0):
				self.valueExit += i
		return self.valueExit

dataEntry = []
dataEntry.append(int(input())); dataEntry.append(int(input()))
dataVerification = MultiplesOf13(dataEntry[0], dataEntry[1])
print(dataVerification.checkMultiples())