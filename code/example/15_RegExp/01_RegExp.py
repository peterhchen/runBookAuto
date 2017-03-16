#!/usr/bin/python3
'''
Regular Expression (Regex) are used to:
1. Search for a specific string in a large amount of data
2. Verify a string is properly format (email. phone, and etc)
3. Find a astring and replace it.
4. Format data.
'''

import re

# Note: The "ape." can match anything "ape" or "apex".
print ("Search")
if re.search ("ape.", "The ape was at at the apex"):
	print ("Ape found.")

print ("Find All:")	
appApes = re.findall ("ape.", "The ape was the apex")
for i in appApes:
	print (i)

theStr = "The ape was the apex"
print ("Find Iter:")
for i in re.finditer ("ape.", theStr):
	locTuple = i.span() 
	print(locTuple)
	print(theStr[locTuple[0]:locTuple[1]])