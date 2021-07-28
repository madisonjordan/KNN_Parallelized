# set.py - set builder

'''
input: csv files from the ./data folder
output: one csv file (matrix) in the ./data folder

This is a program that will take in all csv files (word frequencies) from the ./data folder and
perform a union operation so that all words are included in one table
'''

import os
from functools import reduce
from os import listdir
from os.path import isfile, join

import pandas as pd

# Since this program reads in all the files from the data/ directory,
# we want to make sure it only reads in files we want it too.
# Query book is also removed so it can be added on to the end of the
# matrix later.
unwantedFiles = ['rows.txt', 'cols.txt', 'matrix.csv', 'querybook.csv']
dataPath = 'data/'
fileNames = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
fileNames = [ele for ele in fileNames if ele not in unwantedFiles]


# Removes extension names from the end of file names
columns = [os.path.splitext(x)[0] for x in fileNames]
# Insert another column for the columns matrix
columns.insert(0, 'Word')
fileNames.insert(len(fileNames), 'querybook.csv')
# Add query book column to the end of the matrix
columns.insert(len(columns), 'querybook')

wordData = []
# Create empty matrix but with columns at the top that will be filled in
matrix = pd.DataFrame(columns=columns)

# Open each word count file for each book, store into a list, and then
# insert these lists into another list
for file in fileNames:
    myFile = open(f"./data/{file}", "r")
    readFile = myFile.read()
    dataVector = pd.read_csv(f"./data/{file}", sep=",")
    wordData.append(dataVector)
    myFile.close()

pd.set_option("display.max_rows", None, "display.max_columns", None)
# Fill unknown or blank columns with 0s since some words wont exist in other books
# their word count should be 0.
# Lambda function to merge the wordData list containing all the word counts
matrix = reduce(lambda left, right: pd.merge(left, right, on=['Word'], how='outer'), wordData).fillna(0)
print(columns)
matrix.columns = [columns]
matrix.to_csv(path_or_buf="./data/matrix.csv")

# Rows and cols text files are created to be fed into CPP program to make vector
# initialization dynamic without changing CPP program.
rows = open("./data/rows.txt", "w+")
rows.write(str(len(matrix)))
rows.close()

cols = open("./data/cols.txt", "w+")
cols.write(str(len(matrix.columns)))
cols.close()
