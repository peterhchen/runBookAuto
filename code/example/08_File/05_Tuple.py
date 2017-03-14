#!/usr/bin/python3
# Read and write and file.
myTuple = (1, 2, 3, 5, 8)
	
print ("1st Value:", myTuple[0])
print (myTuple[0:3])
print("Tuple Length: ", len (myTuple))
moreTuple = myTuple + (20, 30, 40)
print ("30 in Tuple", 30 in moreTuple)

for i in moreTuple:
	print (i)
	
aList = [50, 60, 70]
aTuple = tuple(aList)

aList = list (aTuple)

print ("Min: ", min (aTuple))
print ("Max: ", max (aTuple))