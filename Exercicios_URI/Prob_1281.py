class Market:

	def __init__(self, productList):
		self.productList = productList
		self.productRegistration = {}

	def registration(self):
		for i in range(len(self.productList)):
			item = list(map(str, self.productList[i].split()))
			self.productRegistration[item[0]] = float(item[1])
		return self.productRegistration

	def purchase(self, shoppingCart):
		self.shoppingCart, self.purchaseTotal = shoppingCart, 0
		for i in range(len(shoppingCart)):
			self.item = list(map(str, self.shoppingCart[i].split()))
			self.purchaseTotal += self.productRegistration[self.item[0]] * int(self.item[1])
		return self.purchaseTotal

inputTest = int(input())
for i in range(inputTest):
	quantityOfProduct, product = int(input()), []
	for k in range(quantityOfProduct):
		product.append(input())
	market = Market(product)
	market.registration()
	purchaseAmount, buy = int(input()), []
	for j in range(purchaseAmount):
		buy.append(input())
	print('R$ {:.2f}'.format(market.purchase(buy)))
