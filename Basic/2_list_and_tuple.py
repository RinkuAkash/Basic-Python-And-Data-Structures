'''
Created on 09/01/2020
@author: B Akash
'''
'''
problem statement:
    Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
'''

#taking input from user
numbers=input()

#converting input into integer list
List=list(map(int,numbers.split(',')))

#converting input into integer tuple
Tuple=tuple(map(int,numbers.split(',')))

#printing List and Tuple
print(List)
print(Tuple)
