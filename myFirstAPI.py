# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:45:46 2021

@author: Elijah
"""
"""
Program API

Create a Python program with the following functions at the top of the program:

A function that takes a price as an input and returns the price after an eight percent tax.
A function that takes two parameters (bill price and quality of food). Return tip amount. (20 percent for good, 15 percent for fair, 10 percent for bad)
A function that returns the amount of leftover slices if everyone receives an equal amount of slices. Function should take two parameters (number of slices and number of eaters) and prints out “Each person receives [number] and there will be [remaining slices] left.
A function that takes no parameters, and prints out a generic farewell when called.
"""
import math

def dontTaxEvade():
    price = float(input("What was the price of whatever you bought? "))
    tax = 0.08 * price
    priceWithTax = price + tax
    print("Your price with tax is: ${:.2f}".format(priceWithTax))
dontTaxEvade()
def howMuchToTip(billPrice, foodQuality):
    tip = 0
    if foodQuality == "Good" or "good":
        tip = 0.20
    elif foodQuality == "Fair" or "fair":
        tip = 0.15
    else:
        tip = 0.10
    billWithTip = billPrice * tip 
    print("Your tip amount is: ${:.2f}".format(billWithTip))
howMuchToTip(12, "fair")
def leftoversNoneForDavid(numOfPeople, numOfSlices):
    numOfSlicesPerPerson = math.floor(numOfSlices / numOfPeople)
    numOfLeftovers = numOfSlices % numOfPeople
    print("Each person will get " + str(numOfSlicesPerPerson) + " slices, and there will be " + str(numOfLeftovers) + " slices left over.")
leftoversNoneForDavid(5, 13)

def genericFarewell():
    print("Goodbye World")
genericFarewell()