'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to sort files by date. 
'''

import os

files=os.listdir(".")
files.sort(key=os.path.getmtime)
print("\n".join(files))