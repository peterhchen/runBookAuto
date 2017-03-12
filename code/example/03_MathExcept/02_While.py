#!/usr/bin/python3

# Use do .. while loop.
# do while lopp has to do at least one before enter the loop.

secret_no = 7

while True:
    guess = int (input ('Guess a Number (1 to 10): '))
    if guess == secret_no:
        print ('You got it!')
        break
