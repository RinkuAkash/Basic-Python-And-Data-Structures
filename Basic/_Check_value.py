'''
Created on 09/01/2020
@author: B Akash
'''
'''
problem statement:
     Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

#Taking group of values from user
Array=list(map(int,input().split()))

#Input value to check in Array
n=int(input())

#Iterating and checking value in Array
flag=False
for i in range(0,len(Array)):
    if Array[i]==n:
        flag=True
print(flag)
