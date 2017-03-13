#!/usr/bin/python3

import random
import math

randList = ["string", 1.234, 21]

oneToTen = list (range(10))

randList = randList + oneToTen
print (randList[0])

print ("List Length: ", len (randList))
first3 = randList [0:3]
for i in first3:
	print ("{} : {} ". format (first3.index(i), i))
print()

print(first3[0] * 3)	# repeat three times
print ("string" in first3)	# return true or false
print ("Index if string: ", first3.index ("string")) # 0
print ("How many strings: ", first3.count("string")) # 1
print()

first3[0] = "New String"
for i in first3:
	print ("{} : {} ". format (first3.index(i), i))
print()

first3.append ("Another")
for i in first3:
	print ("{} : {} ". format (first3.index(i), i))

