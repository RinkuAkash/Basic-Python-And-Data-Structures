'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
 Write a Python program to count the number of characters (character frequency) in a string. 
'''

String=input("Enter the string : ")
Dict=dict()

for i in range(0,len(String)):
    if String[i] in Dict.keys():
        Dict[String[i]]=Dict.get(String[i])+1
    else:
        Dict[String[i]]=1

print(Dict)