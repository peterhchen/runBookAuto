#!/usr/bin/python3
'''
Ierables: A sequence of values
'''
class FibGenerator:
	def __init__ (self):
		self.first = 0
		self.second = 1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		fibNum = self.first + self.second
		self.first = self.second
		self.second = fibNum
		return fibNum

fibSeq = FibGenerator ()

for i in range (10):
	print (next(fibSeq), end=", ")
		