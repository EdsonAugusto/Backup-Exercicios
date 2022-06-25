x, y, som = int(input()), int(input()), 0
if x < y:
    x, y = y, x
if (x >= 0) and (y >= 0):
    for i in range(y,x):
        if (i % 2 != 0):
            som += i
else:
    for i in range(x,y,-1):
        if (i % 2 != 0):
            som += i
print(som)