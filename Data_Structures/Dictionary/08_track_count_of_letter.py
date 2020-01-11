'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to create a dictionary from a string. 
	Note: Track the count of the letters from the string.
	Sample string : 'w3resource'
	Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

string=input("Enter a string : ")

Dict={}

for i in range(0,len(string)):
    Dict[string[i]]=string.count(string[i])

print(Dict)