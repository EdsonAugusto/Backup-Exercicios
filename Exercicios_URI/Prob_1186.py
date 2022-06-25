class Secondary_Diagonal:

	def __init__(self, sampleList):
		self.sampleList =  sampleList

	def sequence_Organizer(self):
		tempList = []
		for i in range(1,len(self.sampleList)):
			tempList.append(self.sampleList[i][::-1])
		return tempList[::-1]

	def data_Collector(self):
		self.sampleList, self.sampleExit = Secondary_Diagonal.sequence_Organizer(self), []
		for i in range(len(self.sampleList)):
			for k in range(11-i):
				self.sampleExit.append(self.sampleList[i][k])
		print(self.sampleExit)
		return self.sampleExit

def appendMatrix():
	exitList = []
	for i in range(12):
		exitList.append([])
		for k in range(12):
			exitList[i].append(float(input()))
	return exitList

choice = input()
main = Secondary_Diagonal(appendMatrix())
if choice == 'S': print('{:.1f}'.format(sum(main.data_Collector())))
else: print('{:.1f}'.format(sum(main.data_Collector())/66))

def test_appendMatrix():
	exitList, temp = [], 1
	for i in range(12):
		exitList.append([])
		for k in range(12):
			exitList[i].append(int(temp))
			temp += 1
	print(exitList)
	return exitList