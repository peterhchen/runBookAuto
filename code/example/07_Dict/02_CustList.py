#!/usr/bin/python3
#Enter Customer (Yes/No): y
#Enter Customer Name: Peter Chen
#Enter Customer (Yes/No): y
#Enter Customer Name: Irene Huang
#Enter Customer (Yes/No): n
#Peter Chen
#Irene Huang

# Create an Array
customers = []
# Create a Loop
while True:
	# Get Input and make it work for yes/no.
	createEntry = input ("Ener Custmoer (yes/no): ")
	createEntry = createEntry[0].lower()
	# Check to leave loop.
	if createEntry == 'n':
		break
	else:
		fName, lName = input ("Enter Customer Name: ").split()
		customers.append({'fName': fName, 'lName': lName})

# Print custsomer data
for cust in customers:
	print (cust['fName'], cust['lName'])