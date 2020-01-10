'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
'''

def maximum(List):
    value=float('-inf')
    for i in List:
        if value<i:
            value=i
    return value

def minimum(List):
    value=float('+inf')
    for i in List:
        if i<value:
            value=i
    return value

print("Enter space separated numbers :")
List=list(map(int,input().split()))
print("Maximum value : ",maximum(List))
print("Minimum value : ",minimum(List))