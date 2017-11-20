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
		contentofFile=fileOpen.read()
		#call the function to split sentence
		sentenceSplit=findSentenceEnd(contentofFile)
		#initialize counting variables to 0
		sentenceCount=0
		wordCount=0
		letterCount=0
		averageSentencelength=0
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

		
			
		print("Paragraph Analysis for Text file : " + textFileChoice)
		print("---------------------------------------------------------------")
		#print words count
		print("Approximate Word Count ",wordCount)
		#print no.of sentence
		print("Approximate Sentence Count ",sentenceCount)
		#print avaerage letters per words
		print("Average Letter Count ", (letterCount+0.0)/wordCount) 
		#print average words per sentence
		print("Average Word Count ",(wordCount+0.0)/sentenceCount)
	#exception for file not existing
	except IOError:
		print("Error: Sorry File does not appear to exist.")
    #enter choice to continue	
	choice=input("Do you want to analyse another text File? (y)es or (n)o")

#**************************************************************************END*************************************************************************************************************************#