#!/usr/bin/python3

# We import the Decimal module.
# from deciml Modules we import Decimal.
# The module name is decimal (lowercase).
# The function (or method) is Decimal (lowercascse).
# The method Decimal (uppercase) is inside the module decimal (lowrecase). 
# We use D (alias name) for method Decimal.
from decimal import Decimal as D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print ('sum = ', sum)
print ('0.1 + 0.1 + 0.1 - 0.3 = ', 0.1 + 0.1 + 0.1 - 0.3)
