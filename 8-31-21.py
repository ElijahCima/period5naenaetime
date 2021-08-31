# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:50:42 2021

@author: Elijah
"""

#your_name = input("Give me your name!!!!!! ")
#Prints from index 6 until the end
#print(your_name[6:])

school = "Coral Gables Senior High"
#print out 10 letter
print(school[9])

"""
Print out from the tenth letter 
to the end of the String

"""
print(school[9:])

#Print out the second to fifth letter 
print(school[1:4]) 
#In reverse?
print(school[::-1]) 
#The length of the string?
L = len(school)
print("Size of string is ", L)
#Print every other letter
print(school[0:L-1:2])

print("Where is the first space in the string?")
print(school.index(""))
print("Where is the second space in the string?")
print(school.index("", 6))
print(school[:5])
print(school[6:12])

month = input("Birth month: ")
day = input("Birth day: ")
year = input("Birth year: ")
n = input("Your first and last name: ")
space = n.index(" ")
initials = n[0] + n[space + 1]
print("Your Gables password is: ")
print(month + day + year + initials)