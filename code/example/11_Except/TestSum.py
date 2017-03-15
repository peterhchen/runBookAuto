#!/usr/bin/python3

def getSum (*args):
	sum = 0;
	for i in args:
		sum += i
	return sum

def getMult (*args):
	mult = 1;
	for i in args:
		mult *= i
	return mult	
#print ("Sum: ", getSum (1, 2, 3, 4, 5))
#print ("Mult: ", getMult (1, 2, 3, 4, 5))