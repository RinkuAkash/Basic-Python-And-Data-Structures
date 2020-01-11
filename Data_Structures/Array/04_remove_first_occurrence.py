'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to remove the first occurrence of a specified element from an array. 
'''
#function to remove element
def Remove(Array,size,Element):
    for i in range(0,size):
        if Array[i]==Element:
            del Array[i]
            return Array
    return Array

Array=[]
size=int(input("Enter size of array :"))

print("Enter elements : ")
for i in range(0,size):
    Array.append(input())

Element=input("Enter element to remove :")

print("Array after removing element : ",Remove(Array,size,Element))