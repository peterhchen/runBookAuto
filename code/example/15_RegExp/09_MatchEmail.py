#!/usr/bin/python3
'''
match email:
1-20 character
@
2-20 characters
. (Period)
2-3 characters
'''
import re

emailList = "db@aol.com pchen@gmail.com irene@apple.com db@.com eat@email.com"
# Email Matches: 4
print ("Email Matches: ", len(re.findall ("[\w.%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailList)))