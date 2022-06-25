numberOfLanguages, translationDictionary = int(input()), {}
for i in range(numberOfLanguages):
	key = input()
	translationDictionary[key] = input()
numberHangTags, children = int(input()), []
for k in range(numberHangTags):
	name, language = input(), input()
	children.append(name+'\n'+translationDictionary[language])
for exit in range(len(children)): print(children[exit]); print()