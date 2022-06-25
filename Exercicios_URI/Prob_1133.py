class Rest_Of_Division:

	def __init__(self, initialValue, endValue):
		self.initialValue = initialValue
		self.endValue  = endValue

	def restCalculation(self):
		self.truc, self.dataExit = lambda x, y: x > y, []
		self.varification = self.truc(self.initialValue, self.endValue)
		if self.varification: self.initialValue, self.endValue = self.endValue, self.initialValue
		for i in range(self.initialValue+1, self.endValue):
			if (i % 5) > 1 and (i % 5) < 4: self.dataExit.append(i)
		return self.dataExit

dataEntry = []
dataEntry.append(int(input()))
dataEntry.append(int(input()))
checkRest = Rest_Of_Division(dataEntry[0], dataEntry[1])
exit=checkRest.restCalculation()
for i in exit: print(i)