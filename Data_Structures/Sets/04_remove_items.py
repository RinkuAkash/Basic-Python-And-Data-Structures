'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python Program to remove item(s) from set
'''

Set=set({1,2,3,4,5,6,7,8,9,0})
print("Set : ",Set)
n=int(input("Enter number of items you want to remove : "))

for _ in range(n):
    item=int(input())
    Set.remove(item)

print("Set after removing elements : ",Set)