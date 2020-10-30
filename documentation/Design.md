# Design Document

## Environment

The software is developed using Python3, with [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.

## Libraries 

1. NLTK Python Library - NLTK is a leading platform for building Python programs to work with human language data. It help in working with corpora, categorizing text, analyzing linguistic structure, and more using Python3. We have used it to detect stopwords from the input file.

2. Matplotlib - It provides an object-oriented API for embedding plots into applications. Used for word frequency plot.

3. Pandas and Numpy - Pandas is an open-source Python library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. NumPy is a python library used for working with arrays. Both of them are used for statistical analysis of input file.

4. Counter - A Counter is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures are commonly used in other languages. It was used to find least and most frequent words from text file efficiently and faster.

## Design

**Structure**

- *gui.py* - gives proper interface for our application which has various buttons which help to achieve our desired task. This is the main file of application which connects it to other files.
- *stats.py* - returns all the statistical information about the input file. For each line from input file removes the punctuation marks and updates counter for no. of lines. Then splits the line into words and count the words. Then removes stopwords using NLTK library.
- *hist.py* - returns the histogram plot corresponding to frequency of words.
- *keywords.py* - returns the lines in input file having at least one keyword from the keyword file.
- *requirements.txt* - This file contains name of all libraries which has to be install to run the Application. (Run pip3 install -r 
requirements.txt to install all libraries.)
- */testfiles* - includes the input.txr and keyword.txt for testing of software.
- */documentation* - contains all documentation files of application.
- */GUI_images* - contains images used in the user manual.

**Features of GUI**

- *Open Input File Button* - to browse input text file from users pc.
- *Stats TextArea* - shows statistical analysis of input file.
- *Plot Histogram Button* - plots word frequency graph on click.
- *Refresh Button* - when clicked updates stats of inputs file when file changes on disk.
- *Open Keyword File Button* - to browse keyword file from users pc.
- *Sentences with Keywords TextArea* - shows extracted sentences from input files conataing keywords.

## References

1. [https://www.tutorialspoint.com/python_text_processing/python_remove_stopwords.htm](https://www.tutorialspoint.com/python_text_processing/python_remove_stopwords.htm)
2. [https://www.geeksforgeeks.org/python-gui-tkinter/](https://www.geeksforgeeks.org/python-gui-tkinter/)
3. [https://github.com/padmanrajan/DataAdder](https://github.com/padmanrajan/DataAdder)