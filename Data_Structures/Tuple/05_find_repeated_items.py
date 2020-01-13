'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to find the repeated items of a tuple. 
'''

Tuple=(1,2,3,4,5,2,3,4,1,2,3)

Set=set()

for i in range(0,len(Tuple)-1):
    for j in range(i+1,len(Tuple)):
        if Tuple[i]==Tuple[j]:
            Set.add(Tuple[i])
print("Repeated items : ",tuple(Set))