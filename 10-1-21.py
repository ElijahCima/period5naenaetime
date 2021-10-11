# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:28:13 2021

@author: Elijah
"""

#A global variable
var1 = "A Global Variable"

def myFunction():
  print("Var1 inside the function is: ", var1)


print("Var1 - outside of the function is: ", var1)
myFunction()

#Global keyword
var2 = "Another global variable"

def f2():
  global var2 #without this, we get an error
  var2 = var2 + " - Need to know"
  print(var2)

f2()

#local variable
def f3():
    var3 = "A local variable"
    print(var3)
    
f3()

#A mix of global and local
var4 = "Another global"
def f4():
    var4 = "Another local"
    print("Inside the function: ", var4)
f4()