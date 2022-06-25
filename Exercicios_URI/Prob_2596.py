numberTest = int(input())
for number in range(numberTest):
	numberBalls, balls = int(input()), []
	for i in range(1, numberBalls+1):
		dividers = 1
		for k in range(1, i):
			if (i % k) == 0: dividers += 1
		if (dividers % 2) == 0: balls.append(i)
	print(len(balls))
