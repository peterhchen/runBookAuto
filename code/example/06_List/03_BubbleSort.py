#!/usr/bin/python3

import random
import math

#Bubble sort
# 1. outer loop
# 2. Inner loop 
# 3. if list[Index] > list [Index + 1]
# 4. swap
# 5. decrement outer loop by 1.
numList = []
for i in range(5):
	numList.append(random.randrange(1, 10))

print ("Oringinal List: ")
for i in numList:
	print (i, end =", ")
print()

i = len(numList) - 1
while i > 1:
	j = 0
	while j < i:
		print ("\nIs {} > {}?".format (numList[j], numList[j+1]))
		if numList[j] > numList[j + 1]:
			temp = numList[j]
			numList[j] = numList[j + 1]
			numList[j + 1] = temp
		else:
			print ("Don't switch")
		j += 1
		for k in numList:
			print(k, end=",")
		print()
	print ("END OF ROUND")
	i -= 1
	
print()
print ("Bubble Sort List: ")
for k in numList:
	print (k, end =", ")

print()