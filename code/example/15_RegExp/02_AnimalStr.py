#!/usr/bin/python3
'''
Animal String
'''

import re

animalStr = "Cat rat mat pat"

print ("Original String: ")
print (animalStr)
print()

print ("Match c-m,C-M, p: ")
# match Cat, mat, pat
allAnimals = re.findall ("[c-mC-Mp]at", animalStr)
for i in allAnimals:
	print (i)
print()
	
print ("Not Match ^C, ^r: ")
# not match Cat, rat
allAnimals = re.findall ("[^Cr]at", animalStr)
for i in allAnimals:
	print (i)