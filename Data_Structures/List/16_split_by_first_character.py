'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to split a list based on first character of word
'''

print("Enter words (space separated)")
Words=list(map(str,input().split()))


result=[]

for word in Words:
    List=[]
    for second in Words:
        if word[0]==second[0]:
            List.append(second)
            Words.remove(second)
    result.append(List)

for group in result:
    print(group)