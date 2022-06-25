class Miner:

	def __init__(self, stone):
		self.stone = stone
		self.diamond = 0
	
	def extraction(self):
		self.newStone = []
		for string in range(len(self.stone)): self.newStone.append(self.stone[string])
		return self.newStone
	
	def mining(self):
		self.stone, controler = self.extraction(), True
		while controler:
			if(len(self.stone) >= 2):
				if ('<' in self.stone and '>' in self.stone) and (self.stone.index('<') < self.stone.index('>')):
					self.diamond += 1
					del self.stone[self.stone.index('<')]; del self.stone[self.stone.index('>')] 
					controler = True
				else: self.stone = self.stone[1:]; controler = True
			else: return self.diamond
			
inputValue = int(input())
for i in range(inputValue):
	mine = input()	
	miner = Miner(mine)
	print(miner.mining())