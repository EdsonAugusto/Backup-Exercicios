class Triangle_Type:

	def __init__(self, sideA, sideB, sideC):
		self.sideA = sideA
		self.sideB = sideB
		self.sideC = sideC

	def checkTriagle(self):
		if self.sideA >= (self.sideB + self.sideC): return 'NAO FORMA TRIANGULO'
		else:
			if self.sideA**2 == (self.sideB**2 + self.sideC**2): return 'TRIANGULO RETANGULO'
			elif self.sideA**2 > (self.sideB**2 + self.sideC**2): 
				if self.sideA == self.sideB == self.sideC: return 'TRIANGULO OBTUSANGULO\nTRIANGULO EQUILATERO'
				if self.sideA == self.sideC or self.sideB == self.sideA or self.sideB == self.sideC: return 'TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES'
				else: return 'TRIANGULO OBTUSANGULO'
			else:
				if self.sideA == self.sideB == self.sideC: return 'TRIANGULO ACUTANGULO\nTRIANGULO EQUILATERO'
				if self.sideA == self.sideC or self.sideB == self.sideA or self.sideB == self.sideC: return 'TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES'
				else: return 'TRIANGULO ACUTANGULO'

inputTriangle = input()
inputTriangle = list(map(float, inputTriangle.split()))
maxIndex = max(inputTriangle)
maxIndex= inputTriangle.index(maxIndex)
if maxIndex != 0:
	inputTriangle[maxIndex], inputTriangle[0] = inputTriangle[0], inputTriangle[maxIndex]
triangle = Triangle_Type(inputTriangle[0], inputTriangle[1], inputTriangle[2])
print(triangle.checkTriagle())