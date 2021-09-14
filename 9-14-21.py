# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:50:55 2021

@author: Elijah
"""

goods = ["I-phone 13", "Samsung Galaxy 20", "Google Pixel", "Nokia Flip Phone", "MacBook Pro", "Dell Inspiron 15"]
prices = [1299.99, 999.00, 550.79, 345.10, 1450.99, 875.00]
print(len(goods))

"""
Time consuming to go individually
print(goods[0])
print(goods[1])
print(prices[0])
print(prices[1])
"""
#Element by element iteration
for good in goods:
    print("Product: " + good)
    
for p in prices:
    print("Prices ${:.2f}".format(p))
    
#Loop through indices or numbers
for x in range(10):
    print(x, end = " ")
    
for y in range(25, 45):
    print(y, end = " ")

for z in range(920, 1000, 10):
    print(z, end = " ")
    
for i in range(6):
    print("Product: " + goods[i], end = " ----> ")
    print("Prices ${:.2f}".format(prices[i]))
    