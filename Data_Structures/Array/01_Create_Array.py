'''
Created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. 
'''

Array=[]

print("Enter 5 integers :")
for i in range(0,5):
    Array.append(int(input()))

print("Array contains below integers :")
for i in range(0,5):
    print(Array[i])