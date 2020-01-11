'''
Created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to convert a list into a nested dictionary of keys.
'''

List=[1,2,3,4,5,6,7,8,9]

Dictionary={}

for key in List:
    Dictionary[key]={key}
print(Dictionary)