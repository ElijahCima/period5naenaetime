# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Strings
class_name = "p5_Delinquents: "
#Error: class_name + 5       You cannot concatenate a String and number 
student1 = "Carlos"
top_delinquents = student1 + ", Nicholas, Gionna, Gonzalo"
class_students = class_name + top_delinquents

print(class_students)

same_name = "2"
third_student = 3
print(type(same_name))
student2 = "Carlos " + same_name
print(student2)
student3 = "Carlos " + str(third_student)
print(student3)

#Int
grade1 = int(input("What did you get in p1? "))
grade2 = int(input("What did you get in p2? "))
grade3 = int(input("What did you get in p3? "))
grade4 = int(input("What did you get in p4? "))

print("To verify: You scored: " + "\n" + str(grade1) + "\n" + str(grade2) + "\n" + str(grade3) + "\n" + str(grade4))

gpa = (grade1 + grade2 + grade3 + grade4) / 4
print("GPA: " + str(gpa))
print(type(gpa))