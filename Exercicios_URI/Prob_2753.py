from string import ascii_lowercase

alpha, k = list(ascii_lowercase), 0
for i in range(97, 123):
	print('{} e {}'.format(i, alpha[k])); k += 1