def bmi(weight, height):
	calcBMI = weight/(height**2) 
	if calcBMI <= 18.5: return 'Underweight'
	elif calcBMI <= 25.0: return "Normal"
	elif calcBMI <= 30.0: return "Overweight"
	else: return "Obese"


print(bmi(50, 1.80))