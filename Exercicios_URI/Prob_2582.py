inputValue, dicSystem = int(input()), {0 : 'PROXYCITY', 1 : 'P.Y.N.G.', 2 : 'DNSUEY!', 3 : 'SERVERS', 4 : 'HOST!', 5 : 'CRIPTONIZE', 6 : 'OFFLINE DAY', 7 : 'SALT', 8 : 'ANSWER!', 9 : 'RAR?', 10 : 'WIFI ANTENNAS'}
for i in range(inputValue):
	inputDownload = list(map(int, input().split()))
	print(dicSystem[sum(inputDownload)])