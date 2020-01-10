'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to determine if variable is defined or not.
'''

name='Akash'
number=333

check_var=input("Enter variable : ")

if check_var in locals() or check_var in globals():
    print("Variable exists")
else:
    print("Variable not exists")
    print("Try name or number as variables")