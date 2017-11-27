#import packages
import os
import csv
import operator
import collections
from datetime import datetime


ALLOWED_FORMATS = ['%b-%d', '%b-%Y']

def convert_date(string):

    for format in ALLOWED_FORMATS:
        try:
            return datetime.strptime(string, format).strftime('%b-%Y')
        except ValueError:
            pass

#set path for  csv file
filePath=os.path.join("raw_data","budget_data_2.csv")
with open(filePath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       # row[0]=row['Date']
        #row[1]=row['Revenue']
        print(row['Date'].split("-"))
#
#set winner vote as zero

#open csv file
#with open(filePath) as fileOpen:
	#read file
	#readFile1=csv.reader(fileOpen,delimiter=',')
	
	#skip header
	#header=next(readFile1)
	#noOfCol=len(header)
	#read each row in file
	#for row in readFile1:
	#	for i in range(0,noOfCol):
	#		if header[i]=="Date":
				#set count as value for keys in the dictionary
	#			convert_date(row[i]).split('-')
					#print(csvDat)
	

					#csvDat=row[i]
			

				


