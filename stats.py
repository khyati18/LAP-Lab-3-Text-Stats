# Function to find all stats of the input file
def stats_of_file(content):

	# initializing stats as a string
	stats = ""

	# for counting lines in file
	Lines_List = content.split("\n")
	line_count = 0
	for i in Lines_List:
		if i:
			line_count += 1
	stats += "No. of lines in file -" + str(line_count+1) + "\n"

	#1. for counting total words in file

	#2. histogram for various words
	# make seperate python script for it

	#3. no. of stop-words in content

	#4. for removing stop-words from content

	#5. least frequently occuring word

	#6. max. occuring word after removing stop words

	return stats