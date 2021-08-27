# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:58:25 2021

@author: Elijah
"""

day = "Thursday"
print(type(day))
day = 32.5
print(type(day))
day = 19
print(type(day))
day = 3j
print(type(day))


expense1 = input("How much did you spend on Sunday? ")
expense2 = input("How much did you spend on Monday? ")
#total$ is a bad variable name because of $
#2total is a bad variable because it does not begin with a letter 
#total spent is a bad variable because of the space
total = float(expense1) + float(expense2)

print("You spent: $" + "{:.2f}".format(total))


#Casting
x = int(1)
y = int(2.8)
z = int("3")
w = float("4.2")
print(x, end =" ")
print(y, end =" ")
print(z, end =" ")
print(w, end =" ")

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

x = complex(5)
print(x)

#Take a radius as an input. Print out the area of that circle.
#Take a radius as an input. Print out the volume of the sphere.
#Both answers should be to 4 decimal places.
radius = input("What is the radius of your circle? ")
pi = 3.1415
radiussquared = float(radius) * float(radius)
area = radiussquared * pi
print("Your area is: " + "{:.4f}".format(area))

radius = input("What is the radius of your sphere? ")
radiuscubed = float(radius) * float(radius) * float(radius)
fourthirds = 4 / 3
volume = fourthirds * pi * radiuscubed
print("Your volume is: " + "{:.4f}".format(volume))