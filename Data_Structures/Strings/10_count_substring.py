'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to count occurrences of a substring in a string.
'''

String=input("Enter the main string : ")
subString=input("Enter the sub string : ")

count=0
for i in range(0,len(String)):
    if String[i]==subString[0] and String[i:len(subString)+i]==subString:
        count+=1

print(count)