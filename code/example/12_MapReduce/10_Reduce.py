#!/usr/bin/python3
'''
Receive a list and turn into a single result
'''
from functools import reduce
print (reduce ((lambda x, y: x + y), range (1, 6)))