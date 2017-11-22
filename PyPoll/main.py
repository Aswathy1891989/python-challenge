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
	percentageVote=(showKeys/totalVotes)*100
	print(showItems, " : ","%.1f" %percentageVote,"%  (",showKeys,")")
	if showKeys>Winner:
		Winner=showKeys
		winnerName=showItems
print("--------------------------------")
print("Winner: ",winnerName)
print("--------------------------------")
fileWritePath=os.path.join("raw_data","Election_Report.txt")
fileWriter=open(fileWritePath,"w")
fileWriter.write("Election Results\n")
fileWriter.write("--------------------------------\n")
fileWriter.writelines("Total Votes: "+str(totalVotes)+"\n")
fileWriter.write("--------------------------------\n")
for showItems,showKeys in counts.items():
	percentageVote=(showKeys/totalVotes)*100
	fileWriter.writelines(showItems + " : "+"%.1f" %percentageVote +"%  ("+str(showKeys)+")")
	fileWriter.write("\n")
fileWriter.write("--------------------------------\n")
fileWriter.write("Winner: "+winnerName)
fileWriter.write("\n")
fileWriter.write("--------------------------------\n")
fileWriter.close()
