'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to find common items from two lists
'''

List1=[1,2,3,4,5,6]
List2=[1,2,3,7,8,9]
print([x for x in List1 if x in List2])