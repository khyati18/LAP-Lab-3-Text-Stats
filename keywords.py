# Function to find and display lines with keywords
def get_input_lines(file1, file2):

	input_lines = ""

	f = open(file2, "r")
	Lines = f.readlines()
	Keywords = []
	for line in Lines:
		for words in line.strip().split():
			Keywords.append(words)

	f = open(file1, "r")
	Lines = f.readlines()
	for line in Lines:
		words = line.strip().split()
		if(set(Keywords).issubset(set(words))):
			print(line.strip())
			input_lines += line.strip() + "\n"

	return input_lines