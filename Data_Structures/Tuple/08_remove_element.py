'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to remove an item from a tuple
'''

Tuple=(1,2,3,4,5,6,7,8,9)

n=int(input("Enter single digit to remove from tuple : "))

List=list(Tuple)
List.remove(n)
print(tuple(List))