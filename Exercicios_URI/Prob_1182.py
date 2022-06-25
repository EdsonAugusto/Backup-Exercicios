post = int(input())
operation = input()

vector, exit = 0, 0
for line in range(12):
	for column in range(12):
		vector = float(input())
		if column == post:
			exit += vector

if operation == 'S': print('{:.1f}'.format(exit))
else: print('{:.1f}'.format(exit/12))


