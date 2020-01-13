'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to find the list of words that are longer than n from a given list of words
'''

print("Enter a statement : ")
Statement=input()
n=int(input("Enter length : "))
List=[]

Statement=Statement.split(" ")
for word in Statement:
    if len(word)>=n:
        List.append(word)
print("List of words with length above %d are : "%n,List)
