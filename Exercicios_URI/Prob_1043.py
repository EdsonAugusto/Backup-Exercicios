inputValue = list(map(float, input().split()))
if inputValue[0] >= inputValue[1] + inputValue[2] or \
	inputValue[1] >= inputValue[0] + inputValue[2] or \
	inputValue[2] >= inputValue[1] + inputValue[0]:
	print('Area = {:.1f}'.format(((inputValue[0]+inputValue[1])/2)*inputValue[2]))
else:
	triangle = (inputValue[0]+inputValue[1]+inputValue[2])/2
	print('Perimetro = {:.1f}'.format(triangle*2))
