inputDate = input()
listDate = list(inputDate.split('/'))
print('{}/{}/{}'.format(listDate[1], listDate[0], listDate[2]))
print('{}/{}/{}'.format(listDate[2], listDate[1], listDate[0]))
print('{}-{}-{}'.format(listDate[0], listDate[1], listDate[2]))