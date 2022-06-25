inputValue = list(map(float, input().split()))
average = ((inputValue[0]*2)+(inputValue[1]*3)+(inputValue[2]*4)+(inputValue[3]))/10
print('Media: {:.1f}'.format(average))
if (average) >= 7:
	print('Aluno aprovado.')
elif (average) < 5:
	print('Aluno reprovado.')
else:
	print('Aluno em exame.')
	inputValue1 = (float(input()))
	print('Nota do exame: {}'.format(inputValue1))
	media = sum(inputValue)/len(inputValue)
	if ((media+inputValue1)/2) >= 5: print('Aluno aprovado.')
	else: print('Aluno reprovado.')
	print('Media final: {:.1f}'.format((media+inputValue1)/2))