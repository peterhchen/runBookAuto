#!/usr/bin/python3
myDict = {"fName": "Peter", "lName": "Chen",
			"address": "652 Calle Victoria"}

print("My Name:", myDict["fName"])

myDict["address"] = "1225 Vienna Drive"
myDict ["city"] = "Suunyvale"
print ("Is there a city:", "city" in myDict)

print(myDict.values())

for i in myDict:
	print (i)

myDict.clear()

employees = []
fName, lName = input ("Enter Employee Name: ").split()
employees.append({'fName': fName, 'lName': lName})
print (employees)