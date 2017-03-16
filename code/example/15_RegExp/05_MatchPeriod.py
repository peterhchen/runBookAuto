#!/usr/bin/python3
'''
match period character

'''
import re

randStr = "F.B.I. I.R.S. CIA"

# .: Any character,
# \.: Match period character
print ("Match Word Count: ", len(re.findall (".\..\..\.", randStr)))
print ("Match Word: ", re.findall (".\..\..\.", randStr))