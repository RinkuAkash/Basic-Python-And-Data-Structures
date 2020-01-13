'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to remove duplicates from a list
'''

List=[]
n=int(input("Enter the number of elemenet to add to list : "))
print("Enter elements : ")
for _ in range(n):
    List.append(input())

List=list(set(List))

print("List after removing : ",List)