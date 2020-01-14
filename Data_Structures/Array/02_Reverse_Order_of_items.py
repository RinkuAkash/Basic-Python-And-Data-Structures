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

Reverse=[Array[x] for x in range(len(Array)-1,-1,-1)]
print("Your array    : ",Array)
print("Reverse order : ",Reverse)