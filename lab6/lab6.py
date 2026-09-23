"""
Aqeel Hussain
Sep 23, 2026
lab 6 - working with files
"""
"""
open() function allows user to open and write files

syntax:
file_object = open("filename", "mode")
common "mode" = r or w
always close() the file when it's done
"""
print("\n ----- example 1: read a file ")
with open("phrases.txt", 'r') as file1:
    print(file1.read(5)) #read the first 5 characters
    print(file1.read(7)) #print the next 7 characters
    print(file1.read()) #print all lines

#check if the file was closed
print(f"Is the file closed? {file1.closed}")

print("\n ----- example 2: read a file lines ")
#readline function reads a single line
#read up to 30 characters of the first line and then 5 characters of the second line
with open("phrases.txt", 'r') as file1:
    #print(file1.readline(30))
    #print(file1.readline(5))
    print(file1.readline())

print("\n ----- example 3: read a file lines ")
with open("phrases.txt", 'r') as file1:
    print(file1.readlines())

print("\n ----- example 4: loop to each line in a file ")
with open("phrases.txt", 'r') as file1:
    filelines = file1.readlines()
    for eachline in filelines:
        print(f"{len(eachline)}",end="\t")
        print(eachline.strip()) #strip() removes the \n character

print("\n ----- example 5: write mode ")
#w mode creates a new file if the file doesn't exist
#w mode overwrites a file if the file already exists
with open ("lastname.txt", 'w') as file:
    file.write("Python Basics for Data Science\n")
    file.write("Type your full name")

print("\n ----- example 6: append mode ")
#a mode adds information to an existing
#if the file doesn't exist, it will create a new file and append the new data
#example 6, add the date and time

from datetime import datetime

with open("lastname.txt", 'a') as file:
    file.write(f"\n{datetime.now}")

print("\n ----- example 7: pandas ")
#Pandas is a data analysis and manipulation library built on top of 
#Pandas provide data structures like Series and DataFrame
#install Pandas --> pip install pandas

import pandas as pd

data = {
    'name' : ['Alice', 'Bob', 'Charlie'],
    'age' : [25, 30, 19]
}

df = pd.DataFrame(data)
print(df)