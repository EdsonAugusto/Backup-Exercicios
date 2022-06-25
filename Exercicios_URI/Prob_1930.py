inputValue = input()
inputValue = list(map(int, inputValue.split()))
print(sum(inputValue)-len(inputValue)+1)