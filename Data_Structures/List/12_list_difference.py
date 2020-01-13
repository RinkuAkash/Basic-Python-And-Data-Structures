'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to get the difference between the two lists
'''

List1=[1,2,3,4,5,6,7,8,9]
List2=[6,7,8,9,0]

for item in List2:
    if item in List1:
        List1.remove(item)

print(List1)