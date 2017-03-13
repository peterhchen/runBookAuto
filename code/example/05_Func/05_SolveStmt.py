#!/usr/bin/python3
# Given a string: x + 4 = 9
# Solve for x

# Recieve the string and split the string into variable
def solve_eq (equation):
	x, add, num1, equal, num2 = equation.split()
	num1, num2 = int (num1), int (num2)
	return "x = " + str (num2 - num1)

print (solve_eq ("x + 4 = 9"))