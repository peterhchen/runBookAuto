#!/usr/bin/python3

# A-Z: 65-90
# a-z: 97-122
# ord (letter)
# chr (unicode)

# Use isupper() to decde which unicode to work with
# Add the key (number of character to shift) 
# if the key is bigger or smaller than the unicode
# A, Z, a, z increase or decrease by 26.

# Receive the message ot encrypt and the number of character to shift.
# message = "Make me secret"
# shift = 4
# encrypt => char_code = +key - 26
# decrypt => char_code = -key + 26
message = input ("Enter the message: ")
key=int (input("How manay character to shift (1-26): "))

#Prepare the secret_message
secret_message = ""

# Cycle throgh each character in the message
for char in message:
    #if it is not a letter then keep as it is
    if char.isalpha():
        # Get the character code and add the shift amount
        char_code = ord (char)
        char_code += key
        # if uppercase then compare to uppercase unicode
        if char.isupper():
            #if bigger than Z substract 26.
            if char_code > ord ('Z'):
                char_code -= 26
            # if smaler than A add 26.
            if char_code < ord ('A'):
                char_code += 26
        # Do the some for lower characters
        else:
            if char_code > ord ('z'):
                char_code -= 26
            if char_code < ord ('a'):
                char_code += 26
        # Convert from code to letter ad add to message.
        secret_message += chr (char_code)
    else:
        secret_message += char
print ("Encrypted :", secret_message)
# To decry the only that change the sign of the key.

key = -key
orig_message = ""
for char in secret_message:
    #if it is not a letter then keep as it is
    if char.isalpha():
        # Get the character code and add the shift amount
        char_code = ord (char)
        char_code += key
        # if uppercase then compare to uppercase unicode
        if char.isupper():
            #if bigger than Z substract 26.
            if char_code > ord ('Z'):
                char_code -= 26
            # if smaler than A add 26.
            if char_code < ord ('A'):
                char_code += 26
        # Do the some for lower characters
        else:
            if char_code > ord ('z'):
                char_code -= 26
            if char_code < ord ('a'):
                char_code += 26
        # Convert from code to letter ad add to message.
        orig_message += chr (char_code)
    else:
        orig_message += char
print ("Decrypted :", orig_message)