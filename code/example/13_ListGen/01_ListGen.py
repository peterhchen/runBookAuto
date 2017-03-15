#!/usr/bin/python3
'''
Ierables: A sequence of values
'''
class Alphabet:
	def __init__ (self):
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
		self.index = -1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.index >= len (self.letters) - 1:
			raise StopIteration
		self.index += 1
		return self.letters[self.index]

alpha = Alphabet()
for letter in alpha:
	print (letter, end= ", ")
		