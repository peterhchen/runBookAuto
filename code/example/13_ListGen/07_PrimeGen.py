#!/usr/bin/python3
'''
Prime number Generator
'''
def isprime (num):
	for i in range (2, num):
		if (num % i) == 0:
			return False
	return True

def gen_prime (max_number):
	for num1 in range (2, max_number):
		if isprime(num1):
			yield num1

prime = gen_prime (50)
print ("prime: ", next (prime))
print ("prime: ", next (prime))
print ("prime: ", next (prime))
print ("prime: ", next (prime))
print ("prime: ", next (prime))