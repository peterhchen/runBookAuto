#!/usr/bin/python3

import random
import math

#Python sort
numList = []
for i in range(5):
	numList.append(random.randrange(1, 10))

numList.insert (5, 10) 	# insert(index, obj)
numList.remove (10)		# remove (obj)
numList.pop (2)			# pop (obj)

numList.sort()
for k in numList:
	print(k, end=", ")
print()

numList.reverse()
for k in numList:
	print(k, end=", ")
print()