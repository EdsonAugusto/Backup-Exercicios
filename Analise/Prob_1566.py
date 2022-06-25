class Order_Pick:

	def __init__ (self, content):
		self.content = content
		self.control = 0

	def sortBubble (self):
		while self.control < len(self.content)-1:
			for i in range (len(self.content)-1, self.control, -1):
				if self.content[i] < self.content[i-1]:
					self.content[i], self.content[i-1] = self.content[i-1], self.content[i]
			self.control += 1
		return self.content

inputTest, endOrder = int(input()), []
for i in range(inputTest):
	inputNumber = int(input())
	inputList = list(map(int, input().split()))
	order = Order_Pick(inputList)
	endOrder.append(order.sortBubble())
for i in range(len(endOrder)): 
	for k in range(len(endOrder[i])):
		print(endOrder[i][k],end=' ')
	print()