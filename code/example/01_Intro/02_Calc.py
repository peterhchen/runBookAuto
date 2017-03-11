#!/usr/bin/python3

# Ask the user to input 2 values and store them in vairables num1 and num2.
num1, num2 = input ('Enter 2 numbers: ').split()

# COnver the strings into regular Integer
num1 = int (num1)
num2 = int (num2)

# Add the value entered and store in sum
sum = num1 + num2

# Subtract valyes and store in difference
diff = num1 + num2

# Multuiple the values and store in product
prod = num1 * num2

# Divide the values and store in quotient.
quo = num1 / num2


# Use the modules on the values to find the reminder.
rem = num1 % num2


# Print the results.
print ("{} + {} = {}".format (num1, num2, sum))
print ("{} - {} = {}".format (num1, num2, diff))
print ("{} * {} = {}".format (num1, num2, prod))
print ("{} / {} = {}".format (num1, num2, quo))
print ("{} % {} = {}".format (num1, num2, rem))

