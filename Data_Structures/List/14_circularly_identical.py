'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to check whether two lists are circularly identical
'''

print("Enter space separated list1 values")
List1=list(map(str,input().split()))
print("Enter space separated list2 values")
List2=list(map(str,input().split()))

if (''.join(List2) in ''.join(List1*2)):
    print("circular")
else:
    print("Not circular")