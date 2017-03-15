#!/usr/bin/python3
'''
List Comprehension
'''
print (list (map((lambda x: x *2), range (1, 11))))

print ([2 * x for x in range (1, 11)])

print (list (filter((lambda x: x % 2 != 0), range (1, 11))))

print ([x for x in range(1, 11) if x % 2 != 0])

# Generate 50 values. take power of 2. 
# Return Multiples of 8
print ([ i ** 2 for i in range (50) if i % 8 == 0])

print ([ x * y for x in range (1, 3) for y in range (11, 16)])