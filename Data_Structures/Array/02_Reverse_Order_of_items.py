'''
Created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to reverse the order of the items in the array
'''

Array=[]
size=int(input("Enter Array size : "))
print("Enter items :")
for i in range(0,size):
    Array.append(input())

print("Your array    : ",Array)
print("Reverse order : ",Array[::-1])