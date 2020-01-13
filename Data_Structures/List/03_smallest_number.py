'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to get the smallest number from a list
'''

List=[1,2,3,4,5,6,7,8,9]

min=List[0]

for i in range(1,len(List)):
    if List[i]<min:
        min=List[i]
print("Smallest number is : ",min)