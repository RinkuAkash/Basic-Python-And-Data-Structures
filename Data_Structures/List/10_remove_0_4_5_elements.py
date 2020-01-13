'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
	Expected Output : ['Green', 'White', 'Black']
'''

List= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

List=[x for (i,x) in enumerate(List) if i not in (0,4,5)]

print(List)