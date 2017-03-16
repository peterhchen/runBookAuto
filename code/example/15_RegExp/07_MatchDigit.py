#!/usr/bin/python3
'''
match digit

'''
import re

randStr = "12345"
print ("randStr: ", randStr)
print ("Match Length \d: ", len(re.findall ("\d", randStr)))
print ("Match List \d: ", re.findall ("\d", randStr))

print ("Match Length \d{2}: ", len(re.findall ("\d{2}", randStr)))
print ("Match List \d{2}: ", re.findall ("\d{2}", randStr))

randStr1 = "123 12345 123456 1234567"
print ()
print ("randStr1: ", randStr1)
print ("Match Length \d{5,7}: ", len(re.findall ("\d{5,7}", randStr)))
print ("Match List \d{5,7}: ", re.findall ("\d{5,7}", randStr))