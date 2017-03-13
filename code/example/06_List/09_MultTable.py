#!/usr/bin/python3

import random
import math

#Create multi-Dimesional List
multTable = [[0] * 10 for i in range(10)]
#Incement with outer for
for i in range (1, 10):
	#Increment with inner loop
	for j in range(1,10):
		multTable [i][j] = i *j

for i in range (1, 10):
	for j in range (1, 10):
		print(multTable[i][j], end=" , ")
	print()
