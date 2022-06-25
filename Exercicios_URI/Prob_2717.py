inputValue = int(input())
inputNumber = list(map(int, input().split()))
if sum(inputNumber) <= inputValue: print('Farei hoje!')
else: print('Deixa para amanha!') 