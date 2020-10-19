#!/usr/bin/env python3
import string
import io
import nltk
from nltk.corpus import stopwords 

# Function to find all stats of the input file
def stats_of_file(content):

	# initializing stats as a string
	stats = ""

	lines_count,sentences,blank_lines,words_count=0,0,0,0

	words=[] #for storing all the words

	for line in content:

		lines_count+=1		#for counting no. of lines

		if(line.startswith('\n')):
			blank_lines+=1		#for blank lines

		else:

			#assume that each sentence ends with . or ! or ?
			sentences+=line.count('.')+line.count('!')+line.count('?')

			# Remove the leading spaces and newline character 
			line=line.strip()

		    # Remove the punctuation marks from the line 
			line = line.translate(line.maketrans("", "", string.punctuation)) 

			# Split the line into words 
			temp_words = line.split(" ") 	

			words.extend(temp_words)

			words_count+=len(temp_words)

	stats+="No of lines: "+str(lines_count)+"\n"
	stats+="No of blank lines: "+str(blank_lines)+"\n"
	stats+="No of sentences: "+str(sentences)+"\n"
	stats+="No of words: "+str(words_count)+"\n"

#	print(words)

	# #for stop words
	# stop_words = set(stopwords.words('english')) 
	# filtered_sentence = [w for w in words if not w in stop_words] 

	# filtered_sentence = [] 

	# for w in words: 
	# 	if w not in stop_words: 
	# 		filtered_sentence.append(w)
	# print(filtered_sentence) 



	#2. histogram for various words
	# make seperate python script for it


	#3. no. of stop-words in content

	#4. for removing stop-words from content

	#5. least frequently occuring word

	#6. max. occuring word after removing stop words

	return stats





