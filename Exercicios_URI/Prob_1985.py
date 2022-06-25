dicValues = {1001 : 1.5, 1002 : 2.5, 1003 : 3.5, 1004 : 4.5, 1005 : 5.5}
inputValue, totalSale = int(input()), 0
for i in range(inputValue):
	productCode = input()
	productCode = list(map(int, productCode.split()))
	totalSale += dicValues[productCode[0]] * productCode[1]
print('{:.2f}'.format(totalSale))