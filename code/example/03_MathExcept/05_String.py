#!/usr/bin/python3

# integer class and float class.
print (type (3))    # <class 'int'>
print (type (3.14)) # <class 'float'>

# Single quote and double quote strings are the same.
print (type ("3"))  # <class 'str'>
print (type ('3'))  # <class 'str'>


string = "This is a string"
print ('string = ', string)
print ('string[0] = ', string[0])
print ('string[-1] = ', string[-1])
print ('string[3+5] = ', string[3+5])
print ("length = ", len (string))
print ('string[0:4] = ', string[0:4])     # slice
print ('string[8:] = ', string[8:])      # slice
print ("Green " + "Ege")      # concatenate
print ("Hello "* 5)      # repeat 5 times

num_str = str (5)     # Convert a number to string

print ("Print character:")      # repeat 5 times
for char in string:
    print (char + " ", end="")
print()

# range (start, stop, step)
for i in range(0, len(string)-1, 2):   
    #print ('i = ', i)
    print (string[i] + string [i + 1])

# A-Z : 65-90
# a-z : 97 - 122
print ("A =", ord ("A"))    # A = 65
print ("65 =", chr (65))   # 65 = 65
