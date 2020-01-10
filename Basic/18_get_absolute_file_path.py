'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem  statement: 
Write a Python program to get an absolute file path
'''

import os 

File=input("File name :")
print(os.path.abspath(File))