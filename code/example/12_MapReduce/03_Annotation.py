#!/usr/bin/python3
'''
Function Annotation
'''
def random_func (name: str, age: int, weight: float) -> str:
	print ("Name: ", name)
	print ("Ag: ", age)
	print ("Weight: ", weight)
	
	return "{} is {} years old and weigh {}".format (name, age, weight)
	
print (random_func("Peter", 60, 150))
print (random_func (89, "Derek", 'Turtle'))
print (random_func.__annotations__)