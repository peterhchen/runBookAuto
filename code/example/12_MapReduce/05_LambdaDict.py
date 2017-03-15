#!/usr/bin/python3
'''
Lambda Dictionary
'''
attack = {'quick': (lambda: print ("Quick Attack")),
		'power': (lambda: print ("Power Attack")),
		'miss': (lambda: print ("Missed Attack"))}
		
print ("attack['quick'] = ", attack ['quick']())

import random

attackKey = random.choice (list(attack.keys()))
print ("attackKey: ", attackKey)
attack[attackKey]()