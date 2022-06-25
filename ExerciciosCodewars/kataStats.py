def merge_arrays(first, second): 
	exitList, result = first + second, []
	exitList.sort()
	for i in range(len(exitList)):
		if exitList[i] not in result: result.append(exitList[i])
	return result

print(merge_arrays([2, 4, 8], [2, 4, 6]))