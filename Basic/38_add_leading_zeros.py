'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to add leading zeroes to a string
'''

string=input("Enter string : ")
N=int(input("Enter number of 0's to add : "))

print(string.rjust(N+len(string),'0'))