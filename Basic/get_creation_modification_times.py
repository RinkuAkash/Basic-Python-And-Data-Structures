'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get file creation and modification date/times
'''

import os,time

File=input("Enter file name : ")
creation_time=time.ctime(os.path.getctime(File))
modified_time=time.ctime(os.path.getmtime(File))
print("creation time : {}".format(creation_time))
print("Modified time : {}".format(modified_time))