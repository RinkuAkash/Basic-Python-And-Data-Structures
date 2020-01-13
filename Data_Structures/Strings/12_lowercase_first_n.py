'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python Program to lowercase first n characters in a string.
'''

String=input("Enter a string : ")
n=int(input("Enter n number to lowercase : "))

String=String[:n].lower()+String[n:]

print(String)