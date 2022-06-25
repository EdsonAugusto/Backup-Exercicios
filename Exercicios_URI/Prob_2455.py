inputValue = list(map(int, input().split()))
result1, result2 = inputValue[0] * inputValue[1], inputValue[2] * inputValue[3]
if result1 > result2: print(-1)
elif result1 < result2: print(1)
else: print(0)