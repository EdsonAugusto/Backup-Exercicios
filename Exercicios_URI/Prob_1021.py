class Decomposition:

	def __init__(self, value, listValue):
		self.value = value
		self.listValue = listValue
		self.exit = []

	def score (self):
		for i in range(len(self.listValue)):
			self.exit.append(self.value//self.listValue[i])
			self.value -= self.listValue[i]*self.exit[i]
		return self.exit

inputValue, money = list(map(int, input().split('.'))),[[100, 50, 20, 10, 5, 2, 1], [50, 25, 10, 5, 1]]
exit, printExit, temp = ['NOTAS:', 'MOEDAS:'], ['nota', 'moeda'], 0
for i in range(len(inputValue)):
	dec = Decomposition(inputValue[i], money[i])
	deco = dec.score()
	print(exit[i])
	if i < 1: temp = deco[-1]; del deco[-1]
	for k in range(len(deco)):
		if i > 0 and k < 1: print('{} {}(s) de R$ {:.2f}'.format(temp, printExit[i], 1))
		if i < 1:
			print('{} {}(s) de R$ {:.2f}'.format(deco[k], printExit[i], money[i][k]))
		else:
			if len(str(money[i][k])) > 1: 
				print('{} {}(s) de R$ 0.{}'.format(deco[k], printExit[i], money[i][k]))
			else: print('{} {}(s) de R$ 0.0{}'.format(deco[k], printExit[i], money[i][k]))