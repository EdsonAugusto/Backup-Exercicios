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
	
	def sortSeletion (self):
		for i in range(len(self.content)-1):
			for k in range()
			

	
	# Selecionar menor elemento e realizar troca
	# Controlar tamanho da lista para não modificar elemento modificados
	# Controlar numero de execução 


			

test = Order_Pick([5,78,0,4,3,8,7,5])
print(test.sortSeletion())