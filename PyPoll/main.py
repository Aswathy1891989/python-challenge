import os
import csv

filePath=os.path.join("raw_data","election_data_1.csv")

with open(filePath) as fileOpen:
	readFile=csv.reader(fileOpen,delimiter=',')
	#print(readFile)
	for row in readFile:
		print(row)
