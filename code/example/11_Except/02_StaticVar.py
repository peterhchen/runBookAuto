#!/usr/bin/python3
'''
static variable

'''
class Dog:
	num_of_dogs = 0		# Default is static variable 
	
	def __init__ (self, name = "Unknown"):
		self.name = name
		Dog.num_of_dogs += 1

	@staticmethod
	def getNumOfDogs ():
		print ("No of Dog {}".format (Dog.num_of_dogs))
	
def main():
	spot = Dog ("Spot")
	poodle = Dog ("Doug")
	spot.getNumOfDogs()

main()