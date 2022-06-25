inputValue = input()
inputValue = list(map(int, inputValue.split()))
print(inputValue.index(max(inputValue))+1)