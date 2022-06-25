from math import sqrt
inputValue = int(input())
fib = ((((1 + sqrt(5))/2)**inputValue) - (((1 - sqrt(5))/2)**inputValue))/(sqrt(5))
print('{:.1f}'.format(fib))