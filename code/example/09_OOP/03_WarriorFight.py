#!/usr/bin/python3
'''
Warrior Game:
Damage: is a random number.
Game is over and over gain until one of them is die
Shield:

Sam atatcks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is Victorious
Game Over
'''
import random
import math
# Warriors have name, health, and attack and block maximums.
# Warrioe have capabilities to attack and block random amounts.
class Warrior:

	def __init__ (self, name="warrior", health=0, attkMax=0, blockMax=0):
		self.name = name
		self.health = health
		self.attkMax = attkMax
		self.blockMax = blockMax
	# Attack random 0.0 to 1.  * maxAttack + 0.5
	# Block will use random()	
	def attack (self):
		attkAmt = self.attkMax * (random.random() + 0.5)
		return attkAmt
	
	def block (self):
		blockAmt = self.blockMax * (random.random() + 0.5)
		return blockAmt

# Battle class capability of looping untile 1 warrior die.
# Warrior wil each get a turn to attack each other
class Battle:
	def startFight (self, warrior1, warrior2):
		while True:
			if self.getAttackResult (warrior1, warrior2) == "Game Over":
				print ("Game Over")
				break
	
	@staticmethod
	def getAttackResult (warriorA, warriorB):
		warriorAAttkAmt = warriorA.attack()
		warriorBBlockAmt = warriorB.block()
		damage2WarriorB = math.ceil (warriorAAttkAmt - warriorBBlockAmt)
		warriorB.health = warriorB.health - damage2WarriorB
		print ("{} attachs {} and deals {} damange".format (warriorA.name, warriorB.name, damage2WarriorB))
		print ("{} is down to {} health".format(warriorB.name, warriorB.health))
		if warriorB.health <= 0:
			print (("{} has died and {} is Vicotrious").format(warriorB.name, warriorA.name))
			return ("Game Over")
		else:
			return "Fight Again"
def main():
	maximus = Warrior ("Maximus", 50, 20, 10)
	galaxon = Warrior ("Galaxon", 50, 20, 10)
	battle = Battle()
	battle.startFight (maximus, galaxon)

main()
	
# Function gets 2 Warriors
# 1 warrior attack the other/


