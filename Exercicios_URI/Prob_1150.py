inputX = int(input()) 
inputY = inputX - 1
while inputY <= inputX: inputY = int(input())
sumZ, exit = 0, 0
while sumZ < inputY: sumZ += inputX; exit += 1; inputX += 1
print(exit)