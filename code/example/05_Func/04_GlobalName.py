#!/usr/bin/python3
global_name ="Irene"

def change_name ():
	global global_name
	global_name = "Peter"

change_name ()
print (global_name)
