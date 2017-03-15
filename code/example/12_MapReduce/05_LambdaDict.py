#!/usr/bin/python3
'''
Lambda Dictionary
'''
attack = {'quick': (lambda: print ("Quick Attack")),
		'power': (lambda: print ("Power Attack")),
		'miss': (lambda: print ("Missed Attack"))}
		
import random
'''
attack dictionary: {'quick': <funciton <lambda> ar 0x005CA7C8>,
'power': <function <lambda> at 0x005CA780, }
'''
print ("attack dictionary: ", attack)
#print ("attack{'quick'}: ", attack{'quick'})	# Error
attackKey = random.choice (list(attack.keys()))
# dic_keys(['quick'], 'power', 'miss'])
print ("attack.keys(): ", attack.keys())

# list (attack.keys()): ['quick', 'power'. 'miss']
print ("list (attack.keys()): ", list(attack.keys()))

print ("random.choice (list(attack.keys())) = ", \
random.choice (list(attack.keys())))   # quik or miss

print ("attackKey: ", attackKey)	# quick or miss

print ("attack[random.choice (list(attack.keys()))]: ", \
attack[random.choice (list(attack.keys()))]())	# None

attack[attackKey]()
