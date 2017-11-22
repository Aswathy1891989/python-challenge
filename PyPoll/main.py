import os
import csv
import operator
import collections

filePath=os.path.join("raw_data","election_data_1.csv")
Winner=0

with open(filePath) as fileOpen:
	readFile1=csv.reader(fileOpen,delimiter=',')
#	readFile2=csv.reader(fileOpen,delimiter=',')
	
	next(readFile1)

	counts = collections.Counter()
	for row in readFile1:
		counts[row[2]]+=1
with open(filePath) as fileOpen:
	readFile1=csv.reader(fileOpen,delimiter="'")
	totalVotes=len(list(readFile1))
    	
print("Election Results")		
print("--------------------------------")
print("Total Votes: ",totalVotes)
print("--------------------------------")
for showItems,showKeys in counts.items():
	percentageVote=int((showKeys/totalVotes)*100)
	print(showItems, " : " ,percentageVote,"%  (",showKeys,")")
	if showKeys>Winner:
		Winner=showKeys
		winnerName=showItems
print("--------------------------------")
print("Winner: ",winnerName)
print("--------------------------------")