#!/usr/bin/python3
 
# Display what race based on age.
# if age is 5, go to kindergarten
# Ages 6 to 17, go to grade 1 to 12.
# If age is >= 17, go to college
# trye to code in 10 lines.

# Ask for the age
age = eval (input ('Enter age: '))

# If (age < 5)
if age < 5:
   print ('Go to Preschool')

# Output for age 5
elif age == 5: 
   print ('Go to Kindergarden')

# age 6 to 17.
# Display output for 6to 17.
elif (age > 5) and (age <= 17): 
    grade = age - 5 
    print ('Go to {} grade'.format (grade))

else:
    print ('Go to college')
