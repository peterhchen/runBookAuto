#!/usr/bin/python3

# Enter a string to hide in uppercase: Hide
# Secret Message: 3457890
# Orignal Message: HIDE
#
# Uppercase character:
# A-Z: 65-90
# Lowercase character:
# a-z: 97-122

# input "Enter a uppercase string"
# NOTE: 
# Uppercase is two digits.
# Lowercase may be 2-3 digits and more difficult to convert.

string = input ("Enter a uppercase String: ")
secret_string = ""

# Cycle through each character om the string
for char in string:
    # Store each character coe in a new string
    secret_string += str (ord(char)) 

# Print "Secrete Messag" 5634078
print ("Secret Message: ", secret_string)

# Cycle through each character code 2 at a time by increamenting by 2 each time
string = ""
for i in range (0, len (secret_string)-1, 2):
    # Get the 1st and 2nd for the 2 digit numner
    char_code = secret_string[i] + secret_string [i+1]
    # Convert theode into character and add them to a new strimg/
    string += chr(int(char_code))

# Print original Message: HIDE
print ("riginal String: ", string)
