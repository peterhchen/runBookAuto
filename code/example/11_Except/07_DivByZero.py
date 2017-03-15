#!/usr/bin/python3
'''
Divide by Zero
'''

num1, num2 = input ("Enter 2 number to divide: ").split()

try:
	quotient = int(num1)/int(num2)
	print ("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
	print ("Divide by Zero") # 2 / 0

else:
	print ("No excption")  # 1/2 or 2/1

finally:
	print ("Finished.")