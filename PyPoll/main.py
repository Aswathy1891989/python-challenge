#import packages
import os
import csv
import operator
import collections
#set path for  csv file
filePath1=os.path.join("raw_data","election_data_1.csv")
filePath2=os.path.join("raw_data","election_data_2.csv")
#set winner vote as zero
Winner=0
totalVotes=0
#open first csv file
with open(filePath1) as fileOpen1:
	#read file
	readFile1=csv.reader(fileOpen1,delimiter=',')
	#skip header
	header1=next(readFile1)
	noOfCol1=len(header1)
	#declare counts dictionary as counter object
	counts = collections.Counter()
	#read each row in file
	for row1 in readFile1:
		for i in range(0,noOfCol1):
			if header1[i]=="Candidate":
				#set count as value for keys in the dictionary
				counts[row1[i]]+=1
				#count total votes
				totalVotes+=1


#opening and processing second file
with open(filePath2) as fileOpen2:
	#read file
	readFile2=csv.reader(fileOpen2,delimiter=',')
	#skip header
	header2=next(readFile2)
	noOfCol2=len(header2)
		
	#read each row in file
	for row2 in readFile2:
		for i in range(0,noOfCol2):
			if header2[i]=="Candidate":
				#set count as value for keys in the dictionary
				counts[row2[i]]+=1
				#count total votes
				totalVotes+=1

#*********Print to Terminal    	
print("Election Results")		
print("--------------------------------")
print("Total Votes: ",totalVotes)

print("--------------------------------")
#print contents of dictionary
for showItems,showKeys in counts.items():
	#calculate the percentage vote
	percentageVote=(showKeys/totalVotes)*100
	print(showItems, " : ","%.1f" %percentageVote,"%  (",showKeys,")")
	#find the winner
	if showKeys>Winner:
		Winner=showKeys
		winnerName=showItems

print("--------------------------------")
print("Winner: ",winnerName)
print("--------------------------------")


#************Print to File
#set path of text file to write
fileWritePath=os.path.join("raw_data","Election_Report.txt")
#open file in write mode
fileWriter=open(fileWritePath,"w")
#Write Contents
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
#Close File
fileWriter.close()
