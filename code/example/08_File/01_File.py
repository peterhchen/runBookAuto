#!/usr/bin/python3
# Read and write and file.
import os
# Read/write with Unicode (utf-8)
with open ("mydata.txt", mode ="w", encoding="utf-8") as myFile:
	myFile.write ("write a random string\nMore text\nand\nsome more")
	
print("print mydata.txt: ")
with open ("mydata.txt", encoding="utf-8") as myFile:
	print (myFile.read())
	
print(myFile.closed)
print("File Name: ", myFile.name)
print("File mode: ", myFile.mode)

if (os.path.exists ("mydata2.txt")):
	os.remove ("mydata2.txt")
if (os.path.exists ("mydata.txt")):
	os.rename ("mydata.txt", "mydata2.txt")
if (os.path.exists ("mydata2.txt")):
	os.remove ("mydata2.txt")
if (not(os.path.exists ("mydir"))):
	os.mkdir("mydir")
os.chdir ("mydir")
print ("Current Directory: ", os.getcwd())
os.chdir ("..")
print ("Current Directory: ", os.getcwd())
os.rmdir ("mydir")

