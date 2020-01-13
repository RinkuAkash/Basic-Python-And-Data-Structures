'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python function that takes two lists and returns True if they have at least one common member.
'''

def function(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False

print("Enter members of list 1 (space separated)")
list1=list(map(str,input().split()))
print("Enter members of list 2 (space separated)")
list2=list(map(str,input().split()))
print(function(list1,list2))