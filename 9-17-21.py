# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:43:10 2021

@author: Elijah
"""

#Example of while loop
'''
x = 9
while(x < 50):
    print("Carlos was late again")
    x = x + 1
'''

#Algorithm for supermarket cash register.
moreItems = True
total = 0
TAX = 0.75
items = 0
while(moreItems):
    price = float(input("Give the price (enter 0 if there are no more products): "))
    if(price != 0): 
        total = total + price
        items += 1 #same thing as items = items + 1
        print("Your total is ${:.2f}".format(total))
    else:
        moreItems = False
        
total_taxed = total* (1 + TAX)
print("Total Number of Purchased Items: ", items)
print("Pre-tax Total: ${:.2f}".format(total))
print("Tax: ${:.2f}".format(total * TAX))
print("Total owed: ${:.2f}".format(total_taxed))