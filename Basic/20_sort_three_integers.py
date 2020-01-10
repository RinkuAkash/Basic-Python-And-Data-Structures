'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to sort three integers without using conditional statements and loops. 
'''

a=int(input())
b=int(input())
c=int(input())

value1=min(a,b,c)
value3=max(a,b,c)
value2=(a+b+c)-(value1+value3)
print("Sorted order : ",value1,value2,value3)
