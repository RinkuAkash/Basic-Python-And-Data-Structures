'''
Created on 09/01/2020
@author: B Akash
'''
'''
problem statement:
    Write a Python program to print the calendar of a given month and year.
'''

#importing calendar module
import calendar

#Taking input from user
year=int(input("Enter year(YYYY): "))
month=int(input("Enter month (MM): "))

print(calendar.month(year,month))