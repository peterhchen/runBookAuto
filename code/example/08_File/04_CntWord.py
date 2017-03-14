#!/usr/bin/python3
# Read and write and file.
import os
# Read/write with Unicode (utf-8)
with open ("mydata3.txt", mode ="w", encoding="utf-8") as myFile:
	myFile.write ("write a random string\nMore text\nand\nsome more\n")
	
print("print mydata.txt: ")
with open ("mydata3.txt", encoding="utf-8") as myFile:
	print (myFile.read())
	

with open ("mydata3.txt", encoding="utf-8") as myFile:
	lineNum =1
	while True:
		line = myFile.readline()
		if not line:
			break
		print ("Line ", lineNum, " : ", line, end="")
		# split
		wordList = line.split()
		# Count how many characters
		charCount = 0
		for word in wordList:
			for char in word:
				charCount += 1
		# Average Character Count
		avgNumChars = charCount/len(wordList)
		print ("Avg Word Length : {:.2}".format (avgNumChars))
		lineNum += 1

