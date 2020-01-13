'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statment:
Write a Python Program to iteration over sets
'''

Set=set()

n=int(input("Enter number of items you want to add : "))
for _ in range(n):
    Set.add(input())

print("The items present in set are : ")
for item in Set:
    print(item)