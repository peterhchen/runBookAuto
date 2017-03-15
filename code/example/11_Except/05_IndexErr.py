#!/usr/bin/python3
'''
Index Error
'''
try:
	aList=[1, 2, 3]
	print (aList[3])

except IndexError:
	print ("Index Error")

except:
	print ("Other Error")