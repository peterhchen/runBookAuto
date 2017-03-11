#!/usr/bin/python3

# Problem: Receive miles and convert to kilometers
# kilometers = miles * 1.6
# Enter Miles 10.
# 10 Miles euqls to 16 kilometer.

# ask the user to input miles and assign it to the mile variable.
mile = input ('Enter Mile: ')

# Convert the string to integer.
mile = int (mile)

# Perform multiplication 1.6
kilometer = mile * 1.6034

# print result using format.
print ("{} mile equals {} kilometer ".format (mile, kilometer))
