# Requirements Document

## Software Details

The software provides an GUI for input of 2 ASCII text files (One being input file and other keyword file). Users queries are answered by the output of the interface. 

## Queries

**Statistical Analysis of Input File**

- Total No. of Lines
- Total no. of Blank lines
- Total no of Sentences
- Total no. of Words
- Total no. of Stopwords (articles, punctuation,etc)
- Total no. of words after removing Stopwords
- Most frequent word
- Least frequent word

**Frequency Plot**

Histogram with words on X-axis and corresponding frequency on Y-axis is to be generated. This plot should not include stopwords.

**Features of GUI**

- Button to browse the input file from user's pc
- No need to display the text file in the software
- Display the stats of input file on GUI itself
- 'Plot Graph' Button and display it seperately as png file
- 'Refresh' button to update stats dynamically when the text file changes on disk
- Output the lines of input file which contains at least one word from the set of keywords
  - Input keyword file from user
  - Extract sentences containing atleast on keyword
  - Display extracted on the GUI
