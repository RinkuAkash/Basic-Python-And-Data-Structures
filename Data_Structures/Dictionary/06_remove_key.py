'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to remove a key from a dictionary.
'''

dictionary={'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5','key6':'value6','key7':'value7','key8':'value8','key9':'value9'}

key=input("Enter key (eg. key1,key2,...,key9) to remove : ")
del dictionary[key]
print(dictionary)