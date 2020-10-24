# Function to find and display lines with keywords
def get_input_lines(file1, file2):

	input_lines = ""

	# Opening and Reading keyword file
	f = open(file2, "r")
	Lines = f.readlines()

	# adding words to keyword array
	Keywords = []
	for line in Lines:
		for words in line.strip().split():
			Keywords.append(words)

	# for each line in input text check if it contains any keyword
	f = open(file1, "r")
	Lines = f.readlines()
	for line in Lines:
		words = line.strip().split()
		if(set(Keywords).issubset(set(words))):
			# print(line.strip())
			input_lines += line.strip() + "\n"

	return input_lines