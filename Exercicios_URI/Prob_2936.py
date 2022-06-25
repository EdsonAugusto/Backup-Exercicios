portionValue, portions = [300, 1500, 600, 1000, 150], []
for i in range(len(portionValue)):
	portions.append(int(input())*portionValue[i])
print(sum(portions)+225)
