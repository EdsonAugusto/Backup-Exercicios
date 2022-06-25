inputValue = input()
inputValue = list(map(int, input().split()))
print('Menor valor: {}'.format(min(inputValue)))
print('Posicao: {}'.format(inputValue.index(min(inputValue))))