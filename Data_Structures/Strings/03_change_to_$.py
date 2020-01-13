'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  
	Sample String : 'restart'
	Expected Result : 'resta$t'
'''

String=input("Enter the string : ")

First_char=String[0]

String=list(String)

for i in range(1,len(String)):
    if String[i]==First_char:
        String[i]='$'

print("".join(String))