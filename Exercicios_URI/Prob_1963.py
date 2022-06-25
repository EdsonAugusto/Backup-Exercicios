inputValue = input()
inputValue = list(map(float, inputValue.split()))
percentageIncrease = ((inputValue[1] - inputValue[0]) * 100) / inputValue[0]
print('{:.2f}%'.format(percentageIncrease))