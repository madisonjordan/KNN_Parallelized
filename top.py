# top.py - top words

'''
input: txt files from ./books folder
output: csv files into the ./data folder

This is a program that will find the top 100 words from a book discluding the stop words. These 100 top words will
be stored in a csv file in the ./data folder for later use in the set.py program.
'''


# https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0

import collections
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Read input file, note the encoding is specified here 
# It may be different in your text file
##### CHANGE THE FILE = OPEN() LINE #####
def createVector(bookName):
    file = open(f'./books/{bookName}.txt', encoding='utf-8')
    a = file.read()
    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
    # Instantiate a dictionary, and for every word in the file,
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    uniqueCount = 0
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        uniqueCount += uniqueCount+1
        word = word.replace("\“","")
        word = word.replace("_","")
        word = word.replace("(","")
        word = word.replace(")","")
        word = word.replace("[","")
        word = word.replace("-","")
        word = word.replace("]","")
        word = word.replace("&","")
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace(";","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("?","")
        # Fixes issue with ascii chars
        word = word.encode('ascii', 'ignore')
        word = word.decode()
        word = word.replace("*","")
        word = word.replace("\'", "")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    # Print most common word
    n_print=uniqueCount
    #n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
    # Close the file
    file.close()


    # Create a data frame of the most common words
    # Draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')

    df.to_csv(f'data/{bookName}.csv', index=False)

bookPath = 'books/'
fileNames = [f for f in listdir(bookPath) if isfile(join(bookPath, f))]
fileNames = [os.path.splitext(x)[0] for x in fileNames]

for file in fileNames:
    createVector(file)
