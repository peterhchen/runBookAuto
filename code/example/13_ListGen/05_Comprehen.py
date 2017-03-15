#!/usr/bin/python3
'''
Generate a lis of 50 values between 1 and 1000
Return multiples of 9
'''
import random

print ([x for x in [random.randint(1, 1001) for i in range (50)]if x % 9 == 0])
