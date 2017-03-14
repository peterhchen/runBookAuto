#!/usr/bin/python3
# Real World Object: Attriblities and Capabilities
# Note:
# Python use args for variable parameters. 
# Therefore, Python does not have function overloading,
# i.e., parameter matching cannot be used in Python.
# Pyhton uses @property to get the data. 
# and @<avariable-name>.setter to set the data.
# @property
# @<variable-name>.setter

class Animal:
	def __init__ (self, birthType = "Unknown", \
	appearance ="Unknown", blooded="Unknown"):
		self.birthType=birthType
		self.appearance=appearance
		self.blooded=blooded
	
	@property
	def birthType(self):
		return self.__birthType
		
	@birthType.setter
	def birthType(self, birthType):
		self.__birthType = birthType
	
	@property
	def birthType(self):
		return self.__appearance
		
	@birthType.setter
	def birthType(self, appearance):
		self.__appearance = apperance
	
	@property
	def birthType(self):
		return self.__blooded
		
	@birthType.setter
	def birthType(self, blooded):
		self.__blooded = blooded
	
	def __str__(self):
		return "A {} is {} it is {} it is {}".format (type(self).__name__, self.birthType, self.appearance, self.blodded)
	
class Mamal (Animal):
	def __init__ (self, birthType = "born alive", \
	appearance="hair or fur", blooded="warm blooded", \
	nurseYoung = True):
		Animal.__init__ (self, birthType, appearance, blooded)
		self.__nurseYoung = nurseYoung
			
	@property
	def nurseYoung(self):
		return self.__nurseYoung
		
	@nurseYoung.setter
	def nurseYoung(self, nurseYoung):
		self.__nurseYoung = nurseYoung
		
	def __str__ (self):
		# super() from Animal, get string __str__(), 
		return super().__str__() + "and it is {} they " \
		"nurse their young".format(self.nurseYoung)
			
class Reptile (Animal):
	def __init__ (self, birthType = "born in an egg or born" \
	" alive", appearance ="dry cales", blooded= "cold blooded"):
	
		Animal.__init__(self, birthType, appearance, blooded)
		
# Other languages have overloading. 
# Pyhton does not have overloading.
# Only one method in Python. 
# Other languages:
#	def sumAll (self, int, int, string)
#	def sumAll (self, int, int, int, string)

def sumALl (self, *args):
	sum = 0
	for i in args:
		sum += i
	return sum

def main():
	animal = Animal ("born in live")
	print (animal.birthType)

main()