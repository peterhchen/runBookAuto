#!/usr/bin/python3

# Calculate the mortgage
money = input ('How much money you borrow: ')
interest = input ('interest rate: ')
money = float (money)
interest = float(interest) * 0.01

for i in range (10):
    money = money * (1 + interest)

print ('total mortgage you paid is {:.2f}'.format(money))
