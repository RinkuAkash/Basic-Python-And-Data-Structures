'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
	Sample String : 'abc'
	Expected Result : 'abcing' 
	Sample String : 'string'
	Expected Result : 'stringly'
'''

String=input("Enter the string : ")

if String[-3:] =='ing':
    String=String+'ly'
elif len(String)>2:
    String=String+'ing'

print(String)