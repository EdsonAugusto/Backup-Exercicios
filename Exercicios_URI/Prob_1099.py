def sumOdd(a, b):
    authenticator, exit, odd = lambda n: (n % 2 == 0), 0, 0
    if (a >= b): 
        for i in range(a, b, -1): 
            check = authenticator(i)
            if (not check) and (i != a): odd += i
    else:
        
        for i in range(a, b): 
            check = authenticator(i)
            if (not check ) and (i != a): odd += i
    return odd

ent = int(input())
for i in range(ent): 
    inputRange = input()
    inputConverter = list(map(int, inputRange.split()))
    print(sumOdd(inputConverter[0],inputConverter[1]))
