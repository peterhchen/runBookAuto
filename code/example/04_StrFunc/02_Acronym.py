#!/usr/bin/python3

# Input: random acess memory
# Output: RAM

# Ask for a String, e.g., random acess memory
orig_str = input ("Convert to acronym: ")

# Convert the string to uppercase
orig_str = orig_str.upper()

# Convert the string imto a list
list_str = orig_str.split()

# Cycle the list
print("Output: ", end="")
for word in list_str:
    # Gte the 1st character f the work and eliminate the new line
    print(word[0], end="")
# Add a new line.
print()
