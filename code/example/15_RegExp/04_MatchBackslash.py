#!/usr/bin/python3
'''
backslash
'''
import re

randStr = "Here is \\stuff"

print ("Find \\Stuff: ", re.search (r"\\stuff", randStr))