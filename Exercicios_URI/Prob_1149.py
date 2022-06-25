inputValue = list(map(int, input().split()))
inputValue, exit = [x for x in inputValue if x > 0], 0
for i in range(inputValue[1]): exit += inputValue[0] + i
print(exit)