'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to sum all the items in a list
'''

List=[1,2,3,4,5,6,7,8,9]

sum=0
for i in range(0,len(List)):
    sum+=List[i]

print("Sum of list : ",sum)