#import packages
import os
import csv
import operator
import collections
from datetime import date
import operator
#set path for  csv file
filePath=os.path.join("raw_data","budget_data_1.csv")
#set winner vote as zero
month=[]
Winner=0
#open csv file
with open(filePath) as fileOpen:
	#read file
	readFile1=csv.reader(fileOpen,delimiter=',')
	#skip header
	next(readFile1)
	
	sortedlist = sorted(readFile1, key=operator.itemgetter(0), reverse=False)
	#declare counts dictionary as counter object
	counts = collections.Counter()
	#print(counts)
	#read each row in file
	for row in sortedlist:
		month=month+str(row[0]).split('-')
		#d=date.formordinal(row[0])
		date1=date(row[0]).strftime("%d/%m/%y")
		#date1 = date.strftime(row[0], '%m-%d ') 

		#set count as value for keys in the dictionary
		counts[row[0]]+=1
print(date1)
#print(month)
c=1
i=0
while i<len(month)-2:
	if month[i]==month[i+2]:
		c+=1
		#c=1
	else:
		#print("Month:",month[i],":",c)
		c=1
	#print(month[i],month[i+2])
	i+=2
#print(month[0],month[2])
#print(counts)
#print(counts)
	#for key in counts.keys():
	#	value=counts.get(key)
	#	print(value)