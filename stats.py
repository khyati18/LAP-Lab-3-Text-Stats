#!/usr/bin/env python3
import string
import io
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
from collections import Counter 
# Function to find all stats of the input file
def stats_of_file(content):

	# initializing stats as a string
	stats = ""

	lines_count,blank_lines,words_count=0,0,0

	words=[] #for storing all the words

	flag = 0

	line_of_content = ""

	for letter in content:

		if(letter=='\n' and flag==0):

			# Remove the punctuation marks from the line 
			line_of_content = line_of_content.translate(line_of_content.maketrans("", "", string.punctuation)) 

			# Split the line into words 
			temp_words = line_of_content.split(" ") 	

			words.extend(temp_words)

			words_count+=len(temp_words)

			lines_count+=1					# for counting no. of lines
			flag = 1						# if last letter of line

			line_of_content = ""

		elif(letter=='\n' and flag==1):
			blank_lines+=1					#for blank lines
			lines_count+=1					# for counting no. of lines

		else:
			flag = 0						# if not last letter of line
			line_of_content += letter

	if(line_of_content!=""):
		# Remove the punctuation marks from the line 
		line_of_content = line_of_content.translate(line_of_content.maketrans("", "", string.punctuation)) 

		#line_of_content=line_of_content.strip()
		
		# Split the line into words 
		temp_words = line_of_content.split(" ") 	

		words.extend(temp_words)

		lines_count+=1					# for counting no. of lines

	words = [ele for ele in words if ele.strip()]
	words_count=len(words) 

	stats+="No of lines: "+str(lines_count)+"\n"
	stats+="No of blank lines: "+str(blank_lines)+"\n"
	stats+="No of sentences: "+str(lines_count-blank_lines)+"\n"
	stats+="No of words: "+str(words_count)+"\n"

	#for stop words
	stop_words = set(stopwords.words('english')) 
	filtered_sentence = [w for w in words if not w in stop_words] 

	filtered_sentence = [] 

	for w in words: 
		if w not in stop_words : 
			filtered_sentence.append(w)
	
	stop_words_count=words_count-len(filtered_sentence)

	stats+="No of stop words: "+str(stop_words_count)+"\n"
	stats+="No of words after removing stop words: "+str(len(filtered_sentence))+"\n"

	# high_freq = statistics.mode(filtered_sentence) 	
	# low_freq = min(set(filtered_sentence), key = filtered_sentence.count) 

	freq = Counter(filtered_sentence)

	# array sorted with increasing frequency of words
	arr = [pair[0] for pair in sorted(freq.items(), key=lambda item: item[1])]

	# print(arr)
	low_freq = arr[0]
	high_freq = arr[len(freq)-1]


	stats+="Word with highest frequency: "+str(high_freq)+"\n"
	stats+="Word with lowest frequency: "+str(low_freq)

	return stats
