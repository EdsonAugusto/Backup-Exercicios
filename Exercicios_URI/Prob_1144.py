inputValue = int(input())
for i in range(1, inputValue+1):
	print('{} {} {}'.format(i, i*i, (i*i)*i))
	print('{} {} {}'.format(i, (i*i)+1,((i*i)*i)+1))