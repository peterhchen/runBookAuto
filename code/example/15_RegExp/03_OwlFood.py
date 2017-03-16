#!/usr/bin/python3
'''
String Substritution
'''

import re

owlFood = "rat cat mat pat"

regex = re.compile ("[cr]at")

owlFood = regex.sub ("owl", owlFood)
print (owlFood)  # owl owl mat pat