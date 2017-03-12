#!/usr/bin/python3

# This program use try except block to handle the error.
# The try except will ensure no break.

while True: # loop forever
    try: 
        number = int (input ('Enter an integer number: '))
        break 
        # if the number is correct then break the loop
  
    except ValueError:
        print ('You did not enter the integer number.')

    except: 
        print ('Any unknown error.')

# Got the right number.
print ('Thanks. Got intger number')
