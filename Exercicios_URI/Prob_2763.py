inputDoc = input()
listDoc = list(inputDoc.split('.'))
listDoc += listDoc[2].split('-')
del listDoc[2]
for doc in listDoc:
	print(doc)