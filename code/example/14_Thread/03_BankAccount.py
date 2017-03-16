#!/usr/bin/python3
'''
Create Thread and Execute Thread
'''
import threading
import time
import random

# BankAccount parent is threading.Thread
class BankAccount (threading.Thread):
	acctBalance = 100
	def __init__ (self, name, moneyRequest):
		#print ("__init__ ...")
		threading.Thread.__init__(self)
		self.name = name
		self.moneyRequest = moneyRequest
	
	def run(self):
		#print ("threadLock.aquire ...")
		threadLock.acquire()
		#print ("BankAccount.getMoney ...")
		BankAccount.getMoney(self)
		#print ("threadLock.release ...")
		threadLock.release ()
	
	@staticmethod
	def getMoney (customer):
		#print ("getMomeny ...")
		#print (customer.name)
		print ("{} tries to withdrawal ${} at {}".format (customer.name, customer.moneyRequest, time.strftime ("%H:%M:%S", time.gmtime())))
		if BankAccount.acctBalance - customer.moneyRequest > 0:
			BankAccount.acctBalance -= customer.moneyRequest
			print ("Current balance: ${}".format (BankAccount.acctBalance))
		else:
			print ("Not enough money in account")
			print ("Current balance: ${}".format(BankAccount.acctBalance))
			time.sleep (1)

#print ("Start threading.Lock() ...")
threadLock = threading.Lock()

#print ("Start Jonathan ...")
jonathan = BankAccount ("Jonathan", 1)
#print ("Start Peter ...")
peter = BankAccount ("Peter",100)
#print ("Start Irene ...")
irene = BankAccount ("Irene", 50)

jonathan.start()
peter.start()
irene.start()

jonathan.join()
peter.join()
irene.join()

print("Execition Ends")