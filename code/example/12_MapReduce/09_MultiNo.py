#!/usr/bin/python3
'''
Multiple 9 of a radnom value list
'''
import random
# Generate a random list
randList = list (random.randint(1,1001) for i in range (100))
print (list (filter ((lambda x: x % 9 == 0), randList)))