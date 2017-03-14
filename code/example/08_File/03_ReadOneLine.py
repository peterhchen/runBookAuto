#!/usr/bin/python3
# Read and write and file.
import os
# Read/write with Unicode (utf-8)
with open ("mydata3.txt", mode ="w", encoding="utf-8") as myFile:
	myFile.write ("write a random string\nMore text\nand\nsome more")
	
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
		lineNum += 1

