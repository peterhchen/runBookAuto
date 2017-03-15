#!/usr/bin/python3
'''
Map
'''
# Create a List to hold H and T
numList = range (1, 11)

def mapFunc (num):
	return num * 2

print (list (map (mapFunc, numList)))	

print (list(map((lambda x: x * 3), numList)))
	
aList = list (map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))

print (aList)