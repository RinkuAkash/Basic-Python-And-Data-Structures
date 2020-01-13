'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to check multiple keys exists in a dictionary. 
'''
dictionary={'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5','key6':'value6','key7':'value7','key8':'value8','key9':'value9'}

n=int(input("Enter number of keys you want to check (ex. key1,key2,........key9) : "))
check_dict=set()

for _ in range(n):
    check_dict.add(input())

if dictionary.keys()>=check_dict:
    print("Given keys are exists in dictionary")
else:
    print("Given keys are not exists in dictionary")