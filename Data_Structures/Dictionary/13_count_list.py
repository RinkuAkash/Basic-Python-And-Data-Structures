'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to count number of items in a dictionary value that is a list. 
'''

dictionary={'key1':[1,2,3],'key2':'value2','key3':[5,6,7],'key4':'value4','key5':[8,9,0],'key6':'value6','key7':[2,4,6],'key8':'value8','key9':'value9'}

count=0

for value in dictionary.values():
    if type(value)==list:
        count+=1
print(count)