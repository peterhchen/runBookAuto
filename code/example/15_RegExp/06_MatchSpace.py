#!/usr/bin/python3
'''
match space

'''
import re

randStr = '''This is a long
string that goes
on for many lines
'''
print (randStr)

regex = re.compile ("\n")
randStr = regex.sub (" ", randStr) 
# substitue "\n" into ""
print (randStr)

'''
\b: BackSpace
\f: Form Feed
\r: Carriage Return
\t: Tab
\v: Vertical Tab
'''