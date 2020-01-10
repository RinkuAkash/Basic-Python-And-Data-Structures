'''
Created on 10/01/2020
@author: B Akash
'''
'''
Write a Python program to concatenate all elements in a list into a string and return it. 
'''

#Taking input elements from  user
List=list(map(str,input().split()))

string=""

#Looping and concatenating elements to string
for i in range(0,len(List)):
    string+=List[i]

#printing string
print(string)