#!/usr/bin/python

"""Python script to create a histogram of words in a text file.
Text file can contain punctuation, new lines, etc.,
"""

import os
import sys
import string
import argparse
import operator

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
    
def main(content):
    
    
    
    # Path to text file to analyse
    rawfilepath = content
    
    # Print a histogram containing the top N words, and print them and their counts.
    top_n = 100
    
    # Load the file
    filepath = os.path.normpath(os.path.join(rawfilepath))
    # print(filepath)
    file = open(filepath, 'r')
    
    # Parse as a list, removing lines
    content_sublists = [line.split(',') for line in file.readlines()]
    
    # Parse into a single list (from a list of lists)
    content_list = [item for sublist in content_sublists for item in sublist]
    
    # Remove whitespace so we can concatenate appropriately, and unify case
    content_list_strip = [str.strip().lower() for str in content_list]
    
    # Concatenate strings into a single string
    content_concat = ' '.join(content_list_strip)
    
    # Remove punctuation and new lines
    punct = set(string.punctuation)
    unpunct_content = ''.join(x for x in content_concat if x not in punct)

    
    # Split string into list of strings, again
    word_list = unpunct_content.split()

    filtered_sentence = []
    #for stop words
    stop_words = set(stopwords.words('english'))
    for w in word_list:
        if w not in stop_words:
            filtered_sentence.append(w)
    
			
    
    # Perform count
    counts_all = Counter(filtered_sentence)
    
    words, count_values = zip(*counts_all.items())
    
    # Sort both lists by frequency in values (Schwartzian transform) - thanks, http://stackoverflow.com/questions/9543211/sorting-a-list-in-python-using-the-result-from-sorting-another-list
    values_sorted, words_sorted = zip(*sorted(zip(count_values, words), key=operator.itemgetter(0), reverse=True))
    
    # Top N
    words_sorted_top = words_sorted[0:top_n]
    values_sorted_top = values_sorted[0:top_n]
    
    
    # Histogram
    
    # Make xticklabels comprehensible by matplotlib
    xticklabels = str(list(words_sorted_top)).split()
    # Remove the single quotes, commas and enclosing square brackets
    xtlabs = [xstr.replace("'","").replace(",","").replace("]","").replace("[","") for xstr in xticklabels]
    
    indices = np.arange(len(words_sorted_top))
    width = 1
    fig = plt.figure()
    fig.suptitle('Word frequency histogram, top {0}'.format(top_n), fontsize=16)
    plt.xlabel('word', fontsize=12)
    plt.ylabel('count', fontsize=12)
    plt.bar(indices, values_sorted_top, width=0.5 , align='center')
    plt.xticks(indices + width * 0.5, xtlabs, rotation='vertical', fontsize=8)
    plt.show()
    

    
# End
