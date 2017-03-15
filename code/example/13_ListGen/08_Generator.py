#!/usr/bin/python3
'''
Generator
'''
double = (x * 2 for x in range (10))

print ("Double 1: ", next (double)) # 0
print ("Double 2: ", next (double)) # 2
print ("Double 3: ", next (double)) # 4
print ("Double 4: ", next (double)) # 6
'''
print ("Double 5: ", next (double))
print ("Double 6: ", next (double))
print ("Double 7: ", next (double))
print ("Double 8: ", next (double))
print ("Double 9: ", next (double))
print ("Double 10: ", next (double))

print ("Double 11: ", next (double)) # Stop Generator
print ("Double 12: ", next (double))
print ("Double 13: ", next (double))
print ("Double 14: ", next (double))
'''

for num in double:
	print (num) # 8, 10, 12, 14, 16, 18