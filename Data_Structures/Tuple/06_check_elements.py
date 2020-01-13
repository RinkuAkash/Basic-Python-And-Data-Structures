'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to check whether an element exists within a tuple
'''

Tuple=(1,2,3,4,5,6)

n=int(input("Enter single digit number : "))

if n in Tuple:
    print("Present")
else:
    print("Not present")
