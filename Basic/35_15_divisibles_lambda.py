'''
created 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. 
'''

print("Enter numbers, separate with spaces")
List=list(map(int,input().split()))

print(list(filter(lambda x:(x%15==0),List)))