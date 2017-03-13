#!/usr/bin/python3
# A prime can only divide by 1 and prime itself
# 5 is a prime (1 and 5)
# 6 is ais not a prime (1, 2, 3, 6).


def isprime (num):
	for i in range (2, num):
		if (num % i) == 0:
			return False
	return True

def getPrime (max_number):
	list_of_primes = []
	for num1 in range (2, max_number):
		if isprime (num1):
			list_of_primes.append (num1)
	return list_of_primes

max_num_to_check = int (input ("Search for Primes up to: "))

list_of_primes = getPrime (max_num_to_check)
for prime in list_of_primes:
	print(prime, end=" ")

print()
