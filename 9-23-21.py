# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:12:14 2021

@author: Elijah
"""

'''
n = input("Give me your first and last name ")
bday = input("Give me your birthday (mmddyy) ")

first_initial = n[0]
space = n.index(" ")
second_initial = n[space + 1]

pw = bday + first_initial + second_initial
print(pw)
'''
def greeting():
    print("Welcome to the password generator.")
    
def getPW(first = "John", last = "Doe", bday = "010203"):
    f = first[0]
    l = last[0]
    bday = bday
    print(bday + f + l)

greeting()
getPW("Reuben", "Alv", "072305")
getPW("David", "Ake", "091208")
getPW()
#function with parameters
def getGPA(y1, y2, y3, y4):
    gpa = (y1 + y2 + y3 + y4)/4
    return gpa

david_gpa = getGPA(1.7, 2.1, 2.1, 3.2)
print("David's GPA: ", david_gpa)