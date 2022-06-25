inputTest, vector = int(input()), []
for i in range(inputTest): vector.append(int(input()))
vector.sort()
while len(vector) >= 1:
	print('{} aparece {} vez(es)'.format(vector[0], vector.count(vector[0])))
	for i in range(vector.count(vector[0])): del vector[0]