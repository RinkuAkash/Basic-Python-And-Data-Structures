'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to find maximum and the minimum value
'''

maximum=float('-inf')
minimum=float('+inf')

Set={1,2,3,4,5,6,7,8,9,0}

for item in Set:
    if item>maximum:
        maximum=item
    if item<minimum:
        minimum=item

print("Maximum value is %d and Minimum value is %d"%(maximum,minimum))