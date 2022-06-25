from math import sqrt


class Bhaskara:

	def __init__(self, num_A, num_B, num_C ):
		self.num_A = num_A
		self.num_B = num_B
		self.num_C = num_C

	def form_Bhaskara (self):
		#Δ = b² – 4ac
		delta = self.num_B**2 - 4 * self.num_A * self.num_C if sqrt(self.num_A) > 0 and sqrt(self.num_C) > 0 and sqrt(self.num_C) > 0 else "Impossivel calcular"
		print(delta)

	

form_bhas = Bhaskara(0, 20, 5)
print(form_bhas.form_Bhaskara())

	