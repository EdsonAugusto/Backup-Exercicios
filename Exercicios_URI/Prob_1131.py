result = [0, 0, 0]
while True:
	inputResult = list(map(int, input().split()))
	if inputResult[0] > inputResult[1]: result[0] += 1
	elif inputResult[0] < inputResult[1]: result[1] += 1
	elif inputResult[0] == inputResult[1]: result[2] += 1
	print('Novo grenal (1-sim 2-nao)')
	inputValue = int(input())
	if inputValue == 2: break
print('{} grenais'.format(sum(result)))
print('Inter:{}'.format(result[0]))
print('Gremio:{}'.format(result[1]))
print('Empates:{}'.format(result[2]))
if result[0] > result[1]: print('Inter venceu mais')
elif result[0] < result[1]: print('Gremio venceu mais')
elif result[0] == result[1]:print('Nao houve vencedor')