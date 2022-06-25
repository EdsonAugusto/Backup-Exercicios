numberTest, experiences = int(input()), {'R':0, 'C':0, 'S':0, 'tot':0}

for i in range(numberTest):
	inputValue = list(map(str, input().split()))
	experiences[inputValue[1]] += int(inputValue[0])
	experiences['tot'] += int(inputValue[0])

print('Total: {} cobaias'.format(experiences['tot']))
print('Total de coelhos: {}'.format(experiences['C']))
print('Total de ratos: {}'.format(experiences['R']))
print('Total de sapos: {}'.format(experiences['S']))
print('Percentual de coelhos: {:.2f} %'.format((experiences['C']/experiences['tot'])*100))
print('Percentual de ratos: {:.2f} %'.format((experiences['R']/experiences['tot'])*100))
print('Percentual de sapos: {:.2f} %'.format((experiences['S']/experiences['tot'])*100))