'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
'''

n=int(input("Enter a number : "))
Dict={}

for i in range(1,n+1):
    Dict[i]=i*i

print(Dict)