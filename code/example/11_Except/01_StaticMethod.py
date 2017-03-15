#!/usr/bin/python3
'''
static method

Q: What is the difference between @staticmethod and @classmethod?
http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

Ans: It is basically useless in Python -- you can just use a module function instead of a staticmethod. Basically @classmethod makes a method whose first argument is the class it's called from (rather than the class instance), @staticmethod does not have any implicit arguments

@staticmethod has much use.
'''
class Sum:
	@staticmethod
	def getSum (*args):
		sum = 0
		for i in args:
			sum += i
		return sum

def main():
	print ("Sum: ", Sum.getSum (1, 2, 3, 4, 5))

main()