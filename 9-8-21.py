# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:49:31 2021

@author: Elijah
"""
#Boolean Keywords
print(type(True))
print(type(False))
print(type("True"))

David = 4.0
Elijah = 3.5
Cesar = 3.5
Gabin = 1.5

print("Who is better? Is David better than Elijah? ")
print(David > Elijah)

print("Are Elijah and Cesar of equal caliber? ")
print(Elijah == Cesar)

print("Is Cesar in between the worst and best students? ")
print(Gabin < Cesar and Cesar < David)

#Scholarship, University Calculator
y1 = float(input("What was your freshman year gpa? "))
y2 = float(input("What was your sophomore year gpa? "))
y3 = float(input("What was your junior year gpa? "))
musician = input("Are you a talented musician? ")
gpa = (y1 + y2 + y3) / 3
print("Your GPA is {:.5f}".format(gpa))

if(gpa > 3.7):
    print("You are qualified for earning a scholarship")
    
elif(gpa > 3.4 and (musician == "yes" or musician == "Yes")):
    print("You are qualified for earning a scholarship")
    
else:
    print("You better save up for school ")