# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:09:05 2021

@author: Elijah
"""

#takes in an amount and return the value of the amount after ten percent tip
def afterTip(amt):
    toPay = amt * 1.1
    return toPay

print(afterTip(40))

a = lambda i : i * 1.1
print(a(40))

def getAverage(y1, y2, y3, y4, years):
    return (y1 + y2 + y3 + y4) / years

print(getAverage(2.0, 1.5, 2.1, 0, 3))

gpa = lambda y1, y2, y3, y4, years : (y1 + y2 + y3 + y4) / years

print("Roman's GPA: ")
print(gpa(2.0, 1.5, 2.1, 0, 3))

def powered(e):
    return lambda b: b**e

mystery = powered(2)
print(mystery(3))

cubed = powered(3)
print(cubed(3))

quad = powered(4)
print(quad(5))