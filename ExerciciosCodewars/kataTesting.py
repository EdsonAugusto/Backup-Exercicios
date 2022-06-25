def number(lines):
	if len(lines) < 1: return []
	else:
		exit = []
		for i in range(len(lines)):
			exit.append('{}: {}'.format(i+1, lines[i]))
		return exit

print(number([]))
