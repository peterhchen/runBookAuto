#!/usr/bin/python3
'''
Create a function that receives a list and a function.
The function passed will return True or False if a list 
value is odd.
The surrounding function will return a list of odd numbers.
'''
def isOdd (num):
	if num % 2 == 0:
		return False
	else:
		return True
		
def changeList(list, func):
	oddList = []
	for i in list:
		if func (i):
			oddList.append(i)
	return oddList

	aList = range (1, 20)
print (changeList(aList, isOdd))