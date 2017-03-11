#!/usr/bin/python3

# Enter Calculator: 3 * 6
# 3 * 6 = 18

# Store the user input of 2 number and operator.
num1, oper , num2 = input ('Enter Calculator: ').split()

# Conver the strings into integers
num1 = int (num1)
num2 = int (num2)

# if + then need to provide the output based on addition
# Print the result.
if oper == '+':
    print ("{} + {} = {}".format(num1, num2, num1+num2))
elif oper == "-":
    print ("{} - {} = {}".format(num1, num2, num1-num2))
elif oper == "*":
    print ("{} * {} = {}".format(num1, num2, num1*num2))
elif oper == "/":
    print ("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print ("Only support + - * .")
