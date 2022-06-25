from string import ascii_lowercase


codeSecret = {'.':'a', '..':'b', '...':'c', '. .':'d', '.. ..':'e', '... ...':'f', '. . .':'g', '.. .. ..':'h', '... ... ...':'i',
'. . . .':'j', '.. .. .. ..':'k', '... ... ... ...':'l', '. . . . .':'m', '.. .. .. .. ..':'n', '... ... ... ... ...':'o', 
'. . . . . .':'p', '.. .. .. .. .. ..':'q', '... ... ... ... ... ...':'r', '. . . . . . .':'s', '.. .. .. .. .. .. ..':'t',
'... ... ... ... ... ... ...':'u', '. . . . . . . .':'v', '.. .. .. .. .. .. .. ..':'w', '... ... ... ... ... ... ... ...':'x',
'. . . . . . . . .':'y', '.. .. .. .. .. .. .. .. ..':'z'}

while True:
	try:
		numberTest, alpha = int(input()), list(ascii_lowercase)
		for i in range(numberTest):
			inputMessage = input()
			print(codeSecret[inputMessage])
	except EOFError: break

	
