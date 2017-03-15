#!/usr/bin/python3
'''
Pass Function and Decorator
'''
def mult_by_2 (num):
	return num * 2

def do_math (func, num):
	return func(num)

print ("8 * 2 = ", do_math (mult_by_2, 8))

def get_func_mult_by_num (num):
	def mult_by (value):
		return num * value
	return mult_by

generated_func = get_func_mult_by_num (5)

print ("5 * 10 =", generated_func (10))

def times_two (num):
	return mum * 2

listOfFuncs = [times_two, generated_func]
print ("5 * 9 = ", listOfFuncs[1](9))