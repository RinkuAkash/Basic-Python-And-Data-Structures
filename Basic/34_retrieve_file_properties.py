'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to retrieve file properties. 
'''

import os.path, time

File=input("Enter file name : ")

print("File path     : ",os.path.abspath(File))
print("Access Time   : ",time.ctime(os.path.getatime(File)))
print("Modified Time : ",time.ctime(os.path.getmtime(File)))
print("File Size     : ",os.path.getsize(File))