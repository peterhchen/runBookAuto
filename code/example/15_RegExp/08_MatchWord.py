#!/usr/bin/python3
'''
match word:
\w: [a-zA-Z0-9]
\W: [^a-zA-Z0-9]
\s: [\f\n\r\t\v]
\S: [^\f\n\r\t\v]
a+:
'''
import re

phNum = "408-858-7657"

if re.search ("\w{3}-\w{3}-\w{4}", phNum):
	print ("Match phone No.")
else:
	print ("Not Match phone No.")
	
randStr = "Ultraman"

# Match 2-20 character length
if re.search ("\w{2,20}", randStr):
	print ("It is a valid string.")
else:
	print ("It is an invalid string.")
	
randStr1 = "Toshio Wataru"

# Match 2-20 character length
if re.search ("\w{2,20}\s\w{2,20}", randStr1):
	print ("It is a valid full name.")
else:
	print ("It is an invalid full name.")

print()
randStr2 = "a as ape bug"
# Match a+ length = 3 (a, as, ape)
print ("Match len: ", len(re.findall ("a+", randStr2)))	