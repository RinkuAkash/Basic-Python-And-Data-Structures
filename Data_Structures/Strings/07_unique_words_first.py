'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
	Sample Words : red, white, black, red, green, black
	Expected Result : black, green, red, white,red
'''

words=list(map(str,input().split(', ')))

print(", ".join(sorted(list(set(words)))))