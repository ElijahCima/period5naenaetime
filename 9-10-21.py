# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:00:51 2021

@author: Elijah
"""
try:
    account_holder = input("Account Holder: ")
    deposit1 = float(input("Month 1 Deposit: "))
    deposit2 = float(input("Month 2 Deposit: "))
    deposit3 = float(input("Month 3 Deposit: "))
    deposit4 = float(input("Month 4 Deposit: "))
    total = deposit1 + deposit2 + deposit3 + deposit4
    print("Hello " + account_holder + ", Welcome to Gables Bank")
    print("You deposited in total: ${:.2f}".format(total))
    deposits = int(input("How many deposits did you make? "))
    avg_deposits = total / deposits
    print("Your average deposit is: ${:.2f}".format(avg_deposits))

except ValueError:
    print("You gave an improper deposit value. ")
except ZeroDivisionError:
    print("You didn't make any deposits?????? ")
except:
    print("You have a bad input")
finally:
    print("Thank you for using our Gables Bank. ")