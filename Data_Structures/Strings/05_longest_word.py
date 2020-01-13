'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python function that takes a list of words and returns the length of the longest one. 
'''

def LongestWord(words):
    max=0
    for word in words:
        if len(word)>max:
            max=len(word)
    return max

words=list(map(str,input("Enter the statement : ").split()))
print(LongestWord(words))