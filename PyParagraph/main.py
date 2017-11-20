#import required packages
import re 
import os


#function that splits the paragraph
def findSentenceEnd(paragraph):
    sentenceEnd = re.compile(r"""
      						     # Split sentences on whitespace between them.
        (?:             	  	 # Group for two positive lookbehinds.
          (?<=[.!?])    	     # Either an end of sentence punct,
        | (?<=[.!?]['"])	     # or end of sentence punct and quote.
        )                 		 # End group of two positive lookbehinds.
        (?<!  Mr\.   )	   		 # Don't end sentence on "Mr."
        (?<!  Mrs\.  )			 # Don't end sentence on "Mrs."
        (?<!  Ms\.   )			 # Don't end sentence on "Ms."
        (?<!  Jr\.   )			 # Don't end sentence on "Jr."
        (?<!  Dr\.   )			 # Don't end sentence on "Dr."
        (?<!  Prof\. )			 # Don't end sentence on "Prof."
        (?<!  Sr\.   )			 # Don't end sentence on "Sr."
        \s+               		 # Split on whitespace between sentences.
        """, 
        re.IGNORECASE | re.VERBOSE)			#ignore case and treats as verbose(that is spaces, tabs, and carriage returns are not matched as spaces, tabs, and carriage returns and comments )
    return sentenceEnd.split(paragraph)

		


#set the file path
filePath=os.path.join("raw_data","paragraph_1.txt")
fileOpen=open(filePath,'r')
contentofFile=fileOpen.read()
sentenceSplit=findSentenceEnd(contentofFile)
sentenceCount=0
wordCount=0
letterCount=0
averageSentencelength=0
wordsList=[]
for word in sentenceSplit:
	#spliting words at space
	wordsList=word.split(' ')
	#increment sentence count by 1
	sentenceCount+=1
	#calculate wordcount
	wordCount+=len(wordsList)
	#find out length of each word
	for character in wordsList:
		letterCount+=len(character)
		
	
		
print("Paragraph Analysis")
print("--------------------")
print("Approximate Word Count ",wordCount)
print("Approximate Sentence Count ",sentenceCount)
print("Average Letter Count ", (letterCount+0.0)/wordCount) #avaerage letters per words
print("Average Word Count ",(wordCount+0.0)/sentenceCount)  #average words per sentence