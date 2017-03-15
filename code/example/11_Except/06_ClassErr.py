#!/usr/bin/python3
'''
Raise Error
'''
'''
class DogNameError (Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__ (self, *args, **kwargs)
'''

try:
	dogName = input ("What is your name: ")

	if any (char.isdigit() for char in dogName):
		raise DogNameError
	
except DogNameError:
	print ("Dog name cannot contain number")