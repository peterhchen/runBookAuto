#!/usr/bin/python3

# Check the string is alpha or number.

a_letter = "z"
a_number="3.14"
a_space = " "

def isfloat (str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print ("Is Pi a Float: ", isfloat (a_number))
