#***************************************************************************************************************************************************************************************************#
#Create a Python script to automate the analysis of any such passage using these metrics. This  script will do the following:

#Import a text file filled with a paragraph of your choosing.

# Analyse the passage for each of the following:

	#Approximate word count

	#Approximate sentence count

	#Approximate letter count (per word)

	#Average sentence length (in words)

#**************************************************************************************************************************************************************************************************#

#import required packages
import re 
import os


#function that splits the paragraph
def findSentenceEnd(textContent):
    sentenceEnd = re.compile(r"""
      						    
        (?:             	  	 # start group .
          (?<=[.!?])    	     # Either an end of sentence with .,or !,
        | (?<=[.!?]['"])	     # or end of sentence . or ! and quote.
        )                 		 # End group.
        (?<!  Mr\.   )	   		 # Don't end sentence on "Mr."
        (?<!  Mrs\.  )			 # Don't end sentence on "Mrs."
        (?<!  Ms\.   )			 # Don't end sentence on "Ms."
        (?<!  Jr\.   )			 # Don't end sentence on "Jr."
        (?<!  Dr\.   )			 # Don't end sentence on "Dr."
        (?<!  Prof\. )			 # Don't end sentence on "Prof."
        (?<!  Sr\.   )			 # Don't end sentence on "Sr."
        (?<!  \s[A-Z]\.)		 #Don't end sentence on Middle Name followed by dot
        \s+               		 # Split on whitespace .
        """, 
        re.IGNORECASE | re.VERBOSE)			#ignore case and treats as verbose(that is spaces, tabs, and carriage returns are not matched as spaces, tabs, and carriage returns and comments )
    return sentenceEnd.split(textContent)




 #start main program   

#set choice for iterating 	
choice="y"
#iterate the following for  choice is (y)es
while choice=="y":	
	try:
		#enter the file of choice in raw_data folder
		textFileChoice=input("Enter the text file for Paragraph Analysis : ")
		#set the file path
		filePath=os.path.join("raw_data",textFileChoice)
		#open the text file in read mode
		fileOpen=open(filePath,'r')
		#get teh content of file using read()
		splitParagraph=fileOpen.read()
		#call the function to split sentence
		sentenceSplit=findSentenceEnd(splitParagraph)
		#initialize counting variables to 0
		sentenceCount=0
		wordCount=0
		letterCount=0
		
		#create list for storing words
		wordsList=[]
		#Iterate through sentence list
		for word in sentenceSplit:
			#spliting words at space
			wordsList=word.split(' ')
			#increment sentence count by 1
			sentenceCount+=1
			#calculate wordcount
			wordCount+=len(wordsList)
			#find out length of each word as the letter count
			for character in wordsList:
				letterCount+=len(character)

		newFile,ext=textFileChoice.split(".")
		fileWritePath=os.path.join("raw_data",newFile+"_Analysis_Report.txt")	

		#open file in write mode
		fileWriter=open(fileWritePath,"w")#create text file based on text files

		print("Paragraph Analysis for Text file : " + textFileChoice)
		fileWriter.write("Paragraph Analysis for Text file : " + textFileChoice)
		print("---------------------------------------------------------------")
		fileWriter.write("\n")
		fileWriter.write("---------------------------------------------------------------")
		#print words count
		print("Approximate Word Count :",wordCount)
		fileWriter.write("\n")
		fileWriter.write("Approximate Word Count :"+str(wordCount))
		#print no.of sentence
		print("Approximate Sentence Count :",sentenceCount)
		fileWriter.write("\n")
		fileWriter.write("Approximate Sentence Count :"+str(sentenceCount))
		#print avaerage letters per words
		print("Average Letter Count :", (letterCount+0.0)/wordCount) 
		fileWriter.write("\n")
		fileWriter.write("Average Letter Count :"+ str((letterCount+0.0)/wordCount))
		#print average words per sentence
		print("Average Sentence Length :",(wordCount+0.0)/sentenceCount)
		fileWriter.write("\n")
		fileWriter.write("Average Sentence Length :"+str((wordCount+0.0)/sentenceCount))
			
		fileWriter.close()
		
	#exception for file not existing
	except IOError:
		print("Error: Sorry File does not appear to exist.")
    #enter choice to continue	
	choice=input("Do you want to analyse another text File? (y)es or (n)o")

#**************************************************************************END*************************************************************************************************************************#