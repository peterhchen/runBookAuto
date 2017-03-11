#!/usr/bin/python3
 
# Display different format based on age.
# Age 1 to 18: Important
# Age 21, 50, or >= 65: Important
# All othera Ages: Not important

# Get age and store in age
age = eval (input('Enter age: '))

# if age >= 1 and <= 18: important
if (age >= 1) and (age <= 18):
    print ("Important")

# if age == 21 or 50: important
elif (age == 21) or (age == 50):
    print ("Important")

# if age < 65, convert the true to false.
elif not(age < 65):
    print ("Important")

# else not import.
else:
    print ("Not Important")

