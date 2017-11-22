import os
import csv
import operator

filePath=os.path.join("raw_data","election_data_1.csv")
count=0
with open(filePath) as fileOpen:
	readFile=csv.reader(fileOpen,delimiter=',')
	next(readFile)
	sortCSV=sorted(readFile,key=operator.itemgetter(2))
	
	#print(readFile)
	for row in sortCSV:
		
		if row[2]!=next(readFile).row[2]:
			print(count)
			count=0
		else:
			count+=1

#print(count)
