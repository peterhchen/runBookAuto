#!/usr/bin/python3
# 1, 1, 2, 3, 5, 8, 13
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 =1

# 1st: result = fib (2) + fib (1): 2 + 1 = 3
# 2nd: result = (fib (1)+ fib(0)) + fib(0) : 1 + 0 =1

def fib (n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else: 
		result = fib(n-1) + fib(n-2)
		return result

# ASk how many numbers they want
numFibValues = int (input ("How many fibonacci values should be found: "))

i = 1

while i < numFibValues:
	fibValue = fib (i)
	print (fibValue)
	i += 1

print ("Finished")
