#!/usr/bin/python3
'''
Generate a lis of 10 values
Multiple them by 2
Return multiples of 8
'''
print  ([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
