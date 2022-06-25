class Contract_Review:

	def __init__(self, number, contract):
		self.number = number
		self.contract = contract

	def Review(self):
		if self.number in self.contract:
			self.contract = self.contract[:self.contract.index(self.number)] + \
			self.contract[self.contract.index(self.number)+1:]
			return self.Review()
		else:
			if len(self.contract) < 1: return(0)
			else: return int(self.contract)

while True:
	inputValue = list(map(str, input().split()))
	if inputValue[0] != '0' and inputValue[1] != '0':
		check = Contract_Review(inputValue[0],inputValue[1])
		print(check.Review())
	else: break