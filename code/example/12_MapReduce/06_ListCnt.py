#!/usr/bin/python3
'''
Create a random list filled with the characters H and T
for heads and Tail. Output the number of Hs and Ts.
Example Output
Heads: 46
Tails: 54
'''
# Create a List to hold H and T
import random

flipList = []
# file with 100 Hs and Ts
for i in range (1, 101):
	flipList += random.choice (['H', 'T'])

print ("flipList", flipList)	
print ("Heads", flipList.count ('H'))
print ("Tails", flipList.count ('T'))

