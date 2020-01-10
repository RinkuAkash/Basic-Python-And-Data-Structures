'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
 Write a python program to access environment variables. 
'''

import os

variable=input("Enter enviroment variable :")
print(os.getenv(variable, "Not found"))