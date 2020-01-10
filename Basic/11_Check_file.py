'''
Created on 10/01/2020
@author: B Akash
'''
'''
Write a Python program to check whether a file exists.
'''

#Taking file name as input
File_name=input("Enter name with extension: ")

#checking file existance with exception handler
try:
    file_check=open(File_name)
    print("File Exists")
except:
    print("File not exists")