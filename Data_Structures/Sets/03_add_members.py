'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to add member in a set
'''

Set=set()

size=int(input("Enter the number of items you want to add to set : "))
for _ in range(size):
    Set.add(input())
print("Your set is : ",Set)